from llama_index.llms.anthropic import Anthropic
from llama_index.core import Settings

tokenizer = Anthropic().tokenizer
Settings.tokenizer = tokenizer

import os

#os.environ["ANTHROPIC_API_KEY"] = "YOUR ANTHROPIC API KEY"

from llama_index.llms.anthropic import Anthropic

# To customize your API key, do this
# otherwise it will lookup ANTHROPIC_API_KEY from your env variable
# llm = Anthropic(api_key="")

llm = Anthropic(model="claude-3-5-sonnet-20240620")

resp = llm.complete("What do you know about python flet?")
print(resp)

# from llama_index.core.llms import ChatMessage
# from llama_index.llms.anthropic import Anthropic

# messages = [
#     ChatMessage(
#         role="system", content="You are a pirate with a colorful personality"
#     ),
#     ChatMessage(role="user", content="Tell me a story"),
# ]
# resp = Anthropic(model="claude-3-opus-20240229").chat(messages)

#print(resp)