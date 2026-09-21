from pydantic import BaseModel,Field
class AskRequest(BaseModel): content:str=Field(min_length=1,max_length=12000)
class Source(BaseModel): title:str; episode:str; source_url:str; chunk_id:str; relevance:float
class AskResponse(BaseModel): route:str; answer:str; sources:list[Source]; provider:str|None=None; model:str|None=None; artifact_id:str|None=None
