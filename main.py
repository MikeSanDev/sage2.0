from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm2 = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
response = llm2.invoke("Write a haiku about recursion in programming.")
print(response)