import typer
from rich.console import Console

from gitstory import git_log

app = typer.Typer()
console = Console()


@app.command()
def show(path: str = "."):
    """Show a repo's commit history."""
    commits = git_log.get_commits(path)

    if not commits:
        console.print("[yellow]No commits found. Is this a git repo?[/yellow]")
        raise typer.Exit()

    console.print(f"[green]{len(commits)} commits found.[/green]\n")

    # show the first 5
    for c in commits[:5]:
        console.print(f"[dim]{c['date']}[/dim] [cyan]{c['author']}[/cyan]: {c['subject']}")


if __name__ == "__main__":
    app()