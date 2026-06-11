#!/usr/bin/env python3
"""Lightweight validation for local agent skill directories."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str, skill_path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{skill_path}: missing YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{skill_path}: unterminated YAML frontmatter")

    frontmatter = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in frontmatter:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            fail(f"{skill_path}: unsupported frontmatter line: {line}")
        key, value = match.groups()
        data[key] = value.strip().strip('"')
    return data


def validate_evals(path: Path, expected_name: str) -> None:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if data.get("skill_name") != expected_name:
        fail(f"{path}: skill_name does not match {expected_name}")

    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        fail(f"{path}: evals must be a non-empty list")

    for item in evals:
        if not isinstance(item, dict):
            fail(f"{path}: eval item must be an object")
        for key in ("id", "prompt", "expected_output", "files"):
            if key not in item:
                fail(f"{path}: eval item missing {key}")
        if not isinstance(item["files"], list):
            fail(f"{path}: eval files must be a list")


def validate_skill(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        fail(f"{skill_dir}: missing SKILL.md")

    text = skill_file.read_text(encoding="utf-8")
    metadata = parse_frontmatter(text, skill_file)

    for key in ("name", "description"):
        if not metadata.get(key):
            fail(f"{skill_file}: missing frontmatter {key}")

    evals_file = skill_dir / "evals" / "evals.json"
    if evals_file.exists():
        validate_evals(evals_file, metadata["name"])

    print(f"OK: {skill_dir.relative_to(ROOT)}")


def main() -> int:
    if not SKILLS_DIR.exists():
        fail("missing skills directory")

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skill directories found")

    for skill_dir in skill_dirs:
        validate_skill(skill_dir)

    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
