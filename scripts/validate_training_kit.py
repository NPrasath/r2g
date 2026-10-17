#!/usr/bin/env python3
"""Validate portable training assets using Python's standard library only.

This is content validation, not a C# build, business test, or security scan.
"""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)


def metadata(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    check(match is not None, f"{path.relative_to(ROOT)}: missing frontmatter")
    if match is None:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([a-z][a-z0-9-]*):\s*(.+)$", line)
        check(item is not None, f"{path.relative_to(ROOT)}: unsupported/empty metadata: {line}")
        if item:
            check(item[1] not in fields, f"{path.relative_to(ROOT)}: duplicate metadata key {item[1]}")
            fields[item[1]] = item[2].strip()
    for key in ("name", "description"):
        check(bool(fields.get(key)), f"{path.relative_to(ROOT)}: missing {key}")
    return fields


def main():
    markdown = list(ROOT.rglob("*.md"))
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0])
            resolved = (path.parent / relative).resolve()
            check(resolved.is_relative_to(ROOT), f"{path.relative_to(ROOT)}: link leaves repository: {target}")
            check(resolved.exists(), f"{path.relative_to(ROOT)}: broken local link: {target}")

    agents = list((ROOT / ".github/agents").glob("*.agent.md"))
    check(len(agents) >= 4, "Expected the four role-agent profiles")
    for path in agents:
        fields = metadata(path)
        check(fields.get("tools", "").startswith("["), f"{path.name}: explicit tools list required")

    skills = list((ROOT / ".github/skills").glob("*/SKILL.md"))
    check(len(skills) >= 5, "Expected the five initial skills")
    for path in skills:
        fields = metadata(path)
        check(fields.get("name") == path.parent.name, f"{path.parent.name}: skill name must match directory")
        check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", ""))), f"{path.parent.name}: invalid skill name")

    forms = [p for p in (ROOT / ".github/ISSUE_TEMPLATE").glob("*.yml") if p.name != "config.yml"]
    check(len(forms) >= 3, "Expected requirement, implementation, and defect forms")
    for path in forms:
        text = path.read_text(encoding="utf-8")
        for key in ("name", "description", "body"):
            check(re.search(rf"^{key}:", text, re.M) is not None, f"{path.name}: missing {key}")
        ids = re.findall(r"^    id: (.+)$", text, re.M)
        check(len(ids) == len(set(ids)), f"{path.name}: duplicate field IDs")

    for path in list(ROOT.rglob("*.csproj")) + [ROOT / "Directory.Build.props"]:
        tree = ET.parse(path)
        for ref in tree.findall(".//ProjectReference"):
            check((path.parent / ref.attrib["Include"]).exists(), f"{path.name}: missing project reference")

    fixture = json.loads((ROOT / "training/data/rqc-batch.json").read_text(encoding="utf-8"))
    batteries = fixture["batteryIds"]
    check(len(batteries) == 96 and len(set(batteries)) == 96, "Synthetic batch must contain 96 unique IDs")
    check(all(re.fullmatch(r"TRAIN-BAT-\d{3}", item) for item in batteries), "Fixture must use synthetic training IDs")
    check(fixture["batchId"].startswith("TRAIN-"), "Fixture batch ID must be synthetic")

    backlog = json.loads((ROOT / "training/backlog.json").read_text(encoding="utf-8"))
    keys = {item["id"] for item in backlog["issues"]}
    check(len(keys) == len(backlog["issues"]), "Backlog keys must be unique")
    for item in backlog["issues"]:
        check((ROOT / item["labPath"]).is_file(), f"{item['id']}: missing lab")
        for dependency in item["dependsOn"]:
            check(dependency in keys, f"{item['id']}: unknown dependency {dependency}")
        check(bool(item["body"].strip()), f"{item['id']}: empty proposed issue body")

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Training content passed: {len(markdown)} Markdown files, {len(agents)} profiles, {len(skills)} skills, {len(forms)} forms, {len(backlog['issues'])} backlog entries, 96 synthetic IDs.")
    print("Not checked: C# compilation, runtime tests, RQC behavior, SQL, UI, security, or hardware.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
        print(f"ERROR: training asset could not be validated: {exc}", file=sys.stderr)
        sys.exit(1)
