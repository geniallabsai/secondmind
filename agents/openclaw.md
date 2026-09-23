# Adapter: OpenClaw

1. **Opção A (workspace):** copie `BOOT.md` para a raiz do workspace do agente
   (como `BOOT.md`) — OpenClaw lê arquivos de instrução na raiz do workspace.
2. **Opção B (skill):** copie o pacote para `<workspace>/skills/secondmind/`
   e aponte o agente para `skills/secondmind/SKILL.md`.
3. Defina `VAULT=/caminho/MeuVault` na config e libere permissão de leitura e
   escrita no vault.
4. Teste: `evals/golden-session.md`.
