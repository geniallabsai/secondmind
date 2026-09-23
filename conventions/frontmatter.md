# Convenção: frontmatter (dicionário de campos)

| Campo | Tipo | Obrigatório | Valores / formato | Nota |
|---|---|---|---|---|
| `id` | string | sim | `sm-<YYYYMMDD>-<agente>-<slug>` | único; derivado do nome do arquivo |
| `type` | enum | sim | inbox, session, project, concept, decision, playbook | fechado; doctor valida |
| `status` | enum | sim | active, done, archived, superseded | ciclo: active→done→archived |
| `created` | datetime | sim | `YYYY-MM-DDTHH:MM:SSZ` UTC | imutável depois de criado |
| `updated` | datetime | sim | idem | atualizar em TODA edição |
| `agent` | enum | sim | claude-code, codex, copilot, hermes, openclaw, human, init | quem escreveu a última versão |
| `project` | string | não | slug do projeto | vazio quando transversal |
| `tags` | list | sim | strings kebab-case minúsculas | pode ser lista vazia `[]` |
| `model` | string | não | ex.: `claude-opus-4` | rastreabilidade opcional |
| `distilled` | bool | não (session) | true/false | só sessões usam |
| `supersedes` | list | não | ids | notas tornadas obsoletas |
| `superseded_by` | string | não | id | presente quando status=superseded |

Regras gerais: YAML simples (chave: valor, listas inline `[a, b]` ou
`- item`); sem aninhamento profundo; sem arrays multidimensionais. Tudo que o
doctor não reconhece como campo válido é erro.
