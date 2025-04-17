from mcp.server.fastmcp import FastMCP
import os

claude_api = os.environ.get("")




mcp = FastMCP("Test")

@mcp.tool()
def add(user_input: str) -> int:
    """Get distribution data"""
    try:
        