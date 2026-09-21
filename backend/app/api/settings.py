from fastapi import APIRouter
from app.core.config import get_settings
from app.llm.factory import get_llm
router=APIRouter(prefix='/api/settings')
@router.get('/model')
async def model(): return await get_llm().health()
