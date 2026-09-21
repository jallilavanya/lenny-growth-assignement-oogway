import hashlib,math
from .base import EmbeddingProvider
from app.core.config import get_settings
class HashEmbeddingProvider(EmbeddingProvider):
 async def embed(self,text):
  d=get_settings().embedding_dimensions; v=[0.0]*d
  for token in text.lower().split():
   h=int(hashlib.sha256(token.encode()).hexdigest(),16); i=h%d; v[i]+=1.0 if h%2 else -1.0
  n=math.sqrt(sum(x*x for x in v)) or 1; return [x/n for x in v]
