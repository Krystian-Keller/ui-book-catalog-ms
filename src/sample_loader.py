"""Utilities for reading bundled sample catalog files."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

SAMPLE_DIR = Path(__file__).resolve().parent.parent / "books_json_sample"


@dataclass
class ImportSample:
    """Represents a parsed import sample with format and content fields."""

    format: str
    content: str


def list_sample_files() -> List[str]:
    """Return a list of available sample file names."""
    if not SAMPLE_DIR.exists():
        return []
    return sorted(file.name for file in SAMPLE_DIR.glob("*.json"))


def load_sample_content(filename: str) -> Optional[str]:
    """Return the raw text content of the chosen sample file."""
    file_path = SAMPLE_DIR / filename
    if not file_path.exists():
        return None
    return file_path.read_text(encoding="utf-8")


def load_import_sample(filename: str) -> Optional[ImportSample]:
    """Return the parsed import sample containing format and content strings."""
    raw_text = load_sample_content(filename)
    if raw_text is None:
        return None
    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    format_value = payload.get("format")
    content_value = payload.get("content")
    if isinstance(format_value, str) and isinstance(content_value, str):
        return ImportSample(format=format_value, content=content_value)
    return None
