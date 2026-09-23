# Roadmap — do pacote ao programa

**v1 (este repositório):** skills em Markdown + scripts Python 3 stdlib
(sem dependências) para init, manifest e auditoria. O vault se mantém
self-describing (`_system/PROTOCOL/`), então o pacote pode sumir e o
protocolo continua vivo dentro do próprio vault.

## v2 — CLI `sm`

- `sm init | capture | session open | session close | search | distill | doctor | manifest`
- checkpoint automático: cada FECHAR gera `git commit -m "session: <id>"`
- `sm search` = MANIFEST.json (filtro por type/project/tags) + fallback grep

## v3 — Servidor MCP

Funções expostas aos agentes (substitui o texto injetado no prompt):

- `sm_search(query, type?, project?)`
- `sm_read(path)` / `sm_read_head(path, tokens)`
- `sm_capture(type, slug, body_md)` (valida frontmatter antes de gravar)
- `sm_session_start()` / `sm_session_end(summary_sections)`
- `sm_distill(topic)` (aplica a regra das 3 sessões)
- watch mode: fs events → rebuild do manifest (debounce 2 s)

## v4

- SQLite FTS5 para busca full-text (ainda opcional)
- resolução de conflito com `superseded-by` + índice de versões
- dashboard Obsidian (queries Dataview prontas sobre o frontmatter)
- multi-vault: 1 repo por projeto + federacao via índice raiz

**Regra de ouro do programa:** o formato Markdown deste repositório NUNCA
muda por causa de código. O programa é implementação do protocolo,
nunca substituto dele.
