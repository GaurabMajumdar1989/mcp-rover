from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather for a location."""
    return "It is too hot to be true"


if __name__ == "__main__":
    mcp.run(transport="sse")
