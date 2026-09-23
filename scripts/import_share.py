#!/usr/bin/env python3
"""Importa bundle SecondMind (zip ou pasta) em um vault. Idempotente por id/updated."""
import shutil, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_manifest import parse_front  # noqa: E402


def main():
    if len(sys.argv) < 3:
        sys.exit("uso: import_share.py <bundle.zip|pasta> <vault>")
    bundle = Path(sys.argv[1]).expanduser()
    vault = Path(sys.argv[2]).expanduser().resolve()
    src = None
    if bundle.suffix == ".zip":
        src = vault / "_system" / "import-stage"
        if src.exists():
            shutil.rmtree(src)
        src.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(bundle) as z:
            z.extractall(src)
    else:
        src = bundle.resolve()
    log = [f"# Import log — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
           f"bundle: {bundle}", ""]
    kept = replaced = skipped = 0
    for p in sorted(src.rglob("*.md")):
        rel = p.relative_to(src).as_posix()
        tgt = vault / rel
        incoming = parse_front(p.read_text(encoding="utf-8", errors="replace"))
        if not tgt.exists():
            tgt.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(p, tgt)
            kept += 1
            log.append(f"+ criado       {rel}")
        else:
            local = parse_front(tgt.read_text(encoding="utf-8", errors="replace"))
            if incoming.get("updated", "") > local.get("updated", ""):
                arch = vault / "07-archive" / rel.replace("/", "--")
                arch.parent.mkdir(parents=True, exist_ok=True)
                if arch.exists():
                    arch.unlink()
                shutil.move(str(tgt), str(arch))
                shutil.copy(p, tgt)
                replaced += 1
                log.append(f"~ substituido  {rel} (antiga -> 07-archive/{arch.name})")
            else:
                skipped += 1
                log.append(f"- mantido local {rel} (local mais novo ou igual)")
    if src != bundle.resolve():
        shutil.rmtree(src, ignore_errors=True)
    (vault / "_system" / "IMPORT-LOG.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"[secondmind] import: {kept} criados, {replaced} substituidos, {skipped} mantidos locais")
    print("[secondmind] proximo: build_manifest.py + sm_doctor.py")


if __name__ == "__main__":
    main()
