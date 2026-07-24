import pickle
import numpy as np
from pathlib import Path

INDEX_DIR = Path.home() / ".devask"
INDEX_FILE = INDEX_DIR / "index.pkl"

def save_index(chunks : list[dict], vectors : list[list[float]], repo_path : str) -> None:

    INDEX_DIR.mkdir(exist_ok= True)

    data = {
        "repo_path": repo_path,
        "chunks": chunks,
        "vectors": np.array(vectors, dtype=np.float32),
    }

    with open(INDEX_FILE, "wb") as f:
        pickle.dump(data, f)



def load_index() -> dict | None:
    """Index load karo agar available ho, warna None return karo."""
    if not INDEX_FILE.exists():
        return None

    with open(INDEX_FILE, "rb") as f:
        data = pickle.load(f)

    return data
