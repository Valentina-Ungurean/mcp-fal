
import os
from fastmcp import FastMCP
from api.models import register_model_tools
from api.generate import register_generation_tools
from api.storage import register_storage_tools
from api.config import get_api_key, SERVER_NAME, SERVER_VERSION

mcp = FastMCP(SERVER_NAME, version=SERVER_VERSION)
register_model_tools(mcp)
register_generation_tools(mcp)
register_storage_tools(mcp)
get_api_key()

# Expose Streamable HTTP (exact API name varies by fastmcp version)

mcp.serve_http(host="0.0.0.0", port=int(os.getenv("PORT", "8080")), path="/stream")
