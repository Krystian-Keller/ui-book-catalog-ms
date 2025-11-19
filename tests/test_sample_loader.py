from __future__ import annotations

from src.sample_loader import list_sample_files, load_sample_content, SAMPLE_DIR


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
