# Protocolo 02 — RECORDAR (ler bem o vault)

## Ordem de leitura (parar quando houver informação suficiente)
1. `_system/VAULT-INDEX.md` — mapa geral.
2. **Hubs**: campo `hubs` do `_system/MANIFEST.json` (top 5 por grau de
   entrada) — são os nós onde mais memória gravita; ler eles antes de buscar
   cega corta o número de buscas pela metade.
3. `02-projects/<projeto>.md` — estado, decisões vigentes, última sessão.
4. Últimas 2 sessões do projeto (nomes datados, sort desc).
5. Busca full-text apenas com o termo específico que falta.
6. **Backlinks 1-salto** da nota-alvo: para contexto circundante (quem mais
   aponta para ela), seguir no máximo 1 salto.

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

# relações explícitas (sinapses) sobre X
grep -ril "<termo>" --include="*.md" $VAULT/06-synapses/

# histórico de sessões de um tema
grep -ril "<termo>" --include="*.md" $VAULT/01-sessions/
```

## Regras
- Nunca ler o vault inteiro; ler em escopo (índice → hubs → MOC → alvo).
- Antes de ler nota cheia, leia frontmatter + primeiro H2 (barato e
  suficiente para decidir se serve).
- Registrar na sessão quais notas foram usadas (seção Recuperado) — isso é a
  trilha de auditoria da memória.
- Zero resultados → declarar "sessão fria" na seção Recuperado. Nunca
  preencher o buraco com suposição.
- Conflito entre duas notas: vale a mais recente, E ela precisa apontar a
  anterior com `superseded_by` (se não apontar, sinalizar no Em aberto).
