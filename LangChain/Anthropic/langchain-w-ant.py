from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model='claude-3-5-sonnet-20240620')


# llm = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
#     # base_url="...",
#     # organization="...",
#     # other params...
# )

messages = [
    (
        "system",
        "You are a helpful assistant that knows Python. Help the user with the questions.",
    ),
    ("human", "do you know what it is python flet?"),
]
ai_msg = model.invoke(messages)
#print(ai_msg)
print(ai_msg.content)