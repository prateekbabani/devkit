CHUNK_SIZE = 1500      # characters per chunk
CHUNK_OVERLAP = 200    # adjacent chunks kitna overlap karein


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Ek bade text ko overlapping chunks mein todo."""
    if len(text) <= size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap   # peeche hat ke overlap banao

    return chunks


def chunk_files(files: list[dict]) -> list[dict]:
    """Saari files ko chunks mein todo, path track karte hue."""
    all_chunks = []

    for f in files:
        pieces = chunk_text(f["content"])
        for i, piece in enumerate(pieces):
            all_chunks.append({
                "path": f["path"],
                "chunk_index": i,
                "content": piece,
            })

    return all_chunks