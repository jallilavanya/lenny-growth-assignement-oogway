from app.agent.context import build_context,system_prompt
class QASkill:
 def __init__(self,llm,retriever): self.llm=llm; self.retriever=retriever
 async def run(self,query,history):
  results=await self.retriever.search(query)
  if not results: return {'answer':"I couldn't find enough relevant evidence in the transcript knowledge base.",'sources':[],'results':[]}
  context=build_context(results); msgs=[{'role':m['role'],'content':m['content']} for m in history[-8:]]; msgs.append({'role':'user','content':f'Question: {query}\n\nTranscript reference material:\n{context}'})
  r=await self.llm.generate(system_prompt(),msgs,max_tokens=1600)
  return {'answer':r.text,'sources':results,'model':r.model,'provider':r.provider}
