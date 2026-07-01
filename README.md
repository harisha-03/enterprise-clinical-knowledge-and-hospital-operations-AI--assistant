# 🏥 Enterprise AI Clinical Knowledge & Hospital Operations Assistant using Advanced RAG

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![OpenAPI](https://img.shields.io/badge/OAS-3.1-6BA539.svg)
![Python](https://img.shields.io/badge/python-3.11-3776AB.svg?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688.svg?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB.svg?logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-frontend-646CFF.svg?logo=vite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-4169E1.svg?logo=postgresql&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-FF6F00.svg)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**A portfolio-grade Enterprise AI platform that fuses Advanced Retrieval-Augmented Generation with live hospital operations data — one assistant, two knowledge worlds.**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation-guide) • [API Docs](#-swagger-documentation) • [RAG Pipeline](#-rag-pipeline-explanation) • [Roadmap](#-future-roadmap)

</div>

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Objectives](#-objectives)
- [Features](#-features)
- [Architecture](#-architecture)
- [System Workflow](#-system-workflow)
- [Technology Stack](#-technology-stack)
- [Folder Structure](#-folder-structure)
- [Screenshots](#-screenshots)
- [Installation Guide](#-installation-guide)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Environment Variables](#environment-variables)
  - [Running the Project](#running-the-project)
- [Swagger Documentation](#-swagger-documentation)
- [Example API Calls](#-example-api-calls)
- [RAG Pipeline Explanation](#-rag-pipeline-explanation)
- [SQL Agent Explanation](#-sql-agent-explanation)
- [Intent Routing Explanation](#-intent-routing-explanation)
- [Hybrid Search Explanation](#-hybrid-search-explanation)
- [Vector Database Explanation](#-vector-database-explanation)
- [Current Project Status](#-current-project-status)
- [Future Roadmap](#-future-roadmap)
- [Deployment Guide](#-deployment-guide)
- [Docker](#-docker)
- [Project Demonstration](#-project-demonstration)
- [Repository Structure](#-repository-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)

---

## 🧭 Project Overview

**Enterprise AI Clinical Knowledge & Hospital Operations Assistant** is a full-stack system built for hospitals that need a single conversational entry point into two very different worlds:

1. **Unstructured clinical knowledge** — WHO guidelines stored as PDFs (Tuberculosis, Dengue, Hypertension, Diabetes).
2. **Structured operational data** — patients, doctors, admissions, appointments, billing, and lab records living inside PostgreSQL.

Instead of forcing doctors and administrators to manually search PDFs *and* query dashboards *and* remember which system holds which answer, this assistant routes every question to the right subsystem — Retrieval-Augmented Generation (RAG) for clinical knowledge, or a natural-language-to-SQL pipeline for operational data — and returns a single, cited, human-readable answer.

The backend is built with typed request/response contracts (Pydantic), a documented REST API (OpenAPI/Swagger), a hybrid retrieval pipeline (vector + keyword + re-ranking), and session-based conversation memory. The frontend is a polished enterprise dark-theme dashboard built with React 19.

> ⚠️ This is a personal/portfolio project. The hospital operations data (patients, doctors, admissions, billing, etc.) is **synthetically generated** using Python data-generation scripts, not real patient data.

---

## ❗ Business Problem

Hospitals run on fragmented information systems:

| Problem | Impact |
|---|---|
| Clinical guidelines exist only as static PDFs (WHO documents) | Doctors must manually search dozens of pages under time pressure |
| Hospital operations data lives in PostgreSQL, accessible only via dashboards or SQL | Non-technical staff cannot self-serve operational questions |
| No single interface unifies "what does the guideline say" with "what does our data say" | Constant context-switching between systems increases response time and risk of error |
| Generic chatbots hallucinate answers with no source attribution | Clinically risky in a healthcare setting where every claim needs a citation |

**This project addresses that by building one AI Assistant that can search both structured and unstructured healthcare knowledge, cite its sources, and query the hospital database in natural language.**

---

## 🎯 Objectives

- ✅ Build a **document-grounded** clinical assistant that answers clinical questions with a retrieved source.
- ✅ Build a **natural-language-to-SQL** agent that lets non-technical staff query hospital operations.
- ✅ Automatically **route** each incoming question to the correct subsystem (RAG vs. SQL vs. general LLM).
- ✅ Maintain **conversation memory** so follow-up questions retain context.
- ✅ Ship an **enterprise-style UI** — not a bare prototype chat window.
- ✅ Expose functionality through a documented **REST API** (OpenAPI/Swagger).
- ✅ Keep the system **provider-agnostic** at the LLM layer (cloud + local).

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🔎 Advanced RAG
- Hybrid retrieval (vector + BM25)
- Cross-encoder re-ranking
- Query expansion
- Metadata filtering
- Source citation with page numbers

</td>
<td width="50%" valign="top">

### 🗄️ Hospital Operations Assistant
- Natural language → SQL generation
- Read-only SQL execution
- Structured result formatting
- Works across patients, doctors, billing, labs, admissions, appointments

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧠 Conversational Intelligence
- Intent routing (RAG vs SQL vs LLM)
- Session-based conversation memory
- Context-aware follow-up handling

</td>
<td width="50%" valign="top">

### 🖥️ Enterprise UI
- Dark-theme dashboard shell
- Modular workspace (Patients, Doctors, Billing, Labs, Appointments, Admissions…)
- Framer Motion micro-interactions
- Responsive layout

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔌 REST API & Docs
- FastAPI backend
- Auto-generated Swagger / OpenAPI 3.1 docs
- Pydantic-validated schemas

</td>
<td width="50%" valign="top">

### 🤖 Multi-LLM Support
- Google Gemini (cloud)
- Ollama (local/offline)
- Swappable provider layer (`llm/factory.py`)

</td>
</tr>
</table>

<details>
<summary><strong>📋 Full feature checklist (click to expand)</strong></summary>

- [x] Hybrid Search (Vector + BM25)
- [x] Semantic vector search via ChromaDB
- [x] Keyword search (BM25)
- [x] Cross-encoder re-ranking of retrieved chunks
- [x] Query expansion for better recall
- [x] Metadata filtering
- [x] Intent detection / routing (RAG vs SQL vs general)
- [x] SQL generation from natural language
- [x] Read-only SQL execution
- [x] Source citation (document + page number)
- [x] Conversation memory (session-based)
- [x] Multi-provider LLM support (Gemini + Ollama)
- [x] REST API with Swagger/OpenAPI documentation
- [x] Report generation (sample discharge/incident PDF reports included in `/reports`)
- [x] Enterprise dashboard UI (React 19 + Vite + Tailwind)
- [x] Modular hospital workspace navigation (9 sections)
- [ ] Authentication / authorization — **not implemented** (see [Current Project Status](#-current-project-status))
- [ ] Live-data Analytics dashboard — **UI shell only, no backend wiring yet**

</details>

---

## 🏗️ Architecture

The system is split into a document ingestion pipeline, a dual-path reasoning core (RAG + SQL), and an enterprise frontend — all sitting behind a FastAPI backend.

![Architecture Diagram](screenshots/architecture.png)

**High-level flow:**

1. **Users** (doctors, administrators, hospital staff) interact through the **React frontend**.
2. Requests hit the **FastAPI backend** over REST.
3. The **Intent Classifier** (`app/rag/intent.py`) decides whether the query needs clinical knowledge (RAG), operational data (SQL), or a direct LLM response.
4. **RAG path**: Hybrid Retrieval (vector search + BM25 keyword search) pulls candidate chunks from ChromaDB → a Cross-Encoder Re-ranker reorders them by relevance → the top-K chunks become the retrieved context.
5. **SQL path**: SQL Intent Detection → LLM-based SQL Generation → read-only SQL Executor → structured Query Results.
6. Both paths converge into a single **LLM Response Generation** step (Gemini / Ollama), which produces the final response.
7. **Conversation Memory** (`app/rag/memory.py`) threads through both paths so follow-up questions retain context.

> ⚠️ **Security note (honest disclosure):** This project currently has **no authentication or authorization layer**. A `backend/app/auth/` module is scaffolded in the repository but is currently empty — there is no JWT, session auth, or API key enforcement on any route today. Do not deploy this as-is against real patient data. This is tracked in the [Future Roadmap](#-future-roadmap).

---

## 🔄 System Workflow

```
┌──────────────┐     ┌───────────────────┐     ┌────────────────────┐
│   User Query  │ ──▶ │  Intent Classifier │ ──▶ │  Route Decision     │
└──────────────┘     └───────────────────┘     └────────────────────┘
                                                        │
                        ┌───────────────────────────────┼───────────────────────────────┐
                        ▼                                ▼                                ▼
              ┌──────────────────┐            ┌──────────────────┐             ┌──────────────────┐
              │   RAG Pipeline    │            │   SQL Pipeline     │             │  Direct LLM Reply │
              │ (Clinical docs)   │            │ (Hospital DB)      │             │ (General queries)  │
              └──────────────────┘            └──────────────────┘             └──────────────────┘
                        │                                │                                │
                        ▼                                ▼                                │
              Vector + BM25 Search              SQL Generation (LLM)                       │
                        │                                │                                │
                        ▼                                ▼                                │
              Cross-Encoder Re-rank             Read-only SQL Execution                    │
                        │                                │                                │
                        ▼                                ▼                                │
              Top-K Retrieved Context           Structured Query Results                   │
                        │                                │                                │
                        └────────────────┬───────────────┴────────────────────────────────┘
                                          ▼
                              LLM Response Generation
                                  (Gemini / Ollama)
                                          │
                                          ▼
                          Final Response + Source Citations
                                          │
                                          ▼
                            Stored in Conversation Memory
```

---

## 🛠️ Technology Stack

<table>
<tr><th>Layer</th><th>Technology</th><th>Purpose</th></tr>
<tr><td rowspan="6"><strong>Frontend</strong></td><td>React 19</td><td>Component-based UI</td></tr>
<tr><td>Vite</td><td>Build tooling & dev server</td></tr>
<tr><td>Tailwind CSS</td><td>Utility-first styling</td></tr>
<tr><td>TanStack Query</td><td>Server-state management & caching</td></tr>
<tr><td>React Router</td><td>Client-side routing</td></tr>
<tr><td>Framer Motion</td><td>Animations & transitions</td></tr>
<tr><td rowspan="2"><strong>Frontend (icons/data)</strong></td><td>Lucide React</td><td>Icon system</td></tr>
<tr><td>Recharts / Axios</td><td>Charting primitives & HTTP client</td></tr>
<tr><td rowspan="2"><strong>Backend</strong></td><td>Python 3.11</td><td>Core language</td></tr>
<tr><td>FastAPI</td><td>Async REST API framework</td></tr>
<tr><td><strong>Data</strong></td><td>PostgreSQL</td><td>Hospital operational database (schema managed via raw SQL files)</td></tr>
<tr><td><strong>Vector Store</strong></td><td>ChromaDB</td><td>Embedding storage & semantic search over WHO guidelines</td></tr>
<tr><td rowspan="2"><strong>LLM Providers</strong></td><td>Google Gemini</td><td>Cloud-hosted generation (`app/llm/gemini.py`)</td></tr>
<tr><td>Ollama</td><td>Local/offline generation (`app/llm/ollama.py`)</td></tr>
<tr><td rowspan="4"><strong>RAG Internals</strong></td><td>BM25</td><td>Keyword/lexical retrieval</td></tr>
<tr><td>Cross-Encoder Re-ranker</td><td>Relevance re-scoring of retrieved chunks</td></tr>
<tr><td>Query Expansion</td><td>Improves recall for short/ambiguous queries</td></tr>
<tr><td>Metadata Filtering</td><td>Scopes retrieval by document metadata</td></tr>
<tr><td rowspan="2"><strong>Infra</strong></td><td>Docker</td><td>A `docker/` folder with a `Dockerfile` and `docker-compose.yml` is present in the repo</td></tr>
<tr><td>Git & GitHub</td><td>Version control</td></tr>
</table>

> Note: earlier drafts of this README referenced LangChain, Alembic, and JWT-based security libraries. None of these appear in the actual codebase and have been removed from this document.

---

## 📁 Folder Structure

This tree reflects the real repository layout (from `structure.txt`), with build artifacts (`__pycache__`, `node_modules`) omitted for readability.

```text
.
├── readme.md
├── requirements.txt
├── structure.txt
│
├── backend/
│   ├── .env
│   ├── .gitignore
│   ├── test_loader.py
│   ├── app/
│   │   ├── main.py
│   │   ├── test_connection.py
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   ├── router.py
│   │   │   └── routes/
│   │   │       ├── admissions.py
│   │   │       ├── appointments.py
│   │   │       ├── billing.py
│   │   │       ├── dashboard.py
│   │   │       ├── doctors.py
│   │   │       ├── health.py
│   │   │       ├── laboratory.py
│   │   │       └── patients.py
│   │   ├── auth/                    # present but currently empty — no auth implemented
│   │   ├── config/
│   │   │   ├── settings.py
│   │   │   └── __init__.py
│   │   ├── core/
│   │   │   ├── database.py
│   │   │   ├── settings.py
│   │   │   └── __init__.py
│   │   ├── llm/
│   │   │   ├── factory.py
│   │   │   ├── gemini.py
│   │   │   └── ollama.py
│   │   ├── models/
│   │   │   ├── admission.py
│   │   │   ├── appointment.py
│   │   │   ├── billing.py
│   │   │   ├── doctor.py
│   │   │   ├── laboratory.py
│   │   │   └── patient.py
│   │   ├── prompts/                 # present but currently empty
│   │   ├── rag/
│   │   │   ├── bm25.py
│   │   │   ├── bm25_retriever.py
│   │   │   ├── chat.py
│   │   │   ├── embeddings.py
│   │   │   ├── hybrid_retriever.py
│   │   │   ├── hybrid_search.py
│   │   │   ├── intent.py
│   │   │   ├── loader.py
│   │   │   ├── memory.py
│   │   │   ├── metadata.py
│   │   │   ├── query_expansion.py
│   │   │   ├── report_generator.py
│   │   │   ├── reranker.py
│   │   │   ├── retriever.py
│   │   │   ├── splitter.py
│   │   │   ├── sql_executor.py
│   │   │   ├── sql_generator.py
│   │   │   ├── sql_intent.py
│   │   │   ├── vectorstore.py
│   │   │   ├── vector_retriever.py
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   ├── admission_schema.py
│   │   │   ├── appointment_schema.py
│   │   │   ├── billing_schema.py
│   │   │   ├── dashboard_schema.py
│   │   │   ├── doctor_schema.py
│   │   │   ├── laboratory_schema.py
│   │   │   └── patient_schema.py
│   │   ├── services/
│   │   │   ├── admission_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── billing_service.py
│   │   │   ├── dashboard_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── laboratory_service.py
│   │   │   └── patient_service.py
│   │   ├── sql/
│   │   │   └── queries.py
│   │   └── utils/                   # present but currently empty
│   ├── chromadb/                    # persisted vector store data (chroma.sqlite3 + index files)
│   └── scripts/
│       ├── build_vector_db.py
│       ├── evaluate_embeddings.py
│       ├── test_bm25.py
│       ├── test_chat.py
│       ├── test_intent.py
│       ├── test_memory.py
│       ├── test_reranker.py
│       └── test_retrieval.py
│
├── chromadb/                        # empty top-level placeholder folder
│
├── database/
│   ├── functions.sql
│   ├── import_data.sql
│   ├── import_master.sql
│   ├── import_transactions.sql
│   ├── indexes.sql
│   ├── master_tables.md
│   ├── relationships.md
│   ├── schema.sql
│   ├── seed.sql
│   ├── transaction_tables.md
│   └── views.sql
│
├── datasets/
│   ├── admissions.csv
│   ├── appointments.csv
│   ├── beds.csv
│   ├── billing.csv
│   ├── departments.csv
│   ├── discharges.csv
│   ├── doctors.csv
│   ├── incident_reports.csv
│   ├── insurance.csv
│   ├── laboratory_results.csv
│   ├── nurses.csv
│   ├── operation_theatres.csv
│   ├── patients.csv
│   ├── pharmacy_inventory.csv
│   └── prescriptions.csv
│
├── docker/
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── docs/                            # present but currently empty
│
├── documents/
│   ├── clinical_guidelines/
│   │   ├── WHO Dengue Clinical Handbook (Bonus).pdf
│   │   ├── WHO Dengue Guidelines PDF.pdf
│   │   ├── WHO Diabetes Guideline.pdf
│   │   ├── WHO Hypertension Guideline.pdf
│   │   └── WHO Tuberculosis Guidelines.pdf
│   ├── emergency_protocols/         # present but currently empty
│   ├── hospital_policies/           # present but currently empty
│   ├── hospital_sops/               # present but currently empty
│   ├── laboratory_manuals/          # present but currently empty
│   ├── medical_books/               # present but currently empty
│   └── nursing_protocols/           # present but currently empty
│
├── frontend/
│   ├── .gitignore
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       ├── assets/
│       ├── components/
│       │   ├── ai/
│       │   │   ├── ChatInput.jsx
│       │   │   ├── ChatMessage.jsx
│       │   │   ├── SourceCard.jsx
│       │   │   └── TypingIndicator.jsx
│       │   ├── charts/
│       │   │   └── ChartShell.jsx
│       │   ├── dashboard/
│       │   │   └── KpiCard.jsx
│       │   ├── layout/
│       │   │   ├── MainLayout.jsx
│       │   │   ├── Navbar.jsx
│       │   │   └── Sidebar.jsx
│       │   ├── tables/
│       │   │   └── DataTable.jsx
│       │   └── ui/
│       │       ├── Badge.jsx
│       │       ├── Button.jsx
│       │       ├── Card.jsx
│       │       └── Skeleton.jsx
│       ├── context/                 # present but currently empty
│       ├── data/
│       │   └── mockData.js          # local mock data used by parts of the UI
│       ├── hooks/
│       │   └── useAnimatedCounter.js
│       ├── pages/
│       │   ├── Admissions.jsx
│       │   ├── Analytics.jsx        # UI shell — no backend route wired up yet
│       │   ├── Appointments.jsx
│       │   ├── Assistant.jsx
│       │   ├── Billing.jsx
│       │   ├── Dashboard.jsx
│       │   ├── Doctors.jsx
│       │   ├── Laboratory.jsx
│       │   ├── Patients.jsx
│       │   └── Settings.jsx         # UI shell — no backend route wired up yet
│       ├── routes/                  # present but currently empty
│       ├── services/
│       │   └── api.js
│       └── styles/
│           └── index.css
│
├── reports/
│   ├── discharge_report.pdf
│   └── incident_summary.pdf
│
├── screenshots/
│   ├── ai-assistant-home.png
│   ├── api-docs.png
│   ├── architecture.png
│   ├── dashboard.png
│   ├── rag-demo.png
│   ├── sidebar.png
│   └── sql-demo.png
│
└── scripts/
    ├── generate_admissions.py
    ├── generate_appointments.py
    ├── generate_beds.py
    ├── generate_billing.py
    ├── generate_departments.py
    ├── generate_discharges.py
    ├── generate_doctors.py
    ├── generate_incident_reports.py
    ├── generate_insurance.py
    ├── generate_lab_results.py
    ├── generate_nurses.py
    ├── generate_operation_theatres.py
    ├── generate_patients.py
    ├── generate_pharmacy_inventory.py
    ├── generate_prescriptions.py
    ├── test_reranker.py
    ├── validate_datasets.py
    └── validate_foreign_keys.py
```

> Note: the file actually present in the repository is named `ai-assistant-home.png.png` (a duplicate-extension typo). Rename it to `ai-assistant-home.png` (or update the path in this README) so the image renders correctly on GitHub.

---

## 🖼️ Screenshots

### AI Assistant — Home
The landing chat experience, with connected RAG status (`connected to /ai/chat`) and quick-start prompt suggestions.

![AI Assistant Home](screenshots/ai-assistant-home.png)

### Enterprise Dashboard
The main workspace shell — sidebar navigation, top bar search, and the AI Assistant panel embedded in context.

![Dashboard](screenshots/dashboard.png)

### RAG Demo — Clinical Knowledge in Action
A clinical question ("What is hypertension?") answered with a synthesized response and cited sources, each linking back to a specific WHO guideline and page number.

![RAG Demo](screenshots/rag-demo.png)

### 🗄️ SQL Demo — Hospital Operations in Action

Operational requests such as **"How many departments are there?"** and **"Show all departments."** are automatically classified as SQL queries. The assistant generates the required SQL, retrieves live data from PostgreSQL, and returns both the total department count (**10**) and the complete department list, demonstrating natural-language access to structured hospital data.

![SQL Demo](screenshots/sql_demo.png)

### Sidebar Navigation
The full modular workspace: AI Assistant, Dashboard, Patients, Doctors, Appointments, Admissions, Laboratory, Billing, Analytics, and Settings.

![Sidebar](screenshots/sidebar.png)

### API Documentation (Swagger / OpenAPI 3.1)
Auto-generated, interactive API documentation covering Health, Patients, Doctors, Appointments, and more.

![API Docs](screenshots/api-docs.png)

---

## ⚙️ Installation Guide

### Prerequisites

| Requirement | Notes |
|---|---|
| Python 3.11 | Backend runtime (matches compiled `.pyc` files in the repo) |
| Node.js 18+ | Frontend runtime |
| npm | Package manager for the frontend |
| PostgreSQL | Hospital operational database |
| Ollama | Only required if using local LLM inference |
| Google Gemini API Key | Only required if using Gemini as the LLM provider |
| Docker & Docker Compose | Optional — a `docker/` folder with a Dockerfile and compose file is included in the repo |

---

### Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/enterprise-ai-clinical-assistant.git
cd enterprise-ai-clinical-assistant

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies (requirements.txt lives at the project root)
pip install -r requirements.txt

# 4. Create backend/.env and configure it
#    (see the Environment Variables section below — no .env.example
#    ships in this repo, so this file must be created manually)

# 5. Set up the PostgreSQL schema using the SQL files in /database
psql -U <your_user> -d <your_database> -f database/schema.sql
psql -U <your_user> -d <your_database> -f database/functions.sql
psql -U <your_user> -d <your_database> -f database/indexes.sql
psql -U <your_user> -d <your_database> -f database/views.sql

# 6. Load data (synthetic datasets provided in /datasets, imported via /database)
psql -U <your_user> -d <your_database> -f database/import_master.sql
psql -U <your_user> -d <your_database> -f database/import_data.sql
psql -U <your_user> -d <your_database> -f database/import_transactions.sql

# 7. Build the ChromaDB vector store from the WHO guideline PDFs
cd backend
python scripts/build_vector_db.py
```

> There is no Alembic (or other migration tool) in this project. The database schema is created and evolved via the raw `.sql` files under `/database`, applied manually.

---

### Frontend Setup

```bash
# 1. Move into the frontend directory
cd ../frontend

# 2. Install dependencies
npm install

# 3. Configure the API base URL
#    The frontend does not use a .env file — the backend base URL
#    is set directly in src/services/api.js. Update it to match
#    wherever your backend is running (e.g. http://localhost:8000).

# 4. Start the development server
npm run dev
```

---

### Environment Variables

<details>
<summary><strong>Backend — <code>backend/.env</code> (click to expand)</strong></summary>

The backend reads configuration through `app/config/settings.py` and `app/core/settings.py`. Based on the modules present (`core/database.py`, `llm/gemini.py`, `llm/ollama.py`, `rag/vectorstore.py`), the following variables are expected — **confirm exact variable names against those two settings files before relying on this list**:

```env
# --- Database ---
DATABASE_URL=postgresql://user:password@localhost:5432/hospital_db

# --- ChromaDB ---
CHROMA_PERSIST_DIR=./backend/chromadb

# --- LLM Providers ---
GEMINI_API_KEY=your-gemini-api-key
OLLAMA_BASE_URL=http://localhost:11434
```

</details>

> The frontend has no `.env` file in this repository. Any environment-specific values (like the API base URL) are set directly in `frontend/src/services/api.js`.

---

### Running the Project

**Option A — Manual (two terminals)**

```bash
# Terminal 1 — Backend
cd backend
source ../venv/bin/activate
uvicorn app.main:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend
npm run dev
```

**Option B — Docker**

```bash
cd docker
docker compose up --build
```

> The exact services, ports, and volumes defined in `docker/docker-compose.yml` are not reproduced here — refer to that file directly, as its contents were not available for this audit.

Once running (default local ports):

- Frontend → `http://localhost:5173`
- Backend API → `http://localhost:8000`
- Swagger Docs → `http://localhost:8000/docs`
- OpenAPI Schema → `http://localhost:8000/openapi.json`

---

## 📖 Swagger Documentation

The backend automatically generates interactive **OpenAPI 3.1** documentation via FastAPI.

![API Docs](screenshots/api-docs.png)

Available at:

```
http://localhost:8000/docs
```

Resource groups confirmed in the live Swagger UI:

| Group | Endpoint | Method | Description |
|---|---|---|---|
| Health | `/api/v1/health` | GET | Health Check |
| Patients | `/api/v1/patients/` | GET | Read Patients |
| Patients | `/api/v1/patients/` | POST | Add Patient |
| Patients | `/api/v1/patients/search` | GET | Search Patient |
| Patients | `/api/v1/patients/{patient_id}` | GET | Read Patient |
| Doctors | `/api/v1/doctors/` | GET | Read Doctors |
| Doctors | `/api/v1/doctors/search` | GET | Search Doctor |
| Doctors | `/api/v1/doctors/{doctor_id}` | GET | Read Doctor |
| Appointments | `/api/v1/appointments/` | GET | Read Appointments |
| Appointments | `/api/v1/appointments/today` | GET | Today's Appointments |
| Appointments | `/api/v1/appointments/{appointment_id}` | GET | Read Appointment |
| AI Assistant | `/ai/chat` | POST | Unified RAG + SQL conversational endpoint (confirmed via the "connected to `/ai/chat`" badge in the UI) |

> No security scheme (JWT, API key, OAuth) is shown on any endpoint in the Swagger UI — consistent with there being no authentication layer implemented.

---

## 🔌 Example API Calls

> These examples reflect endpoints confirmed via the Swagger UI and the app's own UI badges. No `Authorization` header is included, since no auth layer exists in this project today.

### 1. Health Check

```bash
curl -X GET "http://localhost:8000/api/v1/health"
```

### 2. Ask the AI Assistant a Clinical Question (RAG path)

```bash
curl -X POST "http://localhost:8000/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{
        "message": "What is hypertension?"
      }'
```

Based on the RAG Demo screenshot, a response like this is returned along with cited sources (exact JSON field names are illustrative, since the raw response payload was not inspected directly):

```json
{
  "response": "Hypertension, or elevated blood pressure, is a serious medical condition that significantly increases the risk of diseases of the heart, brain, kidneys, and other organs...",
  "sources": [
    { "document": "WHO Hypertension Guideline", "page": 8 },
    { "document": "WHO Hypertension Guideline", "page": 32 },
    { "document": "WHO Hypertension Guideline", "page": 12 },
    { "document": "WHO Dengue Clinical Handbook", "page": 64 },
    { "document": "WHO Hypertension Guideline", "page": 13 }
  ]
}
```

### 3. Ask the AI Assistant an Operational Question (SQL path)

```bash
curl -X POST "http://localhost:8000/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{
        "message": "How many patients are there?"
      }'
```

Based on the SQL Demo screenshot, the assistant replies:

```json
{
  "response": "There are 4,952 patients in total."
}
```

### 4. Search Patients

```bash
curl -X GET "http://localhost:8000/api/v1/patients/search?query=diabetes"
```

### 5. Get Today's Appointments

```bash
curl -X GET "http://localhost:8000/api/v1/appointments/today"
```

---

## 🧩 RAG Pipeline Explanation

The RAG pipeline is the clinical-knowledge brain of the assistant, implemented under `backend/app/rag/`.

**Stages:**

1. **Ingestion (offline, run via `backend/scripts/build_vector_db.py`)**
   - PDF text extraction and loading (`rag/loader.py`) from the WHO guidelines in `documents/clinical_guidelines/` (Tuberculosis, Dengue Guidelines, Dengue Clinical Handbook, Hypertension, Diabetes).
   - Chunking (`rag/splitter.py`) into windows sized for embedding quality.
   - Embedding generation (`rag/embeddings.py`).
   - Storage in ChromaDB (`rag/vectorstore.py`), with the persisted index visible under `backend/chromadb/`.

2. **Query time**
   - The user's question is expanded (`rag/query_expansion.py`) to capture related clinical phrasing.
   - **Hybrid retrieval** runs both a vector similarity search (`rag/vector_retriever.py`) and a BM25 keyword search (`rag/bm25.py`, `rag/bm25_retriever.py`) over the same corpus (`rag/hybrid_retriever.py`, `rag/hybrid_search.py`).
   - Both result sets are re-ranked by a **cross-encoder** (`rag/reranker.py`).
   - Metadata filtering (`rag/metadata.py`) can scope retrieval further.
   - The top-K re-ranked chunks become the retrieved context.

3. **Generation**
   - The retrieved context + user question + conversation memory (`rag/memory.py`) are passed to the LLM (Gemini or Ollama, via `app/llm/factory.py`).
   - The response is returned alongside its source documents and page numbers, as seen in the [RAG Demo screenshot](#rag-demo--clinical-knowledge-in-action).

The `rag/report_generator.py` module also supports generating downloadable PDF reports — sample outputs (`discharge_report.pdf`, `incident_summary.pdf`) are included under `/reports`.

---

## 🗃️ SQL Agent Explanation

The SQL Agent lets hospital staff query operational data conversationally, implemented under `backend/app/rag/` (`sql_intent.py`, `sql_generator.py`, `sql_executor.py`) alongside `backend/app/sql/queries.py`.

**Stages:**

1. **SQL Intent Detection** (`sql_intent.py`) — confirms the query is operational in nature (e.g., "how many," "show me," "list all").
2. **SQL Generation (LLM)** (`sql_generator.py`) — the LLM generates a candidate SQL query against the hospital schema.
3. **SQL Executor** (`sql_executor.py`) — runs the query in a read-only manner against PostgreSQL.
4. **Query Results** — the result set is formatted into a natural-language response.

As shown in the [SQL Demo screenshot](#sql-demo--hospital-operations-in-action), the agent is conservative: when asked for a breakdown it cannot compute (e.g., a gender breakdown not present in the query result), it says so explicitly rather than fabricating a number.

---

## 🧭 Intent Routing Explanation

Every incoming message first passes through the **Intent Classifier** (`backend/app/rag/intent.py`), which decides which subsystem should handle it:

| Intent | Trigger examples | Destination |
|---|---|---|
| `RAG` | "What is the treatment protocol for dengue?", "What is hypertension?" | Hybrid Retrieval → Re-ranker → LLM |
| `SQL` | "How many patients are there?", "Show today's appointments" | SQL Generation → Read-only Execution |
| `GENERAL` | Greetings, clarifications, small talk | Direct LLM response |

The resolved intent is surfaced in the UI (see the `Intent: RAG` / `Intent: SQL` labels in the screenshots).

---

## 🔀 Hybrid Search Explanation

Neither pure vector search nor pure keyword search is sufficient on its own for clinical text:

- **Vector (semantic) search** (`rag/vector_retriever.py`) excels at conceptual similarity — it finds relevant chunks even when the user's wording differs from the document's wording.
- **BM25 (keyword) search** (`rag/bm25.py`, `rag/bm25_retriever.py`) excels at precision — it reliably surfaces chunks containing exact clinical terms.

`rag/hybrid_search.py` / `rag/hybrid_retriever.py` run both methods over the same query and merge the candidate sets, and the **cross-encoder re-ranker** (`rag/reranker.py`) makes the final relevance call by scoring each (query, chunk) pair jointly rather than independently.

> Note: the patient/doctor "search" box in the UI (`GET /api/v1/patients/search`, `GET /api/v1/doctors/search`) is a separate, structured database search — it is not part of the RAG hybrid search pipeline.

---

## 🧮 Vector Database Explanation

**ChromaDB** is used as the embedding store for ingested clinical documents, managed via `rag/vectorstore.py`. The persisted index is visible on disk under `backend/chromadb/` (a `chroma.sqlite3` file plus binary index segments), confirming this is an active, populated vector store rather than a placeholder.

- Chunks of each WHO guideline are embedded and stored with associated metadata, filterable via `rag/metadata.py`.
- The vector store is rebuilt by running `backend/scripts/build_vector_db.py` against the PDFs in `documents/clinical_guidelines/`.

---

## 📊 Current Project Status

| Component | Status |
|---|---|
| Backend API (FastAPI) | ✅ Implemented |
| PostgreSQL schema (raw SQL, no ORM migrations tooling) | ✅ Implemented |
| ORM-style data models (`app/models/`) | ✅ Implemented |
| Document ingestion pipeline (`scripts/build_vector_db.py`) | ✅ Implemented |
| Hybrid Retrieval (Vector + BM25) | ✅ Implemented |
| Cross-Encoder Re-ranking | ✅ Implemented |
| Query Expansion | ✅ Implemented |
| Metadata Filtering | ✅ Implemented |
| SQL Agent (NL → SQL, read-only execution) | ✅ Implemented |
| Intent Routing | ✅ Implemented |
| Conversation Memory | ✅ Implemented |
| Multi-LLM Support (Gemini + Ollama) | ✅ Implemented |
| PDF report generation (sample outputs in `/reports`) | ✅ Implemented |
| Enterprise Frontend UI (React + Vite + Tailwind) | ✅ Implemented |
| Swagger / OpenAPI Docs | ✅ Implemented |
| Docker / Docker Compose files | 🚧 Present in repo (`/docker`), not verified end-to-end in this audit |
| Authentication (JWT or otherwise) | ❌ Not implemented (`app/auth/` folder is scaffolded but empty) |
| Role-based Access Control | ❌ Not implemented |
| Analytics page | 🚧 UI shell only — no backend route/service wired up |
| Settings page | 🚧 UI shell only — no backend route/service wired up |
| Frontend mock data (`src/data/mockData.js`) | 🚧 Present — some UI elements may rely on local mock data rather than live API calls |
| Automated test suite (pytest-style CI tests) | 🚧 Manual test/eval scripts present (`scripts/test_*.py`, `backend/app/test_connection.py`) — not confirmed to be a wired-up automated suite |
| Database migration tooling (e.g. Alembic) | ❌ Not implemented (schema managed via raw `.sql` files) |
| CI/CD Pipeline | ❌ Not implemented (no workflow files found in the repository) |

---

## 🗺️ Future Roadmap

- [ ] **Authentication & authorization** — implement JWT (or similar) auth and wire it into the currently-empty `app/auth/` module
- [ ] **Role-based Access Control** — separate permissions for doctors, administrators, and lab staff
- [ ] **Wire the Analytics page to real backend data** (currently a UI shell)
- [ ] **Wire the Settings page to a real backend service** (currently a UI shell)
- [ ] **Reduce/remove frontend reliance on `mockData.js`** in favor of live API calls throughout
- [ ] **Database migration tooling** (e.g., Alembic) instead of manually-applied `.sql` files
- [ ] **Automated CI test suite** wired into GitHub Actions (none exists today)
- [ ] **Streaming responses** for the AI Assistant (token-by-token)
- [ ] **Audit logging** for AI-generated SQL queries
- [ ] **Multi-turn SQL refinement** — allow follow-up corrections like "filter that by department"
- [ ] **PDF upload UI** so administrators can add new clinical guidelines without redeploying
- [ ] **Evaluation harness** for RAG answer quality (retrieval precision/recall, citation accuracy) — builds on the existing `scripts/evaluate_embeddings.py`
- [ ] **Kubernetes deployment manifests**, if/when the project is actually deployed
- [ ] **Multi-language support** for clinical guideline retrieval

---

## 🚀 Deployment Guide

This project has **not been deployed** to any hosting environment as part of this repository — there are no CI/CD workflow files, no cloud configuration (Terraform, Kubernetes manifests, Nginx configs, Vercel/Render/Fly configs, etc.), and no managed-database provisioning included in the codebase.

The `docker/` folder (containing a `Dockerfile` and `docker-compose.yml`) provides a starting point for containerized local or self-hosted running, but a full production deployment guide will be added once the project is actually deployed. See the [Future Roadmap](#-future-roadmap) for planned deployment-related work.

---

## 🐳 Docker

A `docker/` folder exists at the project root containing:

- `Dockerfile`
- `docker-compose.yml`

The exact services, images, ports, and volumes defined inside these files were not available as part of this audit (only the file listing, not their contents, was reviewed) — refer to `docker/docker-compose.yml` directly for the authoritative configuration.

**Generic commands** (assuming a standard Compose setup):

```bash
cd docker

# Build and start
docker compose up --build

# Start in detached mode
docker compose up -d

# View logs
docker compose logs -f

# Stop and remove containers
docker compose down
```

---

## 🎬 Project Demonstration

**Clinical Knowledge Flow (RAG):**

> User asks *"What is hypertension?"* → Intent Classifier routes to RAG → Hybrid Retrieval pulls candidate chunks from the WHO Hypertension Guideline and WHO Dengue Clinical Handbook → Cross-Encoder re-ranks them → LLM synthesizes a grounded answer → UI displays the answer with **5 clickable source citations**, each showing the exact document and page number.

**Hospital Operations Flow (SQL):**

> User asks *"How many patients are there?"* → Intent Classifier routes to SQL → the SQL Agent queries PostgreSQL → UI displays *"There are 4,952 patients in total"* — and honestly declines to answer a follow-up gender-breakdown question since that data isn't available in the query result, rather than guessing.

See the [Screenshots](#-screenshots) section above for the full visual walkthrough of both flows, the dashboard shell, and the API documentation.

---

## 🗂️ Repository Structure

See the [Folder Structure](#-folder-structure) section above for the full, structure.txt-verified backend/frontend layout.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes with clear, descriptive messages
   ```bash
   git commit -m "Add: short description of change"
   ```
4. Push to your fork and open a **Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
5. Ensure your PR description explains **what** changed and **why**

**Guidelines:**

- Follow the existing project structure (`backend/app/services/` for business logic, `backend/app/rag/` for RAG/SQL-agent logic, `frontend/src/pages/` + `frontend/src/components/` for UI).
- Add/update Pydantic schemas (`backend/app/schemas/`) for any new API request or response shape.
- Open an issue first for large feature proposals, so the direction can be discussed before implementation.

---

## 📄 License

No `LICENSE` file currently exists in this repository. The terms below are a suggested **MIT License** for the project author to formally adopt by adding a `LICENSE` file at the project root.

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

Built and maintained by the repository owner as a portfolio project demonstrating full-stack, RAG-based, enterprise-style application development.

---

## 🙏 Acknowledgements

- **World Health Organization (WHO)** — for the publicly available clinical guideline PDFs (Tuberculosis, Dengue, Hypertension, Diabetes) used as the knowledge base for the RAG pipeline.
- **FastAPI**, **React**, **ChromaDB**, and the broader open-source Python/JavaScript ecosystem that this project is built on.
- **Google Gemini** and **Ollama** for the LLM inference options integrated into the assistant.
