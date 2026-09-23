# Adapter: Claude Code

1. **Skill (recomendado):** copie o pacote para `~/.claude/skills/secondmind/`
   (o `SKILL.md` precisa estar na raiz dessa pasta). O Claude Code carrega a
   skill automaticamente em toda conversa. Alternativa por projeto:
   `<projeto>/.claude/skills/secondmind/`.
2. **Defina os caminhos** adicionando no `CLAUDE.md` da raiz do trabalho:
   ```
   SecondMind: VAULT=/caminho/MeuVault · SECOND_MIND_PKG=~/.claude/skills/secondmind
   ```
3. **Comando de fechamento:** copie `claude-commands/sm-close.md` para
   `.claude/commands/sm-close.md` → vira `/sm-close` (fecha a sessão e mostra
   o que foi salvo na memória).
4. Na primeira escrita no vault, aceite o prompt de permissão de arquivo
   (ou deixe o workspace fora do plan mode).
5. Teste: `evals/golden-session.md`.
