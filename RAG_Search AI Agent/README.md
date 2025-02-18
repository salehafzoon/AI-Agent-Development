# Sample AI-Agent Implementation using LangChain
![Python](https://img.shields.io/badge/Python-Compatible-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white")
[![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/models)
LangChain 🦜

Includes:
- Retriever tool
- Web Search tool
- OpenAI-based chat interface
- Open-source-based chat interfaces

## Environment variables setup:
- Create the .env file that contains following variables:
```bash
HUGGINGFACEHUB_API_TOKEN= "hugging_face_token"
OPENAI_API_KEY= "openai_api_key"
TAVILY_API_KEY= "tavily_api_key"
USER_AGENT= "browser information"
```
- Load them via the following code:
```python
from dotenv import load_dotenv

load_dotenv()                   # Loading API key from .env file
```


Sample prompts and responses:
```
Prompt: What is the mission of DASA?
----------------------------------------------------------------------
Response: The mission of DASA (DevOps Agile Skills Association) is to empower organizations to transform into high-performance digital organizations by providing guidance, training, and community support to help teams improve efficiency...
```

```
Prompt: How is the weather in Sydney right now?
----------------------------------------------------------------------
Response: The current weather in Sydney is partly cloudy with a temperature of 26.4°C (79.5°F)...
```


## Getting Started

#### 1. Clone and Install

```bash
# Clone the repo

git clone https://github.com/salehafzoon/AI-Agent-Development.git   
```
