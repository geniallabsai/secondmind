# Adapter: Cursor

O Cursor lê regras de projeto em `.cursor/rules/`.

1. Crie `.cursor/rules/secondmind.mdc`:
   ```
   ---
   description: SecondMind — memória persistente em Obsidian para o agente
   globs:
   alwaysApply: true
   ---
   ```
   Seguido do conteúdo completo de `BOOT.md` + as variáveis `VAULT` e
   `SECOND_MIND_PKG` definidas no topo.
2. Alternativa única-fonte: se a sua versão do Cursor honra `AGENTS.md` na
   raiz, use esse em vez do arquivo `.mdc` (mesmo conteúdo).
3. Teste: `evals/golden-session.md`.
