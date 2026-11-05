---
layout: post
title: "MySQL, PostgreSQL ou SQLite: nos meus projetos quase nada dependia do banco, e o teste no banco errado é o risco real"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-125"
description: "A escolha do banco parecia uma decisão de desempenho, sem nenhuma medição por trás. A busca no código mostrou quase nenhum recurso exclusivo, então passou a valer o padrão MySQL com InnoDB, PostgreSQL só com motivo e SQLite fora da produção."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [mysql, postgres, sqlite, postgis, laravel, testes]
---

# MySQL, PostgreSQL ou SQLite: nos meus projetos quase nada dependia do banco, e o teste no banco errado é o risco real

> [!NOTE]
> **Resumo Executivo (DEV-2026-125)**: A escolha do banco parecia uma decisão de desempenho, sem nenhuma medição por trás. A busca no código mostrou quase nenhum recurso exclusivo, então passou a valer o padrão MySQL com InnoDB, PostgreSQL só com motivo e SQLite fora da produção.

---

### 🚨 O Desafio Técnico / Contexto
Os projetos usam MySQL, PostgreSQL e SQLite. Busquei recursos exclusivos de cada banco e encontrei quase nada: dialeto de MySQL entre zero e duas ocorrências por projeto, nenhuma busca textual do PostgreSQL e nenhum vetor. A exceção é um sistema com PostGIS e JSONB. Vários projetos usam MySQL no ambiente e SQLite em memória nos testes.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 MySQL 8 com InnoDB: bom padrão para sistema transacional multiempresa em banco compartilhado. Importou 147 mil pagamentos em 39 segundos dentro de uma transação. A armadilha é o padrão MyISAM de ambientes locais, que ignora o rollback sem avisar.
* 💡 PostgreSQL: vale quando o domínio pede o recurso. Consulta geográfica com PostGIS e JSONB são motivos concretos. Preferência sem recurso não é motivo.
* 💡 SQLite em memória: bom para protótipo e para rodar testes sem instalar nada. O risco é aprovar em um motor o que vai rodar em outro. Quando o esquema usa enum e DEFAULT com expressão, a suíte precisa rodar no banco de produção.
* 💡 Não concluí qual é mais rápido. A mesma suíte levou 146 segundos em uma rodada e 44 na seguinte, então a carga da máquina pesou mais que o banco.
* 💡 Suíte vermelha com SQLite não prova culpa do banco. As 11 falhas que investiguei vinham de um erro no layout, que transformava respostas 403 em 500.

---

### 🛠️ Especificação Técnica & Código-Chave
```html
<!-- phpunit.xml: o mesmo motor da produção, em um banco só de teste -->
<env name="DB_CONNECTION" value="mysql"/>
<env name="DB_DATABASE" value="app_test"/>
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A decisão de banco passou a ter uma pergunta só: qual recurso deste domínio o padrão não atende.

* **Projetos Relacionados**: `monitor-laravel`, `05-orcamento`, `lorentz-cidadao`, `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
