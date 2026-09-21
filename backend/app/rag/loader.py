from pathlib import Path
import yaml

def load_transcript(path:Path):
 text=path.read_text(encoding='utf-8'); meta={}; body=text
 if text.startswith('---'):
  parts=text.split('---',2)
  if len(parts)==3: meta=yaml.safe_load(parts[1]) or {}; body=parts[2]
 return meta,body.strip()
