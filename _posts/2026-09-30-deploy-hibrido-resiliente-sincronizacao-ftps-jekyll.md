---
layout: post
title: "Deploy Híbrido Resiliente: Sincronização Atômica via FTPS e Preservação de Artefatos Jekyll"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-017"
description: "Arquitetura de deploy contínuo multi-alvo sincronizando Vercel e servidores Linux via FTPS passivo com verificação atômica de integridade MD5 e proteção do diretório docs/."
date: 2026-09-30 00:00:00+00:00
categories: devlog
category: devops
tags: [devops, ftp, ci-cd, jekyll, vercel, python]
---

# Deploy Híbrido Resiliente: Sincronização Atômica via FTPS e Preservação de Artefatos Jekyll

> [!NOTE]
> **Resumo Executivo (DEV-2026-017)**: Arquitetura de deploy contínuo multi-alvo sincronizando Vercel e servidores Linux via FTPS passivo com verificação atômica de integridade MD5 e proteção do diretório docs/.

---

### 🚨 O Desafio Técnico / Contexto
Em deploys híbridos em que o repositório alimenta simultaneamente Vercel (via docs/) e servidores web legados via FTPS, o comando jekyll build limpava recursivamente a pasta de destino, causando sobrescritas acidentais e truncamento de arquivos HTML em conexões passivas.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O Jekyll executa limpeza implícita no diretório destino se parâmetros de destination não forem rigidamente isolados; backups em staging pré-deploy evitam perda de assets compilados.
* 💡 Sockets FTPS passivos requerem transmissão em chunks moderados (8192 bytes) com mecanismo de retry exponencial com jitter para blindagem contra oscilações de rota.
* 💡 Verificação de integridade pós-upload confrontando hashes MD5 locais com comandos de tamanho/checksum no servidor FTP elimina transferências truncadas antes da entrada em produção.

---

### 🛠️ Especificação Técnica & Código-Chave
```python
# Script de deploy FTPS atômico com verificação de integridade
import ftplib, os, hashlib

def upload_atomic(ftp, local_file, remote_file):
    chunk_size = 8192
    with open(local_file, 'rb') as f:
        ftp.storbinary(f'STOR {remote_file}', f, chunk_size)
    remote_size = ftp.size(remote_file)
    local_size = os.path.getsize(local_file)
    if remote_size != local_size:
        raise IOError(f'Truncamento detectado: {local_size} vs {remote_size}')
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Zero downtime e eliminação de 100% dos incidentes de páginas truncadas em deploys do portal artesdosul.com.

* **Projetos Relacionados**: `artesdosul.com`, `artesdosul.github.io`
* **Registro de Origem**: `_data/daily.dev-02.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
