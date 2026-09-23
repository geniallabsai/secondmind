# Protocolo 01 — CAPTURAR (escrever bem no vault)

## Tabela de roteamento: conteúdo → tipo → caminho

| Conteúdo que surgiu | Tipo | Caminho |
|---|---|---|
| Captura bruta sem tempo de processar | inbox | `00-inbox/YYYY-MM-DD--HHMM--<slug>.md` |
| Resumo de sessão | session | `01-sessions/YYYY-MM-DD--HHMM--<agente>--<slug>.md` |
| Entrega curada para OUTRO agente | handoff | `01-sessions/handoffs/HANDOFF-YYYY-MM-DD--<de>-para-<para>.md` |
| Estado / meta / tarefas do projeto | project | EDITE `02-projects/<projeto>.md` (nunca crie duplicado) |
| Conceito ou fato reutilizável (1 ideia) | concept | `03-concepts/<slug>.md` |
| Decisão durável | decision | `04-decisions/YYYY-MM-DD--<slug>.md` |
| Procedimento verificável passo a passo | playbook | `05-playbooks/<slug>.md` |
| Relação NÃO óbvia entre dois conceitos | synapse | `06-synapses/<a>-x-<b>.md` (protocolo 06) |

## Slugs
kebab-case, 2–6 palavras, sem acento, sem data (exceto decision/inbox/session/handoff,
que já levam data no nome). Colisão de slug = EDITAR a existente — nunca criar
`...-2.md`.

## Frontmatter obrigatório (toda nota, todo tipo)
```yaml
---
id: sm-<YYYYMMDD>-<agente>-<slug>
type: inbox|session|project|concept|decision|playbook|synapse|handoff
status: active|done|archived|superseded                  # enum fechado
created: 2026-09-23T12:00:00Z                            # UTC ISO-8601
updated: 2026-09-23T12:00:00Z
agent: claude-code|codex|copilot|hermes|openclaw|human|init
project: <slug-do-projeto>                               # vazio se transversal
tags: [kebab, kebab]                                     # minúsculas
shared: false                                            # elegível p/ export
visibility: local                                        # local|team|public
---
```
Campos extras permitidos apenas: `model`, `distilled` (bool), `supersedes`
(lista), `superseded_by` (string), `origin` (`<vault>@<agente>`; só em notas
importadas — nunca reescrita). Nada além disso.

## Esqueletos de corpo (seções fixas, ordem fixa)

**concept**
```markdown
# <Afirmação como título>
## Resumo            (≤3 linhas)
## Conteúdo          (bullets curtos)
## Evidência         (fontes; obrigatória se fato externo)
## Relacionado       (≥1 [[link]])
```

**decision (ADR-lite)**
```markdown
# ADR: <decisão>
## Contexto
## Decisão           (1 linha)
## Racional
## Alternativas descartadas
## Impacto
## Relacionado       (≥1 [[link]])
```

**playbook**
```markdown
# Playbook: <o que resolve>
## Quando usar
## Quando NÃO usar
## Passos            (numerados, executáveis, com comandos exatos)
## Armadilhas
## Última verificação (data + quem)
## Relacionado
```

**synapse**
```markdown
# <A> × <B>
## Por que           (OBRIGATÓRIA; sem ela o doctor reprova)
## Contexto onde surgiu ([[sessão]] + 1 linha)
## Como percorrer    (de qual ponta partir quando)
```

**handoff**
```markdown
# Handoff: <de> → <para>
## Por que a troca
## Decisões vigentes (apenas [[ADR]]s ativos)
## Estado atual      (≤5 bullets)
## Primeiras ações do receptor (3)
## O que NÃO repetir
```

**MOC de projeto**
```markdown
# Projeto <nome>
## Objetivo          (1 frase)
## Estado atual      (link p/ última sessão + ≤2 linhas)
## Decisões vigentes (lista de [[ADR]])
## Tarefas abertas
## Próximos passos
## Sessões           (cronológico, mais recente primeiro)
```

## Orçamento de tokens por tipo
inbox ≤150 · synapse ≤120 · decision ≤500 · concept ≤600 · handoff ≤700 ·
session ≤900 · playbook ≤1200 · MOC ≤1000 (a seção Sessões não conta).
Estourou? DIVIDA em notas menores ligadas por wikilink — nunca acrescente.

## Linkagem (contrato de resolução)
- Nota nova SEMPRE sai com ≥1 `[[wikilink]]` para nota existente (grafo se conecta).
- **Resolução**: nome-exato do arquivo sem `.md`. Para notas datadas
  (session/decision/inbox/handoff) vale também o **slug de cauda** (após o
  último `--`): `[[sessao-cache-decisao]]` resolve para
  `2026-09-23--0900--claude-code--sessao-cache-decisao.md`. Cauda ambígua
  resolve para a nota com `updated` mais recente; para apontar outra,
  escreva o nome completo.
- Alias: `[[nota|texto]]`.
- Ao linkar, verifique se a outra nota merece backlink na seção Relacionado.
- Nota sem nenhum link entrante após 14 dias = candidata a arquivar (protocolo 05).

## Anti-padrões (reprovam no doctor ou na revisão)
Nota sem frontmatter completo · wall of text (>40 linhas sem H2) · slug duplicado ·
nota órfã criada "para ficar" · MOC duplicado de projeto existente ·
sinapse sem "Por que" · compartilhamento sem `visibility` explícito.
