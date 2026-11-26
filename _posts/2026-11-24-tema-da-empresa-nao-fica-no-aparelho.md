---
layout: post
title: "O tema da empresa não pode ficar no aparelho, e o script antigo continua escolhendo sozinho"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-173"
description: "Cada pessoa guardava a cor no próprio navegador, e um script em cache mantinha a escolha velha depois da publicação. A cor passou a ser a da empresa, e o endereço do script leva a versão para o navegador buscar o arquivo novo."
date: 2026-11-24 00:00:00-03:00
categories: devlog
category: frontend
tags: [laravel, css, tema, cache, localstorage]
---

# O tema da empresa não pode ficar no aparelho, e o script antigo continua escolhendo sozinho

> [!NOTE]
> **Resumo Executivo (DEV-2026-173)**: Cada pessoa guardava a cor no próprio navegador, e um script em cache mantinha a escolha velha depois da publicação. A cor passou a ser a da empresa, e o endereço do script leva a versão para o navegador buscar o arquivo novo.

---

### 🚨 O Desafio Técnico / Contexto
A tela logada precisa da mesma aparência para quem entra naquela empresa. localStorage cumpre isso num aparelho só. O arquivo theme.js ia sem versão na URL, então o navegador seguia com a cópia antiga. Gráfico já desenhado também não troca de paleta sozinho.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A coluna é companies.theme, string de 40, na migration 2026_11_24_000800_add_theme_to_companies.php. Appearance::forUser lê a empresa do usuário e, se o valor não está em Appearance::THEMES, devolve atp.
* 💡 O layout logado marca html com data-theme-source=company. Em theme.js, boot() volta nesse caso e não lê a chave app_theme. set() também não grava localStorage quando a origem é a empresa. A entrada usa data-theme-source=device e continua no aparelho.
* 💡 O script entra no head, sem defer, como /js/theme.js?v= e config('app.version'). O mesmo vale para reading.js, sidebar.js e theme.css. Sem a consulta, a publicação nova continua rodando o arquivo que o navegador já tinha.
* 💡 A troca chama PUT /settings/appearance, atrás do middleware supervisor, e devolve JSON com o tema gravado. Se Chart.instances tem gráfico, theme.js recarrega a página: a instância não se repinta com o dataset novo.
* 💡 Appearance::FEATURED deixa três temas à vista (atp, lorentz-dark, auto). O restante fica em Mais opções. O monitor recebe 403 nessa rota.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if (root.dataset.themeSource === 'company') return root.dataset.themeChoice || 'atp';
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Quem entra na empresa vê a cor gravada nela, e a publicação nova não fica presa no script antigo.

* **Projetos Relacionados**: `monitoramento-app`
* **Registro de Origem**: `_data/daily.dev-33.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
