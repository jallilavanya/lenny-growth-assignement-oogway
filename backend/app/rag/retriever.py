from sqlalchemy import select,text as sqltext
from app.db.models import Chunk,Document
from app.core.config import get_settings
class Retriever:
 def __init__(self,db,embedder): self.db=db; self.embedder=embedder; self.s=get_settings()
 async def search(self,query):
  q=await self.embedder.embed(query)
  stmt=select(Chunk,Document).join(Document,Chunk.document_id==Document.id).order_by(Chunk.embedding.cosine_distance(q)).limit(self.s.top_k)
  rows=self.db.execute(stmt).all(); results=[]
  for c,d in rows:
   # pgvector distance is 0 identical; convert to similarity-like score
   dist=float(c.embedding.cosine_distance(q)); score=1-dist
   if score>=self.s.similarity_threshold: results.append({'chunk_id':c.id,'content':c.content,'title':d.title,'episode':d.episode,'guest':d.guest,'source_url':d.source_url,'relevance':round(score,4),'metadata':c.metadata_json})
  return results
