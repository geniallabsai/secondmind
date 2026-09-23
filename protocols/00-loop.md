# Protocolo 00 — O Loop (referência estendida)

Ordem fixa das fases: **ORIENTAR → RECORDAR → ATUAR → CAPTURAR → FECHAR**.

## Falhas comuns e como o protocolo as mata

| Falha | Correção embutida |
|---|---|
| Agente "lembra" de coisa que não existe | Lei 2: o que não está no vault não aconteceu; declarar |
| Reescrever do zero a cada sessão | ORIENTAR lê MOC + últimas 2 sessões primeiro |
| Notas soltas, sem grafo | CAPTURAR exige ≥1 [[link]] p/ nota existente |
| Vault inchando sem servir | Orçamento de tokens por tipo + regra de 3 notas novas/sessão |
| Sessão termina sem deixar rastro | FECHAR é obrigatório e validado pelo doctor |
| Conhecimento morre nas sessões cruas | Destilação (protocolo 04) promove para concept/playbook |

## Se o vault ainda não existe
Rode `python3 $SECOND_MIND_PKG/scripts/vault_init.py <caminho>` e siga.
Nunca invente estrutura paralela ao contrato global (`SKILL.md`, tabela).

## Se o MOC do projeto não existe
Crie `02-projects/<projeto>.md` a partir de `_system/TEMPLATES/project-moc.md`
DENTRO da fase CAPTURAR (conta nas 3 notas novas da sessão).

## Regra de pausa
Durante ATUAR, a cada decisão durável, bug resolvido ou padrão identificável:
pare, capture (01-capturar), retome. Capturar no fim "do nada" gera resumo
vazio — o Aprendizados fica sem matéria-prima.
