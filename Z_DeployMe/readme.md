[![Streamlit](https://img.shields.io/badge/Streamlit-1.4.0-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)

---

**Keys:**

* https://console.anthropic.com/workbench/
* https://console.groq.com/keys
* https://platform.openai.com/api-keys

**Deploy as Container**



```sh
git clone 
cd Z_DeployMe
sudo docker-compose up -d
```

> [!IMPORTANT]
> See the related [**Data-Chat Container** of this repo](https://github.com/JAlcocerT/Data-Chat/pkgs/container/data-chat)

---

**Venv Setup**


> As per [Docs](https://jalcocert.github.io/JAlcocerT/useful-python-stuff/)

```sh
#python -m venv mortage_venv #create the venv
python3 -m venv mortagegenai_venv #create the venv

#mortage_venv\Scripts\activate #activate venv (windows)
source mortagegenai_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
#pip install beautifulsoup4 openpyxl pandas numpy==2.0.0
#pip install -r ./Docker/requirements.txt #all at once
pip install -r ./requirements.txt #all at once, it will take ~2/3min

#pip freeze | grep langchain

#pip show beautifulsoup4
pip list
#pip freeze > requirements.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```

```sh
streamlit run RealEstate.py
```