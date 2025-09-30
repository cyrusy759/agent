import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from prompt import SOURCING_PROMPT
from tools.invoice_tools.invoice_tool import create_invoice_tool

load_dotenv()
API_KEY = os.getenv("API_KEY")

class Agent(BaseModel):
    topic: str
    items: list[str]
    price: int
    bought: bool
    tools_used: list[str]

class SourcingAgent:
    def __init__(self):
        self._prompt = SOURCING_PROMPT
        self._parser = PydanticOutputParser(pydantic_object=Agent)
        self._query = input("Enter your question: ")
        
    def generate_agent(self):
        # Create the tool
        invoice_tool = create_sourcing_tool()
        
        # Create the agent
        agent = create_tool_calling_agent(
            llm=ChatAnthropic(model="claude-3.5-sonnet-20240620", max_retries=3, api_key=API_KEY), 
            tools=[sourcing_tool],
            prompt=SOURCING_PROMPT
        )
        
        # Create the executor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=[sourcing_tool],
            verbose=True
        )
        
        return agent_executor

    def run(self, message):
        # Pass the message from telegram to the agent
        agent_executor = self._generate_agent()
        raw_response = agent_executor.invoke({"input": message})
        return raw_response

