import os, asyncio
from fastmcp import FastMCP
from starlette.responses import JSONResponse
from starlette.requests import Request

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name:str) -> str:
    '''\
    Greet a person by name.
    '''
    return f"Hello, {name}!"

@mcp.custom_route('/health', methods=['GET'])
async def health(request: Request):
    return JSONResponse({"status": "healthy"})

if __name__ == "__main__":
    asyncio.run(mcp.run(host="0.0.0.0", port=8000, transport="streamable-http", path="/mcp/example"))

