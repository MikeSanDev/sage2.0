
# Loads environment variables (like API keys) from a .env file into your Python app
from dotenv import load_dotenv
# Pydantic is a data validation and parsing library
from pydantic import BaseModel
# LangChain wrapper for Anthropic's Claude models, making API calls easy in Python
from langchain_anthropic import ChatAnthropic
# Utility for building reusable, parameterized prompt templates
from langchain_core.prompts import ChatPromptTemplate
# Parses LLM outputs directly into Pydantic models with validation
from langchain_core.output_parsers import PydanticOutputParser
# Agent framework for tool usage and decision-making
from langchain.agents import create_tool_calling_agent, AgentExecutor
# Tools
from tools.tools import search_tool, wiki_tool, save_to_txt

import re
from datetime import datetime

# Load environment variables from a .env file into the environment
load_dotenv()

# ---------------- Pydantic Model ----------------
class ResearchResponse(BaseModel):
    topic: str
    summary: str    
    sources: list[str]
    tools_used: list[str]

# ---------------- LLM Setup ----------------
# Initialize the LLM with specific model and temperature settings
llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)
#take the output of the llm and parse it into a pydantic model

# ---------------- Prompt ----------------
# Create a chat
prompt = ChatPromptTemplate.from_messages(
    [
        (
            #this is the system message that sets the behavior of the LLM
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            You must respond ONLY with a valid JSON object. 
            Do NOT include apologies, explanations, <result>, XML, Markdown, or any extra text. 
            Return exactly this structure:\n{format_instructions}
            """,
        ),
        # Messages from the chat history and user query will be inserted here
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
#.partial allows you to pre-fill certain variables in the prompt template

# ---------------- Agent + Tools ----------------

#Add Tools here - this is now passed to the agent (tools=tools) and our Excecutor (tools=tools)
#did not call save_tool here because we don't want the agent to call it, we call it manually at the end
tools = [search_tool, wiki_tool]

# Create the tool calling agent with the LLM, prompt, and no tools for now
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
# Create an executor to run the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
#this ask you for a query and the executor runs the agent with the query
query = input("Enter your research topic: ") 
raw_response = agent_executor.invoke({"query": query})
print(raw_response)

# Parse the raw response from the LLM into the structured Pydantic model
#you have to access the "output" key and then the text within it
#you can also do print(structured_response.json()) to get it in json format
#or print(structured_response.dict()) to get it in dictionary format
output_list = raw_response.get("output", [])
if output_list:
    raw_text = output_list[0]["text"]
    structured_response = parser.parse(raw_text)
else:
    # If the LLM didn’t return text, load from your saved file or skip parsing
    print("No direct output from agent, falling back to saved file.")
    structured_response = None

# Always save to file (manual call)
#.model_dump_json is a pydantic method that formats the output as json - used to be obj.dict(*)
if structured_response:
    save_to_txt(structured_response.model_dump_json(indent=2))