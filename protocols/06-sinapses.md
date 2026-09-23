# Protocolo 06 — SINAPSES (a camada de conexões da memória)

Notas são neurônios; sinapses decidem quais neurônios conversam ENTRE SI e POR
QUÊ. Sem sinapses o vault é um arquivo morto; com sinapses vira grafo
travável por humanos e por LLMs.

## Tipos de aresta (contrato do grafo)
1. **Referência** — `[[link]]` simples: "relacionado". Aresta fraca, navegação.
2. **Sinapse** — nota dedicada em `06-synapses/`: "X liga a Y porque Z".
   Aresta forte: motivação explícita, contexto e origem (sessão que a descobriu).
3. **Cadeia** — temporal: sessões do mesmo projeto se encadeiam (anterior/
   próximo) na seção Sessões do MOC. Memória através do tempo.
4. **Origem** — proveniência: conceitos destilados citam as sessões que os
   geraram (seção Evidência).
5. **Supersede** — `supersedes` / `superseded_by`: arestas entre versões de
   uma mesma verdade. Nunca apagar, sempre versionar.

## Quando criar sinapse (dentro da fase CAPTURAR)
Dois conceitos co-ocorrem na MESMA sessão E a relação entre eles NÃO é óbvia.
Exemplo óbvio (não criar): "falha no Redis" × "cache em processo" — o
wikilink basta. Exemplo não-óbvio (criar): "TTL do cache" × "frequência de
destilação de sessões" — a conexão só existe porque alguém raciocinou sobre
as duas coisas juntas.

Regra prática: **se um agente futuro precisaria reler três notas para
reconstruir a relação, escreva a sinapse.** Caminho:
`06-synapses/<a>-x-<b>.md` (template `synapse.md`, ≤120 tokens, seção "Por
que" obrigatória — sem ela o doctor reprova).

## Orientação pelo grafo (leitura melhorada do protocolo 02)
1. `_system/VAULT-INDEX.md`
2. **Hubs**: campo `hubs` do `MANIFEST.json` (top 5 por grau de entrada) —
   são os nós que mais memória gravitam em volta; ler primeiro economiza busca.
3. MOC do projeto
4. Nota-alvo
5. Backlinks 1-salto da nota-alvo (contexto circundante)
Parar quando houver informação suficiente. Nunca ler vault inteiro.

## Manutenção do grafo
- Conceito com ≥5 links de entrada = MOC tácito do domínio: considere criar o
  MOC explícito ou consolidar nele.
- Sinapse sem nenhum link de entrada após 14 dias = relação suspeita: revisar
  (manter com motivo ou excluir).
- Orfanatos (0 entradas + 0 saídas) não sobrevivem: toda nota nova sai com ≥1
  link de saída (protocolo 01).

## Anti-padrões
- Sinapse sem "Por que" — isso é referência disfarçada; rebaixar a wikilink.
- Spam de links: >6 saídas num conceito = diluição; manter os 3–4 mais fortes,
  o resto vai para o MOC.
- Ciclo A→B→A sem nó terceiro = cheiro de duas notas que deveriam ser uma.
