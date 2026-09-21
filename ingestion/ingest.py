import asyncio,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'backend'))
from app.db.database import SessionLocal
from app.services.ingestion_service import run_ingestion
async def main():
 db=SessionLocal()
 try: print(await run_ingestion(db))
 finally: db.close()
if __name__=='__main__': asyncio.run(main())
