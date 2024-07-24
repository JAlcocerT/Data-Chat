from llama_index.llms.groq import Groq

llm = Groq(model="llama3-70b-8192"
           #, api_key="your_api_key"
           )

response = llm.complete("Explain the importance of low latency LLMs")
print(response)
