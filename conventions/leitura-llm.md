# Convenção: guia de leitura para LLMs

Como um LLM deve interpretar uma nota SecondMind (contrato de parsing):

1. **Arquivo = unidade.** Cada `.md` carrega UMA ideia/procedimento/sessão.
   Nunca espere uma nota conter outro escopo.
2. **Frontmatter = metadados de filtro.** Use `type`, `project`, `tags`,
   `status` para decidir SE ler, antes de ler. `MANIFEST.json` indexa esses
   campos sem abrir arquivo.
3. **H1 = afirmação/título.** O H1 deve ser verdadeiro sozinho:
   "# Cache em memória vence Redis até 50k chaves" e não "# Notas sobre cache".
4. **H2 numerado = slot com contrato.** A ordem e o nome das seções são
   fixos por tipo (protocolo 01): o leitor sabe exatamente onde está
   Resumo, Decisão, Passos etc. Nunca reordenar ou renomear seção; para
   acrescentar informação, ADICIONE dentro da seção correta.
5. **Wikilinks = arestas do grafo de memória.** Seguir um link = navegar a
   memória; cada aresta existe porque alguém decidiu que os dois temas
   coabitam.
6. **Economia de tokens.** Prefira bullets e tabelas; parágrafo só para
   raciocínio (Racional de ADR). Callout `> [!next]` é o único marcador
   visual reservado: sempre significa "primeira ação da próxima sessão".
7. **Ausência é informação.** Se a seção Recuperado diz "sessão fria" ou o
   grep não retornou nada, trate como dado: o assunto não foi tratado no
   vault antes. Nunca inferir memória inexistente.
8. **Determinismo de escrita.** Mesmos inputs → mesmos nomes de arquivo,
   mesmas seções, mesmos campos. Isso permite diff, deduplicação e,
   futuramente, indexação exata.
