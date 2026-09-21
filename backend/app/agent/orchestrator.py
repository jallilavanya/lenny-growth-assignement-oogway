from .router import AgentRouter
from .skills.qa import QASkill
from .skills.ship30 import Ship30Skill
from .skills.artifact import ArtifactSkill
class Orchestrator:
 def __init__(self,llm,retriever):
  self.router=AgentRouter(); self.skills={'qa':QASkill(llm,retriever),'ship30':Ship30Skill(llm,retriever),'artifact':ArtifactSkill(llm,retriever)}
 async def run(self,text,history):
  route=self.router.route(text); return route,await self.skills[route].run(text,history)
