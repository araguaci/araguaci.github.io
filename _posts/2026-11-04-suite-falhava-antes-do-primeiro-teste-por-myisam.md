---
layout: post
title: "A suíte falhava antes do primeiro teste, porque o MySQL local usa MyISAM por padrão"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-106"
description: "Das 196 execuções, 192 falhavam com 'key too long', e por isso a suíte não dizia nada sobre o código. Com o motor declarado, ela voltou a rodar e mostrou 64 falhas que já existiam."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [mysql, myisam, innodb, laravel, phpunit]
---

# A suíte falhava antes do primeiro teste, porque o MySQL local usa MyISAM por padrão

> [!NOTE]
> **Resumo Executivo (DEV-2026-106)**: Das 196 execuções, 192 falhavam com 'key too long', e por isso a suíte não dizia nada sobre o código. Com o motor declarado, ela voltou a rodar e mostrou 64 falhas que já existiam.

---

### 🚨 O Desafio Técnico / Contexto
O servidor MySQL local tem MyISAM como padrão, e o limite de chave desse motor derrubava as migrations antes de qualquer teste. Ao mudar para InnoDB, apareceu o erro 1824, porque migrations antigas referenciam tabelas criadas depois delas.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Declare o motor em config/database.php, com env('DB_ENGINE', 'InnoDB'). Transação de teste e chave estrangeira dependem dele, então o padrão do servidor não pode decidir.
* 💡 MyISAM aceita a declaração de chave estrangeira e não a aplica. A base de dev antiga continua sem essa proteção até ser recriada.
* 💡 Os eventos MigrationsStarted e MigrationsEnded desligam a checagem de chave estrangeira durante as migrations. É uma solução provisória, e o certo é corrigir a ordem.
* 💡 Antes de atribuir uma falha à entrega, compare com a base: rodar o main numa worktree temporária deu as mesmas 64 falhas, teste a teste, nenhuma nova.
* 💡 Suíte que nunca roda dá falsa segurança: as 64 falhas estavam ali, escondidas pelo erro de configuração.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
Event::listen(MigrationsStarted::class, fn () => Schema::disableForeignKeyConstraints());
Event::listen(MigrationsEnded::class, fn () => Schema::enableForeignKeyConstraints());
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A suíte voltou a rodar em cerca de 1 minuto, com 152 de 216 testes passando e uma lista real do que corrigir.

* **Projetos Relacionados**: `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
