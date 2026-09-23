# Protocolo 02 — RECORDAR (ler bem o vault)

## Ordem de leitura (parar quando houver informação suficiente)
1. `_system/VAULT-INDEX.md` — mapa geral.
2. `02-projects/<projeto>.md` — estado, decisões vigentes, última sessão.
3. Últimas 2 sessões do projeto (nomes datados, sort desc).
4. Busca full-text apenas com o termo específico que falta.

## Buscas padrão
```bash
# por palavra-chave (qualquer lugar)
grep -ril "<termo>" --include="*.md" $VAULT

# tudo ligado a um projeto
grep -rl "^project: <slug>" --include="*.md" $VAULT

# decisões sobre um tema
grep -ril "<termo>" --include="*.md" $VAULT/04-decisions/

# "como faz X?" → playbooks primeiro
ls $VAULT/05-playbooks/; grep -ril "<termo>" --include="*.md" $VAULT/05-playbooks/

# histórico de sessões de um tema
grep -ril "<termo>" --include="*.md" $VAULT/01-sessions/
```

## Regras
- Nunca ler o vault inteiro; ler em escopo (índice → MOC → alvo).
- Antes de ler nota cheia, leia frontmatter + primeiro H2 (barato e
  suficiente para decidir se serve).
- Registrar na sessão quais notas foram usadas (seção Recuperado) — isso é o
  trilha de auditoria da memória.
- Zero resultados → declarar "sessão fria" na seção Recuperado. Nunca
  preencher o buraco com suposição.
- Conflito entre duas notas: vale a mais recente, E ela precisa apontar a
  anterior com `superseded_by` (se não apontar, sinalizar no Em aberto).
