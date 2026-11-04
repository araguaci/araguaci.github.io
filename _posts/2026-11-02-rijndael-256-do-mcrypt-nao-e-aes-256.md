---
layout: post
title: "Rijndael-256 do mcrypt não é AES-256, e o porte para PHP 8 deixou de abrir as senhas"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-100"
description: "O porte para PHP 8 trocou a cifra do mcrypt por AES-256-CBC, supondo que fossem equivalentes, e as senhas gravadas deixaram de abrir. O novo critério é gerar o mesmo texto, byte a byte, em todos os runtimes em uso."
date: 2026-11-02 00:00:00-03:00
categories: devlog
category: seguranca
tags: [php, mcrypt, phpseclib, criptografia, dotnet, compatibilidade]
---

# Rijndael-256 do mcrypt não é AES-256, e o porte para PHP 8 deixou de abrir as senhas

> [!NOTE]
> **Resumo Executivo (DEV-2026-100)**: O porte para PHP 8 trocou a cifra do mcrypt por AES-256-CBC, supondo que fossem equivalentes, e as senhas gravadas deixaram de abrir. O novo critério é gerar o mesmo texto, byte a byte, em todos os runtimes em uso.

---

### 🚨 O Desafio Técnico / Contexto
Sem o mcrypt no PHP 8, a migração adotou AES-256-CBC, e o login com as senhas existentes parou de funcionar. O inventário das bases mostrou que quase todas as senhas estavam no formato antigo e nenhuma no novo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O 256 de MCRYPT_RIJNDAEL_256 é o tamanho do bloco. O AES tem sempre bloco de 128 bits, e o 256 de AES-256 é o tamanho da chave. São algoritmos diferentes.
* 💡 O OpenSSL do PHP não oferece bloco de 256 bits. phpseclib 2.x é código puro e roda do PHP 5.6 ao 8.x. No .NET moderno, o caminho é BouncyCastle.
* 💡 Quando o outro lado compara o texto cifrado, 'decifra igual' não basta. O critério é o mesmo Base64 byte a byte em PHP 5.6, PHP 8, .NET 4.8 e .NET 9.
* 💡 O mcrypt real continua sendo a referência: uma imagem Docker de PHP 5.6 gera os vetores que os novos implementadores precisam reproduzir.
* 💡 A conferência das bases roda em memória e só devolve contagens. Senha de cliente não vai para arquivo, nem durante um diagnóstico.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// Bloco de 256 bits, ausente no OpenSSL do PHP
$c = new \phpseclib\Crypt\Rijndael(\phpseclib\Crypt\Rijndael::MODE_CBC);
$c->setBlockLength(256);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A correção do login ganhou um critério verificável, e o legado em produção fica protegido de outra troca de formato.

* **Projetos Relacionados**: `omnichannel`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
