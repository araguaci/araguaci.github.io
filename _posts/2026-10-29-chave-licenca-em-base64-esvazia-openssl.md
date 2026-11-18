---
layout: post
title: "Tratar a chave da licença como Base64 faz o OpenSSL devolver texto vazio"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-144"
description: "A página da licença voltava vazia. A chave e o IV são texto puro, e o código os decodificava como Base64 antes do AES. O OpenSSL recusava o material e a função devolvia string vazia."
date: 2026-10-29 00:00:00-03:00
categories: devlog
category: seguranca
tags: [php, openssl, licenca, aes, php8]
---

# Tratar a chave da licença como Base64 faz o OpenSSL devolver texto vazio

> [!NOTE]
> **Resumo Executivo (DEV-2026-144)**: A página da licença voltava vazia. A chave e o IV são texto puro, e o código os decodificava como Base64 antes do AES. O OpenSSL recusava o material e a função devolvia string vazia.

---

### 🚨 O Desafio Técnico / Contexto
O porte da licença para OpenSSL aplicava base64_decode na chave e no IV. Os dois são texto puro, com tamanho ajustado na hora do uso. openssl_encrypt devolvia false, e encrypt transformava esse false em string vazia. Sem o texto cifrado, a leitura da licença não tinha o que mostrar.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A chave e o IV da licença entram crus no OpenSSL. base64_decode neles troca o material e o AES-256-CBC falha.
* 💡 licencaAesMaterial corta a chave em 32 bytes e o IV em 16. AES-256 pede chave desse tamanho, e o CBC pede IV de 16 bytes.
* 💡 encrypt e decrypt devolvem string vazia quando o OpenSSL retorna false. A página fica em branco, sem exceção.
* 💡 O Base64 continua só no texto cifrado, na ida e na volta. Isso é outro caminho do que o Rijndael de bloco 256 usado nas senhas de usuário.

---

### 🛠️ Especificação Técnica & Código-Chave
```php
function licencaAesMaterial($key, $iv) {
    return array(substr((string) $key, 0, 32), substr((string) $iv, 0, 16));
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A licença volta a cifrar e a abrir no PHP 8, com a chave usada como texto e o Base64 só no resultado.

* **Projetos Relacionados**: `supervisor`
* **Registro de Origem**: `_data/daily.dev-24.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
