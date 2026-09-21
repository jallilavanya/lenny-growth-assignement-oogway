from app.llm.ollama import OllamaProvider
from app.llm.anthropic import AnthropicProvider
from app.embeddings.local import HashEmbeddingProvider
import pytest, asyncio
@pytest.mark.asyncio
async def test_hash_embedding_dimensions(): assert len(await HashEmbeddingProvider().embed('hello world'))==768
