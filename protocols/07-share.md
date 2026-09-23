# Protocolo 07 — SHARE (memória persistente ENTRE agentes)

Memória de agente único morre com o agente. Memória compartilhada é a mesma
memória com **origem explícita e permissão controlada**. Compartilhar não é
"enviar tudo": é exportar o que serve de novo, com proveniência intacta.

## O que pode ser compartilhado
| Tipo | Compartilha? | Motivo |
|---|---|---|
| concept, playbook, decision, synapse | sim (se `shared: true`) | conhecimento reutilizável |
| handoff | sim | contexto curado para outro agente |
| session | só sob demanda | auditoria |
| inbox, project (MOC) | nunca automático | estado é de quem opera |

## Permissões (frontmatter)
```yaml
shared: true                 # elegível p/ export
visibility: local            # local | team | public
origin: vault-a@claude-code  # origem; NUNCA reescrita no import
```
Padrão de tudo: `shared: false`, `visibility: local`. Uma nota entra no
bundle somente se `shared: true` E `visibility` ⊇ destino (local < team <
public). Quem marca `shared` responde por estar tirando a nota do privado.

## Handoff (agente → agente)
Quando a sessão termina E a continuação vai acontecer com OUTRO
agente/modelo/instância: gere
`01-sessions/handoffs/HANDOFF-YYYY-MM-DD--<de>-para-<para>.md`
(template `handoff.md`) contendo:
1. quem pede, para quem, por que a troca;
2. decisões vigentes (apenas links para ADRs ativos);
3. estado atual do projeto em ≤5 bullets;
4. as primeiras 3 ações esperadas do receptor;
5. o que NÃO repetir (pegadas conhecidas, alternativas descartadas).
Handoff é FILTRO, não resumo: entra só o que muda a próxima ação do agente
receptor.

## Export (bundle)
```bash
python3 $SECOND_MIND_PKG/scripts/export_share.py <vault> \
  --out _system/export/sm-<data>.zip --visibility team
```
Bundle = notas elegíveis com caminhos relativos preservados + `MANIFEST.json`
+ `EXPORT-INFO.json` (origem, data, seleção). Formato portátil por
definição: pasta ou zip, sempre texto diffável — nunca binário proprietário.

## Import (merge idempotente)
```bash
python3 $SECOND_MIND_PKG/scripts/import_share.py <bundle.zip|pasta> <vault>
```
- Decisão por `id` e `updated`: local mais novo → mantém local;
  entrada mais nova → versão antiga vai para `07-archive/` marcada
  `superseded` (nunca apagada).
- `origin` nunca é reescrito: import enriquece, não apaga proveniência.
- Toda decisão registrada em `_system/IMPORT-LOG.md`.
- Ao final: `build_manifest.py` + `sm_doctor.py`.
- Rodar o mesmo bundle duas vezes = segunda vez não faz nada (idempotente).

## Sinapses no destino
Sinapse cujas pontas não foram exportadas gera link quebrado no destino — o
doctor local acusa; remédio: exportar as pontas junto (recomendado) ou
reescrever o link para o mais próximo existente.

## Federação (multi-máquina / times)
- O vault É o protocolo: é um repo git. Outro agente sincroniza com
  `git pull → sm_doctor.py → trabalhar`. Sem servidor, sem middleware.
- Entre máquinas/empresas sem git: envia-se o bundle (zip) por qualquer canal.
- Conflito entre duas origens com o mesmo `updated` → revisão humana; o
  doctor lista candidatos suspeitos.
