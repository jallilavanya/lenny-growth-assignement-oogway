from pathlib import Path
import subprocess
from app.core.config import get_settings
from app.embeddings.factory import get_embedder
from app.rag.indexer import index_file
async def run_ingestion(db,repo_url='https://github.com/ChatPRD/lennys-podcast-transcripts.git',target='data/lenny-transcripts'):
 p=Path(target)
 if not p.exists(): subprocess.run(['git','clone','--depth','1',repo_url,str(p)],check=True)
 settings=get_settings(); embedder=get_embedder(); count=0
 for f in p.glob('episodes/*/transcript.md'): count += await index_file(db,f,embedder,settings)
 return {'files_processed':len(list(p.glob('episodes/*/transcript.md'))),'chunks_created':count,'path':str(p)}
