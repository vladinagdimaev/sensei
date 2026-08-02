from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"

STATIC_DIRECTORIES = (
    "images",
    "styles",
    "fonts",
    "vcard",
)


def copy_static_directory(name: str) -> None:
    source = ROOT / name
    destination = CONTENT / name

    if not source.is_dir():
        print(f"Skipped missing directory: {name}")
        return

    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
    print(f"Prepared static directory: {name}")


def main() -> None:
    CONTENT.mkdir(exist_ok=True)

    for directory in STATIC_DIRECTORIES:
        copy_static_directory(directory)


if __name__ == "__main__":
    main()
