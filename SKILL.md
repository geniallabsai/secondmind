---
name: secondmind
version: 1.1.0
description: >
  Transforma um vault Obsidian na segunda mente persistente do agente:
  captura, destilação, sinapses entre conceitos e memória compartilhada
  entre agentes. Acionar no início da sessão, antes de escrever qualquer
  coisa nova, ao tomar decisões e OBRIGATORIAMENTE no fim da sessão.
agents: [claude-code, codex, copilot, hermes, openclaw, gemini-cli, cursor,
         aider, cline, roo-code, openhands, goose, amp, windsurf]
entrypoint: BOOT.md
---

# SecondMind — Skill principal

## Quando acionar

- Início de qualquer sessão de trabalho com contexto de projeto.
- Antes de criar qualquer arquivo/nova nota.
- Ao tomar decisão que atravessa mais de 1 sessão.
- Fim de sessão (obrigatório).
- Pergunta "isso já foi resolvido antes?" → fase RECORDAR.

## As 5 fases (executar nesta ordem, sem pular)

### 1. ORIENTAR
Ler, nesta ordem, parando quando houver informação suficiente:
1. `_system/VAULT-INDEX.md`
2. **Hubs**: campo `hubs` do `_system/MANIFEST.json` (top 5 por grau de
   entrada — os nós onde mais memória gravita; ler antes de buscar cega).
3. MOC do projeto: `02-projects/<projeto>.md`
4. As 2 sessões mais recentes do projeto (nomes iniciam com data).

### 2. RECORDAR
Antes de escrever qualquer coisa, responder no raciocínio: **"isso já existe no vault?"**
```bash
grep -ril "<termo>" --include="*.md" $VAULT
ls $VAULT/03-concepts/ $VAULT/05-playbooks/
```
Zero resultados → declarar "sessão fria" no arquivo de fechamento.
Protocolo completo: `_system/PROTOCOL/02-recordar.md` (agora com caminhada pelo grafo).

### 3. ATUAR
Fazer o trabalho. Cada vez que surgir algo reaproveitável (decisão, bug
resolvido, padrão), parar e CAPTURAR na hora — nunca empurrar para o fim.
Se DOIS conceitos co-ocorrem e a relação entre eles não é óbvia → sinapse
(protocolo 06).

### 4. CAPTURAR
Seguir `_system/PROTOCOL/01-capturar.md`:
- caminho fixo por tipo (tabela de roteamento lá — inclui `06-synapses/`);
- frontmatter completo (obrigatório);
- mínimo 1 `[[link]]` para nota existente;
- dentro do orçamento de tokens do tipo.

### 5. FECHAR (obrigatório)
1. Criar `01-sessions/YYYY-MM-DD--HHMM--<agente>--<slug>.md` preenchendo TODAS as 7 seções do template `_system/TEMPLATES/session-summary.md`.
2. Atualizar o MOC do projeto: link da sessão + 1 linha de estado atual.
3. Atualizar `_system/VAULT-INDEX.md` (sessões recentes e novos arquivos).
4. Rodar `python3 $SECOND_MIND_PKG/scripts/build_manifest.py $VAULT` quando possível.
5. Destilação: se esta sessão + 2 anteriores tocam o mesmo tema, criar/atualizar a nota de síntese e marcar as 3 sessões com `distilled: true`.
6. **Handoff**: se a continuação vai para OUTRO agente/modelo/instância, gerar
   também `01-sessions/handoffs/HANDOFF-*.md` (template `handoff.md`, protocolo 07).

## Leis (invioláveis)

1. O vault é a única verdade; contexto é cache.
2. Não inventar memória: o que não está no vault "não aconteceu" — declarar.
3. Busca antes de escrita, sempre.
4. Frontmatter incompleto = nota inválida; o doctor acusa.
5. Máximo de 3 notas novas por sessão além do resumo de fechamento (anti-estouro).
6. Idioma das notas = idioma da sessão; chaves, enums e tags em inglês.
7. Sinapse é para relação NÃO óbvia; relação óbvia é só wikilink. Sinapse sem "Por que" não existe.
8. Memória é local por padrão. `shared: true` só com `visibility` explícito — quem compartilha responde pela nota.

## Estrutura do vault (contrato global)

| Diretório | Tipo guardado | Quem escreve |
|---|---|---|
| `00-inbox/` | inbox | todos (captura rápida) |
| `01-sessions/` | session | agentes na fase FECHAR |
| `01-sessions/handoffs/` | handoff | agente que fecha PARA outro agente |
| `02-projects/` | project (MOC) | agentes + humanos |
| `03-concepts/` | concept | agentes/humanos |
| `04-decisions/` | decision | agentes ao decidir coisas duráveis |
| `05-playbooks/` | playbook | destilação |
| `06-synapses/` | synapse | agentes na CAPTURAR (relação não óbvia) |
| `07-archive/` | tudo que fechou | humano / heartbeat |
| `_system/` | protocolo, templates, índices, exports | init + agentes |
