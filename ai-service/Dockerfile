FROM python:3.11-slim

LABEL maintainer="Tony405-spec"
LABEL version="1.0"
LABEL description="AI Service for Assignment Automation"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001", "--reload"]
