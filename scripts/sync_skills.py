#!/usr/bin/env python3
"""Synchronize canonical Agentic Brain skill bundles to supported host folders."""

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
        description="Copy canonical skill files and supporting resources to a host discovery folder."
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
            skill_files = sorted(path for path in skill.rglob("*") if path.is_file())
            for source in skill_files:
                relative_file = source.relative_to(skill)
                target = root / relative_destination / skill.name / relative_file
                label = f"{host}:{skill.name}/{relative_file.as_posix()}"

                if not is_within_repo(source, root) or not is_within_repo(target, root):
                    print(f"refusing path outside repository: {label}")
                    return 2

                if target.exists() and target.is_dir():
                    print(f"conflict {label} (destination is a directory)")
                    issues.append(label)
                elif not target.exists():
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
