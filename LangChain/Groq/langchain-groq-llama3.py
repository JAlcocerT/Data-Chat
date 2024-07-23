#https://python.langchain.com/v0.2/docs/integrations/chat/groq/

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

## export GROQ_API_KEY="sk-..." #linux
## export OPENAI_API_KEY="sk-..." #PS

#https://python.langchain.com/v0.2/docs/concepts/#chat-models
chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    # api_key="" # Optional if not set as an environment variable
)

system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat
print(chain.invoke({"text": "Explain the importance of low latency for LLMs."}))