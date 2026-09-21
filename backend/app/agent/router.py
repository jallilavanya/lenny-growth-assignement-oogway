import re
class AgentRouter:
 def route(self,text):
  t=text.lower()
  if any(x in t for x in ['ship 30','ship30','essay','write an article','write a post']): return 'ship30'
  if any(x in t for x in ['artifact','markdown','html','landing page','strategy document','document from this']): return 'artifact'
  return 'qa'
