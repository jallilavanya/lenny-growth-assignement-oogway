from app.rag.chunker import chunk_text
def test_chunker_preserves_content():
 t='\n\n'.join([f'Paragraph {i} with useful product advice.' for i in range(100)])
 c=chunk_text(t,50,10); assert len(c)>1; assert 'Paragraph 0' in c[0]; assert 'Paragraph 99' in c[-1]
