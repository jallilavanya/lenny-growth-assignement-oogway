from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories import get_or_create_user,get_session
from app.embeddings.factory import get_embedder
from app.rag.retriever import Retriever
from app.llm.factory import get_llm
from app.agent.orchestrator import Orchestrator
from app.services.chat_service import ChatService
from app.services.artifact_service import ArtifactService
from app.schemas.chat import *
router=APIRouter(prefix='/api/sessions')
def svc(db): return ChatService(db,Orchestrator(get_llm(),Retriever(db,get_embedder())),get_or_create_user(db).id)
@router.post('/{sid}/messages',response_model=AskResponse)
async def ask(sid:str,payload:AskRequest,db:Session=Depends(get_db)):
 try: route,res=await svc(db).ask(sid,payload.content)
 except ValueError: raise HTTPException(404,'Session not found')
 return {'route':route,'answer':res.get('answer',res.get('content','')),'sources':res.get('sources',[]),'provider':res.get('provider'),'model':res.get('model')}
@router.post('/{sid}/ask',response_model=AskResponse)
async def ask_alias(sid:str,payload:AskRequest,db:Session=Depends(get_db)): return await ask(sid,payload,db)
@router.post('/{sid}/artifacts',response_model=AskResponse)
async def artifact(sid:str,payload:AskRequest,db:Session=Depends(get_db)):
 try: route,res=await svc(db).ask(sid,payload.content)
 except ValueError: raise HTTPException(404,'Session not found')
 if route!='artifact': raise HTTPException(400,'Request did not route to artifact generation')
 a=ArtifactService(db).save(sid,res)
 return {'route':route,'answer':res['content'],'sources':res.get('sources',[]),'provider':res.get('provider'),'model':res.get('model'),'artifact_id':a.id}
