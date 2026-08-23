import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from mcp_rover.llm import llm
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

stdio_server_params = StdioServerParameters(
    command="python",
    args=["run", "python", "-m", "mcp_rover.math_server"],
)

async def main():
    print("Hello from async rover mcp server!!!!")

def cli():
    asyncio.run(main())