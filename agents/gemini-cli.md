# Adapter: Gemini CLI

O Gemini CLI lê `GEMINI.md` na raiz do projeto (ou global em `~/.gemini/GEMINI.md`).

1. Crie `GEMINI.md` na raiz do trabalho com um apontamento curto + o bloco
   completo de `BOOT.md` colado depois.
2. Defina no topo do arquivo: `VAULT=/caminho/MeuVault`.
3. Conceda permissão de escrita quando solicitado.
4. Fallback: se a versão não carregar `GEMINI.md` sozinha, cole `BOOT.md` no
   prompt inicial da sessão.
5. Teste: `evals/golden-session.md`.
