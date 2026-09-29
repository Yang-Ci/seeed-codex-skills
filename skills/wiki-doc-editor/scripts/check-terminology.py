#!/usr/bin/env python3
"""Report non-canonical terminology in human-readable Wiki source files."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


TEXT_EXTENSIONS = {".md", ".mdx", ".js", ".jsx", ".ts", ".tsx", ".json", ".yaml", ".yml"}
SKIP_DIRECTORIES = {".git", ".docusaurus", "build", "node_modules"}
MARKDOWN_EXTENSIONS = {".md", ".mdx"}
URL_RE = re.compile(r"https?://[^\s)>\]}'\"]+")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
FRONT_MATTER_KEY_RE = re.compile(r"^\s*([A-Za-z0-9_-]+)\s*:")
PROTECTED_FRONT_MATTER_KEYS = {
    "id",
    "image",
    "pagination_next",
    "pagination_prev",
    "slug",
    "url",
}


@dataclass(frozen=True)
class Rule:
    canonical: str
    pattern: re.Pattern[str]


def term_rule(canonical: str, expression: str) -> Rule:
    return Rule(canonical, re.compile(expression, re.IGNORECASE))


RULES = (
    term_rule("MuJoCo", r"(?<![\w])mujoco(?![\w])"),
    term_rule("Isaac Sim", r"(?<![\w])isaac[\s_-]*sim(?![\w])"),
    term_rule("Isaac Lab", r"(?<![\w])isaac[\s_-]*lab(?![\w])"),
    term_rule("Isaac ROS", r"(?<![\w])isaac[\s_-]*ros(?![\w])"),
    term_rule("NVIDIA", r"(?<![\w])nvidia(?![\w])"),
    term_rule("ROS 2", r"(?<![\w])ros\s*2(?![\w])"),
    term_rule("GitHub", r"(?<![\w])github(?![\w])"),
    term_rule("JavaScript", r"(?<![\w])javascript(?![\w])"),
    term_rule("TypeScript", r"(?<![\w])typescript(?![\w])"),
    term_rule("PyTorch", r"(?<![\w])pytorch(?![\w])"),
    term_rule("TensorFlow", r"(?<![\w])tensorflow(?![\w])"),
    term_rule("OpenAI", r"(?<![\w])openai(?![\w])"),
    term_rule("LeRobot", r"(?<![\w])lerobot(?![\w])"),
    term_rule("Hugging Face", r"(?<![\w])hugging[\s_-]*face(?![\w])"),
    term_rule("macOS", r"(?<![\w])mac[\s_-]*os(?![\w])"),
    term_rule("Raspberry Pi", r"(?<![\w])raspberry[\s_-]*pi(?![\w])"),
    term_rule("JetPack SDK", r"(?<![\w])jetpack\s+sdk(?![\w])"),
    term_rule("Atom-S", r"(?<![\w])atom[\s_-]*s(?![\w])"),
    term_rule("StackForce", r"(?<![\w])stackforce(?![\w])"),
    term_rule("Seeed Studio", r"(?<![\w])seeed\s+studio(?![\w])"),
)


def mask_pattern(text: str, pattern: re.Pattern[str]) -> str:
    return pattern.sub(lambda match: " " * (match.end() - match.start()), text)


def source_files(paths: Iterable[str]) -> Iterable[tuple[str, str, str]]:
    """Yield display name, suffix, and content for each requested source."""
    seen: set[Path] = set()
    stdin_consumed = False

    for raw_path in paths:
        if raw_path == "-":
            if not stdin_consumed:
                stdin_consumed = True
                yield "<stdin>", ".md", sys.stdin.read()
            continue

        path = Path(raw_path)
        candidates = (path.rglob("*") if path.is_dir() else (path,))
        for candidate in candidates:
            if not candidate.is_file() or candidate.suffix.lower() not in TEXT_EXTENSIONS:
                continue
            if any(part in SKIP_DIRECTORIES for part in candidate.parts):
                continue
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            try:
                content = candidate.read_text(encoding="utf-8", errors="replace")
            except OSError as error:
                print(f"{candidate}: unable to read: {error}", file=sys.stderr)
                continue
            yield str(candidate), candidate.suffix.lower(), content


def scan_source(name: str, suffix: str, content: str) -> list[str]:
    findings: list[str] = []
    markdown = suffix in MARKDOWN_EXTENSIONS
    fence_marker: str | None = None
    front_matter = False

    for line_number, line in enumerate(content.splitlines(), start=1):
        if markdown:
            if line_number == 1 and line.strip() == "---":
                front_matter = True
                continue
            if front_matter and line.strip() == "---":
                front_matter = False
                continue
            if front_matter:
                key_match = FRONT_MATTER_KEY_RE.match(line)
                if key_match and key_match.group(1).lower() in PROTECTED_FRONT_MATTER_KEYS:
                    continue

            fence_match = FENCE_RE.match(line)
            if fence_match:
                marker = fence_match.group(1)[0]
                if fence_marker is None:
                    fence_marker = marker
                elif marker == fence_marker:
                    fence_marker = None
                continue
            if fence_marker is not None:
                continue

        masked = mask_pattern(mask_pattern(line, URL_RE), INLINE_CODE_RE)
        line_findings: list[tuple[int, str]] = []
        for rule in RULES:
            for match in rule.pattern.finditer(masked):
                found = line[match.start() : match.end()]
                if found == rule.canonical:
                    continue
                line_findings.append(
                    (
                        match.start(),
                        f"{name}:{line_number}:{match.start() + 1}: "
                        f"use '{rule.canonical}' instead of '{found}'",
                    )
                )
        findings.extend(message for _, message in sorted(line_findings))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report non-canonical product names, capitalization, and spacing."
    )
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="print findings but exit successfully",
    )
    parser.add_argument("paths", nargs="+", help="files or directories to scan; use - for stdin")
    args = parser.parse_args()

    findings: list[str] = []
    for name, suffix, content in source_files(args.paths):
        findings.extend(scan_source(name, suffix, content))

    for finding in findings:
        print(finding)

    if findings:
        sys.stdout.flush()
        print(f"Found {len(findings)} terminology issue(s).", file=sys.stderr)
        return 0 if args.warn_only else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
