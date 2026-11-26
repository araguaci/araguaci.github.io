---
layout: post
title: "PHP 5.4 recusa expressão em parâmetro por referência do IssabelPBX"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-183"
description: "O script de ramais funcionava ao criar e quebrava ao atualizar um ramal existente. A função q() do IssabelPBX recebe o valor por referência, e o caminho de atualização passava uma concatenação."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [php, issabel, legado]
---

# PHP 5.4 recusa expressão em parâmetro por referência do IssabelPBX

> [!NOTE]
> **Resumo Executivo (DEV-2026-183)**: O script de ramais funcionava ao criar e quebrava ao atualizar um ramal existente. A função q() do IssabelPBX recebe o valor por referência, e o caminho de atualização passava uma concatenação.

---

### 🚨 O Desafio Técnico / Contexto
issabel-extensions-batch.php cria ou atualiza ramais chan_sip. Na segunda rodada, com os ramais já criados, deu "Cannot pass parameter 1 by reference". A primeira suspeita foi a função sql(), e a mudança nela não resolveu. A causa era q(&$value), que escapa valores para o SQL, chamada com q('SIP/' . $ext) no UPDATE de devices. O mesmo script é usado pelos sincronizadores de ramais da VPS, que também quebravam ao atualizar.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Função que declara &$param exige variável. Literal ou concatenação passa no php -l e só falha quando a linha roda.
* 💡 Testar só a criação deixa o caminho de atualização sem prova. A segunda rodada do deploy foi o teste que faltava.
* 💡 Antes de mudar a função suspeita, ler a assinatura das que estão na mesma linha. Aqui a suspeita errada custou uma rodada.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
$dial = 'SIP/' . $ext;  // q() é function q(&$value)
sql("UPDATE devices SET dial = " . q($dial) . " WHERE id = " . q($ext));
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Atualizar um ramal existente voltou a funcionar no laboratório e nos sincronizadores da VPS.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
