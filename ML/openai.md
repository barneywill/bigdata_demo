# OpenAI

- LLM(Large Language Model)
- RAG(Retrieval Augmented Generation)


## Install
```
pip install openai
export OPENAI_API_KEY=***
```

## OpenAI
```
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(model='gpt-4o', messages=[{"role":"user", "content":"my question?"}])
response
response.choices[0].message.content
```

## Search
### minsearch
```
import minsearch
import json

documents = [{"question":"","text":"","section":"","course":""}]
index = minsearch.Index(text_fields=["question", "text", "section"], keyword_fields=["course"])
index.fit(documents)

results = index.search(query='my question?', filter_dict={'course':'a'}, boost_dict={'question':3.0}, num_results=5)
```

### ElasticSearch
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

### OpenAI
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

client = OpenAI()
response = client.chat.completions.create(model='gpt-4o', messages=[{"role":"user", "content":prompt}])
response
```

