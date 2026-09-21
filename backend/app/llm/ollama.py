import httpx
from .base import LLMProvider,LLMResult
from app.core.config import get_settings
from app.core.exceptions import LLMUnavailable
class OllamaProvider(LLMProvider):
 def __init__(self): self.s=get_settings()
 async def generate(self,system,messages,temperature=.2,max_tokens=1800):
  payload={'model':self.s.ollama_model,'system':system,'messages':messages,'stream':False,'options':{'temperature':temperature,'num_predict':max_tokens}}
  try:
   async with httpx.AsyncClient(timeout=self.s.request_timeout_seconds) as c:
    r=await c.post(f'{self.s.ollama_base_url}/api/chat',json=payload); r.raise_for_status(); data=r.json()
   return LLMResult(data.get('message',{}).get('content','').strip(),self.s.ollama_model,'ollama')
  except Exception as e: raise LLMUnavailable() from e
 async def health(self):
  try:
   async with httpx.AsyncClient(timeout=5) as c:
    r=await c.get(f'{self.s.ollama_base_url}/api/tags'); r.raise_for_status(); models=[m.get('name') for m in r.json().get('models',[])]
   return {'available':True,'model':self.s.ollama_model,'model_available':self.s.ollama_model in models,'provider':'ollama'}
  except Exception: return {'available':False,'model':self.s.ollama_model,'model_available':False,'provider':'ollama'}
