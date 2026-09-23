# Eval — golden session (aceitação com QUALQUER agente)

Objetivo: provar que um agente operando só com `BOOT.md` injetado (sem ler o
resto do pacote) executa o protocolo completo sem supervisão.

## Cenário
1. Vault limpo: `python3 scripts/vault_init.py /tmp/vault-teste`
2. Injetar `BOOT.md` no agente + definir `VAULT=/tmp/vault-teste`.
3. Dar ao agente esta tarefa de trabalho real:
   > "O projeto `api-notas` precisa de GET /notas com cache de 60 s.
   > Ontem usei Redis e ele derrubou em produção (memória estourou).
   > Decida o que usar, implemente a decisão e feche a sessão."

## Critério de passagem (TODOS)
- [ ] Buscou (grep) antes de escrever; registrou o resultado no Recuperado
      (ou declarou sessão fria).
- [ ] Criou/editou o MOC `02-projects/api-notas.md` (não criou duplicado).
- [ ] Criou `04-decisions/<data>--cache-sem-redis.md` com Racional e
      Alternativas descartadas.
- [ ] Fechou com `01-sessions/<data>--<hora>--<agente>--<slug>.md` com as
      7 seções preenchidas e callout `> [!next]`.
- [ ] MOC e `_system/VAULT-INDEX.md` atualizados junto do fechamento.
- [ ] Frontmatter completo e enums válidos em tudo que foi criado.
- [ ] `python3 scripts/sm_doctor.py /tmp/vault-teste` sai verde (exit 0).

## Falhas clássicas (reprovam)
- Nota sem frontmatter completo ou type fora do enum.
- Sessão sem Aprendizados nem pointer de próxima sessão.
- `[[wikilink]]` quebrado.
- MOC esquecido: o próximo agente não encontra o fio.
- Inventar memória: citar "na sessão anterior" sem que exista sessão anterior.
