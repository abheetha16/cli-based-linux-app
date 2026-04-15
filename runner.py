import subprocess
import sys

def run(command: str, check: bool = True):
    """
    Executes a shell command.
    Exits on failure if check=True.
    """

    print(f"[CMD] {command}")

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.stdout:
        print(result.stdout.strip())

    if result.returncode != 0:
        print(f"❌ Command failed: {command}")
        print(result.stderr.strip())

        if check:
            sys.exit(result.returncode)

    return result
