---
layout: post
title: "O conversor de PHP 5.6 para 8 reescreve trechos que o PHP 8 recusa"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-145"
description: "O lote php5-to-php8.php aplica o que a leitura arquivo a arquivo deixava passar. Parte da reescrita quebra no PHP 8, e uma regra pelo nome each também pegaria JavaScript."
date: 2026-10-29 00:00:00-03:00
categories: devlog
category: backend
tags: [php, php8, migracao, supervisor]
---

# O conversor de PHP 5.6 para 8 reescreve trechos que o PHP 8 recusa

> [!NOTE]
> **Resumo Executivo (DEV-2026-145)**: O lote php5-to-php8.php aplica o que a leitura arquivo a arquivo deixava passar. Parte da reescrita quebra no PHP 8, e uma regra pelo nome each também pegaria JavaScript.

---

### 🚨 O Desafio Técnico / Contexto
corrige_php8.php percorre o Supervisor legado para tirar construções do PHP 5.6. each() saiu do PHP 8. implode com a lista no primeiro argumento vira TypeError. count() em string ou null derruba a página. O operador ?? dentro do argumento de ew_AddMessage cria um temporário, e o PHP 8 recusa temporário em parâmetro por referência.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 while (list($k, $v) = each($a)) vira foreach ($a as $k => $v). A troca não pode alcançar .each( de JavaScript. Outro each() fica marcado para revisão manual.
* 💡 implode($lista, ',') é TypeError no PHP 8. A ordem passa a ser separador e depois lista. implode($sep, $lista) fica quieto, porque o segundo argumento não é texto fixo.
* 💡 count() global vira acount() em userfn9.php. $obj->count() e o count() de dentro da própria acount() ficam de fora.
* 💡 ew_AddMessage(($_SESSION[...] ?? null), $v) não compila no PHP 8. O conversor garante a chave com string vazia e passa a variável de sessão.
* 💡 define($nome, $valor, TRUE) perde o terceiro argumento no PHP 8. O conversor grava define com dois argumentos.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if (!isset($_SESSION[$chave])) {
    $_SESSION[$chave] = "";
}
ew_AddMessage($_SESSION[$chave], $v);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O lote deixa de gerar TypeError, aviso de referência e reescrita de JavaScript, e o que não cabe na regra fica para revisão manual.

* **Projetos Relacionados**: `supervisor`
* **Registro de Origem**: `_data/daily.dev-24.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
