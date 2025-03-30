<div align="center">
  <a href="https://www.python.org/downloads/release/python-310">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.10-blue.svg" />
  </a>
</div>


* https://jalcocert.github.io/JAlcocerT/python-real-estate-mortage-calculator/
* https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data
* https://jalcocert.github.io/JAlcocerT/streamlit-is-cool/


```sh
python3 Chat_with_md.py
streamlit run st_chatmd_rag.py --server.fileWatcherType none
```


**Keys:**

* https://console.anthropic.com/settings/keys
* https://platform.openai.com/api-keys

---


* https://github.com/JAlcocerT/Data-Chat/pkgs/container/data-chat

```sh
docker pull ghcr.io/jalcocert/data-chat:properties
```

---

> [!IMPORTANT]
> This is just a **sample of a Real Estate Agent** using LLama-Index and Mem0 (OpenAI + Anthropic API's)

---

* https://pypi.org/project/mem0ai/
* https://pypi.org/project/llama-index/

* https://www.anthropic.com/api
  * https://console.anthropic.com/settings/keys
* https://platform.openai.com/
  * https://platform.openai.com/api-keys

  ---

  This code defines a `RealEstateAssistant` class that simulates a real estate agent's conversational AI, using OpenAI's GPT-4o, Anthropic's Claude 3.5 Sonnet, and LlamaIndex for document querying. Here's a breakdown of the code:

**1. Imports and Environment Setup:**

* `os`: For interacting with the operating system (e.g., getting environment variables).
* `csv`: (Commented out) Likely intended for loading data from CSV files.
* `openai.OpenAI`: For interacting with OpenAI's API.
* `mem0.Memory`: A custom class (likely defined in `mem0.py`) for storing and retrieving conversational memories.
* `llama_index.llms.anthropic.Anthropic`: For using Anthropic's Claude models with LlamaIndex.
* `llama_index.embeddings.huggingface.HuggingFaceEmbedding`: For embedding text using Hugging Face models.
* `llama_index.core`: for interacting with LlamaIndex core functions.
* `llama_index.core.Settings`: For setting global settings for LlamaIndex.
* `llama_index.core.VectorStoreIndex`: For creating and querying vector store indexes.
* `llama_index.core.SimpleDirectoryReader`: For loading documents from a directory.
* `dotenv.load_dotenv`: For loading environment variables from a `.env` file.
* The code loads API keys from environment variables using `load_dotenv()` and `os.getenv()`.

**2. `RealEstateAssistant` Class:**

* **`__init__(self)`:**
    * Initializes the OpenAI client (`self.client`).
    * Initializes the `Memory` object (`self.memory`).
    * Sets up the initial system message for the conversation (`self.messages`). This message instructs the AI to act as a real estate agent.
    * Initializes `self.follow_up_count` to track the number of user questions.
    * Sets up Llama Index with the Anthropic Claude model and HuggingFace Embedding model.
    * Loads documents from the `./datamd` directory using `SimpleDirectoryReader` and creates a `VectorStoreIndex`. This index is used to query the documents based on user queries.
* **`ask_question(self, question, user_id)`:**
    * This is the main function for handling user questions.
    * It fetches previous memories related to the current question using `self.search_memories()`.
    * It constructs a prompt that includes the user's question and any relevant previous memories.
    * It appends the user's question to the `self.messages` list.
    * It sends the conversation history to the GPT-4o model using `self.client.chat.completions.create()` and gets the AI's response.
    * It appends the AI's response to the `self.messages` list.
    * It adds the user's question to the `self.memory`.
    * It increments `self.follow_up_count`.
    * If `self.follow_up_count` reaches 3, it calls `self.query_properties()` to query the document index and resets the counter.
    * Returns the AI's response.
* **`get_memories(self, user_id)`:**
    * Retrieves all memories for a given `user_id` from the `self.memory` object.
    * Returns a list of memory texts.
* **`search_memories(self, query, user_id)`:**
    * Searches the `self.memory` for memories related to the given `query` for a specific `user_id`.
    * Returns a list of matching memory texts.
* **`query_properties(self, user_id)`:**
    * Retrieves all memories for the given `user_id`.
    * Joins the memory texts into a single query string.
    * Creates a query engine from the `self.index`.
    * Queries the index using the combined memory query.
    * Resets the follow up count.
    * Returns the response from the Llama Index query.

**3. `main()` Function:**

* Creates an instance of the `RealEstateAssistant` class.
* Enters a loop that prompts the user for questions.
* Calls `ai_assistant.ask_question()` to get the AI's response.
* Prints the AI's response and the user's memories.
* If the answer is not a string, it prints the property query response.
* Exits the loop when the user enters 'q' or 'exit'.

**Key Functionality:**

* **Conversational AI:** The code simulates a conversation with a real estate agent, maintaining context using the `self.messages` list and `Memory` class.
* **Memory Management:** The `Memory` class (likely a custom implementation) stores and retrieves user interactions, allowing the AI to remember past conversations.
* **Document Querying:** LlamaIndex is used to query a set of documents (likely containing real estate listings) based on the user's conversation. This allows the AI to provide relevant information about properties.
* **Contextual Responses:** The AI combines user input and previous memories to generate more relevant and contextual responses.
* **Follow-up Question Handling:** The `follow_up_count` variable ensures that the AI queries the document index after a certain number of user questions, using the conversation history as context.
* **Environment Variables:** The code uses `.env` files to store API keys and other sensitive information.

In essence, this code creates a conversational AI that can answer real estate-related questions and provide information about properties by leveraging both a large language model and a document indexing and retrieval system.