#!/usr/bin/env python3
"""Exporta memoria compartilhavel do vault (notas com shared: true)."""
import argparse, json, shutil, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_manifest import parse_front  # noqa: E402

VIS_RANK = {"local": 0, "team": 1, "public": 2}


def main():
    ap = argparse.ArgumentParser(description="Gera bundle portavel de memoria.")
    ap.add_argument("vault")
    ap.add_argument("--out", default=None, help="zip de saida (padrao: _system/export/sm-<data>.zip)")
    ap.add_argument("--visibility", default="team", choices=sorted(VIS_RANK))
    ap.add_argument("--types", default="concept,playbook,decision,synapse,handoff")
    a = ap.parse_args()
    vault = Path(a.vault).expanduser().resolve()
    types = [t.strip() for t in a.types.split(",") if t.strip()]
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    sel = []
    for p in sorted(vault.rglob("*.md")):
        if "_system" in p.parts:
            continue
        meta = parse_front(p.read_text(encoding="utf-8", errors="replace"))
        if meta.get("shared") != "true":
            continue
        if VIS_RANK.get(meta.get("visibility", "local"), 0) > VIS_RANK[a.visibility]:
            continue
        if meta.get("type") not in types:
            continue
        sel.append((p, p.relative_to(vault).as_posix()))
    stage = vault / "_system" / "export" / f"sm-{now}"
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True, exist_ok=True)
    for p, rel in sel:
        tgt = stage / rel
        tgt.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(p, tgt)
    info = {"origin_vault": str(vault), "generated": now,
            "visibility_cap": a.visibility, "count": len(sel),
            "paths": [rel for _, rel in sel]}
    (stage / "EXPORT-INFO.json").write_text(
        json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    man = vault / "_system" / "MANIFEST.json"
    if man.exists():
        shutil.copy(man, stage / "MANIFEST.json")
    out = Path(a.out) if a.out else vault / "_system" / "export" / f"sm-{now}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(stage.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(stage).as_posix())
    print(f"[secondmind] export: {len(sel)} notas -> {out}")
    if not sel:
        print("[secondmind] nada elegivel: marque shared: true (+ visibility) no frontmatter")


if __name__ == "__main__":
    main()
