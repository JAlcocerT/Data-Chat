from llama_index.llms.groq import Groq

#https://console.groq.com/docs/models
llm = Groq(model="llama3-70b-8192" #llama-3.1-405b-reasoning #llama-3.1-8b-instant
           #, api_key="your_api_key"
           )

response = llm.complete("Explain the importance of low latency LLMs")
print(response)