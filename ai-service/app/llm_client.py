import os
from typing import Optional
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self):
        self.deepseek_key = os.getenv("DEEPSEEK_API_KEY")
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.deepseek_url = "https://api.deepseek.com/v1/chat/completions"
        self.openai_url = "https://api.openai.com/v1/chat/completions"
        
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def generate(self, prompt: str, model: str = "deepseek-chat") -> str:
        """
        Generate text using DeepSeek or fallback to OpenAI
        """
        logger.info(f"Generating response for prompt: {prompt[:50]}...")
        
        # Try DeepSeek first if key exists
        if self.deepseek_key:
            try:
                return await self._call_deepseek(prompt)
            except Exception as e:
                logger.warning(f"DeepSeek failed: {e}, falling back to OpenAI")
                
        # Fallback to OpenAI
        if self.openai_key:
            return await self._call_openai(prompt)
            
        # No API keys available
        return "Error: No API keys configured. Please add DEEPSEEK_API_KEY or OPENAI_API_KEY to .env"
        
    async def _call_deepseek(self, prompt: str) -> str:
        """Call DeepSeek API"""
        # TODO: Implement actual DeepSeek API call
        # This is a placeholder
        return f"DeepSeek generated: {prompt[:100]}..."
        
    async def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API as fallback"""
        # TODO: Implement actual OpenAI API call
        # This is a placeholder
        return f"OpenAI generated: {prompt[:100]}..."
