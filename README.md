<div align="center">
  <h1>Data-Chat</h1>
</div>

<div align="center">
  <h3>Chat over Custom Data</h3>
</div>


<div align="center">
  <h4>LangChain | LlamaIndex | PandasAI | HayStack</h3>
</div>

<div align="center">
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat?tab=GPL-3.0-1-ov-file" style="margin-right: 5px;">
    <img alt="Code License" src="https://img.shields.io/badge/License-GPLv3-blue.svg" />
  </a>
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GHA_MultiArch.yml" style="margin-right: 5px;">
    <img alt="GH Actions Workflow" src="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GHA_MultiArch.yml/badge.svg" />
  </a>
  <a href="https://GitHub.com/JAlcocerT/Streamlit-Multichat/graphs/commit-activity" style="margin-right: 5px;">
    <img alt="Mantained" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://www.python.org/downloads/release/python-312">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.12-blue.svg" />
  </a>
</div>


> [!IMPORTANT]
> See the related [**Container** of this repo](https://github.com/JAlcocerT/Data-Chat/pkgs/container/data-chat)


---

> Tools to Chat with our Data

* LLamaIndex
    * With OpenAI ✔️
    * With Groq ✔️
    * With Anthropic ✔️
    * With LangChain ✔️
    * With Mem0 ✔️
        * With OpenAI and Anthropic API
        * HF Embedding Model - https://huggingface.co/BAAI/bge-base-en-v1.5
        * Takes context from a `.md` file at `./datamd`

* [LangChain](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/)
    * Groq ✔️
    * OpenAI ✔️
    * Anthropic ✔️
    * qdrant - https://fossengineer.com/selfhosting-vector-admin-docker/
    * ChromaDB -  https://fossengineer.com/selfhosting-chromadb-docker/
        * in-memory - in a python script or jupyter notebook
        * in-memory with persistance - in a script or notebook and save/load to disk
        * in a docker container - as a server running your local machine or in the cloud
    * [ChatWithPDF Repo](https://github.com/JAlcocerT/ask-multiple-pdfs/) and Blog [Post](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-pdfs/)
    * [ChatWithCSV Repo](https://github.com/JAlcocerT/langchain-ask-csv) and Blog [Post](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/#chat-with-csv-with-langchain)
    * ChatWithDB - Blog [Post](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/) - `./LangChain/ChatWithDB`
    * Chat with Pandas DF - [Blog Post](https://jalcocert.github.io/JAlcocerT/using-langchain-with-pandas-df) `./LangChain/ChatWithPandas`

* [**PandasAI**](https://jalcocert.github.io/JAlcocerT/how-to-use-pandasAI/) with 
    * GroqAPI
    * OpenAI ✔️
    * SQLite DB

* [EmbedChain/Mem0](https://jalcocert.github.io/JAlcocerT/how-to-use-rags-with-python/#embedchain---mem0)

* [HayStack](https://jalcocert.github.io/JAlcocerT/how-to-use-rags-with-python/#haystack-as-rag-framework)



[![Tech Talk - Chat with your Databases using LLMs](https://img.youtube.com/vi/KXamTdJA-uc/0.jpg)](https://www.youtube.com/watch?v=KXamTdJA-uc)


---

## Quick Venv Setup

```sh
python3 -m venv datachat_venv #create the venv Linux
#python -m venv datachat_venv #create the venv W

#datachat_venv\Scripts\activate #activate venv (windows)
source datachat_venv/bin/activate #(linux)
```

Set **API credentials**:

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