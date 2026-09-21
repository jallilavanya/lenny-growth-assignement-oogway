from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories import *
from app.schemas.sessions import *
router=APIRouter(prefix='/api/sessions')
def user(db): return get_or_create_user(db)
def out(s): return {'id':s.id,'title':s.title,'created_at':s.created_at.isoformat(),'updated_at':s.updated_at.isoformat()}
@router.post('',response_model=SessionOut)
def create(payload:SessionCreate,db:Session=Depends(get_db)):
 u=user(db); return out(create_session(db,u.id,payload.title))
@router.get('',response_model=list[SessionOut])
def list_(db:Session=Depends(get_db)):
 u=user(db); return [out(s) for s in list_sessions(db,u.id)]
@router.get('/{sid}',response_model=SessionOut)
def get(sid:str,db:Session=Depends(get_db)):
 s=get_session(db,sid,user(db).id)
 if not s: raise HTTPException(404,'Session not found')
 return out(s)
@router.delete('/{sid}')
def delete(sid:str,db:Session=Depends(get_db)):
 s=get_session(db,sid,user(db).id)
 if not s: raise HTTPException(404,'Session not found')
 delete_session(db,sid); return {'deleted':True}
@router.get('/{sid}/messages',response_model=list[MessageOut])
def messages(sid:str,db:Session=Depends(get_db)):
 if not get_session(db,sid,user(db).id): raise HTTPException(404,'Session not found')
 return [{'id':m.id,'role':m.role,'content':m.content,'created_at':m.created_at.isoformat(),'metadata':m.metadata_json} for m in history(db,sid,100)]
