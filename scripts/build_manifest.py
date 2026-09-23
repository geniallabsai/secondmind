#!/usr/bin/env python3
"""Gera _system/MANIFEST.json. Determinístico (sort por path), com grafo
de entrada (inbound) e hubs — os nós em que mais memória gravita."""
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def parse_front(text):
    meta = {}
    if not text.startswith("---"):
        return meta
    end = text.find("\n---", 3)
    if end == -1:
        return meta
    cur = None
    for line in text[3:end].splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^([\w][\w-]*):\s*(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            cur = k
            if v == "":
                meta[k] = ""
            elif v.startswith("[") and v.endswith("]"):
                meta[k] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
            else:
                meta[k] = v.strip("'\"")
        elif s.startswith("- ") and cur is not None:
            if not isinstance(meta.get(cur), list):
                meta[cur] = []
            meta[cur].append(s[2:].strip().strip("'\""))
    return meta


def build_resolve(notes):
    """Resolução de [[link]]: nome exato do arquivo primeiro; senão o slug de
    cauda de notas datadas (após o último '--'). Cauda ambígua -> nota com
    'updated' mais recente. Retorna [índice] ou []."""
    exact, tails = {}, {}
    for i, n in enumerate(notes):
        stem = n["path"].split("/")[-1][:-3].lower()
        exact.setdefault(stem, i)
        if "--" in stem:
            tails.setdefault(stem.rsplit("--", 1)[1], []).append(i)

    def resolve(link):
        k = link.strip().lower()
        if k in exact:
            return [exact[k]]
        cands = tails.get(k, [])
        if not cands:
            return []
        if len(cands) == 1:
            return cands
        best = max(cands, key=lambda i: (notes[i].get("updated", ""), notes[i]["path"]))
        return [best]

    return resolve


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: build_manifest.py <vault>")
    vault = Path(sys.argv[1]).expanduser().resolve()
    notes = []
    for p in sorted(vault.rglob("*.md")):
        if "_system" in p.parts:
            continue
        rel = p.relative_to(vault).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        meta = parse_front(text)
        title = ""
        for ln in text.splitlines():
            if ln.startswith("# "):
                title = ln[2:].strip()
                break
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [tags] if tags else []
        notes.append({
            "path": rel, "title": title, "type": meta.get("type", ""),
            "status": meta.get("status", ""), "agent": meta.get("agent", ""),
            "project": meta.get("project", ""), "tags": tags,
            "created": meta.get("created", ""), "updated": meta.get("updated", ""),
            "shared": meta.get("shared", "false"),
            "visibility": meta.get("visibility", "local"),
            "origin": meta.get("origin", ""),
            "links": sorted({t.strip() for t in WIKI.findall(text)}),
            "words": len(text.split()),
        })

    resolve = build_resolve(notes)
    inbound = [0] * len(notes)
    for n in notes:
        for link in set(n["links"]):
            for j in resolve(link):
                inbound[j] += 1
    for n, c in zip(notes, inbound):
        n["inbound"] = c
    hubs_idx = sorted(range(len(notes)), key=lambda i: (-inbound[i], notes[i]["path"]))[:5]
    hubs = [{"name": notes[i]["path"].split("/")[-1][:-3], "path": notes[i]["path"],
             "inbound": inbound[i]} for i in hubs_idx if inbound[i] > 0]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = {"generated": now, "count": len(notes), "hubs": hubs, "notes": notes}
    (vault / "_system" / "MANIFEST.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[secondmind] manifest: {len(notes)} notas, {len(hubs)} hubs -> _system/MANIFEST.json")


if __name__ == "__main__":
    main()
