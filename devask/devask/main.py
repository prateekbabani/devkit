import typer
from rich.console import Console
from devask import scanner, chunker, embedder, store, ai   # ai add


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

    with console.status("[dim]Embeddings ban rahe...[/dim]", spinner="dots"):
        texts = [c["content"] for c in chunks]
        vectors = embedder.embed_texts(texts)

    store.save_index(chunks, vectors, path)
    console.print(f"[green]Index saved.[/green] [dim]({store.INDEX_FILE})[/dim]")



@app.command()
def ask(question: str):
    """Codebase se sawaal poocho."""
    index = store.load_index()

    if index is None:
        console.print("[yellow]Koi index nahi mila. Pehle `devask index` chala.[/yellow]")
        raise typer.Exit()

    with console.status("[dim]Dhoondh raha hoon...[/dim]", spinner="dots"):
        results = ai.search(question, index)
        response = ai.answer(question, results)

    console.print(f"\n{response}\n")
    console.print("[dim]Sources:[/dim]")
    for r in results:
        console.print(f"  [cyan]{r['path']}[/cyan] [dim](score: {r['score']:.3f})[/dim]")


if __name__ == "__main__":
    app()