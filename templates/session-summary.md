---
id: sm-{{YYYYMMDD}}-{{agente}}-{{slug}}
type: session
status: active
created: {{AAAA-MM-DDTHH:MM:SSZ}}
updated: {{AAAA-MM-DDTHH:MM:SSZ}}
agent: {{claude-code|codex|copilot|hermes|openclaw}}
project: {{slug-do-projeto}}
model: {{opcional}}
tags: []
distilled: false
supersedes: []
---
# Sessão: {{título objetivo em ≤8 palavras}}

## 1. Contexto
2–4 linhas: o que foi pedido e qual era o estado inicial.

## 2. Recuperado
- [[nota]] — o que serviu dela
_(se nada: "sessão fria: busca no vault não retornou nada relevante para X")_

## 3. Ações
- [x] ação concluída (resultado, não intenção)

## 4. Decisões
| Decisão | Motivo | Alternativa descartada |
|---|---|---|
| ... | ... | ... |
_(decisão durável → criar ADR em 04-decisions/ e linkar aqui)_

## 5. Artefatos
- `caminho/arquivo` — o que mudou ([[nota]] se gerou nota)

## 6. Aprendizados
- 1 linha, acionável, aplicável pelo próximo agente sem contexto extra
_(ou "nenhum — sessão curta")_

## 7. Em aberto e próximos passos
- [ ] pergunta sem resposta / tarefa para a próxima sessão

> [!next] Pointer da próxima sessão
Primeira coisa que o próximo agente deve fazer: …
