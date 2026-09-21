from pydantic import BaseModel
class ArtifactOut(BaseModel): id:str; type:str; title:str; content:str; sources:list; created_at:str
