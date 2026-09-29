#!/usr/bin/env python3
"""Remind reviewers when changed Chinese Wiki sources lack English counterparts."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path, PurePosixPath


ZH_PREFIX = PurePosixPath("sites/zh-CN")
EN_PREFIX = PurePosixPath("sites/en")
SOURCE_EXTENSIONS = {".md", ".mdx", ".js", ".jsx", ".ts", ".tsx", ".json", ".yaml", ".yml"}
SKIP_DIRECTORIES = {".docusaurus", "build", "node_modules"}


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(detail or f"git {' '.join(args)} failed")
    return result.stdout


def resolve_repo() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError("run this script inside a Git repository")
    return Path(result.stdout.strip())


def default_base(repo: Path) -> str:
    for candidate in ("upstream/docusaurus-version", "origin/docusaurus-version"):
        if subprocess.run(
            ["git", "show-ref", "--verify", "--quiet", f"refs/remotes/{candidate}"],
            cwd=repo,
            check=False,
        ).returncode == 0:
            return candidate
    if subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD^"],
        cwd=repo,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0:
        return "HEAD^"
    return "HEAD"


def changed_paths(repo: Path, base_ref: str) -> set[str]:
    commands = (
        ("diff", "--name-only", f"{base_ref}...HEAD"),
        ("diff", "--cached", "--name-only"),
        ("diff", "--name-only"),
        ("ls-files", "--others", "--exclude-standard"),
    )
    paths: set[str] = set()
    for command in commands:
        paths.update(line for line in git(repo, *command).splitlines() if line)
    return paths


def english_candidates(chinese_path: str) -> list[str]:
    path = PurePosixPath(chinese_path)
    try:
        relative = path.relative_to(ZH_PREFIX)
    except ValueError:
        return []

    names = [relative.name]
    if relative.name.startswith("cn_"):
        names.insert(0, relative.name[3:])

    candidates: list[str] = []
    for name in names:
        candidate = EN_PREFIX / relative.parent / name
        rendered = candidate.as_posix()
        if rendered not in candidates:
            candidates.append(rendered)
    return candidates


def existing_or_tracked(repo: Path, path: str) -> bool:
    if (repo / path).is_file():
        return True
    return subprocess.run(
        ["git", "cat-file", "-e", f"HEAD:{path}"],
        cwd=repo,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report Chinese Wiki source changes whose English counterpart is absent from the proposed diff."
    )
    parser.add_argument("base_ref", nargs="?", help="Git base ref; defaults to the Wiki upstream branch")
    args = parser.parse_args()

    try:
        repo = resolve_repo()
        base_ref = args.base_ref or default_base(repo)
        git(repo, "rev-parse", "--verify", f"{base_ref}^{{commit}}")
        changed = changed_paths(repo, base_ref)
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    reminders: list[tuple[str, str | None]] = []
    for changed_path in sorted(changed):
        path = PurePosixPath(changed_path)
        if path.suffix.lower() not in SOURCE_EXTENSIONS:
            continue
        if any(part in SKIP_DIRECTORIES for part in path.parts):
            continue
        if not path.is_relative_to(ZH_PREFIX):
            continue

        candidates = english_candidates(changed_path)
        counterpart = next((item for item in candidates if existing_or_tracked(repo, item)), None)
        if counterpart and counterpart in changed:
            continue
        reminders.append((changed_path, counterpart))

    print("Locale synchronization review")
    if not reminders:
        print("No Chinese-only source changes with a missing English diff were detected.")
        return 0

    for chinese_path, counterpart in reminders:
        if counterpart:
            print(f"REVIEW: {chinese_path}")
            print(f"        English counterpart not changed: {counterpart}")
        else:
            print(f"REVIEW: {chinese_path}")
            print("        English counterpart could not be resolved; verify manually.")

    print(
        "Classify each reminder as sync required, Chinese-only justified, or counterpart unresolved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
