# string_tools_server.py
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("StringTools")

@mcp.tool()
def reverse_string(text: str) -> str:
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> int:
    return len(text.split())

if __name__ == "__main__":
    # Start server with stdio transport (Python only)
    mcp.run(transport="stdio")
