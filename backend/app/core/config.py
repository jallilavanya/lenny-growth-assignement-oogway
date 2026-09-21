from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_env: str = 'development'
    database_url: str = 'postgresql+psycopg://postgres:postgres@localhost:5432/lenny'
    llm_provider: str = 'ollama'
    ollama_base_url: str = 'http://localhost:11434'
    ollama_model: str = 'qwen3:4b'
    anthropic_api_key: str = ''
    anthropic_model: str = 'claude-3-5-sonnet-latest'
    embedding_provider: str = 'ollama'
    embedding_model: str = 'nomic-embed-text'
    embedding_dimensions: int = 768
    top_k: int = 6
    similarity_threshold: float = 0.35
    cors_origins: str = 'http://localhost:5173'
    request_timeout_seconds: float = 60.0
    max_history_messages: int = 12
    chunk_target_tokens: int = 900
    chunk_overlap_tokens: int = 120
    model_config = SettingsConfigDict(env_file='.env', case_sensitive=False, extra='ignore')

    @property
    def cors_list(self): return [x.strip() for x in self.cors_origins.split(',') if x.strip()]

@lru_cache
def get_settings(): return Settings()
