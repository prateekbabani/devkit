from pathlib import Path


# Yeh folders skip karenge — inme code nahi, junk hota hai
SKIP_DIRS = {
    ".git", "venv", ".venv", "node_modules", "__pycache__",
    "dist", "build", ".idea", ".vscode", "egg-info",
}

# Sirf yeh extensions padhenge
CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java",
    ".go", ".rs", ".c", ".cpp", ".h", ".md",
}

def scan_repo(root : str = ".") -> list[dict] :
    files = []
    root_path= Path(root)

    for path in root_path.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue

        if not  path.is_file() or path.suffix not in CODE_EXTENSIONS:
            continue

        try :
            content =  path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        if content.strip():
            files.append({
                "path" : str(path.relative_to(root_path)),
                "content" : content
            })

    return files


