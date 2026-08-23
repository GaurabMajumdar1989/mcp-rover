import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model = os.environ["LLM_MODEL"],
    api_key= os.environ["OPENROUTER_API_KEY"],
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    temperature=0
)