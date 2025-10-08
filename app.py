from fastapi import FastAPI
from fastapi.routing import APIRoute
import logging, os

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "fal-mcp"}

@app.get("/healthz", include_in_schema=False)
def healthz():
    return {"status": "ok"}

@app.on_event("startup")
async def _log_routes():
    routes = [r.path for r in app.routes if isinstance(r, APIRoute)]
    logging.getLogger("uvicorn.error").info("HTTP shim started. Routes: %s", routes)
    logging.getLogger("uvicorn.error").info("PORT=%s", os.getenv("PORT"))
