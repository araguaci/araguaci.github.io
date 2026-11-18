---
layout: post
title: "Chave estrangeira auto-referenciada em tabela UUID no PostgreSQL 16 exige que a PK já exista"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-153"
description: "A migration de service_orders quebrava no PostgreSQL 16 ao declarar a chave estrangeira parent_order_id para a própria tabela dentro do Schema::create. Separar a constraint em um bloco Schema::table logo após a criação da tabela resolveu o erro SQLSTATE[42830]."
date: 2026-11-12 00:00:00-03:00
categories: devlog
category: backend
tags: [postgresql, laravel, migrations, uuid, sqlstate-42830]
---

# Chave estrangeira auto-referenciada em tabela UUID no PostgreSQL 16 exige que a PK já exista

> [!NOTE]
> **Resumo Executivo (DEV-2026-153)**: A migration de service_orders quebrava no PostgreSQL 16 ao declarar a chave estrangeira parent_order_id para a própria tabela dentro do Schema::create. Separar a constraint em um bloco Schema::table logo após a criação da tabela resolveu o erro SQLSTATE[42830].

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-12, durante o php artisan migrate --force do 30-FieldFlow no PostgreSQL 16, a migration 2026_03_27_144054_create_service_orders_table.php falhou com SQLSTATE[42830]: there is no unique constraint matching given keys for referenced table "service_orders". Além disso, assigned_to usava foreignUuid apontando para users.id, que é BIGINT.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em database/migrations/2026_03_27_144054_create_service_orders_table.php, $table->uuid('id')->primary() e $table->foreignUuid('parent_order_id')->constrained('service_orders') no mesmo Schema::create geram o ALTER TABLE da FK antes de a constraint service_orders_pkey estar disponível para auto-referência no PostgreSQL 16.
* 💡 Declarar apenas a coluna $table->uuid('parent_order_id')->nullable() no Schema::create e adicionar $table->foreign('parent_order_id')->references('id')->on('service_orders')->nullOnDelete() em um Schema::table('service_orders') subsequente garante que a chave primária já exista no catálogo.
* 💡 Quando a tabela users usa $table->id() (BIGINT) e as tabelas de domínio usam UUID, referências a users.id precisam de foreignId('assigned_to') ou foreignId('user_id') em vez de foreignUuid, evitando SQLSTATE[42804] (incompatibilidade entre uuid e bigint).
* 💡 A ordem dos arquivos de migration precisa respeitar dependências: create_checklist_templates_table deve ter timestamp anterior a create_checklist_responses_table.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
Schema::create('service_orders', function (Blueprint $table) {
    $table->uuid('id')->primary();
    $table->uuid('parent_order_id')->nullable();
    $table->foreignId('assigned_to')->nullable()->constrained('users')->nullOnDelete();
});

Schema::table('service_orders', function (Blueprint $table) {
    $table->foreign('parent_order_id')
        ->references('id')
        ->on('service_orders')
        ->nullOnDelete();
});
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Todas as 14 migrations do ProntOS passaram a rodar de forma idempotente no PostgreSQL 16 sem falha de chave primária ou tipo de coluna.

* **Projetos Relacionados**: `30-FieldFlow`
* **Registro de Origem**: `_data/daily.dev-27.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
