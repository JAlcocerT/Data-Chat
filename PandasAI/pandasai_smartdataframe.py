from pandasai.smart_dataframe import SmartDataframe
from pandasai.llm.openai import OpenAI
import pandas as pd

## export OPENAI_API_KEY="sk-..." #linux
## $Env:OPENAI_API_KEY = "sk-..." #PS

df = pd.read_csv("https://raw.githubusercontent.com/TirendazAcademy/PandasAI-Tutorials/main/Datasets/population.csv")
llm = OpenAI()

df = SmartDataframe(df, config={"llm": llm})
response = df.chat("What is the average population?")
print(response)
# The average loan amount is $15,000.