# The Lenny Growth Assistant

Production-oriented take-home implementation of a transcript-grounded product/growth assistant. It uses React/Vite, FastAPI, PostgreSQL + pgvector, Ollama, an LLM provider abstraction, RAG, routed skills, persisted sessions/messages/artifacts, and a sandboxed artifact viewer.

## Architecture

`Browser → React → FastAPI → Agent Router → Skill → Retriever → pgvector → LLM Provider → PostgreSQL`

The local demo uses Ollama for generation and embeddings. Anthropic can be selected by changing `LLM_PROVIDER` and providing `ANTHROPIC_API_KEY`; application services do not call either provider directly.

## Prerequisites

- Docker + Docker Compose
- Ollama installed locally
- Node 20+ for non-Docker frontend development
- Python 3.12+ for non-Docker backend/ingestion development

## Quick start

1. Copy `.env.example` to `.env` for native development.
2. Start Ollama and install models:

```bash
ollama pull qwen3:4b
ollama pull nomic-embed-text
```

3. Start the stack:

```bash
docker compose up --build
```

4. Run ingestion after the backend is ready:

```bash
python ingestion/ingest.py
```

For Dockerized ingestion, run it from a backend-capable environment with the repository mounted, or use `POST /api/ingestion/run`.

Frontend: `http://localhost:8080`  
Backend: `http://localhost:8000`  
Swagger: `http://localhost:8000/docs`

## Native development

Create PostgreSQL with pgvector, then:

```bash
cd backend
python -m venv .venv
# activate it
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Set `VITE_API_URL=http://localhost:8000` if needed.

## Ingestion

The ingestion script clones the official public ChatPRD transcript archive, reads `episodes/*/transcript.md`, parses YAML frontmatter, cleans/chunks the body, creates embeddings, and persists documents/chunks. It is idempotent by transcript content hash.

```bash
python ingestion/ingest.py
```

The source archive documents 269 episode transcripts, each as a standalone markdown file with YAML metadata. See the source repository link in `PRD.md`.

## API

- `GET /health`
- `GET /api/health`
- `POST /api/sessions`
- `GET /api/sessions`
- `GET /api/sessions/{id}`
- `DELETE /api/sessions/{id}`
- `GET /api/sessions/{id}/messages`
- `POST /api/sessions/{id}/messages`
- `POST /api/sessions/{id}/ask`
- `POST /api/sessions/{id}/artifacts`
- `GET /api/artifacts/{id}`
- `GET /api/settings/model`
- `POST /api/ingestion/run`

## RAG

Chunks target ~900 whitespace tokens with ~120-token paragraph overlap. Retrieval is top-K cosine similarity with a configurable threshold. Only retrieved chunks are passed to the model, and low-confidence/no-result queries return an explicit insufficient-evidence response.

## Agent routing

The router selects `qa`, `ship30`, or `artifact`. Each skill has its own retrieval and prompt policy. Retrieved transcript text is explicitly labeled untrusted reference material so instructions embedded in source content cannot override the system rules.

## Ship 30 for 30

The writing skill encodes explicit principles from the supplied Ship 30 for 30 guide: clear WHO/WHAT/WHY headline, one central idea, hook, consistent section structure, short paragraphs, headings, lists, selective bold emphasis, skimmability, varied rhythm, and a practical conclusion. The guide is cited in `PRD.md` and the implementation avoids copying its prose.

## Artifact security

Generated HTML is sanitized with BeautifulSoup: scripts/object/embed/base/form are removed; event-handler attributes and dangerous URL schemes are removed; iframe hosts are restricted. The browser also renders HTML in a sandboxed iframe without `allow-scripts`. Markdown is rendered through DOMPurify. This is defense-in-depth, not a claim of perfect sanitization.

## Tests

```bash
cd backend
pytest -q
```

Tests cover routing, chunking, schema validation, deterministic embedding dimensions, and malicious HTML payloads. Provider/network calls are not made by unit tests.

## Troubleshooting

**Ollama unavailable:** run `ollama serve`, then verify the configured model exists with `ollama list`.

**Embedding dimension mismatch:** ensure the configured embedding model produces the configured `EMBEDDING_DIMENSIONS` (default 768 for `nomic-embed-text`).

**Database not ready:** wait for the Postgres health check, then rerun `alembic upgrade head`.

**Frontend cannot connect:** set `VITE_API_URL=http://localhost:8000` for native development.

## Limitations

- The current UI uses one implicit local user rather than authentication/multi-tenancy.
- Full streaming is intentionally omitted to keep the provider abstraction simple.
- Retrieval uses vector similarity only; hybrid lexical search can be added later.
- Docker is not available in this execution environment, so the Compose stack could not be launched here; the files are provided and the non-Docker Python tests can be executed locally.
