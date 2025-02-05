import os
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

# OLLAMA_MODEL = "deepseek-r1" # currently does not support tools 😭
OLLAMA_MODEL = "mistral"
OPENAI_MODEL = "gpt-4"

llm = None

if os.getenv("OPENAI_API_KEY") != None:
    llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0)
else:
    # Note: model must support tools -> https://ollama.com/search?c=tools
    llm = ChatOllama(model=OLLAMA_MODEL, temperature=0)
