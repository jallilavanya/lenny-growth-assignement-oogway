from app.artifacts.sanitizer import sanitize_html
def test_script_and_handlers_removed():
 x=sanitize_html('<div onclick="alert(1)"><script>alert(1)</script><img src="javascript:alert(1)"></div>'); assert '<script' not in x.lower(); assert 'onclick' not in x.lower(); assert 'javascript:' not in x.lower()
def test_iframe_restricted():
 x=sanitize_html('<iframe src="https://evil.example/x"></iframe><iframe src="https://www.youtube.com/embed/abc"></iframe>'); assert 'evil.example' not in x; assert 'youtube.com/embed/abc' in x
