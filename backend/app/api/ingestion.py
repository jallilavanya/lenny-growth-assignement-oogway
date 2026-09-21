from fastapi import APIRouter,Depends,BackgroundTasks
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.ingestion_service import run_ingestion
router=APIRouter(prefix='/api/ingestion')
@router.post('/run')
async def run(db:Session=Depends(get_db)): return await run_ingestion(db)
