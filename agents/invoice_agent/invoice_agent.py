import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from prompt import INVOICE_PROMPT
from tools.invoice_tools.invoice_tool import create_invoice_tool

load_dotenv()
API_KEY = os.getenv("API_KEY")

class Agent(BaseModel):
    topic: str
    items: list[str]
    quantity: int
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=Agent)

agent_executor = AgentExecutor( 
    agent=create_tool_calling_agent(
        llm=ChatAnthropic(model="claude-3.5", max_retries=3, api_key=API_KEY), 
        tools=[],
        prompt=INVOICE_PROMPT
    )
    tools=[create_invoice_tool,],
    verbose=True
)

query = input("Enter yoour question")
raw_response = agent_executor.invoke({"query": query})
