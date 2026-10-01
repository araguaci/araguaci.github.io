---
layout: post
title: "Governança de Metadados e Prevenção de Erros 404 em Tag Clouds no Jekyll Estático"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-026"
description: "Estratégia de normalização taxonômica e criação de coleções seguras no Jekyll para evitar links quebrados em nuvens de tags geradas no GitHub Pages."
date: 2026-08-14 00:00:00+00:00
categories: devlog
category: devops
tags: [jekyll, metadata, taxonomy, safe-mode, github-pages]
---

# Governança de Metadados e Prevenção de Erros 404 em Tag Clouds no Jekyll Estático

> [!NOTE]
> **Resumo Executivo (DEV-2026-026)**: Estratégia de normalização taxonômica e criação de coleções seguras no Jekyll para evitar links quebrados em nuvens de tags geradas no GitHub Pages.

---

### 🚨 O Desafio Técnico / Contexto
No Safe Mode do GitHub Pages, a ausência de plugins de terceiros para criação automática de arquivos de tags gerava links para rotas inexistentes e erros 404 ao clicar em tags livres.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A definição de um arquivo canônico _featured_tags ou dicionário de whitelist garante que apenas tags com páginas de destino declaradas recebam hyperlinks.
* 💡 O filtro Liquid slugify: "latin" deve ser aplicado universalmente para uniformizar diacríticos e evitar falhas de codificação UTF-8 entre sistemas operacionais.
* 💡 Testes automatizados de integridade estática no CI detectam nós órfãos antes da sincronização dos builds.

---

### 🛠️ Especificação Técnica & Código-Chave
```html
<!-- Nuvem de tags resiliente com verificação de existência -->
{% for tag in site.tags %}
  {% assign tag_slug = tag[0] | slugify: "latin" %}
  {% if site.data.featured_tags contains tag_slug %}
    <a href="/tags/{{ tag_slug }}/" class="tag-badge">{{ tag[0] }} ({{ tag[1].size }})</a>
  {% else %}
    <span class="tag-badge tag-plain">{{ tag[0] }}</span>
  {% endif %}
{% endfor %}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Eliminação de 100% dos links quebrados em taxonomias de projetos e conformidade total com os padrões do GitHub Pages.

* **Projetos Relacionados**: `artesdosul`, `araguaci.github.io`
* **Registro de Origem**: `_data/daily.dev-02.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
