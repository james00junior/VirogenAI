from pathlib import Path

from data.ingestion import detect_genomic_format, validate_genomic_file


def test_detects_supported_genomic_formats():
    assert detect_genomic_format(Path("reads.fastq.gz")) == "fastq.gz"
    assert detect_genomic_format(Path("assembly.fasta")) == "fasta"
    assert detect_genomic_format(Path("aligned.bam")) == "bam"
    assert detect_genomic_format(Path("aligned.sam")) == "sam"
    assert detect_genomic_format(Path("legacy.sff")) == "sff"


def test_rejects_unsupported_format(tmp_path):
    path = tmp_path / "reads.xlsx"
    path.write_text("not genomic data")
    result = validate_genomic_file(path)

    assert result.accepted is False
    assert "unsupported_format" in result.reasons
