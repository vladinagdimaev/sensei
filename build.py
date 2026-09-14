from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def run(*command: str) -> None:
    print(f"Running: {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def build() -> None:
    run("npm", "ci")
    run("npm", "run", "build:css")
    run(sys.executable, "-m", "pelican", "content", "-s", "pelicanconf.py")


if __name__ == "__main__":
    build()
