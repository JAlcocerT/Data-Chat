import os
import streamlit as st
from openai import OpenAI
from mem0 import Memory
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API keys and other environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DATA_DIRECTORY = os.getenv("DATA_DIRECTORY", "./datamd")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", 0.0))

SYSTEM_CONTENT_OpenAI = os.getenv("SYSTEM_CONTENT", """You are a Real Estate Agent that will make relevant follow-up questions
                                                to the user to provide the best housing option.
                                                When you see a match in the given amenities, you can comment on them.
                                                If there is not a pure match, you will also recommend the 2 closer matches from the offerings we have.
                                                You will also provide the link information as hyperlink for the client to see the offer details. """)

class RealEstateAssistant:
    def __init__(self, data_directory):
        self.client = OpenAI()
        self.memory = Memory()
        self.messages = [{"role": "system", "content": SYSTEM_CONTENT_OpenAI}]
        self.follow_up_count = 0

        # Set up Llama Index with Anthropic
        llm = Anthropic(temperature=0.0, model='claude-3-5-sonnet-20240620')
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        Settings.llm = llm
        Settings.embed_model = embed_model
        Settings.chunk_size = 512

        # Load documents and create the index
        documents = SimpleDirectoryReader(data_directory).load_data()
        self.index = VectorStoreIndex.from_documents(documents)

    def ask_question(self, question, user_id):
        # Fetch previous related memories
        previous_memories = self.search_memories(question, user_id=user_id)
        prompt = question
        if previous_memories:
            prompt = f"User input: {question}\nPrevious memories: {previous_memories}"
        self.messages.append({"role": "user", "content": prompt})

        # Generate response using GPT-4o
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        # Store the question in memory
        self.memory.add(question, user_id=user_id)
        self.follow_up_count += 1

        # After 3 follow-up questions, feed memories to the Llama Index
        if self.follow_up_count >= 3:
            return self.query_properties(user_id)

        return answer

    def get_memories(self, user_id):
        memories = self.memory.get_all(user_id=user_id)
        return [m['text'] for m in memories]

    def search_memories(self, query, user_id):
        memories = self.memory.search(query, user_id=user_id)
        return [m['text'] for m in memories]

    def query_properties(self, user_id):
        memories = self.get_memories(user_id=user_id)
        query = " ".join(memories)
        query_engine = self.index.as_query_engine(similarity_top_k=3)
        response = query_engine.query(f"User's memories: {query}")
        self.follow_up_count = 0  # Reset follow-up count after query
        return response

def st_openai_md_genai():
    st.header("Explore our Properties 🏠")
    st.subheader("Talk with our Real Estate Agent - RAG version")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.ai_assistant = RealEstateAssistant(DATA_DIRECTORY)  # Initialize the assistant

    user_id = "user_123"  # Static user ID for simplicity

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask your question:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            answer = st.session_state.ai_assistant.ask_question(prompt, user_id=user_id)
            if isinstance(answer, str):
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                memories = st.session_state.ai_assistant.get_memories(user_id=user_id)
                st.markdown("Memories:")
                for memory in memories:
                    st.markdown(f"- {memory}")
                st.markdown("-----")
            else:
                message_placeholder.markdown(f"Properties Query Response: {answer}")
                st.session_state.messages.append({"role": "assistant", "content": f"Properties Query Response: {answer}"})

if __name__ == "__main__":
    st_openai_md_genai()