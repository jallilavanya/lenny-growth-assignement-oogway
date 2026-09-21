from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories import get_artifact
router=APIRouter(prefix='/api/artifacts')
@router.get('/{aid}')
def get(aid:str,db:Session=Depends(get_db)):
 a=get_artifact(db,aid)
 if not a: raise HTTPException(404,'Artifact not found')
 return {'id':a.id,'type':a.type,'title':a.title,'content':a.content,'sources':a.sources,'created_at':a.created_at.isoformat()}
