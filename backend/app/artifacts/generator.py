from app.agent.skills.artifact import ArtifactSkill

class ArtifactGenerator:
    """Small service facade around the artifact skill."""
    def __init__(self, llm, retriever):
        self.skill = ArtifactSkill(llm, retriever)
    async def generate(self, request, history):
        return await self.skill.run(request, history)
