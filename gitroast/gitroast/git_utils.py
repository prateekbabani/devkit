import subprocess

def get_staged_diff() -> str :
    result =  subprocess.run(
        ["git", "diff", "--cached"],
        capture_output= True,
        text = True

    )

    if result.returncode != 0:
        return ""
    return result.stdout or ""