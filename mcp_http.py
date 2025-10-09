import os, logging
from fastmcp import FastMCP
from api.models import register_model_tools
from api.generate import register_generation_tools
from api.storage import register_storage_tools
from api.config import get_api_key, SERVER_NAME, SERVER_VERSION

PORT = int(os.environ.get("PORT", "8080"))
PATH = "/stream"  # n8n’s HTTP Streamable default

mcp = FastMCP(SERVER_NAME, version=SERVER_VERSION)
register_model_tools(mcp)
register_generation_tools(mcp)
register_storage_tools(mcp)
get_api_key()

logging.basicConfig(level=logging.INFO)
logging.info(f"Starting MCP HTTP on {PATH} port {PORT}")

mcp.run(transport="http", host="0.0.0.0", port=PORT, path=PATH)
