> Thanks to https://github.com/pixegami/langchain-rag-tutorial and https://www.youtube.com/watch?v=tcqEUSNCn8I

**Commented it** [here](https://jalcocert.github.io/JAlcocerT/how-to-use-rags-with-python/#exploring-langchain)


```sh
#wc -w ./data/books/alice_in_wonderland.md #~20k words context
python3 create_database.py
python3 query_data.py "How does Alice meet the Mad Hatter?"
#docker build -t st_datachat_langchainmd .
#sudo docker image ls
#sudo docker compose -d
```

or alternatively:

```sh
docker run -d \
--name st_datachat_langchainmd \
--volume ai_st_datachat_langchainmd:/app \
--workdir /app \
--publish 8505:8501 \
--restart always \
--env MODEL_API_KEY=sk-proj-openaiAPIhere \
st_datachat_langchainmd \
tail -f /dev/null

#docker exec -it st_datachat_langchainmd /bin/bash
```

---

**Venv setup:**

```sh
sudo apt install python3-pip
sudo apt install python3.10-venv
#apt install python3.12-venv
#sudo apt install python3.12-dev
```


```sh
#python -m venv solvingerror_venv #create the venv
python3 -m venv langchainmd_venv #create the venv

#solvingerror_venv\Scripts\activate #activate venv (windows)
source langchainmd_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
#pip install beautifulsoup4 openpyxl pandas numpy==2.0.0
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show beautifulsoup4
pip list
#pip freeze > requirements-snapshot.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```


```sh
pip3 install unstructured[md]
#pip show markdown
#3.7
```