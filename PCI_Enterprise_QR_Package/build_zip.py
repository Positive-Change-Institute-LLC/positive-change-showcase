"""Build a portable ZIP archive of this package."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

PACKAGE_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = PACKAGE_ROOT.parent
ARCHIVE = REPOSITORY_ROOT / "PCI_Enterprise_QR_Package.zip"
EXCLUDED_PARTS = {".git", ".venv", "__pycache__"}


def main() -> None:
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED) as package:
        for path in sorted(PACKAGE_ROOT.rglob("*")):
            if not path.is_file() or EXCLUDED_PARTS.intersection(path.parts):
                continue
            package.write(path, path.relative_to(REPOSITORY_ROOT))
    print(f"Created {ARCHIVE}")


if __name__ == "__main__":
    main()
