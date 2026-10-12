---
layout: post
title: "Jekyll ignora posts criados diretamente na pasta de build docs"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-077"
description: "Arquivos markdown gravados diretamente no diretório docs/ poluem a pasta de build e não entram no pipeline de coleções do Jekyll. A publicação exige arquivos canônicos em _posts/ com data no prefixo e permalinks por categoria antes do build e do sync FTP."
date: 2026-10-12 00:00:00+00:00
categories: devlog
category: devops
tags: [jekyll, build, markdown, ftp, static-site]
---

# Jekyll ignora posts criados diretamente na pasta de build docs

> [!NOTE]
> **Resumo Executivo (DEV-2026-077)**: Arquivos markdown gravados diretamente no diretório docs/ poluem a pasta de build e não entram no pipeline de coleções do Jekyll. A publicação exige arquivos canônicos em _posts/ com data no prefixo e permalinks por categoria antes do build e do sync FTP.

---

### 🚨 O Desafio Técnico / Contexto
Quatro artigos temáticos haviam sido gravados como arquivos markdown avulsos dentro do diretório docs/, que atua como pasta de saída configurada em _config.yml (destination: docs). Como consequência, o Jekyll não reconhecia os documentos como posts da coleção, não gerava as tags de metadados nem os permalinks canônicos.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O diretório docs/ é área de compilação efêmera; arquivos fonte devem ficar em _posts/ para receber layout e permalink.
* 💡 A nomenclatura de posts no Jekyll exige o padrão YYYY-MM-DD-slug.md para alimentar a engine de datas e categorias.
* 💡 Com permalink definido como :categories/:title/, o Jekyll gera subdiretórios semânticos automáticos na pasta de build.
* 💡 O script de sincronização FTP que compara st_size local e ftp.size remoto evita tráfego inútil de milhares de arquivos.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# 1. Fonte canônica em _posts com taxonomia
# _posts/estudos/2026-10-11-ciclos-do-brasil.md
# 2. Build para a pasta de saída configurada
bundle exec jekyll build
# 3. Deploy seletivo comparando st_size local com ftp.size remoto
python scripts/sync_ftp.py
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Padronização do fluxo de publicação em _posts/ garantindo integridade de rotas, SEO e sincronização FTP sem sujeira na área de build.

* **Projetos Relacionados**: `artesdosul`
* **Registro de Origem**: `_data/daily.dev-14.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
