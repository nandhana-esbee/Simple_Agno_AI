import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.ollama import Ollama

from tools.calculator import calculator_tool
from tools.currency import currency_tool
from tools.stockdata import stock_tool
from tools.userjson import save_user_data


load_dotenv()

# LLM setup using env
model=Ollama(id="llama3.1")

agent = Agent(
    name="Smart Banking Assistant",
    model=model,
    instructions="""
    You are an intelligent assistant.

    You can:
    - Chat naturally
    - Use tools when required
    - Ask follow-up questions if data is missing

    BANK ACCOUNT FLOW:
    If user wants to open account:
    Ask for:
    - Name
    - Age
    - Bank name
    - Account type
    - Place

    Ask step-by-step if missing.
    Once all collected → call save_user_data.
    """,
    tools=[
        calculator_tool,
        currency_tool,
        stock_tool,
        save_user_data
    ],
    debug_mode=True,
    markdown=True
)