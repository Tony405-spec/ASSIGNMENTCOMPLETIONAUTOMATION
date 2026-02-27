from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Assignment AI Service",
    description="AI-powered answer generation for KCA assignments",
    version="1.0.0",
    contact={
        "name": "Tony405-spec",
        "url": "https://github.com/Tony405-spec",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "service": "Assignment AI Service",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "generate": "/generate",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ai-service",
        "model": "deepseek-ready",
        "owner": "Tony405-spec"
    }

@app.post("/generate")
async def generate_answer(request: dict):
    # Test response - will replace with real AI later
    return {
        "answer": f"This is a test answer for: {request.get('assignment_text', '')[:50]}...",
        "citations": [
            "Tony, KCA University (2024). Introduction to Computing",
            "DeepSeek AI (2024). Language Model Documentation"
        ],
        "quality_score": 0.95,
        "subject": request.get("subject", "general"),
        "tokens_used": 150,
        "generated_by": "Tony405-spec"
    }

@app.get("/docs")
async def docs():
    return {"message": "API documentation available at /docs"}
