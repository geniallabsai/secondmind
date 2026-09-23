#!/usr/bin/env python3
"""Checa integridade de um vault SecondMind. exit 0 = ok, exit 1 = erros."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_manifest import parse_front, WIKI  # noqa: E402

TYPES = {"inbox", "session", "project", "concept", "decision", "playbook"}
STATUSES = {"active", "done", "archived", "superseded"}
BUDGET = {"inbox": 150, "session": 900, "project": 1000, "concept": 600,
          "decision": 500, "playbook": 1200}
REQ = ["id", "type", "status", "created", "updated", "agent"]


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: sm_doctor.py <vault>")
    vault = Path(sys.argv[1]).expanduser().resolve()
    errs, warns = [], []
    files = [p for p in vault.rglob("*.md") if "_system" not in p.parts]
    stems = {}
    existing = {q.stem for q in vault.rglob("*.md")}

    for p in files:
        rel = p.relative_to(vault).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        meta = parse_front(text)
        if not meta:
            errs.append(f"{rel}: sem frontmatter")
            continue
        for k in REQ:
            if not meta.get(k):
                errs.append(f"{rel}: frontmatter sem campo obrigatorio '{k}'")
        if meta.get("type") and meta["type"] not in TYPES:
            errs.append(f"{rel}: type invalida '{meta['type']}' (permitidas: {sorted(TYPES)})")
        if meta.get("status") and meta["status"] not in STATUSES:
            errs.append(f"{rel}: status invalido '{meta['status']}'")
        key = p.stem.lower()
        if key in stems:
            errs.append(f"{rel}: slug duplicado com {stems[key]}")
        stems[key] = rel
        t = meta.get("type")
        if t in BUDGET:
            w = len(text.split())
            if w > BUDGET[t] * 1.5:
                warns.append(f"{rel}: {w} palavras (orcamento {BUDGET[t]} * 1.5)")
        for link in set(WIKI.findall(text)):
            if link.strip() not in existing:
                errs.append(f"{rel}: [[{link}]] nao existe no vault")

    man = vault / "_system" / "MANIFEST.json"
    if man.exists():
        newest = max((p.stat().st_mtime for p in files), default=0)
        if man.stat().st_mtime + 1 < newest:
            warns.append("_system/MANIFEST.json desatualizado (rode build_manifest.py)")

    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERRO ", e)
    print(f"[secondmind] doctor: {len(errs)} erro(s), {len(warns)} aviso(s) em {len(files)} notas")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
