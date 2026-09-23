# Convenção: guia de leitura para LLMs

Como um LLM deve interpretar uma nota SecondMind (contrato de parsing):

1. **Arquivo = unidade.** Cada `.md` carrega UMA ideia/procedimento/sessão/sinapse.
   Nunca espere uma nota conter outro escopo.
2. **Frontmatter = metadados de filtro.** Use `type`, `project`, `tags`,
   `status`, `shared`, `visibility` para decidir SE ler, antes de ler.
   `MANIFEST.json` indexa esses campos — e `hubs` diz por onde começar.
3. **H1 = afirmação/título.** O H1 deve ser verdadeiro sozinho:
   "# Cache em memória vence Redis até 50k chaves" e não "# Notas sobre cache".
4. **H2 numerado = slot com contrato.** A ordem e o nome das seções são
   fixos por tipo (protocolo 01): o leitor sabe exatamente onde está
   Resumo, Decisão, Passos, Por que etc. Nunca reordenar ou renomear seção;
   para acrescentar informação, ADICIONE dentro da seção correta.
5. **Wikilinks = arestas fracas; sinapses = arestas fortes.** Ao navegar,
   preferir caminhos que passem por notas `synapse`: elas carregam o POR QUÊ
   da conexão, que wikilink comum não tem. Links resolvem por nome
   exato ou por slug de cauda de notas datadas (ver protocolo 01).
6. **Hubs antes de busca.** Os nós com mais links de entrada (campo `hubs`)
   concentram memória gravitacional: ler hub primeiro é mais barato que grep
   às cegas e raramente erra o alvo.
7. **Economia de tokens.** Prefira bullets e tabelas; parágrafo só para
   raciocínio (Racional de ADR, Por que de sinapse). Callout `> [!next]` é o
   único marcador visual reservado: significa "primeira ação da próxima sessão".
8. **Ausência é informação.** Se a seção Recuperado diz "sessão fria" ou o
   grep não retornou nada, trate como dado: o assunto não foi tratado no
   vault antes. Nunca inferir memória inexistente.
9. **Proveniência é sagrada.** `origin` indica de onde a nota veio; ao citar
   nota importada, cite também sua origem. Nunca reescrever `origin`.
10. **Determinismo de escrita.** Mesmos inputs → mesmos nomes de arquivo,
    mesmas seções, mesmos campos. Isso permite diff, deduplicação e,
    futuramente, indexação exata.
