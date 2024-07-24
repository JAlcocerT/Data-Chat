from langchain.llms import OpenAI
from llama_index.llms.langchain import LangChainLLM


llm = LangChainLLM(llm=OpenAI())

response_gen = llm.stream_complete("Which Model are you? can you help me to code in python?")

for delta in response_gen:
    print(delta.delta, end="")