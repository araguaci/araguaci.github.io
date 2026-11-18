---
layout: post
title: "Em demo, a base de demonstração deixa de recusar e apaga os dados"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-151"
description: "A instância de apresentação ficou em demo para aceitar a base fictícia. Nesse ambiente o comando que a produção recusa roda, e o do ATP recria o banco do zero."
date: 2026-11-05 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, artisan, app-env, demo]
---

# Em demo, a base de demonstração deixa de recusar e apaga os dados

> [!NOTE]
> **Resumo Executivo (DEV-2026-151)**: A instância de apresentação ficou em demo para aceitar a base fictícia. Nesse ambiente o comando que a produção recusa roda, e o do ATP recria o banco do zero.

---

### 🚨 O Desafio Técnico / Contexto
ATP_APP_ENV e CIDADAO_APP_ENV no .env da stack definem o APP_ENV. O padrão continua production, que recusa atp:base-demo e cidadao:base-demo. Em demo essa recusa não dispara.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 atp:base-demo, em lorentz-atp/app/Console/Commands/BaseDemo.php, só retorna falha quando environment('production'). Fora isso chama migrate:fresh e db:seed. A opção --force pula a pergunta.
* 💡 cidadao:base-demo recusa do mesmo jeito, só em production. Com --limpar executa TRUNCATE de request_events, notifications, requests e citizens.
* 💡 scripts/render-laravel-apps.py é quem leva ATP_APP_ENV e CIDADAO_APP_ENV para o APP_ENV do container. Apagar as duas chaves e recriar os containers devolve o padrão production.
* 💡 Enquanto a chave estiver em demo, dado real não entra nessa instância. Um base-demo apaga o que estiver no banco.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
if ($this->laravel->environment('production')) {
    $this->error('Recusado: APP_ENV=production. A base de demonstração apaga todos os dados.');
    return self::FAILURE;
}
$this->call('migrate:fresh', ['--force' => true]);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Instância em demo ficou marcada como lugar sem dado real, e a volta ao padrão passa por apagar as duas chaves e recomeçar com base vazia.

* **Projetos Relacionados**: `lorentz-atp`, `lorentz-cidadao`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-26.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
