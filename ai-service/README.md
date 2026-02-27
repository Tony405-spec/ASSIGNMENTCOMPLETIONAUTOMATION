# AI Service for Assignment Automation

## Overview
This service handles AI-powered answer generation using DeepSeek/ChatGPT.

## Endpoints
- GET /health - Service health check
- POST /generate - Generate assignment answers
- GET / - Service info

## Environment Variables
- DEEPSEEK_API_KEY - Your DeepSeek API key
- OPENAI_API_KEY - Your OpenAI API key (fallback)
- MAX_TOKENS - Max tokens per request

## Local Development
`ash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5001
docker build -t tonykenga405/assignment-ai-service .
docker run -p 5001:5001 tonykenga405/assignment-ai-service
