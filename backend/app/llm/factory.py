from app.core.config import get_settings
from .ollama import OllamaProvider
from .anthropic import AnthropicProvider
def get_llm():
 p=get_settings().llm_provider.lower(); return AnthropicProvider() if p=='anthropic' else OllamaProvider()
