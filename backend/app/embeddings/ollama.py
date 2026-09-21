import httpx
from .base import EmbeddingProvider
from app.core.config import get_settings
class OllamaEmbeddingProvider(EmbeddingProvider):
 def __init__(self): self.s=get_settings()
 async def embed(self,text):
  async with httpx.AsyncClient(timeout=self.s.request_timeout_seconds) as c:
   r=await c.post(f'{self.s.ollama_base_url}/api/embeddings',json={'model':self.s.embedding_model,'prompt':text}); r.raise_for_status(); return r.json()['embedding']
