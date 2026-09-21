from app.agent.context import build_context,system_prompt
class Ship30Skill:
 def __init__(self,llm,retriever): self.llm=llm; self.retriever=retriever
 async def run(self,query,history):
  results=await self.retriever.search(query)
  if not results: return {'answer':"I couldn't find enough relevant evidence in the transcript knowledge base to write a grounded essay.",'sources':[]}
  rules='''Write approximately 1,250 words. Use one central idea, a strong one-sentence hook, a clear narrative progression, skimmable H2/H3 headings, short paragraphs, selective bold emphasis, concrete examples, and a practical takeaway. Use a clear headline answering who/what/why. Prefer clarity over cleverness. Organize sections consistently (steps, lessons, or principles). Vary paragraph/sentence rhythm and use lists where they improve skimmability. Every substantive factual claim about the podcast material must be supported by the supplied sources and cite it inline as [SOURCE N]. Do not invent quotes.'''
  msgs=[{'role':'user','content':f'User request: {query}\n\nWriting framework:\n{rules}\n\nTranscript reference material:\n{build_context(results)}'}]
  r=await self.llm.generate(system_prompt(),msgs,max_tokens=2600)
  return {'answer':r.text,'sources':results,'model':r.model,'provider':r.provider}
