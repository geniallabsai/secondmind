# MATRIX — quem é suportado e como

14 agentes suportados. Cada linha é instalável em ≤2 minutos seguindo o arquivo do adapter.

| Agente | Mecanismo de injeção | Adapter |
|---|---|---|
| Claude Code | skill + `CLAUDE.md` | `claude-code.md` |
| Codex CLI | `AGENTS.md` | `codex.md` |
| GitHub Copilot | `AGENTS.md` | `codex.md` |
| Hermes | system prompt (`BOOT.md`) | `hermes.md` |
| OpenClaw | raiz do workspace / skills | `openclaw.md` |
| Gemini CLI | `GEMINI.md` | `gemini-cli.md` |
| Cursor | `.cursor/rules/secondmind.mdc` | `cursor.md` |
| Aider | `CONVENTIONS.md` | `aider.md` |
| Cline | `.clinerules/` | `cline-roo.md` |
| Roo Code | `.clinerules/` (ou `.roo/rules/`) | `cline-roo.md` |
| OpenHands | microagents | `openhands.md` |
| Goose (Block) | pasta de skills (`SKILL.md`) | `goose.md` |
| Amp (Sourcegraph) | `AGENTS.md` | `amp.md` |
| Windsurf | `.windsurf/rules/` | `windsurf.md` |

## Como adicionar um agente novo (receita)
1. Identifique o mecanismo de instrução do agente (arquivo de regras, system
   prompt, skill).
2. Crie `agents/<nome>.md` com 4 linhas: mecanismo · caminho · conteúdo
   (sempre o bloco `BOOT.md` integral) · variáveis `VAULT` e `SECOND_MIND_PKG`.
3. Sem mecanismo de arquivo na sua versão? O fallback universal é colar
   `BOOT.md` no prompt inicial — ele foi escrito para ser autossuficiente.
4. Teste com `evals/golden-session.md` e adicione a linha na matriz.
