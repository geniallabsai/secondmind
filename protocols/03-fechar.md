# Protocolo 03 — FECHAR (o arquivo de sessão)

O arquivo de sessão é o contrato entre agentes: quem fecha deixa o próximo
agente (qualquer modelo, qualquer dia) capaz de retomar sem reescrever a
história. Sem ele, a memória morre no contexto.

## Nome do arquivo
`01-sessions/YYYY-MM-DD--HHMM--<agente>--<slug>.md`
Data/hora do INÍCIO da sessão, UTC. `<agente>` ∈ {claude-code, codex, copilot,
hermes, openclaw}. Slug descreve o tema em 2–4 palavras.

## As 7 seções (todas obrigatórias, ordem fixa)
1. **Contexto** — 2–4 linhas: o que foi pedido e qual era o estado inicial.
2. **Recuperado** — quais notas do vault foram lidas/usadas + o que serviu;
   ou "sessão fria".
3. **Ações** — bullets `- [x]` do que foi executado (resultado, não intenção).
4. **Decisões** — tabela decisão/motivo/alternativa; decisão durável vira ADR
   em `04-decisions/` e recebe link aqui.
5. **Artefatos** — arquivos criados/alterados (`path` + 1 linha); nota gerada
   ganha `[[link]]`.
6. **Aprendizados** — 1 linha cada, acionável. Se a sessão não gerou nenhum,
   escrever "nenhum — sessão curta" (mas 2 sessões seguidas assim = revisar
   a profundidade do trabalho).
7. **Em aberto e próximos passos** — perguntas sem resposta + callout
   `> [!next]` dizendo EXATAMENTE a primeira coisa que o próximo agente deve fazer.

## Limites
≤900 tokens. Estourou? Sessão grande demais → dividir em 2 sessões no vault
(arquivos separados, mesma data-hora base, prefixo `a`/`b`).

## Anti-padrões que reprovam
- Sessão sem Aprendizados e sem `> [!next]` (memória que não ensina nada).
- Log sem decisões (só ações = diário, não segunda mente).
- Recuperado vazio em sessão quente (não procurou antes de trabalhar).
- MOC e VAULT-INDEX não atualizados junto do fechamento.
