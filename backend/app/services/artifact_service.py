from app.db.repositories import save_artifact
class ArtifactService:
 def __init__(self,db): self.db=db
 def save(self,sid,data): return save_artifact(self.db,sid,data['type'],data['title'],data['content'],data.get('sources',[]))
