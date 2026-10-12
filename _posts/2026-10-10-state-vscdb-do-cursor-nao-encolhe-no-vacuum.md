---
layout: post
title: "Os 17 GB do Cursor estão no state.vscdb, e o VACUUM não devolve espaço"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-075"
description: "Os 17,3 GB que pareciam memória do Cursor são o SQLite de globalStorage, a cópia .backup e o CLI do agente. O banco vivo quase não tem página livre, então VACUUM não devolve disco."
date: 2026-10-10 00:00:00+00:00
categories: devlog
category: windows
tags: [cursor, sqlite, appdata, vacuum]
---

# Os 17 GB do Cursor estão no state.vscdb, e o VACUUM não devolve espaço

> [!NOTE]
> **Resumo Executivo (DEV-2026-075)**: Os 17,3 GB que pareciam memória do Cursor são o SQLite de globalStorage, a cópia .backup e o CLI do agente. O banco vivo quase não tem página livre, então VACUUM não devolve disco.

---

### 🚨 O Desafio Técnico / Contexto
A busca por uma pasta de memória não achou memories nem %USERPROFILE%\.cursor\rules. A conta fechou em três itens de %APPDATA%\Cursor\User\globalStorage: state.vscdb com 12,15 GB, state.vscdb.backup com 3,18 GB e anysphere.cursor-agent-worker com 1,97 GB. No momento da medição o volume C: tinha cerca de 20,9 GiB livres.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A soma de 17,3 GB é state.vscdb (12,15 GB), state.vscdb.backup (3,18 GB) e a pasta anysphere.cursor-agent-worker (1,97 GB).
* 💡 state.vscdb tem ItemTable (1317 chaves), composerHeaders (606 conversas, 27 arquivadas) e cursorDiskKV (752715 chaves, 382083 com prefixo agentKv:blob). PRAGMA freelist_count devolveu 1, com page_size 4096 e page_count 3184602. VACUUM não encolhe esse arquivo.
* 💡 O peso do agent-worker está em agent-cli\.local\share\cursor-agent\versions. Havia 11 pastas, de 2026.06.26-7079533 até 2026.09.18-9a7762b. Isso é instalador do CLI, não o texto do chat.
* 💡 CachedData tinha 34 hashes de instalação e 1,61 GB no total. A pasta mais nova na medição era cd6d2a1f2e56e9841f0ed9c7c24542087b4e69b0, de 9 de outubro de 2026. As outras são sobra de atualização.
* 💡 User Rules ficam na conta do Cursor. Apagar state.vscdb apaga o histórico local. Apagar só o .backup tira a cópia antiga e deixa o banco que ainda abre os chats.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
PRAGMA page_size;       -- 4096
PRAGMA page_count;      -- 3184602
PRAGMA freelist_count;  -- 1
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Dá para recuperar o backup e as versões velhas do editor e do CLI sem mexer no banco que ainda abre os chats.

* **Projetos Relacionados**: `cursor`
* **Registro de Origem**: `_data/daily.dev-12.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
