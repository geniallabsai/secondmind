# SecondMind 🧠

**Memória persistente para frotas de agentes de IA — o vault Obsidian como corpo.**

SecondMind é um pacote de *skills* em Markdown que transforma qualquer vault
Obsidian na segunda mente compartilhada dos seus agentes (Claude Code,
Codex/Copilot, Hermes, OpenClaw e você). Sem banco, sem daemon, sem API:
apenas arquivos com estrutura fixa que qualquer LLM lê bem e escreve certo.

> **Filosofia (nível Tanos):** memória é o recurso escasso do agente.
> Modelo, contexto e ferramenta são substituívels; o que ficou gravado no vault
> sobrevive a troca de modelo, reset de contexto e morte do agente.
> O pacote existe para maximizar o que é capturado por token gasto.

## Por que Markdown e não banco de dados

| Escolha | Motivo |
|---|---|
| Markdown + YAML | formato nativo de LLMs e do Obsidian; diffável no git |
| Caminhos determinísticos | o agente nunca "acha" onde escrever: o protocolo define |
| `[[wikilinks]]` | grafo de memória navegável por humanos e indexável por `grep` |
| `_system/MANIFEST.json` | índice máquina-gerado para busca rápida sem embeddings |
| Git | transação, auditoria e undo; cada sessão fecha como checkpoint |

## O que tem dentro

```
secondmind/
├── README.md               ← você está aqui
├── SKILL.md                ← entrada da skill (as 5 fases + leis)
├── BOOT.md                 ← bloco autossuficiente pra injetar em QUALQUER agente
├── AGENTS.md / CLAUDE.md   ← entradas padrão por ecossistema
├── agents/                 ← passo a passo de instalação por agente
│   ├── claude-code.md  ├── codex.md  ├── hermes.md  └── openclaw.md
├── claude-commands/        ← /sm-close pronto
├── protocols/              ← os 6 protocolos operacionais (copia pro vault)
│   ├── 00-loop.md  ├── 01-capturar.md  ├── 02-recordar.md
│   ├── 03-fechar.md ├── 04-destilar.md └── 05-higiene.md
├── conventions/            ← frontmatter + guia de leitura p/ LLM
├── templates/              ← 6 templates com {{placeholders}}
├── scripts/                ← Python 3 stdlib: init, manifest, doctor
│   ├── vault_init.py  ├── build_manifest.py  └── sm_doctor.py
├── evals/golden-session.md ← teste de aceitação com qualquer agente
└── ROADMAP.md              ← do pacote ao programa (v2 CLI, v3 MCP)
```

## Instalação (2 minutos)

```bash
git clone https://github.com/<seu-usuario>/secondmind
python3 secondmind/scripts/vault_init.py ~/MeuVault
```

Depois injete seus agentes (blocos prontos em `agents/`):

- **Claude Code** → `CLAUDE.md` + skill (`agents/claude-code.md`)
- **Codex / Copilot** → `AGENTS.md` (`agents/codex.md`)
- **Hermes / OpenClaw** → colar `BOOT.md` no system prompt (`agents/hermes.md`, `agents/openclaw.md`)

Feche com `python3 secondmind/scripts/sm_doctor.py --vault ~/MeuVault` (verde = ok).

## O loop do agente (coração do pacote)

**ORIENTAR → RECORDAR → ATUAR → CAPTURAR → FECHAR** (detalhe em `SKILL.md` e `protocols/`)

## Regras de ouro

1. O vault é a única verdade. Contexto é cache, não registro.
2. Busca antes de escrita, sempre.
3. Toda sessão termina com resumo estruturado em `01-sessions/`.
4. Nota tem tipo, caminho fixo e frontmatter completo.
5. 3+ sessões no mesmo tema → destilar em conceito ou playbook.

## Licença

MIT
