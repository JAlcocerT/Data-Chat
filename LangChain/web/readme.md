* https://pythonology.eu/a-rag-web-scraper-with-langchain-ollama-and-chroma/


Thanks to: https://www.youtube.com/watch?v=0zgYu_9WF7A

Try them with: 

```sh
source .venv/bin/activate #(linux)

python3 ./LangChain/web/langchain-scrap-joboffer-ollama.py #fully local
#python3 ./LangChain/web/langchain-scrap-repo-openai.py ##partially local
#python3 ./LangChain/web/langchain-scrap-repo-groq.py #partially local
```

* OpenAI API Keys - <https://platform.openai.com/api-keys>
* Anthropic - <https://console.anthropic.com/settings/keys>
* Groq - <https://console.groq.com/keys>
* For [Ollama](https://github.com/JAlcocerT/Docker/tree/main/AI_Gen/Ollama), you need [this setup](https://fossengineer.com/selfhosting-llms-ollama/)

**Example:**

* Question: what it is this offer about?
* Answer: Based on the job offer context and the provided Zadania (duties), I would guess that this is an opportunity for a Data Analyst or Business Intelligence Analyst position in the data analytics space.

The specific tasks mentioned, such as:

* Definiowanie wizji, celów i kierunków rozwoju w oparciu o potrzeby rynku oraz cele organizacji (Tworzenie i wdrażanie strategii produktowej),
* Zarządzanie cyklem życia produktów GenAI (łączenie wiedzy technicznej z perspektywą biznesową, etc.),
* Współpraca z zespołami scrumowymi (priorytetyzacja backlogu, planowanie sprintów, etc.) oraz
* Analiza rynku i potrzeb klientów (Analiza rynku i potrzeb klientów) are all typical tasks associated with data analyst or business intelligence analyst roles.

Additionally, the mention of "KPI" (Key Performance Indicators), " danych rynkowe" (market data), and "informacje zwrotnej od klientów" (client feedback data) also suggest a role in data analysis and management.

---

```sh
cd ./LangChain/web
#python -m venv solvingerror_venv #create the venv
python3 -m venv reporeadweb_venv #create the venv

#reporeadweb_venv\Scripts\activate #activate venv (windows)
source reporeadweb_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
# !pip install requests
# !pip install beautifulsoup4
# !pip install langchain-community

#pip install beautifulsoup4 openpyxl pandas numpy==2.0.0
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show beautifulsoup4
pip list
pip freeze > requirements-output.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```