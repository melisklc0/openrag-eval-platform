# OpenRAG Eval Platform

OpenRAG Eval Platform is a production-minded RAG evaluation and observability project for developer documentation.

The project focuses on building a practical RAG system with document indexing, retrieval, evaluation, observability, and a maintainable backend architecture.

## Project Goal

This project aims to combine:

- FastAPI API layer for chat, retrieval, documents, and evaluation endpoints
- Qdrant-backed semantic retrieval over public documentation
- Hybrid retrieval with keyword search, metadata filters, and reranking
- LangGraph workflow for query rewrite, retrieval, answer generation, and citation checks
- LLM-as-judge evaluation for groundedness, answer relevance, and citation correctness
- Structured logging and Langfuse-style observability for debugging runs

## Current Status

The repository currently contains the first application skeleton: FastAPI, settings, structured logging, Docker Compose wiring, and basic tests.

Planned build phases:

- Phase 1: MVP RAG with ingestion, embeddings, Qdrant, and chat
- Phase 2: Hybrid retrieval and retrieval debug tooling
- Phase 3: LangGraph RAG workflow
- Phase 4: Evaluation runner and scoring endpoints
- Phase 5: Observability and tracing

## Development

```bash
uv sync
make run
```

```bash
make test
```

```bash
make docker-up
```
