# Changelog

## 1.1.0 (2026-09-23)
- **+8 adapters** → 14 agentes: Gemini CLI, Cursor, Aider, Cline, Roo Code,
  OpenHands, Goose, Amp, Windsurf; nova `agents/MATRIX.md` com a receita
  para adicionar agente novo.
- **Protocolo 06 (Sinapses)**: camadas de aresta (referência, sinapse,
  cadeia, origem, supersede); `synapse` vira tipo de nota de 1ª classe em
  `06-synapses/` com seção "Por que" obrigatória; leitura passa a usar hubs
  (top in-degree) antes de busca cega.
- **Protocolo 07 (Share)**: memória persistente e compartilhável — campos
  `shared`/`visibility`/`origin`, handoffs entre agentes, export/import
  idempotente por `id`/`updated` com proveniência preservada, federação via git.
- **Scripts novos**: `export_share.py` (bundle portátil) e `import_share.py`
  (merge idempotente + `IMPORT-LOG.md`); `build_manifest.py` agora calcula
  grafo de entrada (`inbound`) e `hubs`; `sm_doctor.py` valida synapse sem
  "Por que" e `shared` sem `visibility`.
- **Templates novos**: `synapse.md`, `handoff.md`.
- **Eval novo**: `evals/share-roundtrip.md` (roundtrip entre dois vaults).
- `vault_init.py` cria `06-synapses/`, `01-sessions/handoffs/`, `_system/export/`.

## 1.0.0 (2026-09-23)
- Pacote inicial: SKILL (5 fases + leis), BOOT autossuficiente, 6 protocolos,
  6 templates, init/manifest/doctor em Python stdlib, 4 adapters
  (Claude Code, Codex/Copilot, Hermes, OpenClaw), golden-session, roadmap.
