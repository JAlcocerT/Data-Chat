import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Setup the MySQL database connection URI
mysql_uri = 'mysql+mysqlconnector://root:your_password@localhost:3306/Chinook'

# Initialize the database connection
db = SQLDatabase.from_uri(mysql_uri)

# Define the ChatPromptTemplate for generating the SQL query
template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)

# Function to get the schema of the database
def get_schema(_):
    schema = db.get_table_info()
    return schema

# Initialize the OpenAI model
llm = ChatOpenAI()

# Define the SQL chain that generates SQL query based on schema and user question
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)  # Assign the schema to the chain
    | prompt  # Use the template to create the SQL query
    | llm.bind(stop=["\nSQLResult:"])  # Ensure the response stops after SQL query
    | StrOutputParser()  # Convert the result to string
)

# Function to run the generated SQL query in the database
def run_query(query): 
    return db.run(query)

# Full chain that generates the SQL query and runs it on the database
full_chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
        schema=get_schema,  # Fetch the schema
        response=lambda vars: run_query(vars["query"]),  # Execute the query
    )
)

# Function to format the response based on the schema, question, SQL query, and SQL result
template_response = """Based on the table schema below, question, SQL query, and SQL response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}"""
prompt_response = ChatPromptTemplate.from_template(template_response)

# Full chain for natural language response after executing SQL query
full_chain_response = (
    RunnablePassthrough.assign(query=sql_chain).assign(
        schema=get_schema,  # Fetch schema
        response=lambda vars: run_query(vars["query"]),  # Execute the SQL query
    )
    | prompt_response  # Generate a natural language response
    | llm  # Use OpenAI to process the response
    | StrOutputParser()  # Optionally parse the result as a string
)

# Streamlit App UI
st.title("Langchain Database Query App")

user_question = st.text_input("Ask a question about the database:")

if user_question:
    result = full_chain_response.invoke({"question": user_question})
    st.write("Answer:", result)