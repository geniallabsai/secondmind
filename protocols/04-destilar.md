# Protocolo 04 — DESTILAR (de sessão crua a memória longa)

Sessões são registro; conceitos e playbooks são memória. Sem destilação o
vault vira depósito de minutas.

## A regra das 3
Se 3 ou mais sessões tocam o MESMO tema (mesmo projeto + mesma área de
decisão), a próxima sessão que tocar o tema DEVE:
1. Criar ou atualizar uma nota de síntese em `03-concepts/<slug>.md` (ideia)
   ou `05-playbooks/<slug>.md` (procedimento).
2. A síntese é AUTOSSUFICIENTE: quem lê só ela aprende tudo que as 3+ sessões
   sabiam — absorver, não resumir ("na sessão X vimos Y" só aparece em
   Evidência).
3. Marcar `distilled: true` nas sessões-fonte e listar seus paths em
   `supersedes` da síntese? Não: a síntese lista as sessões em Evidência; as
   sessões apenas ganham `distilled: true`.

## Heartbeat semanal (disparado por humano, opcional)
1. Processar `00-inbox/`: cada captura vira nota de tipo adequado ou some
   (lixo se vai para o arquivo direto).
2. Notas com `status: done` há 30+ dias → `status: archived` + mover para
   `07-archive/` mantendo o caminho relativo no nome (ex.:
   `07-archive/03-concepts-x.md`).
3. Notas com >150% do orçamento → dividir (protocolo 01).
4. Notar orfanatos: notas sem link entrante há 14+ dias (doctor avisa).
5. Rodar `build_manifest.py` + `sm_doctor.py`.

## Conflito de notas (supersede)
Quando nova nota contradiz antiga:
- Nova nota: `supersedes: [id-da-antiga]` + link no corpo.
- Antiga: `status: superseded` + `superseded_by: id-da-nova`. A antiga NÃO se
  move: é evidência histórica.
- Nunca editar a decisão original de um ADR; cria ADR novo que a supõe.
