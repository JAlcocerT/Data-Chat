#https://api.python.langchain.com/en/latest/chat_models/langchain_groq.chat_models.ChatGroq.html
from langchain_groq import ChatGroq

## export GROQ_API_KEY="sk-..." #linux
## $Env:GROQ_API_KEY = "sk-..." #PS

#https://python.langchain.com/v0.2/docs/concepts/#chat-models
model = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
    # other params...
    )

messages = [
    ("system", "You are a helpful translator. Translate the user\
    sentence to French."),
    ("human", "I love programming."),
]

print(model.invoke(messages))
