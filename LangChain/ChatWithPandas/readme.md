[There is a **blog post** about this topic **here** →](https://jalcocert.github.io/JAlcocerT/using-langchain-with-pandas-df)

* Time to improve Trip-Planner

### Quick Environment Setup

1. Install [Python](https://jalcocert.github.io/JAlcocerT/guide-python/#installing-python-)

2. Follow any of [these Python environment setup](https://jalcocert.github.io/JAlcocerT/useful-python-stuff/#python-apps-reliability) to use the **project dependencies** reliably.

<details>
  <summary>Using Python Venv...👇</summary>
  &nbsp;


```sh
pip install langchain
```

```sh
#sudo apt install python3.12-venv
python3 -m venv langchainChatPandas_venv
#python -m venv langchainChatDB_venv

#Unix
source langchainChatPandas_venv/bin/activate
#.\langchainChatDB_venv\Scripts\activate #Windows

cd ./LangChain/ChatWithPandas
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