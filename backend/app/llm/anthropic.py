import httpx
from .base import LLMProvider,LLMResult
from app.core.config import get_settings
class AnthropicProvider(LLMProvider):
 def __init__(self): self.s=get_settings()
 async def generate(self,system,messages,temperature=.2,max_tokens=1800):
  if not self.s.anthropic_api_key: raise RuntimeError('ANTHROPIC_API_KEY is not configured')
  payload={'model':self.s.anthropic_model,'max_tokens':max_tokens,'temperature':temperature,'system':system,'messages':messages}
  async with httpx.AsyncClient(timeout=self.s.request_timeout_seconds) as c:
   r=await c.post('https://api.anthropic.com/v1/messages',headers={'x-api-key':self.s.anthropic_api_key,'anthropic-version':'2023-06-01','content-type':'application/json'},json=payload); r.raise_for_status(); d=r.json()
  return LLMResult(''.join(x.get('text','') for x in d.get('content',[])),self.s.anthropic_model,'anthropic')
 async def health(self): return {'available':bool(self.s.anthropic_api_key),'model':self.s.anthropic_model,'model_available':bool(self.s.anthropic_api_key),'provider':'anthropic'}
