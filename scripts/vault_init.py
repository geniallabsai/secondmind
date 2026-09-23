#!/usr/bin/env python3
"""Cria/normaliza a estrutura SecondMind num vault Obsidian. Idempotente."""
import argparse, json, shutil
from datetime import datetime, timezone
from pathlib import Path

DIRS = ["00-inbox", "01-sessions", "02-projects", "03-concepts", "04-decisions",
        "05-playbooks", "07-archive", "_system", "_system/TEMPLATES", "_system/PROTOCOL"]

INDEX_SEED = """---
type: system-index
updated: {now}
---
# VAULT INDEX
_Atualizado por cada agente ao fechar sessão (fase FECHAR) e por build_manifest.py._

## Projetos ativos
_(nenhum)_

## Sessões recentes
_(nenhuma)_

## Conceitos-chave
_(nenhum)_

## Playbooks
_(nenhum)_
"""

GITIGNORE = """.obsidian/workspace*
.trash/
.DS_Store
"""


def main():
    ap = argparse.ArgumentParser(description="Inicia um vault SecondMind (idempotente).")
    ap.add_argument("vault", help="caminho do vault (criado se não existir)")
    ap.add_argument("--force", action="store_true", help="sobrescreve arquivos de sistema")
    a = ap.parse_args()
    vault = Path(a.vault).expanduser().resolve()
    pkg = Path(__file__).resolve().parent.parent
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    made = []

    for d in DIRS:
        p = vault / d
        if not p.is_dir():
            p.mkdir(parents=True)
            made.append(d + "/")

    for src_dir, dst_dir in (("templates", "_system/TEMPLATES"),
                             ("protocols", "_system/PROTOCOL"),
                             ("conventions", "_system/PROTOCOL")):
        src, dst = pkg / src_dir, vault / dst_dir
        dst.mkdir(parents=True, exist_ok=True)
        for f in sorted(src.glob("*.md")):
            tgt = dst / f.name
            if not tgt.exists() or a.force:
                shutil.copy(f, tgt)
                made.append(dst.as_posix() + "/" + f.name)

    boot = vault / "_system" / "BOOT.md"
    if not boot.exists() or a.force:
        shutil.copy(pkg / "BOOT.md", boot)
        made.append("_system/BOOT.md")

    idx = vault / "_system" / "VAULT-INDEX.md"
    if not idx.exists() or a.force:
        idx.write_text(INDEX_SEED.format(now=now), encoding="utf-8")
        made.append("_system/VAULT-INDEX.md")

    man = vault / "_system" / "MANIFEST.json"
    if not man.exists() or a.force:
        man.write_text(json.dumps({"generated": now, "count": 0, "notes": []}, indent=2),
                       encoding="utf-8")

    gi = vault / ".gitignore"
    if not gi.exists():
        gi.write_text(GITIGNORE, encoding="utf-8")

    print(f"[secondmind] vault ok: {vault}")
    for m in made:
        print("  +", m)
    print("[secondmind] próximo: injete seu agente (pasta agents/) e rode sm_doctor.py")


if __name__ == "__main__":
    main()
