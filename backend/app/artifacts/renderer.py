from .sanitizer import sanitize_html

def render_html(content: str) -> str:
    return sanitize_html(content)
