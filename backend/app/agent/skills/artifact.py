from app.agent.context import build_context,system_prompt
from app.artifacts.sanitizer import sanitize_html
class ArtifactSkill:
 def __init__(self,llm,retriever): self.llm=llm; self.retriever=retriever
 async def run(self,query,history):
  results=await self.retriever.search(query)
  if not results: return {'type':'markdown','title':'Insufficient evidence','content':"I couldn't find enough relevant evidence in the transcript knowledge base.",'sources':[]}
  wants_html=any(x in query.lower() for x in ['html','landing page','css'])
  fmt='html' if wants_html else 'markdown'
  instruction='Return only the artifact. For HTML, return a complete document body or fragment with inline CSS and no scripts. For Markdown, use clean headings and lists.'
  r=await self.llm.generate(system_prompt(),[{'role':'user','content':f'Create a {fmt} artifact for: {query}\n{instruction}\nGround it in these sources:\n{build_context(results)}'}],max_tokens=2400)
  content=sanitize_html(r.text) if fmt=='html' else r.text
  return {'type':fmt,'title':'Lenny Growth Artifact','content':content,'sources':results,'model':r.model,'provider':r.provider}
