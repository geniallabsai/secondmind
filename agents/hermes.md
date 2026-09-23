# Adapter: Hermes

1. Cole o conteúdo completo de `BOOT.md` no system prompt (ou campo de
   instruções) do perfil do Hermes. O bloco é autossuficiente: caminhos,
   frontmatter, orçamentos e loop de sessão estão todos nele.
2. Defina a variável: `VAULT=/caminho/MeuVault`.
3. Garanta as ferramentas de filesystem: leitura, escrita e busca (grep/glob)
   sobre a pasta do vault.
4. Depois de rodar `scripts/vault_init.py`, o vault vira self-describing
   (`_system/PROTOCOL/`): mesmo sem o pacote no disco, o agente lê os
   protocolos completos do próprio vault.
5. Teste: `evals/golden-session.md`.
