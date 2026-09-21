import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, Integer, Float, JSON, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector
from .database import Base
from app.core.config import get_settings
V=get_settings().embedding_dimensions

def uid(): return str(uuid.uuid4())
class User(Base):
    __tablename__='users'; id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    sessions=relationship('Session',back_populates='user',cascade='all,delete-orphan')
class Session(Base):
    __tablename__='sessions'; id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); user_id:Mapped[str]=mapped_column(ForeignKey('users.id',ondelete='CASCADE')); title:Mapped[str]=mapped_column(String(200),default='New Chat'); created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow); updated_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    user=relationship('User',back_populates='sessions'); messages=relationship('Message',back_populates='session',cascade='all,delete-orphan'); artifacts=relationship('Artifact',back_populates='session',cascade='all,delete-orphan')
class Message(Base):
    __tablename__='messages'; id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); session_id:Mapped[str]=mapped_column(ForeignKey('sessions.id',ondelete='CASCADE'),index=True); role:Mapped[str]=mapped_column(String(20)); content:Mapped[str]=mapped_column(Text()); metadata_json:Mapped[dict]=mapped_column('metadata',JSON,default=dict); created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    session=relationship('Session',back_populates='messages')
class Document(Base):
    __tablename__='documents'; id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); title:Mapped[str]=mapped_column(Text()); episode:Mapped[str]=mapped_column(Text(),default=''); guest:Mapped[str]=mapped_column(Text(),default=''); source_url:Mapped[str]=mapped_column(Text(),default=''); transcript_path:Mapped[str]=mapped_column(Text(),unique=True); publish_date:Mapped[str]=mapped_column(String(20),default=''); content_hash:Mapped[str]=mapped_column(String(64),index=True); created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    chunks=relationship('Chunk',back_populates='document',cascade='all,delete-orphan')
class Chunk(Base):
    __tablename__='chunks'; id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); document_id:Mapped[str]=mapped_column(ForeignKey('documents.id',ondelete='CASCADE'),index=True); chunk_index:Mapped[int]=mapped_column(Integer); content:Mapped[str]=mapped_column(Text()); embedding:Mapped[list]=mapped_column(Vector(V)); token_start:Mapped[int|None]=mapped_column(Integer,nullable=True); token_end:Mapped[int|None]=mapped_column(Integer,nullable=True); metadata_json:Mapped[dict]=mapped_column('metadata',JSON,default=dict)
    document=relationship('Document',back_populates='chunks')
    __table_args__=(Index('ix_chunks_document_index','document_id','chunk_index'),)
class Artifact(Base):
    __tablename__='artifacts'; id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); session_id:Mapped[str]=mapped_column(ForeignKey('sessions.id',ondelete='CASCADE'),index=True); type:Mapped[str]=mapped_column(String(20)); title:Mapped[str]=mapped_column(String(300)); content:Mapped[str]=mapped_column(Text()); sources:Mapped[list]=mapped_column(JSON,default=list); created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    session=relationship('Session',back_populates='artifacts')
