import re

def approx_tokens(s): return max(1,len(s.split()))
def chunk_text(text,target=900,overlap=120):
 paragraphs=[p.strip() for p in re.split(r'\n\s*\n+',text) if p.strip()]
 out=[]; cur=[]; n=0
 for p in paragraphs:
  pn=approx_tokens(p)
  if cur and n+pn>target:
   out.append('\n\n'.join(cur)); tail=[]; tn=0
   for q in reversed(cur):
    qn=approx_tokens(q)
    if tn+qn>overlap: break
    tail.insert(0,q); tn+=qn
   cur=tail+[p]; n=tn+pn
  else: cur.append(p); n+=pn
 if cur: out.append('\n\n'.join(cur))
 return out
