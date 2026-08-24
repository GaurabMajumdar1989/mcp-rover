import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from mcp_rover.llm import llm
from langchain_core.messages import HumanMessage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

stdio_server_params = StdioServerParameters(
    command="uv",
    args=["run", "python", "-m", "mcp_rover.servers.math_server"],
)

async def main():
    print("Hello from async rover mcp server!!!!")
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized...")
            # tools = await session.list_tools()
            ### If we pass the above session.list_tools() in langchain agent it will throw error because langchain expects langchain tools obj for agent
            ### so we need load_mcp_tool from langchain_mcp_adapters abstraction for langchain tools
            tools = await load_mcp_tools(session)
            # print(tools)
            agent = create_agent(llm,tools)
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 100 + 2 * 8?")]})
            print(result["messages"][-1].content)


def cli():
    asyncio.run(main())