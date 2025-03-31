---
layout: image-right
image: https://cover.sli.dev
---

# LLM API Calls

Use code snippets and get the highlighting directly, and even types hover!

```py {all|1-2|4-7|9-18|20-22|all} twoslash
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you recommend me properties to buy near the Sea?",
        }
    ],
    model="gpt-4o-mini",
    temperature=0.3,
)

completed_message = chat_completion.choices[0].message.content
print(completed_message)
```


<arrow v-click="[5, 6]" x1="350" y1="310" x2="195" y2="334" color="#953" width="2" arrowSize="1" />

<!-- This allow you to embed external code blocks -->
<<< @/snippets/external.ts#snippet

<!-- Footer -->

This is a very simple example. See it [here](https://github.com/JAlcocerT/Streamlit-MultiChat/blob/main/Z_Tests/OpenAI/pyopen.py).

<!-- Inline style -->
<style>
.footnotes-sep {
  @apply mt-5 opacity-10;
}
.footnotes {
  @apply text-sm opacity-75;
}
.footnote-backref {
  display: none;
}
</style>



---
level: 2
---

# Improving API Calls

Lets add some context to our API calls!

Even simple API calls to LLMs can have interesting performance.

See an [example](https://github.com/JAlcocerT/Streamlit-MultiChat/blob/main/Z_Tests/OpenAI/openai_t2t.py):



````md magic-move {lines: true}
```py {*|8-11|*}
#Step 1 - Read the Keys

import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai>0.28

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)
```

```py {*}
#Step 2 - Define a System Prompt

system_must_have= """You are a Real Estate Agent that will make relevant follow-up questions
                                                to the user to provide the best housing option.
                                                When you see a match in the given amenities, you can comment on them.
                                                If there is not a pure match, you will also recommend the 2 closer matches from the offerings we have.
                                                You will also provide the link information as hyperlink for the client to see the offer details. """
```

```py{7|*}
# Step 3 - Query the LLM with better context
chat_completion = client.chat.completions.create(
    messages=[
                     {
                                "role": "system",
                                "content": f"""{SYSTEM_CONTENT_OpenAI}.
                                                These are the properties we have:
                                                  {properties_must_have}  
                                            """,
                            },
                            {"role": "user", "content": prompt}

    ],
    model="gpt-4o-mini",
    temperature=0.8,
)
```


````


---

# API Workflow

You can create diagrams / graphs from textual descriptions, directly in your Markdown.

<div class="grid grid-cols-1 gap-1 pt-10 -mb-10">


```mermaid {theme: 'neutral', scale: 0.7}
graph LR
    C[Load .env, Get API Key];
    C --> D[Initialize OpenAI Client];
    D --> E[System Message];
    E --> F[User Message];
    F --> G[OpenAI API Call - Chat Completion Response];
```

</div>