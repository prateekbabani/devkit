import typer
from rich.console import Console

from devask import scanner

app = typer.Typer()
console = Console()


@app.command()
def index(path: str = "."):
    """Repo scan karke index banao."""
    console.print(f"[dim]Scanning {path}...[/dim]")

    files = scanner.scan_repo(path)

    console.print(f"[green]{len(files)} files mili.[/green]\n")

    # pehli 10 files dikhao
    for f in files[:10]:
        console.print(f"  [cyan]{f['path']}[/cyan] — {len(f['content'])} chars")


if __name__ == "__main__":
    app()