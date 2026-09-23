# Eval: share roundtrip (memória entre agentes)

Objetivo: provar que a memória sai de um vault e chega íntegra, idempotente e
com proveniência em outro.

## Passos
1. `vault_init.py /tmp/vA && vault_init.py /tmp/vB`
2. Em vA: 2 conceitos (ambos `shared: true`, `visibility: team`, com `origin`),
   1 sinapse entre eles (`shared: true`) e 1 conceito local
   (`shared: false`) como isca.
3. `export_share.py /tmp/vA --out /tmp/bundle.zip --visibility team`
4. `import_share.py /tmp/bundle.zip /tmp/vB` → esperado: apenas as 3 notas
   compartilhadas criadas; a isca local NÃO aparece.
5. `build_manifest.py /tmp/vB` e `sm_doctor.py /tmp/vB` exit 0 (link p/ ponta não exportada vira WARN documentado p/ notas importadas);
   manifest mostra `origin` preservado.
6. Importar o MESMO bundle de novo → esperado: 0 criados, 0 substituídos.
## Reprova se
- nota sem `shared: true` vazar no bundle · `origin` perder no import ·
  segundo import duplicar ou conflitar · link quebrado sem acusação no doctor.
