---
layout: post
title: "Contraste vira teste que lê o CSS, e um tema novo não passa abaixo de 4,5:1"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-104"
description: "As telas da equipe pareciam legíveis, e a medição encontrou pares de texto bem abaixo do mínimo em todos os temas. O contraste passou a ser verificado na suíte de testes, tema a tema."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: frontend
tags: [acessibilidade, wcag, contraste, tokens, phpunit]
---

# Contraste vira teste que lê o CSS, e um tema novo não passa abaixo de 4,5:1

> [!NOTE]
> **Resumo Executivo (DEV-2026-104)**: As telas da equipe pareciam legíveis, e a medição encontrou pares de texto bem abaixo do mínimo em todos os temas. O contraste passou a ser verificado na suíte de testes, tema a tema.

---

### 🚨 O Desafio Técnico / Contexto
Etiquetas do tema claro estavam entre 2,66:1 e 3,83:1, e o texto branco sobre botão verde ou azul nos temas escuros ficava entre 1,6:1 e 4,06:1. No omnichannel-system, a mesma medição encontrou 14 pares abaixo do mínimo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O teste lê os tokens direto do CSS, então um tema novo entra na medição sem ajuste no teste, e a falha informa o par e a razão medida.
* 💡 Texto branco fixo sobre cor de acento quebra nos temas escuros. Os tokens --sobre-acento, --sobre-ok e --sobre-erro dão a cada tema o próprio texto sobre botão.
* 💡 O texto fraco era o pior caso: --tenue estava em 2,56:1. Listas vazias, rodapé e títulos de grupo passaram para --suave, porque essas partes também precisam ser lidas.
* 💡 No sistema Vue, os temas vêm de um mapeamento de paletas. A correção ficou em CONTRAST_OVERRIDES, e npm run check:contraste mede 18 pares nos 3 temas.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
foreach (self::PARES as [$frente, $fundo]) {
    $razao = self::razao($t[$frente], $t[$fundo]);
    $this->assertGreaterThanOrEqual(4.5, $razao, "--{$frente} sobre --{$fundo}: ".round($razao, 2).':1');
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O mínimo de 4,5:1 passou a ser conferido por teste, e uma cor nova abaixo dele não passa despercebida.

* **Projetos Relacionados**: `lorentz-atp`, `lorentz-cidadao`, `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
