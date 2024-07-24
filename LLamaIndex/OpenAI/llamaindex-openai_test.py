from llama_index.llms.openai import OpenAI

resp = OpenAI(model="gpt-4o"
              #,api_key="BAD_KEY" #if you want to specify it here
              ).complete("Which model are you? ")
#resp = OpenAI(model="gpt-3.5-turbo").complete("Paul Graham is ")
print(resp)