---
layout: post
title: "Migração de SQLite para MySQL 9.1 com InnoDB Forçado e Isolamento de Testes no Laravel 11"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-138"
description: "A migração do ERP de SQLite para MySQL 9.1 exigiu parametrização de engine InnoDB estrita e revisão do ciclo de testes. Desativamos rotinas destrutivas de bootstrap preservando simulações no banco corporativo."
date: 2026-11-08 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [laravel, mysql, sqlite, pest, devops]
---

# Migração de SQLite para MySQL 9.1 com InnoDB Forçado e Isolamento de Testes no Laravel 11

> [!NOTE]
> **Resumo Executivo (DEV-2026-138)**: A migração do ERP de SQLite para MySQL 9.1 exigiu parametrização de engine InnoDB estrita e revisão do ciclo de testes. Desativamos rotinas destrutivas de bootstrap preservando simulações no banco corporativo.

---

### 🚨 O Desafio Técnico / Contexto
O driver padrão do MySQL criava tabelas sob collation e engines legadas quando omitidas, gerando falhas em chaves estrangeiras com cascades e deadlocks durante a instalação modular de 11 plugins. Simultaneamente, o helper de testes executava migrate:fresh a cada execução do Pest, apagando a base MySQL de desenvolvimento.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Forçar 'engine' => 'InnoDB' na conexão mysql do config/database.php garante integridade relacional entre plugins.
* 💡 TestBootstrapHelper não pode invocar migrate:fresh em ambientes locais com dados persistidos de simulação.
* 💡 O uso da trait DatabaseTransactions no Pest isola cada teste revertendo commits sem truncar tabelas.
* 💡 Comandos que acessam soquetes de rede locais no Windows exigem desvio de isolamento quando executados fora do servidor.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
'mysql' => [
    'driver' => 'mysql',
    'engine' => 'InnoDB',
    'charset' => 'utf8mb4',
    'collation' => 'utf8mb4_unicode_ci',
    'prefix' => '',
    'strict' => true,
],
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Ambiente de desenvolvimento e testes rodando sobre MySQL real com isolamento de transações em 16 segundos.

* **Projetos Relacionados**: `laravel-ERP`
* **Registro de Origem**: `_data/daily.dev-23.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
