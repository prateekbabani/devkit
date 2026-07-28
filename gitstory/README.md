# 📊 gitstory

Visualize any git repository's history right in your terminal — contributors, activity over time, and file hotspots at a glance.

`gitstory` parses a repo's commit log and renders a clean dashboard: who's committing, when the project was most active, and which files change the most.

## Features

- Summary of total commits, contributors, and date range
- Top contributors ranked by commit count
- Commit activity broken down by month
- File hotspots — the most frequently changed files
- Pure terminal output, no dependencies beyond typer and rich

## Installation

```bash
git clone https://github.com/prateekbabani/devkit.git
cd devkit/gitstory

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -e .
```

## Usage

```bash
gitstory --path /path/to/repo
```

Run it with no path to analyze the current directory:

```bash
gitstory
```

## How it works

1. `git_log.py` — runs `git log` via `subprocess` with a custom format to extract commits and changed files
2. `stats.py` — aggregates the raw data using `Counter` (commits per author, per month, per file)
3. `main.py` — a `typer` CLI that renders everything as proportional bar charts with `rich`

## Tech stack

- **Python 3.12**
- **typer** — CLI framework
- **rich** — terminal formatting and bar charts

## Roadmap

- Activity by day of week / hour
- Date range filtering (`--since`, `--until`)
- Export dashboard as an image