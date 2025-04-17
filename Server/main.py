from mcp.server.fastmcp import FastMCP
import os
import anthropic
import requests
import json

claude_api = os.environ.get("CLAUDE_API")
partner_id = os.environ.get("PARTNER_ID")
api_base = os.environ.get("API_BASE")



client = anthropic.Anthropic(
    api_key=claude_api,
)


mcp = FastMCP("Test", cors=True, port=8000)
print("FastMCP server initialized.") 

@mcp.tool()
def get_distribution_data(user_input: str) -> int:
    """Get distribution data"""
    try:
        api_response = requests.get(api_base, headers={
            "X-API-Key": partner_id
        })
        
        api_data = api_response.json()
        
        message = client.message.create(
                model="claude-3-haiku@20240307",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are an assistant tasked with fetching partner distribution data. Your task
                is to use the information from the dashboard to help the user with their questions about
                distribution data.

                Here is the current data:
                ${JSON.dumps(api_data)}


                User query:
                ${user_input.userInput}

                Provide detailed and well structured responses that addresses the user's queries."""
            }
        ]
        )
        
        return message.content[0].text
    except Exception as e:
        print(e)
        return "Something went wrong."
        
        
if __name__ == "__main__":
    print("Starting FastMCP server...")
    mcp.run(transport="stdio")
    print("FastMCP server started.")