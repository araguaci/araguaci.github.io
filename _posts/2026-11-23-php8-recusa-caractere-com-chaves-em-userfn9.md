---
layout: post
title: "O PHP 8 recusa o acesso a caractere com chaves em userfn9.php"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-172"
description: "Este checkout do Supervisor ainda é interpretado. A partir do PHP 8.0 a leitura de caractere com chaves deixou de existir, e userfn9.php ainda usa essa forma numa função de depuração."
date: 2026-11-23 00:00:00-03:00
categories: devlog
category: backend
tags: [php, legado]
---

# O PHP 8 recusa o acesso a caractere com chaves em userfn9.php

> [!NOTE]
> **Resumo Executivo (DEV-2026-172)**: Este checkout do Supervisor ainda é interpretado. A partir do PHP 8.0 a leitura de caractere com chaves deixou de existir, e userfn9.php ainda usa essa forma numa função de depuração.

---

### 🚨 O Desafio Técnico / Contexto
print_r_tree testa se a string começa com { para então decodificar JSON. A condição usa $var{0}. O PHP 8.0 removeu esse acesso. O conversor já registrado trata each, implode e referência; esta linha não entrou naquele artigo. O interpretador que valida e serve este checkout é o PHP 5.6.40.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A linha está em userfn9.php, dentro de print_r_tree, por volta da 2107: is_string($var) && $var{0}=='{'. Não é uma tela de negócio. Qualquer include que passe por userfn9 chega nela.
* 💡 No PHP 8 a forma aceita é $var[0]. Enquanto o arquivo não for reescrito, o vhost deste checkout permanece no PHP 5.6.40.
* 💡 Não misturar com o artigo do conversor. Aquele reescreve each, implode e passagem por referência. Este é um offset de string que ficou de fora.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if (is_string($var) && $var{0}=='{' && !is_null($var2 = json_decode($var, true))) {
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O checkout elevado continua no PHP 5.6.40, e a página deixa de morrer na função de depuração.

* **Projetos Relacionados**: `supervisor-elevar-legado`
* **Registro de Origem**: `_data/daily.dev-32.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
