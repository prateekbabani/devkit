import typer
from rich.console import Console

from devask import scanner
from devask.devask import chunker

app = typer.Typer()
console = Console()


@app.command()
def index(path: str = "."):
    """Repo scan karke index banao."""
    console.print(f"[dim]Scanning {path}...[/dim]")

    files = scanner.scan_repo(path)
    console.print(f"[green]{len(files)} files mili.[/green]")

    chunks = chunker.chunk_files(files)
    console.print(f"[green]{len(chunks)} chunks bane.[/green]")

    # pehli 10 files dikhao
    for f in files[:10]:
        console.print(f"  [cyan]{f['path']}[/cyan] — {len(f['content'])} chars")


if __name__ == "__main__":
    app()