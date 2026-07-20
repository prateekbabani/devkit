import typer
from rich.console import Console

from gitroast import git_utils, ai

app = typer.Typer()
console = Console()


@app.command()
def roast():
    """Tere staged changes ko roast karo."""
    diff = git_utils.get_staged_diff()

    if not diff.strip():
        console.print("[yellow]Kuch staged nahi hai bhai. Pehle `git add` kar.[/yellow]")
        raise typer.Exit()

    with console.status("[dim]Roast likh raha hoon...[/dim]", spinner="dots"):
        roast_text = ai.roast_diff(diff)

    console.print(f"[bold red]🔥 ROAST 🔥[/bold red]\n")
    console.print(roast_text)


if __name__ == "__main__":
    app()