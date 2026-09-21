from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.exceptions import AppError
from app.api import health,sessions,chat,artifacts,settings,ingestion
configure_logging(); s=get_settings()
app=FastAPI(title='The Lenny Growth Assistant',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=s.cors_list,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
@app.exception_handler(AppError)
async def app_error(_:Request,e:AppError): return JSONResponse(e.status,{'error':{'code':e.code,'message':e.message,'details':e.details}})
@app.exception_handler(Exception)
async def unhandled(_:Request,e:Exception): return JSONResponse(500,{'error':{'code':'INTERNAL_ERROR','message':'An unexpected error occurred.','details':None}})
app.include_router(health.router); app.include_router(sessions.router); app.include_router(chat.router); app.include_router(artifacts.router); app.include_router(settings.router); app.include_router(ingestion.router)
