# from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

#from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

# /home/jalcocert/Desktop/langchain-rag-tutorial/solvingerror_venv/lib/python3.10/site-packages/langchain_core/_api/deprecation.py:139:
#  LangChainDeprecationWarning: The class `OpenAIEmbeddings` was deprecated in LangChain 0.0.9 and will be removed in 0.3.0.
#  An updated version of the class exists in the langchain-openai package and should be used instead. 
# To use it run `pip install -U langchain-openai` and import as `from langchain_openai import OpenAIEmbeddings`.

from langchain_community.vectorstores import Chroma
import openai 
from dotenv import load_dotenv
import os
import shutil

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key 
# Change environment variable name from "OPENAI_API_KEY" to the name given in 
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


CHROMA_PATH = "chroma"
DATA_PATH = "data/books"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


# def save_to_chroma(chunks: list[Document]):
#     # Clear out the database first.
#     if os.path.exists(CHROMA_PATH):
#         shutil.rmtree(CHROMA_PATH)

#     # Create a new DB from the documents.
#     db = Chroma.from_documents(
#         chunks, OpenAIEmbeddings("text-embedding-3-large"), persist_directory=CHROMA_PATH
#     )
#     db.persist()
#     print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(),
        #OpenAIEmbeddings(model="text-embedding-3-large"),
        persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil
import chromadb

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key
# Change environment variable name from "OPENAI_API_KEY" to the name given in
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

CHROMA_PATH = "chroma"
DATA_PATH = "data/books"
CHROMA_DOCKER_HOST = "localhost"  # Or the IP address of your Docker host
CHROMA_DOCKER_PORT = "8000"
CHROMA_COLLECTION_NAME = "alice_book_collection"

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma_docker(chunks)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

def save_to_chroma_docker(chunks: list[Document]):
    client_settings = chromadb.config.Settings(
        chroma_client_impl="rest",
        chroma_server_host=CHROMA_DOCKER_HOST,
        chroma_server_http_port=CHROMA_DOCKER_PORT,
    )

    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")

    client = chromadb.HttpClient(host=CHROMA_DOCKER_HOST, port=CHROMA_DOCKER_PORT, settings=client_settings)

    # Get or create the collection
    collection = client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

    # Extract text and metadata from chunks
    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]
    ids = [str(i) for i in range(len(chunks))]  # Generate unique IDs

    # Add embeddings to the collection
    embeddings = embedding_function.embed_documents(texts)
    collection.add(embeddings=embeddings, metadatas=metadatas, ids=ids)

    print(f"Saved {len(chunks)} chunks to Chroma DB in Docker (collection: {CHROMA_COLLECTION_NAME}).")

# Remove the original save_to_chroma function call in main
def main():
    generate_data_store()

# Remove the original save_to_chroma function definition
# def save_to_chroma(chunks: list[Document]):
#     # Clear out the database first.
#     if os.path.exists(CHROMA_PATH):
#         shutil.rmtree(CHROMA_PATH)
#
#     # Create a new DB from the documents.
#     db = Chroma.from_documents(
#         chunks,
#         OpenAIEmbeddings(),
#         #OpenAIEmbeddings(model="text-embedding-3-large"),
#         persist_directory=CHROMA_PATH
#     )
#     db.persist()
#     print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()