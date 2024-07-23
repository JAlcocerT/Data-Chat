from dotenv import load_dotenv
import pandas as pd
import os
from langchain_groq.chat_models import ChatGroq
from pandasai import SmartDataframe


load_dotenv(override=True)


#data = pd.read_csv("population.csv")
data = pd.read_csv("https://github.com/TirendazAcademy/PandasAI-Tutorials/blob/main/Datasets/population.csv")
data.head()



llm = ChatGroq(
    model_name="mixtral-8x7b-32768", 
    api_key = os.environ["GROQ_API_KEY"])


df = SmartDataframe(data, config={"llm": llm})

df.chat('Which are the top 5 countries by population?')


### ./exports/charts
# df.chat("First sort countries by population and \
# create a bar plot of the top 5 countries")