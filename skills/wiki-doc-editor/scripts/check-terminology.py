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
INLINE_CODE_RE = re.compile(r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)")
MARKDOWN_DESTINATION_RE = re.compile(
    r"(?<=\]\()[ \t]*(?:<[^>\n]+>|(?:\\.|[^()\s\\]|\([^()\s]*\))+)"
    r"|^\s*\[[^\]]+\]:[ \t]*(?:<[^>\n]+>|\S+)"
)
PATH_ATTRIBUTE_RE = re.compile(
    r"""\b(?:href|src|to|id|srcSet|poster)\s*=\s*(?:\{\s*)?(["'])(.*?)\1""",
)
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
    # Latin identifiers need word boundaries even when prose omits spaces around them.
    boundary = r"[a-z0-9_]"
    pattern = re.compile(rf"(?<!{boundary})(?:{expression})(?!{boundary})", re.IGNORECASE)
    return Rule(canonical, pattern)


RULES = (
    term_rule("MuJoCo", r"mujoco"),
    term_rule("Isaac Sim", r"isaac[\s_-]*sim"),
    term_rule("Isaac Lab", r"isaac[\s_-]*lab"),
    term_rule("Isaac ROS", r"isaac[\s_-]*ros"),
    term_rule("NVIDIA", r"nvidia"),
    term_rule("ROS 2", r"ros\s*2"),
    term_rule("GitHub", r"github"),
    term_rule("JavaScript", r"javascript"),
    term_rule("TypeScript", r"typescript"),
    term_rule("PyTorch", r"pytorch"),
    term_rule("TensorFlow", r"tensorflow"),
    term_rule("OpenAI", r"openai"),
    term_rule("LeRobot", r"lerobot"),
    term_rule("Hugging Face", r"hugging[\s_-]*face"),
    term_rule("macOS", r"mac[\s_-]*os"),
    term_rule("Raspberry Pi", r"raspberry[\s_-]*pi"),
    term_rule("JetPack SDK", r"jetpack\s+sdk"),
    term_rule("Atom-S", r"atom[\s_-]*s"),
    term_rule("StackForce", r"stackforce"),
    term_rule("Seeed Studio", r"seeed\s+studio"),
)


def mask_pattern(text: str, pattern: re.Pattern[str]) -> str:
    # Preserve columns and keep a multi-word term from matching across the mask.
    return pattern.sub(lambda match: "\0" * len(match[0]), text)


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
        path.stat()
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
            content = candidate.read_text(encoding="utf-8", errors="replace")
            yield str(candidate), candidate.suffix.lower(), content


def scan_source(name: str, suffix: str, content: str) -> list[str]:
    findings: list[str] = []
    markdown = suffix in MARKDOWN_EXTENSIONS
    fence: str | None = None
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
            if fence is not None:
                if (
                    fence_match
                    and fence_match[1].startswith(fence)
                    and not line[fence_match.end():].strip()
                ):
                    fence = None
                continue
            if fence_match:
                fence = fence_match[1]
                continue

        masked = mask_pattern(line, PATH_ATTRIBUTE_RE)
        if markdown:
            masked = mask_pattern(masked, INLINE_CODE_RE)
            masked = mask_pattern(masked, MARKDOWN_DESTINATION_RE)
        masked = mask_pattern(masked, URL_RE)
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
        help="print terminology findings without failing (input errors still fail)",
    )
    parser.add_argument("paths", nargs="+", help="files or directories to scan; use - for stdin")
    args = parser.parse_args()

    findings: list[str] = []
    try:
        for name, suffix, content in source_files(args.paths):
            findings.extend(scan_source(name, suffix, content))
    except OSError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    for finding in findings:
        print(finding)

    if findings:
        sys.stdout.flush()
        print(f"Found {len(findings)} terminology issue(s).", file=sys.stderr)
        return 0 if args.warn_only else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
