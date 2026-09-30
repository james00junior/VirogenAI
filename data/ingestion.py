"""Phase 2 remediation primitives for genomic data ingestion."""
from dataclasses import dataclass
from pathlib import Path

SUPPORTED_GENOMIC_EXTENSIONS = {
    ".fastq", ".fastq.gz", ".fasta", ".fa", ".bam", ".sam", ".sff",
}


@dataclass(frozen=True)
class IngestionValidation:
    path: str
    detected_format: str | None
    accepted: bool
    size_bytes: int
    reasons: tuple[str, ...] = ()


def detect_genomic_format(path: Path) -> str | None:
    name = path.name.lower()
    for extension in sorted(SUPPORTED_GENOMIC_EXTENSIONS, key=len, reverse=True):
        if name.endswith(extension):
            return extension.lstrip(".")
    return None


def validate_genomic_file(
    path: Path, *, max_bytes: int | None = None
) -> IngestionValidation:
    if not path.exists():
        return IngestionValidation(str(path), None, False, 0, ("file_not_found",))
    if not path.is_file():
        return IngestionValidation(str(path), None, False, 0, ("not_a_file",))

    reasons: list[str] = []
    detected = detect_genomic_format(path)
    if detected is None:
        reasons.append("unsupported_format")

    size = path.stat().st_size
    if max_bytes is not None and size > max_bytes:
        reasons.append("file_too_large")

    return IngestionValidation(
        path=str(path),
        detected_format=detected,
        accepted=not reasons,
        size_bytes=size,
        reasons=tuple(reasons),
    )
