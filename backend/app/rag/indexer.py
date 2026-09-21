import hashlib
from sqlalchemy import select
from app.db.models import Document,Chunk
from .chunker import chunk_text
from .loader import load_transcript
async def index_file(db,path,embedder,settings):
 meta,body=load_transcript(path); h=hashlib.sha256(body.encode()).hexdigest(); existing=db.scalar(select(Document).where(Document.transcript_path==str(path)))
 if existing and existing.content_hash==h: return 0
 if existing: db.delete(existing); db.commit()
 doc=Document(title=meta.get('title') or path.parent.name,episode=meta.get('title') or path.parent.name,guest=meta.get('guest',''),source_url=meta.get('youtube_url',''),transcript_path=str(path),publish_date=str(meta.get('publish_date','')),content_hash=h); db.add(doc); db.flush()
 for i,chunk in enumerate(chunk_text(body,settings.chunk_target_tokens,settings.chunk_overlap_tokens)):
  vec=await embedder.embed(chunk); db.add(Chunk(document_id=doc.id,chunk_index=i,content=chunk,embedding=vec,metadata_json={'title':doc.title,'guest':doc.guest,'source_url':doc.source_url}))
 db.commit(); return len(doc.chunks)
