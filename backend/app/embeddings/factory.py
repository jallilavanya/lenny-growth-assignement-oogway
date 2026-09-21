from app.core.config import get_settings
from .ollama import OllamaEmbeddingProvider
from .local import HashEmbeddingProvider
def get_embedder(): return HashEmbeddingProvider() if get_settings().embedding_provider=='hash' else OllamaEmbeddingProvider()
