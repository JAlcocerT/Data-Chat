from langchain.document_loaders import TextLoader
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator

document_path = "./houses.txt"
loader = TextLoader(document_path)
documents = loader.load()

index = VectorstoreIndexCreator().from_loaders([loader])

qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=index.vectorstore.as_retriever())

query = "What it is the most expensive house in the list?"
result = qa.run(query)
print(result)