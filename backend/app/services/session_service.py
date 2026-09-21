from app.db.repositories import create_session, list_sessions, get_session, delete_session
class SessionService:
    def __init__(self, db, user_id): self.db=db; self.user_id=user_id
    def create(self,title='New Chat'): return create_session(self.db,self.user_id,title)
    def list(self): return list_sessions(self.db,self.user_id)
    def get(self,sid): return get_session(self.db,sid,self.user_id)
    def delete(self,sid): return delete_session(self.db,sid)
