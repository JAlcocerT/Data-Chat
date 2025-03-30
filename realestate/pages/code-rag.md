---

# RAG Concepts

You can create diagrams / graphs from textual descriptions, directly in your Markdown.

<div class="grid grid-cols-1 gap-1 pt-10 -mb-10">

```mermaid {scale: 0.4}
mindmap
  root((RAG Workflow))
    Data Ingestion
      Documents Source
        SimpleDirectoryReader("./datamd")
      Document Loading
    Indexing
      Embedding Model
        HuggingFaceEmbedding("BAAI/bge-base-en-v1.5")
      Vector Store Index
        VectorStoreIndex.from_documents(documents)
    User Interaction
      User Query
        "Question: ..."
      Memory Storage
        Memory.add(question, user_id=user_id)
      Memory Retrieval
        Memory.search(query, user_id=user_id)
    Query Processing
      Contextualization
        Combine user query with memory
      Query Engine
        index.as_query_engine(similarity_top_k=3)
      Property Retrieval
        Query vector store index
    Response Generation
      LLM (Anthropic)
        claude-3-5-sonnet-20240620
      Generate Answer
        Based on retrieved properties and context
      Output
        "Answer: ..."
```

</div>


---
layout: image-right
image: https://github.com/JAlcocerT/Data-Chat/blob/main/realestate/RE-bot.jpeg?raw=true
---

<!-- 
image: RE-bot.jpeg 
-->

# Implementing a RAG

See an example [here](https://github.com/JAlcocerT/Data-Chat/tree/main/LLamaIndex/With_Mem0)

<logos-claude />

<logos-openai />


```plantuml {scale: 0.7}
@startuml

package "Some Group" {
  HTTP - [First Component]
  [Another Component]
}

node "Other Groups" {
  FTP - [Second Component]
  [First Component] --> FTP
}

cloud {
  [Example 1]
}

database "MySql" {
  folder "This is my folder" {
    [Folder 3]
  }
  frame "Foo" {
    [Frame 4]
  }
}

[Another Component] --> [Example 1]
[Example 1] --> [Folder 3]
[Folder 3] --> [Frame 4]

@enduml
```


---
class: px-20
---

# Do More with RAGs

RAGs can have many more use cases. From Chatting with a DB, to talk with PDF or CSV data.

<div grid="~ cols-2 gap-2" m="t-2">

```yaml
Use RAG to chat with your DataBase 
```

```yaml
Use RAG to chat with PDFs
```

<!-- <img border="rounded" src="https://github.com/JAlcocerT/JAlcocerT/blob/main/static/blog_img/GenAI/dbchat/langchain-AI.jpeg?raw=true" alt=""> -->
<img border="rounded" src="https://github.com/JAlcocerT/JAlcocerT/blob/main/static/blog_img/GenAI/dbchat/langchain-AI.jpeg?raw=true" alt="" style="width: 70%;">
<img border="rounded" src="https://github.com/JAlcocerT/ask-multiple-pdfs/blob/main/docs/PDF-LangChain.jpg?raw=true" alt="">

</div>

Read more about [RAG use cases](https://jalcocert.github.io/JAlcocerT/how-to-chat-with-your-data).

---