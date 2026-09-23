# Roadmap — do pacote ao programa

**v1 (este repositório):** skills em Markdown + scripts Python 3 stdlib
(sem dependências) para init, manifest (com grafo e hubs), auditoria, export
e import de memória compartilhada. O vault se mantém self-describing
(`_system/PROTOCOL/`), então o pacote pode sumir e o protocolo continua vivo
dentro do próprio vault. 14 agentes cobertos por adapters.

## v2 — CLI `sm`

- `sm init | capture | session open | session close | search | distill | doctor | manifest`
- `sm synapse <a> <b> --porque "..."` — cria sinapse validando que as duas
  pontas existem (grafo só cresce com arestas fortes reais)
- `sm share export --vis team` / `sm share import <bundle>` — os protocolos 07
  viram subcomando (mesma lógica dos scripts atuais)
- checkpoint automático: cada FECHAR gera `git commit -m "session: <id>"`
- `sm search` = MANIFEST.json (filtro por type/project/tags/shared) + fallback grep

## v3 — Servidor MCP

Funções expostas aos agentes (substitui o texto injetado no prompt):

- `sm_search(query, type?, project?)`
- `sm_read(path)` / `sm_read_head(path, tokens)`
- `sm_capture(type, slug, body_md)` (valida frontmatter antes de gravar)
- `sm_session_start()` / `sm_session_end(summary_sections)`
- `sm_distill(topic)` (aplica a regra das 3 sessões)
- `sm_synapse(a, b, porque)` (cria aresta forte validando pontas)
- watch mode: fs events → rebuild do manifest (debounce 2 s)

## v4 — rede de mentes

- multi-vault federado: 1 repo por projeto + índice raiz; `sm peer add <repo>`
- sync de pares via bundle (sem git entre partes): canal arbitrário, merge
  idempotente já implementado
- SQLite FTS5 para busca full-text (ainda opcional)
- resolução de conflito entre origens com `updated` + revisão humana assistida
- dashboard Obsidian (queries Dataview prontas sobre o frontmatter, incluindo
  hubs e sinapses recentes)

**Regra de ouro do programa:** o formato Markdown deste repositório NUNCA
muda por causa de código. O programa é implementação do protocolo,
nunca substituto dele.
