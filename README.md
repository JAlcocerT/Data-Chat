# Data-Chat

> Tools to chat with our Data

* LLamaIndex-Mem0 ✔️
    * With OpenAI and Anthropic API
    * HF Embedding Model - https://huggingface.co/BAAI/bge-base-en-v1.5
    * Takes context from a `.md` file at `./datamd`

* LangChain
    * Groq
    * OpenAI
    * qdrant - https://fossengineer.com/selfhosting-vector-admin-docker/
    * ChromaDB -  https://fossengineer.com/selfhosting-chromadb-docker/
        * in-memory - in a python script or jupyter notebook
        * in-memory with persistance - in a script or notebook and save/load to disk
        * in a docker container - as a server running your local machine or in the cloud

* PandasAI with 
    * GroqAPI
    * OpenAI ✔️
    * SQLite DB