# Adapter: Codex / GitHub Copilot (padrão AGENTS.md)

1. Na raiz da pasta de trabalho (repo ou vault), garanta um `AGENTS.md` com o
   conteúdo do `AGENTS.md` deste pacote + o bloco do `BOOT.md` (é curto o
   bastante para inlining; ambos ficam na raiz).
2. Aponte os caminhos dentro do próprio `AGENTS.md`:
   ```
   VAULT=/caminho/MeuVault
   SECOND_MIND_PKG=/caminho/secondmind
   ```
3. Feito: Codex e Copilot leem `AGENTS.md` nativamente — nenhuma configuração
   extra é necessária além de permissão de escrita no filesystem.
4. Teste: `evals/golden-session.md`.
