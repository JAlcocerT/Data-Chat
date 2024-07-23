from pandasai.smart_dataframe import SmartDataframe
from pandasai.llm.openai import OpenAI
import pandas as pd

## export OPENAI_API_KEY="sk-..." #linux
## $Env:OPENAI_API_KEY = "sk-..." #PS

df = pd.read_csv("https://raw.githubusercontent.com/TirendazAcademy/PandasAI-Tutorials/main/Datasets/population.csv")
llm = OpenAI(
        #api_token="sk-proj-" #or specified as env variable
        )

df = SmartDataframe(df, config={"llm": llm})
response = df.chat("What is the average population?")
print(response)

######

# import pandas as pd
# from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI

# import os
# openai_api_key = os.environ["OPENAI_API_KEY"]
# llm = OpenAI(api_token=openai_api_key)
# pandas_ai = PandasAI(llm)

# df = pd.read_csv("ds_salaries.csv")
# df.head()

# response = pandas_ai.run(df, prompt='List the first 5 job titles by salary in usd')
# print(response)

# response=pandas_ai.run(df, prompt='Plot a bar chart showing top 10 job titles, using different colors for each bar')
# print(response)