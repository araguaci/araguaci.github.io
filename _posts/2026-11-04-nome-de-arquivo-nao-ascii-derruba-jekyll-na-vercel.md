---
layout: post
title: "Nome de arquivo com travessão derruba o Jekyll na Vercel, e o Windows não mostra o erro"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-109"
description: "O build passava no Windows e falhava na Vercel, por causa de um arquivo estático com caractere fora do ASCII no nome. Uma variável de ambiente resolveu sem mudar nenhuma URL pública."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [jekyll, vercel, utf-8, locale, ruby]
---

# Nome de arquivo com travessão derruba o Jekyll na Vercel, e o Windows não mostra o erro

> [!NOTE]
> **Resumo Executivo (DEV-2026-109)**: O build passava no Windows e falhava na Vercel, por causa de um arquivo estático com caractere fora do ASCII no nome. Uma variável de ambiente resolveu sem mudar nenhuma URL pública.

---

### 🚨 O Desafio Técnico / Contexto
O jekyll build na Vercel parou com a mensagem "\xE2" from ASCII-8BIT to UTF-8 em um arquivo estático com travessão no nome. O mesmo build funcionava na máquina Windows, e renomear o arquivo mudaria uma URL já publicada.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O byte xE2 é o início do travessão em UTF-8, e ASCII-8BIT mostra que o Ruby leu o nome do arquivo sem encoding definido.
* 💡 LC_ALL=C.UTF-8 no projeto da Vercel dá o locale que o ambiente de build não define.
* 💡 Ajustar o ambiente preserva as URLs públicas. Renomear o arquivo resolveria o erro, mas quebraria quem já tem o link.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Variável de ambiente do projeto na Vercel
LC_ALL=C.UTF-8
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O build voltou a passar na Vercel sem mudar nenhum endereço publicado.

* **Projetos Relacionados**: `artesdosul`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
