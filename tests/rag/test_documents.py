from pathlib import Path

from rag.documents import inventory_documents


def test_inventory_missing_directory_returns_empty(tmp_path: Path) -> None:
    assert inventory_documents(tmp_path / "missing", "ksp37") == []


def test_inventory_filters_supported_extensions(tmp_path: Path) -> None:
    (tmp_path / "paper.pdf").write_text("x", encoding="utf-8")
    (tmp_path / "notes.py").write_text("x", encoding="utf-8")
    records = inventory_documents(tmp_path, "ksp37")
    assert len(records) == 1
    assert records[0].domain == "ksp37"
