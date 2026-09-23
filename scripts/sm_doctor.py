#!/usr/bin/env python3
"""Checa integridade de um vault SecondMind. exit 0 = ok, exit 1 = erros."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_manifest import parse_front, WIKI, build_resolve  # noqa: E402

TYPES = {"inbox", "session", "project", "concept", "decision", "playbook",
         "synapse", "handoff"}
STATUSES = {"active", "done", "archived", "superseded"}
BUDGET = {"inbox": 150, "session": 900, "project": 1000, "concept": 600,
          "decision": 500, "playbook": 1200, "synapse": 120, "handoff": 700}
REQ = ["id", "type", "status", "created", "updated", "agent"]


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: sm_doctor.py <vault>")
    vault = Path(sys.argv[1]).expanduser().resolve()
    errs, warns = [], []
    files = [p for p in vault.rglob("*.md") if "_system" not in p.parts]

    mini, docs = [], {}
    for p in files:
        rel = p.relative_to(vault).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        meta = parse_front(text)
        mini.append({"path": rel, "updated": meta.get("updated", "")})
        docs[rel] = (text, meta)
    resolve = build_resolve(mini)

    stems_seen = {}
    for p in files:
        rel = p.relative_to(vault).as_posix()
        text, meta = docs[rel]
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
        if key in stems_seen:
            errs.append(f"{rel}: slug duplicado com {stems_seen[key]}")
        stems_seen[key] = rel
        t = meta.get("type")
        if t in BUDGET:
            w = len(text.split())
            if w > BUDGET[t] * 1.5:
                warns.append(f"{rel}: {w} palavras (orcamento {BUDGET[t]} x 1.5)")
        if t == "synapse" and "## Por que" not in text:
            errs.append(f"{rel}: synapse sem secao '## Por que'")
        if meta.get("shared") == "true" and not meta.get("visibility"):
            warns.append(f"{rel}: shared:true sem visibility")
        for link in set(WIKI.findall(text)):
            if not resolve(link):
                # nota importada (origin preenchido): ponta nao exportada é esperado
                # (protocolo 07) -> aviso; nota local com link quebrado -> erro do autor.
                bucket = warns if meta.get("origin") else errs
                suffix = "" if meta.get("origin") else " (ponta nao exportada? ver protocolo 07)" if not meta.get("origin") else ""
                msg = f"{rel}: [[{link}]] nao existe no vault"
                if meta.get("origin"):
                    msg += " [ponta nao exportada - protocolo 07]"
                bucket.append(msg)

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
