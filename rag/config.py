"""Configuration primitives for the scientific RAG workflow."""
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = PROJECT_ROOT / "data"

@dataclass(frozen=True)
class DomainConfig:
    name: str
    relative_path: str
    description: str

DOMAINS = (
    DomainConfig("ksp37", "raw/ksp37", "KSP37 literature: immune profiling, biomarkers, molecular function."),
    DomainConfig("aptamers", "raw/aptamers", "Aptamer literature and molecular targeting evidence."),
    DomainConfig("linkers", "raw/linkers", "Linker literature and molecular design evidence."),
    DomainConfig("virogen_reports", "raw/virogen_reports", "Primary Viro-Gen experimental reports."),
)
