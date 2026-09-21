from app.db.repositories import add_message,history,get_session
from app.agent.orchestrator import Orchestrator
class ChatService:
 def __init__(self,db,orch,user_id): self.db=db; self.orch=orch; self.user_id=user_id
 async def ask(self,sid,text):
  s=get_session(self.db,sid,self.user_id)
  if not s: raise ValueError('SESSION_NOT_FOUND')
  hist=history(self.db,sid)
  add_message(self.db,sid,'user',text)
  route,res=await self.orch.run(text,[{'role':m.role,'content':m.content} for m in hist])
  meta={'route':route,'provider':res.get('provider'),'model':res.get('model'),'sources':res.get('sources',[])}
  if route=='artifact':
   from app.db.repositories import save_artifact
   a=save_artifact(self.db,sid,res['type'],res['title'],res['content'],res.get('sources',[])); meta['artifact_id']=a.id
  add_message(self.db,sid,'assistant',res.get('answer',res.get('content','')),meta)
  return route,res
