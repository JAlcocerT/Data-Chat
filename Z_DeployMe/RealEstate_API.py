#########################
#USING OPENAI API AS LLM#
########################

import streamlit as st
#from UDF_GenAI import read_markdown_files

from openai import OpenAI

import os
from dotenv import load_dotenv
import logging
# Load environment variables
load_dotenv()


# Get API keys and other environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_DIRECTORY = os.getenv("DATA_DIRECTORY", "./properties.md")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", 0.0))

SYSTEM_CONTENT_OpenAI = os.getenv("SYSTEM_CONTENT", """You are a Real Estate Agent that will make relevant follow-up questions
                                                to the user to provide the best housing option.
                                                When you see a match in the given amenities, you can comment on them.
                                                If there is not a pure match, you will also recommend the 2 closer matches from the offerings we have.
                                                You will also provide the link information as hyperlink for the client to see the offer details. """)

def st_openai_md_genai():

    st.header("Explore our Properties 🏠")
    st.subheader("Talk with our Real Estate Agent (API)")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask your question:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            properties_must_have = read_markdown_file(DATA_DIRECTORY)

            if properties_must_have:
                try:
                    chat_completion = OpenAI().chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": f"""{SYSTEM_CONTENT_OpenAI}.
                                                These are the properties we have:
                                                  {properties_must_have}  
                                            """,
                            },
                            {"role": "user", "content": prompt}
                        ],
                        model=OPENAI_MODEL,
                        temperature=OPENAI_TEMPERATURE,
                        stream=True
                    )

                    for response in chat_completion:
                        delta = response.choices[0].delta
                        if delta.content is not None:
                            full_response += delta.content
                            message_placeholder.markdown(full_response + "▌")

                    message_placeholder.markdown(full_response)
                    st.session_state.messages.append({"role": "assistant", "content": full_response})

                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.session_state.messages.append({"role": "assistant", "content": f"An error occurred: {e}"})

            else:
                st.session_state.messages.append({"role": "assistant", "content": "Could not load markdown files."})
                message_placeholder.markdown("Could not load markdown files.")


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_markdown_file(filepath):
    """Reads and returns the content of a single .md file given its path."""
    try:
        logging.info(f"Reading file: {filepath}")
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return None
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
        return None


# Example usage:

#"./SimpleOpenAImd/datamd"
#"/home/jalcocert/Documents/py_stocks/EDA_Mortage_GenAI/SimpleOpenAImd"
# file_path = "/home/jalcocert/Documents/py_stocks/EDA_Mortage_GenAI/SimpleOpenAImd/datamd/properties.md"  # Replace with the actual path
# content = read_markdown_file(file_path)

# if content:
#     print(content)



def read_markdown_files(directory):
    """Reads and concatenates content from all .md files in a directory."""
    all_content = ""
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".md"):
                filepath = os.path.join(directory, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    all_content += file.read() + "\n\n"
    except FileNotFoundError:
        st.error(f"Directory not found: {directory}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    return 

# print(read_markdown_files("./SimpleOpenAImd/datamd"))
#print(read_markdown_files("/home/jalcocert/Documents/py_stocks/EDA_Mortage_GenAI/SimpleOpenAImd/datamd"))