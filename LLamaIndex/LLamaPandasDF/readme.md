* [Pandas Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/)


[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JAlcocerT/Data-Chat/blob/main/LangChain/ChatWithDB/test_langchainChatDB.ipynb)


### Quick Environment Setup

Follow any of [these Python environment setup](https://jalcocert.github.io/JAlcocerT/useful-python-stuff/#python-apps-reliability) to use the **project dependencies** reliably.

For the `ipynb` vscode will ak you for the `ipykernel` module.

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JAlcocerT/Data-Chat/blob/main/LLamaIndex/LLamaPandasDF/llamaindex_pandasDF.ipynb)

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
export OPENAI_API_KEY=YOUR_API_KEY
$env:OPENAI_API_KEY="YOUR_API_KEY"
set OPENAI_API_KEY=YOUR_API_KEY
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

cd ./LLamaIndex/LLamaPandasDF
pip install -r requirements.txt


python3 chatwithDB.py
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