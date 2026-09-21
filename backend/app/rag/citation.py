def citations(results):
 seen=set(); out=[]
 for r in results:
  key=(r['title'],r['source_url'])
  if key in seen: continue
  seen.add(key); out.append({'title':r['title'],'episode':r['episode'],'source_url':r['source_url'],'chunk_id':r['chunk_id'],'relevance':r['relevance']})
 return out
