# devkit

A collection of small, focused developer tools — self-contained command-line utilities for everyday engineering work, built in Python.

![Python](https://img.shields.io/badge/python-3.12-blue)

Each tool lives in its own package with its own README and installs independently. They share a philosophy: do one thing well, run locally, and stay dependency-light.

---

## Tools

| Tool | What it does |
|------|--------------|
| 🔥 **[gitroast](./gitroast)** | AI-powered code reviewer that roasts your staged git diff — sharp, funny, and technically grounded. |
| 🔍 **[devask](./devask)** | RAG-powered codebase Q&A. Index any repo, then ask questions in plain English with cited sources. |
| 📊 **[gitstory](./gitstory)** | Terminal dashboard for a repo's git history — contributors, activity over time, and file hotspots. |

---

## Quick look

**gitroast** — roast your staged changes
```bash
git add .
gitroast
```

**devask** — ask your codebase anything
```bash
devask index --path /path/to/repo
devask ask "how does authentication work?"
```

**gitstory** — visualize a repo's history
```bash
gitstory --path /path/to/repo
```

---

## Design philosophy

Most developer tooling is either heavyweight — needing a server, a database, a dashboard — or a black box you can't see inside. `devkit` tools are the opposite: each is a single `pip install`, runs locally, and does one thing well.

They're also a hands-on exploration of building real systems from scratch — prompt design, RAG pipelines, embeddings and vector search, and git internals — without leaning on managed services.

---

## Tech stack

**Python 3.12** · typer · rich · openai · numpy

---

## Getting started

Each tool installs independently. Clone the repo, enter a tool's folder, and follow its README:

```bash
git clone https://github.com/prateekbabani/devkit.git
cd devkit/gitroast   # or devask, or gitstory
```

---

## Roadmap

- A shared core for config and OpenAI client setup
- PyPI publishing so tools install with a plain `pip install`
- More tools coming in the future
