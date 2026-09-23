# Adapter: Aider

O Aider lê automaticamente `CONVENTIONS.md` na raiz do repo.

1. Copie o conteúdo de `BOOT.md` para `<repo>/CONVENTIONS.md` com as variáveis
   `VAULT` e `SECOND_MIND_PKG` definidas no topo.
2. Dê o índice do vault como contexto de leitura:
   `aider --read $VAULT/_system/VAULT-INDEX.md`
3. Escrita: o agente edita arquivos direto (fluxo git normal); cada fechamento
   de sessão já prevê o checkpoint (ver `ROADMAP.md`, v2).
