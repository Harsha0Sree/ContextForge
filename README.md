
# ContextForge

> **Build production-ready Retrieval-Augmented Generation (RAG) systems from documents—not just file uploads.**
>
> ContextForge is a Django-based document ingestion platform that securely accepts files, prepares them for downstream AI pipelines, and serves as the foundation for scalable knowledge systems.

---

> **Status:** Early Development

## Why ContextForge?

Most document upload applications stop after saving a file.

ContextForge is designed to become the **ingestion layer** of a complete RAG platform.

Traditional upload apps provide:

- File storage
- Simple CRUD

ContextForge is designed to provide:

- Secure document ingestion
- Processing pipelines
- Metadata extraction
- Background processing
- Vector indexing
- Enterprise deployment
- AI-ready architecture

---

# Features

| Feature | Status |
|----------|--------|
| Django Backend | ✅ |
| File Uploads | ✅ |
| SQLite Development | ✅ |
| PostgreSQL Ready | ✅ |
| uv Package Management | ✅ |
| Production Architecture | 🚧 |
| Async Processing | 🚧 |
| Embedding Pipeline | 🚧 |
| Vector Search | 🚧 |
| Cloud Storage | 🚧 |

---

# Architecture

```text
              Client
                 │
                 ▼
        Django Upload API
                 │
                 ▼
         Document Database
                 │
                 ▼
      Background Task Queue
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
Text Extraction      Metadata
       │                   │
       └─────────┬─────────┘
                 ▼
          Chunk Generation
                 │
                 ▼
          Embedding Engine
                 │
                 ▼
            Vector Store
                 │
                 ▼
             RAG System
```

---

# Quick Start

## Requirements

- Python 3.12+
- uv

## Installation

```bash
git clone <repository-url>
cd ContextForge

uv sync
uv run manage.py migrate
uv run manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

# Project Layout

```text
ContextForge/
├── config/
├── documents/
├── media/
├── manage.py
├── pyproject.toml
└── uv.lock
```

---

# API

## GET /

Returns service status.

## GET /upload/

Upload page.

## POST /upload/

Uploads a document.

Fields

| Name | Type |
|------|------|
| title | string |
| file | multipart/form-data |

## GET /admin/

Django administration.

---

# Current Architecture

Current implementation focuses on:

- Document persistence
- Local development
- Django MVC
- SQLite

Future iterations add:

- Celery
- Redis
- PostgreSQL
- pgvector
- S3
- OCR
- Embeddings

---

# Production Roadmap

## Phase 1

- Secure uploads
- Validation
- Metadata

## Phase 2

- Background workers
- OCR
- Parsing

## Phase 3

- Embeddings
- Vector database

## Phase 4

- Search API
- Chat API

## Phase 5

- Multi-tenant SaaS

---

# Security

Planned production improvements:

- Environment variables
- Secret management
- MIME validation
- Size limits
- Virus scanning
- Signed URLs
- Authentication
- Authorization

---

# Deployment

Recommended production stack

```text
Internet
    │
NGINX
    │
Gunicorn
    │
Django
    │
PostgreSQL
    │
Redis
    │
Celery
    │
S3
```

---

# Development

```bash
uv sync
uv run manage.py migrate
uv run manage.py runserver
```

---

# Contributing

1. Fork
2. Create branch
3. Commit
4. Open Pull Request

---

# License

MIT
