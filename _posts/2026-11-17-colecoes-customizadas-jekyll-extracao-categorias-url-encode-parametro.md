---
layout: post
title: "Coleções customizadas no Jekyll exigem extração manual de categorias e url_encode isolado no parâmetro"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-160"
description: "Páginas de categorias e tags baseadas em site.categories e site.tags ficavam vazias num projeto Jekyll cuja base de dados residia na coleção site.anuncios, além de gerarem URLs quebradas por serialização de array e encadeamento incorreto de url_encode. A migração para agregação direta sobre site.anuncios com extração do primeiro item da categoria e codificação restrita ao valor da query string restaurou toda a navegação e indexação."
date: 2026-11-17 00:00:00-03:00
categories: devlog
category: frontend
tags: [jekyll, liquid, seo, schema-org, css-variables, static-site]
---

# Coleções customizadas no Jekyll exigem extração manual de categorias e url_encode isolado no parâmetro

> [!NOTE]
> **Resumo Executivo (DEV-2026-160)**: Páginas de categorias e tags baseadas em site.categories e site.tags ficavam vazias num projeto Jekyll cuja base de dados residia na coleção site.anuncios, além de gerarem URLs quebradas por serialização de array e encadeamento incorreto de url_encode. A migração para agregação direta sobre site.anuncios com extração do primeiro item da categoria e codificação restrita ao valor da query string restaurou toda a navegação e indexação.

---

### 🚨 O Desafio Técnico / Contexto
No projeto Jekyll Classificados Bombinhas (classibombinhas.com.br), os 124 registros de estabelecimentos e serviços estavam armazenados na coleção _anuncios (site.anuncios), sem arquivos em _posts. Como os layouts categories.html e tags.html iteravam sobre site.categories e site.tags — objetos que o Jekyll popula exclusivamente a partir de site.posts —, as rotas /categories, /tags e /tag renderizavam vazias. Adicionalmente, ao referenciar page.categories ou anuncio.categories diretamente em links e blocos case do Liquid, o Jekyll devolvia um array de um elemento (ex.: ["webdesigner"]), gerando URLs como /categories?cat=%5B%22webdesigner%22%5D, enquanto o filtro encadeado '/tag?t=' | append: t | url_encode codificava o caminho inteiro para /%2Ftag%3Ft=Valor. Por fim, a presença de jekyll-archives em _config.yml quebrava o build quando executado fora do bundle que continha a gem opcional.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 No Jekyll, site.categories e site.tags indexam apenas site.posts; projetos baseados em collections customizadas (como site.anuncios) precisam agregar categorias e tags iterando diretamente sobre a coleção com where e uniq.
* 💡 A chave categories no frontmatter de um item de coleção é desserializada como lista mesmo quando declarada como string simples; usar anuncio.categories | first | default: anuncio.categories garante uma string limpa para comparações e URLs.
* 💡 Filtros Liquid executam da esquerda para a direita: aplicar url_encode após append na rota ('/tag?t=' | append: t | url_encode) escapa também a barra e o ponto de interrogação; o filtro deve incidir somente sobre o parâmetro ({{ '/tag' | relative_url }}?t={{ t | url_encode }}).
* 💡 Para evitar Flash of Unstyled Content (FOUC) em sites estáticos multi-página com temas dinâmicos, o snapshot de variáveis CSS salvo em localStorage deve ser reaplicado por um script inline síncrono no <head> antes da folha de estilos principal.

---

### 🛠️ Especificação Técnica & Código-Chave
```json
{% assign cat_slug = anuncio.categories | first | default: anuncio.categories %}
{% assign uniq_tags = anuncio.tags | uniq %}
<a href="{{ '/categories' | relative_url }}?cat={{ cat_slug }}">{{ cat_name }}</a>
{% for t in uniq_tags %}
  <a href="{{ '/tag' | relative_url }}?t={{ t | url_encode }}">#{{ t }}</a>
{% endfor %}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O portal classibombinhas.com.br passou a indexar 124 anúncios em 14 categorias e 98 tags sem links quebrados, com busca global por atalhos (/ e Ctrl+Espaço), 5 temas dinâmicos sem FOUC e grafo Schema.org JSON-LD validado.

* **Projetos Relacionados**: `classibombinhas.com.br`, `artesdosul`
* **Registro de Origem**: `_data/daily.dev-29.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
