import subprocess
import sys
from utils.logger import log_info, log_error

def run(command: str, check: bool = True):
    """
    Executes a shell command with logging and error handling.

    Args:
        command (str): Command to execute
        check (bool): Exit program if command fails

    Returns:
        subprocess.CompletedProcess
    """

    print(f"\n[CMD] {command}")
    log_info(f"Executing: {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Print standard output
        if result.stdout:
            print(result.stdout.strip())

        # Handle errors
        if result.returncode != 0:
            print(f"❌ Command failed: {command}")
            if result.stderr:
                print(result.stderr.strip())

            log_error(f"Command failed: {command}")
            log_error(result.stderr.strip())

            if check:
                sys.exit(result.returncode)

        return result

    except Exception as e:
        print(f"❌ Exception occurred while running: {command}")
        print(str(e))

        log_error(f"Exception: {str(e)}")

        if check:
            sys.exit(1)
