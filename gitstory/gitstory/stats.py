from collections import Counter


def author_counts(commits: list[dict]) -> list[tuple[str, int]]:
    """Count commits per author, most active first."""
    counter = Counter(c["author"] for c in commits)
    return counter.most_common()

def commits_by_month(commits: list[dict]) -> list[tuple[str, int]]:
    """Count commits per month (YYYY-MM), oldest first."""
    counter = Counter(c["date"].strip()[:7] for c in commits)   # strip whitespace
    return sorted(counter.items())

def date_range(commits: list[dict]) -> tuple[str, str]:
    """Return (earliest date, latest date)."""
    dates = sorted(c["date"] for c in commits)
    return dates[0], dates[-1]

