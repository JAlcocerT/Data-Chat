# Data-Chat

> Tools to chat with our Data

* LLamaIndex
    * With OpenAI ✔️
    * With Groq
    * With Mem0 ✔️
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

```sh
python -m venv properties_venv #create the venv | python3 if you are on linux

properties_venv\Scripts\activate #activate venv (windows)
source properties_venv/bin/activate #(linux)
```

```sh
export GROQ_API_KEY=YOUR_API_KEY
$env:GROQ_API_KEY="YOUR_API_KEY"
set GROQ_API_KEY=YOUR_API_KEY

export OPENAI_API_KEY=YOUR_API_KEY
$env:OPENAI_API_KEY="YOUR_API_KEY"
set OPENAI_API_KEY=YOUR_API_KEY

export ANTHROPIC_API_KEY=YOUR_API_KEY
$env:ANTHROPIC_API_KEY="YOUR_API_KEY"
set ANTHROPIC_API_KEY=YOUR_API_KEY
```