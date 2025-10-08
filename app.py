# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "fal-mcp"}

@app.get("/healthz")
def health():
    return {"status": "ok"}
