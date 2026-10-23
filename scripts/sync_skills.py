#!/usr/bin/env python3
"""Synchronize canonical Agentic Brain skills to supported host folders."""

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


HOSTS = {
    "codex": ".agents/skills",
    "claude": ".claude/skills",
    "abacus": ".abacusai/skills",
}


def is_within_repo(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy canonical skills to an agent host's discovery folder."
    )
    parser.add_argument("--host", choices=(*HOSTS.keys(), "all"), required=True)
    parser.add_argument("--write", action="store_true", help="Copy missing skill files.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace differing copies when used with --write.",
    )
    args = parser.parse_args()
    if args.force and not args.write:
        parser.error("--force requires --write")

    root = Path(__file__).resolve().parent.parent
    source_root = root / "skills"
    skills = sorted(
        path
        for path in source_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )
    selected_hosts = HOSTS if args.host == "all" else {args.host: HOSTS[args.host]}
    issues = []

    for host, relative_destination in selected_hosts.items():
        for skill in skills:
            source = skill / "SKILL.md"
            target = root / relative_destination / skill.name / "SKILL.md"
            label = f"{host}:{skill.name}"

            if not is_within_repo(source, root) or not is_within_repo(target, root):
                print(f"refusing path outside repository: {label}")
                return 2

            if not target.exists():
                if args.write:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
                    print(f"copied {label}")
                else:
                    print(f"missing {label}")
                    issues.append(label)
            elif filecmp.cmp(source, target, shallow=False):
                print(f"current {label}")
            elif args.write and args.force:
                shutil.copy2(source, target)
                print(f"updated {label}")
            else:
                print(f"conflict {label} (review or use --write --force)")
                issues.append(label)

    if issues:
        return 1
    print("Selected host copies match canonical skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
