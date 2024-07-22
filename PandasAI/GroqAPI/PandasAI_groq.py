from dotenv import load_dotenv

load_dotenv(override=True)

import pandas as pd
data = pd.read_csv("population.csv")
data.head()

import os
from langchain_groq.chat_models import ChatGroq

llm = ChatGroq(
    model_name="mixtral-8x7b-32768", 
    api_key = os.environ["GROQ_API_KEY"])

from pandasai import SmartDataframe
df = SmartDataframe(data, config={"llm": llm})

df.chat('Which are the top 5 countries by population?')


### ./exports/charts
# df.chat("First sort countries by population and \
# create a bar plot of the top 5 countries")