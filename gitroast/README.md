# 🔥 gitroast

An AI-powered CLI that roasts your staged git changes — because your code deserves an honest opinion.

`gitroast` reads your staged diff, sends it to an LLM, and returns a savage-but-technically-valid roast of your code. Part code review, part comedy.


## Features

- Reads staged changes via `git diff --cached`
- LLM-generated roasts with actual technical observations
- Clean terminal UI with a loading spinner
- Graceful error handling (network failures don't crash the tool)

## Installation

```bash
git clone https://github.com/prateekbabani/devkit.git
cd devkit/gitroast

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -e .
```

## Setup

Create a `.env` file in the `gitroast/` folder:

OPENAI_API_KEY=your-key-here


## Usage

```bash
git add .        # stage your changes
gitroast         # roast them
```

## How it works

1. `git_utils.py` — runs `git diff --cached` via `subprocess` and captures the staged diff
2. `ai.py` — sends the diff to the OpenAI API with a "savage senior dev" system prompt
3. `main.py` — a `typer` CLI that ties it together, with a `rich` spinner and styled output

## Tech stack

- **Python 3.12**
- **typer** — CLI framework
- **rich** — terminal formatting and spinners
- **openai** — LLM calls
- **python-dotenv** — environment config

## Roadmap

- `--last` flag to roast the most recent commit
- Adjustable roast intensity (mild / medium / savage)
- Support for other LLM providers