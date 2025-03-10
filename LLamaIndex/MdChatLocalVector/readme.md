> [!IMPORTANT]
> Kudos to [**Samual Chan** YT Video](https://www.youtube.com/watch?v=OzDhJOR5IfQ) and source code: https://github.com/onlyphantom/llm-python/blob/main/10_journal.py


---


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