# Protocolo 05 — HIGIENE (mantener o vault saudável)

O estado esperado é medido, não sentido: `scripts/sm_doctor.py` é a fonte da
verdade. Check-list manual (espelha o doctor):

## Erros (bloqueiam)
- [ ] Todo `.md` fora de `_system/` tem frontmatter com `id, type, status, created, updated, agent`.
- [ ] `type` e `status` dentro dos enums (protocolo 01).
- [ ] Sem slugs duplicados (mesmo stem = conflito).
- [ ] Nenhum `[[wikilink]]` aponta para arquivo inexistente.

## Avisos (corrigir no próximo heartbeat)
- [ ] Manifest desatualizado → `build_manifest.py`.
- [ ] Nota acima de 150% do orçamento → dividir.
- [ ] Sessões 3+ sobre mesmo tema sem `distilled: true` → aplicar protocolo 04.
- [ ] Orfanatos (sem link entrante 14+ dias) → promover ou arquivar.

## Manuais
- Arquivar movendo arquivo PARA `07-archive/` e editando MOC/index que o citavam.
- Renomear slug: mover arquivo, atualizar TODOS os wikilinks (doctor pega os esquecidos).
- Nunca apagar nota com `status: active`; o ciclo é active → done → archived
  (ou superseded).
