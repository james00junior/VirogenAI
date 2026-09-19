"""Document inventory and lightweight metadata extraction."""
from dataclasses import dataclass
from pathlib import Path

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".json", ".csv"}

@dataclass(frozen=True)
class DocumentRecord:
    path: str
    domain: str
    extension: str


def inventory_documents(root: Path, domain: str) -> list[DocumentRecord]:
    """Return supported files for a domain without reading their contents."""
    if not root.exists():
        return []
    return [
        DocumentRecord(str(path), domain, path.suffix.lower())
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
