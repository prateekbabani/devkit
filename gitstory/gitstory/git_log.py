import subprocess


def get_commits(repo_path: str = ".") -> list[dict]:
    """Parse git log and return a list of commits."""
    # Custom format: hash | author | date | subject
    # %H=hash, %an=author name, %ad=date, %s=subject
    result = subprocess.run(
        ["git", "-C", repo_path, "log",
         "--pretty=format:%H|%an|%ad|%s", "--date=short"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return []

    commits = []
    for line in result.stdout.splitlines():
        parts = line.split("|", 3)   # split on first 3 pipes only
        if len(parts) == 4:
            commits.append({
                "hash": parts[0],
                "author": parts[1],
                "date": parts[2],
                "subject": parts[3],
            })

    return commits