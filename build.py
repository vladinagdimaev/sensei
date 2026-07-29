from pathlib import Path
import shutil


ROOT = Path(__file__).parent
OUTPUT = ROOT / "public"


def copy_directory(name: str) -> None:
    source = ROOT / name
    destination = OUTPUT / name

    if source.exists():
        shutil.copytree(source, destination)
        print(f"Copied directory: {name}")
    else:
        print(f"Skipped missing directory: {name}")


def copy_page(source_name: str, destination: Path) -> None:
    source = ROOT / source_name

    if not source.exists():
        raise FileNotFoundError(f"Required file not found: {source_name}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"Copied page: {source_name} -> {destination.relative_to(ROOT)}")


def build() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)

    OUTPUT.mkdir()

    copy_page("index.html", OUTPUT / "index.html")
    copy_page("privacy.html", OUTPUT / "privacy" / "index.html")
    copy_page(
        "accessibility.html",
        OUTPUT / "accessibility" / "index.html",
    )
    
    for directory in ("images", "styles", "fonts", "scripts", "vcard"):
        copy_directory(directory)

    print("\nBuild completed successfully.")
    print(f"Output directory: {OUTPUT}")


if __name__ == "__main__":
    build()
