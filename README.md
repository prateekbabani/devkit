# devkit

A growing collection of AI-powered developer tools — small, focused CLIs that make everyday dev work faster (and occasionally funnier).

Each tool is self-contained: its own package, its own README, installable on its own. Built with Python, `typer`, and the OpenAI API.

## Tools

### 🔥 [gitroast](./gitroast)
An AI CLI that roasts your staged git changes. It reads your diff and returns a savage-but-technically-valid critique of your code — part code review, part comedy.

```bash
git add .
gitroast
```

### 🔍 [devask](./devask)
A RAG-powered CLI that answers plain-English questions about any codebase. Index a repo once, then ask it anything — answers are grounded in your actual code and cite their sources.

```bash
devask index --path /path/to/repo
devask ask "how does authentication work?"
```

## Why devkit

Most dev tooling is either heavyweight (needs a server, a database, a dashboard) or a black box. `devkit` tools are the opposite — each one is a single `pip install`, runs locally, and does one thing well. They're also a playground for building real, small-scale AI systems from scratch: prompt design, RAG pipelines, embeddings, and vector search without leaning on managed services.

## Stack

Python 3.12 · typer · rich · openai · numpy

## Getting started

Each tool installs independently. Head into its folder and follow its README:

```bash
git clone https://github.com/prateekbabani/devkit.git
cd devkit/gitroast   # or devkit/devask
```

## Roadmap

- More tools (a git history visualizer is next)
- A shared core for config and OpenAI client setup
- PyPI publishing so tools install with a plain `pip install`
