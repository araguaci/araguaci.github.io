# -*- coding: utf-8 -*-
"""
Utilitário de Ingestão e Publicação: Converte _data/daily.dev-*.yml em Posts Jekyll (_posts/)
Repositório: D:\app_aragua\araguaci.github.io
Entrada: python diario_dev.py importar [arquivo|all]
Roteiro: docs/roteiro-automacao-diario-dev.md
"""

import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '_data')
POSTS_DIR = os.path.join(BASE_DIR, '_posts')

def detect_language(snippet):
    s = snippet.strip()
    if s.startswith('<?php') or (s.startswith('function ') and '$' in s):
        return 'php'
    if s.startswith('# -*-') or 'def ' in s or 'import ' in s or 'print(' in s or 'subprocess.' in s:
        return 'python'
    if 'network_mode:' in s or '\nservices:' in s or s.startswith('services:'):
        return 'yaml'
    if s.startswith('--') or 'INSERT INTO' in s or 'SHOW GLOBAL' in s:
        return 'sql'
    if s.startswith(';') or s.startswith('deny=') or '[Dirs]' in s:
        return 'ini'
    if 'DirectoryIndex' in s:
        return 'apache'
    if s.startswith(('<svg', '<div', '<!--', '<a ', '<span')) or '</svg>' in s or 'viewBox=' in s:
        return 'html'
    if 'void ' in s or '#include' in s or 'xTaskCreate' in s or 'esp_now' in s or 'Queue' in s or 'portMAX_DELAY' in s:
        return 'cpp'
    if 'const ' in s or 'function ' in s or 'addEventListener' in s or 'let ' in s or '=>' in s or 'Math.cos' in s or 'document.' in s:
        return 'javascript'
    if ('grid-template' in s or 'display:' in s or 'backdrop-filter:' in s or '@media' in s) and '{' in s:
        return 'css'
    if s.startswith('{') or '"mcpServers"' in s:
        return 'json'
    if s.startswith('#!') or './scripts/' in s or 'ufw ' in s or 'docker ' in s or 'git ' in s or 'readlink' in s or 'php artisan' in s or 'php scripts/' in s or 'asterisk ' in s:
        return 'bash'
    if 'network_mode:' in s or s.startswith('services:'):
        return 'yaml'
    return 'yaml'

def load_file(filename):
    try:
        import yaml
        full_path = os.path.join(DATA_DIR, filename) if not os.path.isabs(filename) else filename
        if not os.path.exists(full_path):
            print(f"Arquivo não encontrado: {full_path}")
            return []
        with open(full_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            entries = data.get('entries', [])
            return [(e, os.path.basename(full_path)) for e in entries]
    except ImportError:
        print("Módulo pyyaml não encontrado. Instale com 'pip install pyyaml'.")
        return []

def run_import(target_file=None):
    entries_with_source = []
    
    if target_file and target_file != 'all':
        entries_with_source.extend(load_file(target_file))
    else:
        pattern = os.path.join(DATA_DIR, 'daily.dev-*.yml')
        for f in sorted(glob.glob(pattern)):
            entries_with_source.extend(load_file(f))

    if not entries_with_source:
        print("Nenhuma entrada localizada para importação.")
        return

    print(f"=== INICIANDO IMPORTAÇÃO DE APRENDIZADOS DE DEV ===")
    print(f"Total de registros a processar: {len(entries_with_source)}")
    os.makedirs(POSTS_DIR, exist_ok=True)

    created_count = 0
    updated_count = 0

    for e, source_filename in entries_with_source:
        tags_str = ", ".join(e.get('tags', []))
        learnings_list = "\n".join([f"* 💡 {k}" for k in e.get('key_learnings', [])])
        
        snippet = e.get('code_snippet', '')
        code_block = ""
        if snippet:
            lang = detect_language(snippet)
            code_block = f"```{lang}\n{snippet.strip()}\n```"

        related = ", ".join([f"`{p}`" for p in e.get('related_projects', [])])

        post_md = f"""---
layout: post
title: "{e.get('title')}"
subtitle: "Diário de Desenvolvimento 2026 • Registro #{e.get('id')}"
description: "{e.get('summary')}"
date: {e.get('date')} 00:00:00+00:00
categories: devlog
category: {e.get('category')}
tags: [{tags_str}]
---

# {e.get('title')}

> [!NOTE]
> **Resumo Executivo ({e.get('id')})**: {e.get('summary')}

---

### 🚨 O Desafio Técnico / Contexto
{e.get('problem_statement', '').strip()}

---

### 💡 Principais Lições Aprendidas & Descobertas
{learnings_list}

---

### 🛠️ Especificação Técnica & Código-Chave
{code_block}

---

### 📈 Impacto no Ecossistema & Valor Prático
{e.get('impact_value', '')}

* **Projetos Relacionados**: {related}
* **Registro de Origem**: `_data/{source_filename}`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
"""
        filename = f"{e['date']}-{e['slug']}.md"
        dest_path = os.path.join(POSTS_DIR, filename)
        is_new = not os.path.exists(dest_path)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(post_md)
        
        if is_new:
            created_count += 1
            print(f"[NOVO] _posts/{filename}")
        else:
            updated_count += 1
            print(f"[ATUALIZADO] _posts/{filename}")

    print(f"\nImportação concluída com sucesso!")
    print(f"Novos artigos gerados: {created_count}")
    print(f"Artigos atualizados: {updated_count}")
    print(f"Total processado: {len(entries_with_source)}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    run_import(target)
