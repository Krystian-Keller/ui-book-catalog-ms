from __future__ import annotations

from src.sample_loader import (
    SAMPLE_DIR,
    ImportSample,
    list_sample_files,
    load_import_sample,
    load_sample_content,
)


def test_list_sample_files_returns_json_files() -> None:
    files = list_sample_files()
    assert files
    assert all(name.endswith(".json") for name in files)


def test_load_sample_content_reads_file() -> None:
    files = list_sample_files()
    first_file = files[0]
    content = load_sample_content(first_file)
    assert content
    assert SAMPLE_DIR.name in str(SAMPLE_DIR)


def test_load_import_sample_extracts_format_and_content() -> None:
    sample = load_import_sample("dummy_import_4_xml.json")
    assert isinstance(sample, ImportSample)
    assert sample.format == "xml"
    assert sample.content.startswith("<?xml")


def test_load_import_sample_json_catalog_body_only() -> None:
    sample = load_import_sample("dummy_import_2.json")
    assert isinstance(sample, ImportSample)
    assert sample.format == "json"
    assert sample.content.startswith("{\"catalog\"")
