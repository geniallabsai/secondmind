# SecondMind 🧠

**Memória persistente para frotas de agentes de IA — o vault Obsidian como corpo.**

SecondMind é um pacote de *skills* em Markdown que transforma qualquer vault
Obsidian na segunda mente compartilhada dos seus agentes (14 agentes
suportados: Claude Code, Codex/Copilot, Hermes, OpenClaw, Gemini CLI, Cursor,
Aider, Cline, Roo Code, OpenHands, Goose, Amp, Windsurf — matriz completa em
`agents/MATRIX.md`). Sem banco, sem daemon, sem API: apenas arquivos com
estrutura fixa que qualquer LLM lê bem e escreve certo.

> **Filosofia (nível Tanos):** memória é o recurso escasso do agente.
> Modelo, contexto e ferramenta são substituívels; o que ficou gravado no vault
> sobrevive a troca de modelo, reset de contexto e morte do agente.
> O pacote existe para maximizar o que é capturado por token gasto.

## Por que Markdown e não banco de dados

| Escolha | Motivo |
|---|---|
| Markdown + YAML | formato nativo de LLMs e do Obsidian; diffável no git |
| Caminhos determinísticos | o agente nunca "acha" onde escrever: o protocolo define |
| `[[wikilinks]]` + sinapses | grafo de memória navegável por humanos e indexável por grep |
| `_system/MANIFEST.json` | índice máquina-gerado com grafo de entrada e hubs, sem embeddings |
| Git | transação, auditoria e undo; cada sessão fecha como checkpoint |

## O que tem dentro

```
secondmind/
├── README.md               ← você está aqui
├── SKILL.md                ← entrada da skill (as 5 fases + 8 leis)
├── BOOT.md                 ← bloco autossuficiente pra injetar em QUALQUER agente
├── AGENTS.md / CLAUDE.md   ← entradas padrão por ecossistema
├── CHANGELOG.md
├── agents/                 ← 14 adapters + MATRIX.md (receita p/ adicionar novo)
├── claude-commands/        ← /sm-close pronto
├── protocols/              ← os 8 protocolos operacionais (copia pro vault)
│   ├── 00-loop      ├── 01-capturar   ├── 02-recordar   ├── 03-fechar
│   ├── 04-destilar  ├── 05-higiene    ├── 06-sinapses   └── 07-share
├── conventions/            ← frontmatter + guia de leitura p/ LLM
├── templates/              ← 8 templates com {{placeholders}}
├── scripts/                ← Python 3 stdlib (zero dependências):
│   ├── vault_init.py   ├── build_manifest.py  ├── sm_doctor.py
│   └── export_share.py └── import_share.py
└── evals/                  ← golden-session + share-roundtrip
```

## Instalação (2 minutos)

```bash
git clone https://github.com/geniallabsai/secondmind
python3 secondmind/scripts/vault_init.py ~/MeuVault
```

Depois injete seus agentes (blocos prontos em `agents/`):

- **Claude Code** → `CLAUDE.md` + skill (`agents/claude-code.md`)
- **Codex / Copilot / Amp** → `AGENTS.md` (`agents/codex.md`, `agents/amp.md`)
- **Gemini CLI** → `GEMINI.md` · **Cursor** → `.cursor/rules/` · **Windsurf** → `.windsurf/rules/`
- **Aider** → `CONVENTIONS.md` · **Cline/Roo** → `.clinerules/`
- **Hermes / OpenClaw** → colar `BOOT.md` no system prompt
- **OpenHands / Goose** → microagent / skill

Feche com `python3 secondmind/scripts/sm_doctor.py ~/MeuVault` (verde = ok).

## O loop do agente (coração do pacote)

**ORIENTAR → RECORDAR → ATUAR → CAPTURAR → FECHAR** (detalhe em `SKILL.md` e `protocols/`)

## Sinapses — a camada de conexões (`protocols/06-sinapses.md`)

Nota é neurônio; sinapse decide quais neurônios conversam e **por quê**:
- arestas fracas (`[[wikilink]]`) para navegação, arestas fortes (nota
  `synapse` em `06-synapses/`) para relações não óbvias com motivação escrita;
- cadeia temporal entre sessões do mesmo projeto;
- origem (proveniência) nas destilações;
- `supersede` para versionar verdades sem apagar nada;
- o manifest calcula **hubs** (top in-degree): o agente orienta a leitura por
  gravidade de memória antes de buscar às cegas.

## Memória compartilhada entre agentes (`protocols/07-share.md`)

Memória de agente único morre com o agente. SecondMind compartilha com
proveniência e permissão:
- frontmatter `shared` + `visibility` (local/team/public) + `origin`;
- **handoffs**: entrega curada para outro agente/modelo (`01-sessions/handoffs/`);
- **export/import idempotente**: `export_share.py` gera bundle portátil
  (zip, sempre texto); `import_share.py` mescla por `id`/`updated`, arquiva
  versões supersedidas e registra tudo em `IMPORT-LOG.md`;
- federação sem servidor: o vault é um repo git — outro agente sincroniza com
  `git pull → doctor → trabalhar`.

## Regras de ouro

1. O vault é a única verdade. Contexto é cache, não registro.
2. Busca antes de escrita, sempre.
3. Toda sessão termina com resumo estruturado em `01-sessions/`.
4. Nota tem tipo, caminho fixo e frontmatter completo.
5. 3+ sessões no mesmo tema → destilar em conceito ou playbook.
6. Relação não óbvia entre conceitos → sinapse com "Por que" escrito.
7. Tudo é local por padrão; compartilhar exige `shared: true` + `visibility`.

## Licença

MIT
