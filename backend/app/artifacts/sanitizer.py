from bs4 import BeautifulSoup
from urllib.parse import urlparse

def sanitize_html(html):
 soup=BeautifulSoup(html,'html.parser')
 for tag in soup.find_all(['script','object','embed','base','form']): tag.decompose()
 for tag in soup.find_all(True):
  for a in list(tag.attrs):
   if a.lower().startswith('on-'): del tag.attrs[a]
  for a in ['href','src','action']:
   if a in tag.attrs:
    v=str(tag.attrs[a]).strip().lower()
    if v.startswith(('javascript:','data:','vbscript:')): del tag.attrs[a]
  if tag.name=='iframe':
   src=str(tag.get('src','')); host=urlparse(src).netloc.lower()
   if not (src.startswith('https://www.youtube.com/embed/') or src.startswith('https://player.vimeo.com/video/')): tag.decompose()
  if tag.name=='a' and tag.get('target')=='_blank': tag['rel']='noopener noreferrer'
 return str(soup)
