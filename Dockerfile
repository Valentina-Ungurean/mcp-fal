# Dockerfile (at repo root)
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

# If you don't have requirements.txt, you can install deps inline:
RUN pip install --no-cache-dir fastmcp==0.3.5 fastapi uvicorn httpx pydantic aiofiles

# Copy app code
COPY . .

# Cloud Run listens on $PORT
ENV PORT=8080
CMD ["sh","-c","uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
