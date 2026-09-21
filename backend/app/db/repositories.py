from sqlalchemy import select, delete
from sqlalchemy.orm import Session as DB
from app.db.models import User, Session, Message, Document, Chunk, Artifact
from datetime import datetime

def get_or_create_user(db:DB):
    u=db.scalar(select(User).order_by(User.created_at).limit(1))
    if not u: u=User(); db.add(u); db.commit(); db.refresh(u)
    return u

def create_session(db,user_id,title='New Chat'):
    s=Session(user_id=user_id,title=title); db.add(s); db.commit(); db.refresh(s); return s

def list_sessions(db,user_id): return list(db.scalars(select(Session).where(Session.user_id==user_id).order_by(Session.updated_at.desc())))
def get_session(db,sid,user_id): return db.scalar(select(Session).where(Session.id==sid,Session.user_id==user_id))
def add_message(db,sid,role,content,metadata=None):
    m=Message(session_id=sid,role=role,content=content,metadata_json=metadata or {}); db.add(m); db.execute(select(Session).where(Session.id==sid)); db.commit(); db.refresh(m); return m
def history(db,sid,limit=12): return list(db.scalars(select(Message).where(Message.session_id==sid).order_by(Message.created_at.desc()).limit(limit)))[::-1]
def save_artifact(db,sid,typ,title,content,sources):
    a=Artifact(session_id=sid,type=typ,title=title,content=content,sources=sources); db.add(a); db.commit(); db.refresh(a); return a
def get_artifact(db,aid): return db.get(Artifact,aid)
def delete_session(db,sid): db.execute(delete(Session).where(Session.id==sid)); db.commit()
