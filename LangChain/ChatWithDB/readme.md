[I commented the **DB** and CSV Chat **here** →](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data/#chat-with-a-db-with-langchain)

**Thanks to AlejandroAO [YT Video](https://www.youtube.com/watch?v=9ccl1_Wu24Q) and  [article](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)**


### Quick Setup - Venv

<details>
  <summary>Using Python Venv...👇</summary>
  &nbsp;


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