# 🔍 devask

Ask questions about any codebase in plain English — a RAG-powered CLI that actually reads your code.

`devask` indexes a repository locally, then answers natural-language questions about it using retrieval-augmented generation. No database, no server — just `pip install` and ask.

## Features

- Index any local repo with a single command
- Ask questions in plain English, get answers grounded in your actual code
- Cites the source files each answer came from
- Exact vector search with NumPy — no external vector DB needed
- Local, portable index stored in your home directory

## Installation

```bash
git clone https://github.com/prateekbabani/devkit.git
cd devkit/devask

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -e .
```

## Setup

Create a `.env` file in the `devask/` folder:

OPENAI_API_KEY=your-key-here

## Usage

```bash
devask index --path /path/to/repo    # index a codebase (run once)
devask ask "how does authentication work?"
```

## How it works

1. `scanner.py` — walks the repo and reads code files, skipping junk like `node_modules` and `venv`
2. `chunker.py` — splits files into overlapping chunks so context isn't lost at boundaries
3. `embedder.py` — converts chunks to vectors via OpenAI `text-embedding-3-small`, batched
4. `store.py` — saves chunks + vectors as a NumPy matrix to `~/.devask/index.pkl`
5. `ai.py` — embeds the question, ranks chunks by cosine similarity, and feeds the top matches to the LLM

## Tech stack

- **Python 3.12**
- **typer** — CLI framework
- **numpy** — vector math and cosine similarity
- **openai** — embeddings + LLM calls
- **rich** — terminal formatting
- **python-dotenv** — environment config

## Roadmap

- Incremental re-indexing (only changed files)
- Support for multiple saved indexes (per-repo)
- Configurable chunk size and top-K