from fastapi import APIRouter,Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.llm.factory import get_llm
router=APIRouter()
@router.get('/health')
def health(db:Session=Depends(get_db)):
 db_ok=True
 try: db.execute(text('SELECT 1'))
 except Exception: db_ok=False
 return {'status':'healthy' if db_ok else 'degraded','database':'healthy' if db_ok else 'unavailable'}
@router.get('/api/health')
async def api_health(db:Session=Depends(get_db)):
 h=health(db); h['ollama']=await get_llm().health(); return h
