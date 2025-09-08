from dotenv import load_dotenv
from pydantic import BaseeModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# llm = ChatOpenAI(model="gpt-4", temperature=0)
# llm2 = ChatAnthropic(model="claude-2", temperature=0)
