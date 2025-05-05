import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama.llms import OllamaLLM
#from langchain.chains import RetrievalQA

def get_response_from_website_with_chunks(
    ollama_base_url: str,
    embedding_model_name: str,
    llm_model_name: str,
    question: str,
    website_url: str,
    content_class: str = "MuiBox-root css-rcazos", #class="MuiBox-root css-16nvqld" class="MuiBox-root css-rcazos"
    chunk_size: int = 1200,
    chunk_overlap: int = 100,
    search_kwargs_k: int = 3
) -> str:
    """
    Scrapes a website, creates embeddings using Ollama,
    stores them in Chroma, retrieves relevant chunks, and
    answers a question using an Ollama language model,
    following the provided code chunk structure.

    Args:
        ollama_base_url: The base URL of your Ollama server (e.g., "http://localhost:11434").
        embedding_model_name: The name of the Ollama embedding model (e.g., "all-minilm").
        llm_model_name: The name of the Ollama language model to use (e.g., "llama3.2:1b").
        question: The question you want to ask about the website content.
        website_url: The URL of the website to process.
        content_class: The CSS class name of the main content area on the website.
        chunk_size: The size of each text chunk.
        chunk_overlap: The overlap between adjacent text chunks.
        search_kwargs_k: The number of top documents to retrieve.

    Returns:
        A string containing the answer to the question based on the website content.
    """
    try:
        # Step 1: Web Scraping with LangChain
        bs4_strainer = bs4.SoupStrainer(class_=(content_class))
        loader = WebBaseLoader(
            web_paths=(website_url,),
            bs_kwargs={"parse_only": bs4_strainer},
        )
        docs = loader.load()

        # Step 2: Text Splitting for Manageable Chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap, add_start_index=True
        )
        all_splits = text_splitter.split_documents(docs)

        # Step 3: Generating Embeddings with Ollama and Chroma
        local_embeddings = OllamaEmbeddings(base_url=ollama_base_url, model=embedding_model_name)
        vectorstore = Chroma.from_documents(documents=all_splits, embedding=local_embeddings)

        # Step 4: Implementing the Retrieval System
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": search_kwargs_k})
        retrieved_docs = retriever.invoke(question)
        context = ' '.join([doc.page_content for doc in retrieved_docs])

        # Step 5: Generating Responses with a Language Model
        llm = OllamaLLM(base_url=ollama_base_url, model=llm_model_name)
        response = llm.invoke(f"""Answer the question according to the job offer context given. Reply in English and try to guess for which position it is in the Data Analytics Space. Justify your answer.
                   Question: {question}.
                   Context: {context}
        """)
        return response

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":

    ###Change these parameters and lets go###
    ollama_url = "http://192.168.1.5:11434"  # Replace with your Ollama server URL if different
    embedding_model = "all-minilm"
    llm_model = "llama3.2:1b"
    user_question = "what it is this offer about?"
    target_website = "https://justjoin.it/job-offer/link-group-product-manager-warszawa-ai"
    content_area_class = "MuiBox-root css-rcazos" # Use the same class as in the example

    answer = get_response_from_website_with_chunks(
        ollama_url,
        embedding_model,
        llm_model,
        user_question,
        target_website,
        content_class=content_area_class
    )
    print(f"Question: {user_question}")
    print(f"Answer: {answer}")