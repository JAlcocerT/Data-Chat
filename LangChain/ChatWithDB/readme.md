I made a [**POST**](https://jalcocert.github.io/JAlcocerT/langchain-chat-with-database/) about the [**DB** and CSV Chat **here** →](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/#chat-with-a-db-with-langchain)

**Thanks to AlejandroAO [YT Video](https://www.youtube.com/watch?v=9ccl1_Wu24Q) and  [article](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)**


[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JAlcocerT/Data-Chat/blob/main/LangChain/ChatWithDB/LangChain_MySQL_DB_Chat.ipynb)

> [!IMPORTANT]
> I have made a [**Tech Talk**](https://wearecommunity.io/events/winter-data-meetup2025/talks/84337) about this. Covered on [this post](https://jalcocert.github.io/JAlcocerT/langchain-chat-with-database/).

[![Tech Talk - Chat with your Databases using LLMs](https://img.youtube.com/vi/KXamTdJA-uc/0.jpg)](https://www.youtube.com/watch?v=KXamTdJA-uc)

<div align="center">
[![Tech Talk - Chat with your Databases using LLMs](https://img.youtube.com/vi/KXamTdJA-uc/0.jpg)](https://www.youtube.com/watch?v=KXamTdJA-uc)
</div>

---


### Quick Environment Setup

Follow any of [these Python environment setup](https://jalcocert.github.io/JAlcocerT/useful-python-stuff/#python-apps-reliability) to use the **project dependencies** reliably.

For the `ipynb` vscode will ak you for the `ipykernel` module.

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JAlcocerT/Data-Chat/blob/main/LangChain/ChatWithDB/test_langchainChatDB.ipynb)

Then you will be asked to **select the Python env**.

You will need : https://platform.openai.com/api-keys

<details>
  <summary>Using Python Venv...👇</summary>
  &nbsp;



```sh
python3 -m venv datachat_venv #create the venv Linux
#python -m venv datachat_venv #create the venv W

#datachat_venv\Scripts\activate #activate venv (windows)
source datachat_venv/bin/activate #(linux)
```

Set **API credentials**:

```sh
#source .env
export OPENAI_API_KEY=YOUR_API_KEY
$env:OPENAI_API_KEY="YOUR_API_KEY"
set OPENAI_API_KEY=YOUR_API_KEY
```

Install the libraries one by one...

```sh
pip install langchain==0.1.7 mysql-connector-python 
```


Or with `requirements.txt`:

```sh
#sudo apt install python3.12-venv
python3 -m venv langchainChatDB_venv
#python -m venv langchainChatDB_venv

#Unix
source langchainChatDB_venv/bin/activate
#.\langchainChatDB_venv\Scripts\activate #Windows

source .env
#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY

cd ./LangChain/ChatWithDB
pip install -r requirements.txt


python3 chatwithDB.py
streamlit run langchain_chat_db.py

# git add .
# git commit -m "better langchain chatdb"
# git push
```

</details>


Make sure to have the [Sample DB ready](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/#database-setup) and the [API creds loaded](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/#langchain-setup-to-chat-with-db) and just:


```sh
python3 chatwithDB.py
```

And for the streamlit Chat with DB version:

```sh
streamlit run st_ChatWithDB.py
```


<details>
  <summary>Using Conda...👇</summary>
  &nbsp;

* Get [MiniConda](http://conda.pydata.org/miniconda.html)

```sh
conda create --name myenv python=3.10
```

```sh
pip install langchain
```

```sh
#sudo apt install python3.12-venv
python3 -m venv langchainChatDB_venv
#python -m venv langchainChatDB_venv

#Unix
source langchainChatDB_venv/bin/activate
#.\langchainChatDB_venv\Scripts\activate #Windows

pip install -r requirements.txt


source .env
#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY

streamlit run langchain_chat_db.py

# git add .
# git commit -m "better langchain chatdb"
# git push
```

</details>