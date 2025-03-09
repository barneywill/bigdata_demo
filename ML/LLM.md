# OpenAI

- LLM(Large Language Model)
- RAG(Retrieval Augmented Generation)


## 1 Install
```
pip install openai
export OPENAI_API_KEY=***
```

## 2 OpenAI
```
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(model='gpt-4o', messages=[{"role":"user", "content":"my question?"}])
response
response.choices[0].message.content
```

## 3 Search
### 3.1 minsearch
```
import minsearch
import json

documents = [{"question":"","text":"","section":"","course":""}]
index = minsearch.Index(text_fields=["question", "text", "section"], keyword_fields=["course"])
index.fit(documents)

results = index.search(query='my question?', filter_dict={'course':'a'}, boost_dict={'question':3.0}, num_results=5)
```

### 3.2 ElasticSearch
```
from ealsticsearch import Elasticsearch
es_client = Elasticsearch('http://localhost:9200')
es_client.info()

index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"}
        }
    }
}
index_name = "course_question"
es_client.indices.create(index=index_name, body=index_settings)

from tqdm.auto import tqdm
for doc in tqdm(documents):
    es_client.index(index=index_name, document=doc)

search_query = {
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": "my question?",
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "a"
                }
            }
        }
    }
}
response = es_client.search(index=index_name, body=search_query)
response
results = []
for hit in response['hits']['hits']:
    results.append(hit['_source'])
```

### 3.3 prompt
```
context = ''
for doc in results:
    context += f"section: {doc['section']} \nquestion: {doc['question'] \nanswer: {doc['text']}} \n\n"

prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database. Use only the facts from the CONTEXT when answer the QUESTION.
If the CONTEXT doesn't contain the answer, output NONE.

QUESTION: {question}

CONTEXT: 
{context}
"""
prompt = prompt_template.format(question=q, context=context)
```

## 4 rag

### 4.1 OpenAI
```
def llm(prompt):
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

llm(prompt)
```

### 4.2 google-t5
```
import os
os.environ['HF_HOME'] = '/run/cache/'

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl", device_map="auto")

def llm(prompt, generate_params=None):
    if generate_params is None:
        generate_params = {}

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
    outputs = model.generate(
        input_ids,
        max_length=generate_params.get("max_length", 100),
        num_beams=generate_params.get("num_beams", 5),
        do_sample=generate_params.get("do_sample", False),
        temperature=generate_params.get("temperature", 1.0),
        top_k=generate_params.get("top_k", 50),
        top_p=generate_params.get("top_p", 0.95),
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result
```

### 4.3 microsoft-phi-3
```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def llm(prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]

    generation_args = {
        "max_new_tokens": 500,
        "return_full_text": False,
        "temperature": 0.0,
        "do_sample": False,
    }

    output = pipe(messages, **generation_args)
    return output[0]['generated_text'].strip()
```

### 4.4 mistral
```
os.environ['HF_TOKEN'] = 'hf_blabla'
from huggingface_hub import login
login(token=os.environ['HF_TOKEN'])

from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1", device_map="auto", load_in_4bit=True
)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", padding_side="left")

from transformers import pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def llm(prompt):
    response = generator(prompt, max_length=500, temperature=0.7, top_p=0.95, num_return_sequences=1)
    response_final = response[0]['generated_text']
    return response_final[len(prompt):].strip()
```

### 4.5 ollama
https://ollama.com/
```
ollama run phi3
```

compatible with openai api
```
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

def llm(prompt):
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

llm(prompt)
```

## 5 streamlit
```
import streamlit as st
import time

def rag(input):
    return 'hello'

def main():
    st.title("RAG Function Invocation")

    user_input = st.text_input("Enter your input:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)

if __name__ == "__main__":
    main()
```

## 6 Metrics
- Vector similarity between expected and LLM answers
- LLM-as-a-judge 
  - to compute toxicity of LLM answer
  - to assess quality of LLM answer
- User feedbacks
- System metrics(4x golden signals): Latency, Traffic, Errors, Saturation
- Cost

### Evaluation
- offline evaluation
  - cosine similarity
  - LLM-as-a-judge
  - hitrate
  - mrr
- online evaluation
  - A/B test
  - user feedback
- monitoring
  - overall health of the system
  - How good the answer is
