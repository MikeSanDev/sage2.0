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

#Prompt, Parser, LLM, Model

# Load environment variables from a .env file into the environment
load_dotenv()

# Define a Pydantic model to structure the LLM's response
class ResearchResponse(BaseModel):
    topic: str
    summary: str    
    sources: list[str]
    tools_used: list[str]

# Initialize the LLM with specific model and temperature settings
llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)

#take the output of the llm and parse it into a pydantic model
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Create a chat
prompt = ChatPromptTemplate.from_messages(
    [
        (
            #this is the system message that sets the behavior of the LLM
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        # Messages from the chat history and user query will be inserted here
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
#.partial allows you to pre-fill certain variables in the prompt template

#Creating the Agent and Executor

# Create the tool calling agent with the LLM, prompt, and no tools for now
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[]
)
# Create an executor to run the agent
agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_response = agent_executor.invoke({"query": "What is the capital of the Philippines?"})
print(raw_response)

# Parse the raw response from the LLM into the structured Pydantic model
#you have to access the "output" key and then the text within it
#you can also do print(structured_response.json()) to get it in json format
#or print(structured_response.dict()) to get it in dictionary format
structured_response = parser.parse(raw_response.get("output")[0]["text"])
print(structured_response)

