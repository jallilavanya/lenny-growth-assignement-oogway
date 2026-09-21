# Troubleshooting

- **Ollama unavailable:** `ollama serve`; check `ollama list`; pull `qwen3:4b` and `nomic-embed-text`.
- **Postgres unavailable:** check `docker compose ps` and `pg_isready`.
- **Migration failure:** run `alembic upgrade head` from `backend` with the correct `DATABASE_URL`.
- **Vector mismatch:** keep `EMBEDDING_DIMENSIONS` aligned with the selected embedding model.
- **CORS:** set `CORS_ORIGINS` to the exact frontend origin.
