import typer
from rich.console import Console

from gitstory import git_log, stats

app = typer.Typer()
console = Console()


def bar(count: int, max_count: int, width: int = 30) -> str:
    """Make a simple text bar proportional to count."""
    filled = int((count / max_count) * width) if max_count else 0
    return "█" * filled


@app.command()
def show(path: str = "."):
    """Show a repo's commit history dashboard."""
    commits = git_log.get_commits(path)

    if not commits:
        console.print("[yellow]No commits found. Is this a git repo?[/yellow]")
        raise typer.Exit()

    # --- Summary ---
    start, end = stats.date_range(commits)
    authors = stats.author_counts(commits)
    console.print(f"\n[bold]📊 Repo History[/bold]")
    console.print(f"[dim]{len(commits)} commits · {len(authors)} contributors · {start} → {end}[/dim]\n")

    # --- Top contributors ---
    console.print("[bold cyan]Top Contributors[/bold cyan]")
    max_author = authors[0][1]
    for name, count in authors[:5]:
        console.print(f"  {name:<20} [green]{bar(count, max_author)}[/green] {count}")

    # --- Activity by month ---
    console.print("\n[bold cyan]Activity by Month[/bold cyan]")
    months = stats.commits_by_month(commits)
    max_month = max(c for _, c in months)
    for month, count in months:
        console.print(f"  [dim]{month}[/dim] [magenta]{bar(count, max_month)}[/magenta] {count}")

    # --- File hotspots ---
    console.print("\n[bold cyan]File Hotspots[/bold cyan]")

    changed_files = git_log.get_changed_files(path)
    hotspots = stats.file_hotspots(changed_files)

    if hotspots:
        top_count = hotspots[0][1]  # sabse zyada badli file ka count
        for filepath, count in hotspots[:5]:
            file_bar = bar(count, top_count)
            console.print(f"  {filepath:<40} [yellow]{file_bar}[/yellow] {count}")


if __name__ == "__main__":
    app()