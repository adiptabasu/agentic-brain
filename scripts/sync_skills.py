#!/usr/bin/env python3
"""Check or copy canonical Agentic Brain skills to a selected host adapter."""

import argparse
import filecmp
import json
import re
import shutil
import sys
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Tuple


def within_root(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def has_symlink_component(path: Path, root: Path) -> bool:
    current = path
    while current != root:
        if current.is_symlink():
            return True
        current = current.parent
    return root.is_symlink()


def load_adapters(adapter_root: Path) -> Dict[str, dict]:
    adapters = {}
    for path in sorted(adapter_root.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        host = data.get("host")
        discovery = data.get("discovery_directory")
        if not isinstance(host, str) or not host or host != path.stem:
            raise ValueError(f"{path}: host must match the adapter filename")
        if not isinstance(discovery, str) or not discovery:
            raise ValueError(f"{path}: discovery_directory is required")
        relative = PurePosixPath(discovery)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"{path}: discovery_directory must stay inside the repository")
        adapters[host] = data
    return adapters


def validate_skill(skill_dir: Path, root: Path) -> Tuple[List[Path], Optional[str]]:
    if skill_dir.is_symlink() or not within_root(skill_dir, root):
        return [], f"refusing skill directory outside repository: {skill_dir}"

    manifest = skill_dir / "SKILL.md"
    if not manifest.is_file() or manifest.is_symlink():
        return [], f"missing regular SKILL.md: {skill_dir.name}"
    if not within_root(manifest, root):
        return [], f"refusing manifest outside repository: {manifest}"

    try:
        content = manifest.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [], f"SKILL.md is not UTF-8: {skill_dir.name}"

    if not content.startswith("---\n"):
        return [], f"SKILL.md must start with YAML front matter: {skill_dir.name}"
    end = content.find("\n---", 4)
    if end < 0:
        return [], f"SKILL.md has unclosed YAML front matter: {skill_dir.name}"
    front_matter = content[4:end]
    name_match = re.search(r"^name:\s*(.+?)\s*$", front_matter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+?)\s*$", front_matter, re.MULTILINE)
    skill_name = name_match.group(1).strip(" \'\"") if name_match else ""
    description = description_match.group(1).strip(" \'\"") if description_match else ""
    if not skill_name or not description:
        return [], f"SKILL.md requires non-empty name and description: {skill_dir.name}"
    if skill_name != skill_dir.name:
        return [], f"skill name {skill_name!r} does not match directory {skill_dir.name!r}"

    files = []
    for path in sorted(skill_dir.rglob("*")):
        if path.is_symlink() or not within_root(path, root):
            return [], f"refusing symlink or path outside repository: {path}"
        if path.is_file():
            files.append(path)
    return files, None


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Check or synchronize canonical skills to a documented host folder."
    )
    parser.add_argument("--host", required=True, help="adapter ID, or 'all'")
    parser.add_argument("--write", action="store_true", help="copy missing skill files")
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace differing copies; use only after approval for the exact files",
    )
    args = parser.parse_args()
    if args.force and not args.write:
        parser.error("--force requires --write")

    try:
        adapters = load_adapters(root / "adapters")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"adapter configuration error: {error}", file=sys.stderr)
        return 2

    if args.host == "all":
        selected = adapters
    elif args.host in adapters:
        selected = {args.host: adapters[args.host]}
    else:
        print(f"unsupported host {args.host!r}; available adapters: {', '.join(adapters) or '(none)'}")
        return 2

    root_skills = root / "skills"
    skill_dirs = sorted(path for path in root_skills.iterdir() if path.is_dir()) if root_skills.is_dir() else []
    skills = []
    issues = []
    for skill_dir in skill_dirs:
        files, error = validate_skill(skill_dir, root)
        if error:
            print(f"invalid {skill_dir.name}: {error}")
            issues.append(error)
        else:
            skills.append((skill_dir, files))

    if not skills:
        print("No valid canonical skills found under skills/.")
        return 1 if issues else 0

    for host, adapter in selected.items():
        destination_root = root / adapter["discovery_directory"]
        if not within_root(destination_root, root) or has_symlink_component(destination_root, root):
            print(f"refusing unsafe discovery directory for {host}: {destination_root}")
            return 2
        print(f"host {host}: {adapter['discovery_directory']}")

        if destination_root.exists() and not destination_root.is_dir():
            print(f"conflict {destination_root} (discovery path is not a directory)")
            issues.append(str(destination_root))
            continue
        if not destination_root.exists():
            if args.write:
                destination_root.mkdir(parents=True, exist_ok=True)
                print(f"created {adapter['discovery_directory']}")
            else:
                print(f"missing discovery folder: {adapter['discovery_directory']}")

        expected_skill_dirs = {skill_dir.name for skill_dir, _ in skills}
        if destination_root.is_dir():
            for entry in sorted(destination_root.iterdir()):
                if entry.name not in expected_skill_dirs:
                    print(f"extra target entry preserved: {host}:{entry.name}")
                    issues.append(f"{host}:{entry.name}")

        for skill_dir, source_files in skills:
            target_skill = destination_root / skill_dir.name
            if not within_root(target_skill, root) or has_symlink_component(target_skill, root):
                print(f"refusing unsafe target directory: {target_skill}")
                return 2
            if target_skill.exists() and not target_skill.is_dir():
                print(f"conflict {host}:{skill_dir.name} (destination is not a directory)")
                issues.append(f"{host}:{skill_dir.name}")
                continue

            source_relatives = {file.relative_to(skill_dir) for file in source_files}
            for source in source_files:
                relative = source.relative_to(skill_dir)
                target = target_skill / relative
                label = f"{host}:{skill_dir.name}/{relative.as_posix()}"
                if not within_root(target, root) or has_symlink_component(target, root):
                    print(f"refusing unsafe target path: {label}")
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
                    print(f"conflict {label} (review or use --write --force with approval)")
                    issues.append(label)

            if target_skill.is_dir():
                for target in sorted(path for path in target_skill.rglob("*") if path.is_file()):
                    if not within_root(target, root):
                        print(f"refusing target file outside repository: {target}")
                        return 2
                    relative = target.relative_to(target_skill)
                    if relative not in source_relatives:
                        label = f"{host}:{skill_dir.name}/{relative.as_posix()}"
                        print(f"extra target file preserved: {label}")
                        issues.append(label)

    if issues:
        print(f"check incomplete: {len(issues)} missing, conflicting, or extra item(s)")
        return 1
    print("Selected host copies match canonical skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
