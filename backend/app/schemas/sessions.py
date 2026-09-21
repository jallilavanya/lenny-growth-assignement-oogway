from pydantic import BaseModel,Field
class SessionCreate(BaseModel): title:str=Field(default='New Chat',max_length=200)
class SessionOut(BaseModel): id:str; title:str; created_at:str; updated_at:str
class MessageOut(BaseModel): id:str; role:str; content:str; created_at:str; metadata:dict
