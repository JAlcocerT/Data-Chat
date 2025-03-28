---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Chat with Real Estate Data
info: |
  ## Slidev Data Chat
  Using LLMs with your Data.

  Learn more at [jalcocertech.com](https://jalcocertech.com)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
fonts:
  # basically the text
  sans: Roboto
  # use with `font-serif` css class from UnoCSS
  serif: Robot Slab
  # for code blocks, inline code, etc.
  mono: Fira Code
---

# RAG-Powered Real Estate Matching

April 4, 2025

Jesus Alcocer Tagua



<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  Let's Get Started <carbon:arrow-right />
</div>

<div class="abs-br m-6 text-xl">
  <button @click="$slidev.nav.openInEditor" title="Open in Editor" class="slidev-icon-btn">
    <carbon:edit />
  </button>
  <a href="https://github.com/JAlcocerT/Data-Chat" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
---

# AI for Real Estate: Our Agenda

* **Intro:** 🚀 AI in Real Estate & Personalized Recommendations 🎯
* **API Calls:** 📞 Basic Matching (👍 Pros & 👎 Cons)
* **RAG:** 🧠 Advanced Personalization & 📈 Real-Time Data
* **Comparison:** ⚖️ API vs. RAG Use Cases
* **Demo:** 🎬 Client Matching - API vs. RAG
* **Conclusions**
* **Q&A** 🗣️

<!--
You can have `style` tag in markdown to override the style for the current page.
Learn more: https://sli.dev/features/slide-scope-style
-->

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

<!--
Here is another comment.
-->


---
layout: two-cols
layoutClass: gap-16
---

# Table of contents


* **Intro:** 🚀 AI in Real Estate & Personalized Recommendations 🎯
* **API Calls:** 📞 Basic Matching (👍 Pros & 👎 Cons)
* **RAG:** 🧠 Advanced Personalization & 📈 Real-Time Data
* **Comparison:** ⚖️ API vs. RAG Use Cases
* **Demo:** 🎬 Client Matching - API vs. RAG
* **Conclusions**
* **Q&A** 🗣️

::right::

<Toc text-sm minDepth="1" maxDepth="2" />


---
src: ./pages/code-llm-api-rag.md
hide: false
---


---
class: px-20
---

# Do More with RAGs

Slidev comes with powerful theming support. Themes can provide styles, layouts, components, or even configurations for tools. Switching between themes by just **one edit** in your frontmatter:

<div grid="~ cols-2 gap-2" m="t-2">

```yaml
Use RAG to chat with your DataBase 
```

```yaml
Use RAG to chat with PDFs
```

<img border="rounded" src="https://github.com/JAlcocerT/JAlcocerT/blob/main/static/blog_img/GenAI/dbchat/langchain-AI.jpeg?raw=true" alt="">

<img border="rounded" src="https://github.com/JAlcocerT/ask-multiple-pdfs/blob/main/docs/PDF-LangChain.jpg?raw=true" alt="">

</div>

Read more about [How to use a theme](https://sli.dev/guide/theme-addon#use-theme) and
check out the [Awesome Themes Gallery](https://sli.dev/resources/theme-gallery).

---

# Clicks Animations

You can add `v-click` to elements to add a click animation.

<div v-click>

This shows up when you click the slide:

```html
<div v-click>This shows up when you click the slide.</div>
```

</div>

<br>

<v-click>

The <span v-mark.red="3"><code>v-mark</code> directive</span>
also allows you to add
<span v-mark.circle.orange="4">inline marks</span>
, powered by [Rough Notation](https://roughnotation.com/):

```html
<span v-mark.underline.orange>inline markers</span>
```

</v-click>

<div mt-20 v-click>

[Learn more](https://sli.dev/guide/animations#click-animation)

</div>



---

# Diagrams

You can create diagrams / graphs from textual descriptions, directly in your Markdown.

<div class="grid grid-cols-2 gap-1 pt-10 -mb-10">


```mermaid {theme: 'neutral', scale: 0.4}
graph TD
    C[Load .env, Get API Key];
    C --> D[Initialize OpenAI Client];
    D --> E[System Message];
    E --> F[User Message];
    F --> G[OpenAI API Call - Chat Completion Response];
```

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

Learn more: [Mermaid Diagrams](https://sli.dev/features/mermaid) and [PlantUML Diagrams](https://sli.dev/features/plantuml)


---
layout: image-right
image: https://cover.sli.dev
---

# Implementing a RAG

See an example [here](https://github.com/JAlcocerT/Data-Chat/tree/main/LLamaIndex/With_Mem0)


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
src: ./pages/thanks-qna.md
hide: false
---



---
src: ./pages/references.md
hide: false
---




<!-- <PoweredBySlidev mt-10 /> -->