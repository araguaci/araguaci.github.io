# -*- coding: utf-8 -*-
"""
Diário de Desenvolvimento — importar, exportar, validar.

  python diario_dev.py indice
  python diario_dev.py exportar-posts
  python diario_dev.py validar _data/daily.dev-04.yml
  python diario_dev.py proximo
  python diario_dev.py novo
  python diario_dev.py importar _data/daily.dev-04.yml
  python diario_dev.py verificar

Roteiro: docs/roteiro-automacao-diario-dev.md
Modelos: _data/templates/
"""

import glob
import os
import re
import sys
from datetime import date

import yaml

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '_data')
POSTS_DIR = os.path.join(BASE_DIR, '_posts')
EXPORT_DIR = os.path.join(DATA_DIR, 'export')
VOLUME_GLOB = os.path.join(DATA_DIR, 'daily.dev-*.yml')

REQUIRED = (
    'id', 'date', 'title', 'category', 'tags', 'slug', 'summary',
    'problem_statement', 'key_learnings', 'impact_value', 'related_projects',
)
ID_RE = re.compile(r'^DEV-(\d{4})-(\d{3})$')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
SLUG_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
SECRET_RE = re.compile(
    r'-----BEGIN [A-Z ]*PRIVATE KEY-----'
    r'|\bAKIA[0-9A-Z]{16}\b'
    r'|\bghp_[A-Za-z0-9]{20,}'
    r'|\bxox[baprs]-[A-Za-z0-9-]{10,}'
)
SECRET_ASSIGN_RE = re.compile(
    r'(password|passwd|api[_-]?key|client_secret)\s*[:=]\s*[\'"][^\'"*\s]{6,}',
    re.IGNORECASE,
)


class Literal(str):
    pass


def _represent_literal(dumper, data):
    style = '|' if '\n' in data else None
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style=style)


yaml.add_representer(Literal, _represent_literal)


def volume_paths():
    return sorted(glob.glob(VOLUME_GLOB))


def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f'{path} não é um mapa YAML')
    return data


def load_entries():
    found = []
    for path in volume_paths():
        data = load_yaml(path)
        for entry in data.get('entries') or []:
            found.append((entry, os.path.basename(path)))
    return found


def dump_yaml(path, payload):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(
            '# Gerado por diario_dev.py. Não editar à mão.\n'
        )
        yaml.dump(
            payload,
            handle,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            width=100,
        )


def next_numbers():
    last_seq = 0
    year = date.today().year
    last_volume = 0
    for entry, _volume in load_entries():
        match = ID_RE.match(str(entry.get('id', '')))
        if match:
            year = int(match.group(1))
            last_seq = max(last_seq, int(match.group(2)))
    for path in volume_paths():
        match = re.search(r'daily\.dev-(\d+)\.yml$', os.path.basename(path))
        if match:
            last_volume = max(last_volume, int(match.group(1)))
    return year, last_seq, last_volume


def entry_errors(entry, where):
    errors = []
    label = entry.get('id') or where
    for key in REQUIRED:
        value = entry.get(key)
        if value is None or value == '' or value == []:
            errors.append(f'{label}: campo vazio `{key}`')
    entry_id = str(entry.get('id', ''))
    match = ID_RE.match(entry_id)
    if not match:
        errors.append(f'{label}: id fora do padrão DEV-AAAA-NNN')
    elif entry_id.endswith('-000'):
        errors.append(f'{label}: id 000 é o modelo, troque pelo próximo livre')
    entry_date = str(entry.get('date', ''))
    if not DATE_RE.match(entry_date):
        errors.append(f'{label}: date deve ser AAAA-MM-DD')
    elif match and not entry_date.startswith(match.group(1)):
        errors.append(f'{label}: o ano do id e o ano da date divergem')
    slug = str(entry.get('slug', ''))
    if slug and not SLUG_RE.match(slug):
        errors.append(f'{label}: slug em kebab-case, sem acento')
    if not isinstance(entry.get('tags'), list) or not isinstance(entry.get('key_learnings'), list):
        errors.append(f'{label}: tags e key_learnings são listas')
    elif len(entry.get('key_learnings') or []) < 2:
        errors.append(f'{label}: pelo menos duas lições')
    if not isinstance(entry.get('related_projects'), list):
        errors.append(f'{label}: related_projects é lista')
    blob = yaml.dump(entry, allow_unicode=True)
    if SECRET_RE.search(blob) or SECRET_ASSIGN_RE.search(blob):
        errors.append(f'{label}: possível segredo no texto; tire senha, token ou chave')
    return errors


def validate_file(path):
    data = load_yaml(path)
    entries = data.get('entries') or []
    errors = []
    seen_ids = {}
    seen_slugs = {}
    for entry, volume in load_entries():
        if os.path.abspath(os.path.join(DATA_DIR, volume)) == os.path.abspath(path):
            continue
        seen_ids[entry.get('id')] = volume
        seen_slugs[entry.get('slug')] = volume
    local_ids = set()
    local_slugs = set()
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f'entrada {index} não é um mapa')
            continue
        errors.extend(entry_errors(entry, f'entrada {index}'))
        entry_id = entry.get('id')
        slug = entry.get('slug')
        if entry_id in seen_ids:
            errors.append(f'{entry_id}: já existe em {seen_ids[entry_id]}')
        if entry_id in local_ids:
            errors.append(f'{entry_id}: repetido neste arquivo')
        if slug in seen_slugs:
            errors.append(f'{slug}: slug já usado em {seen_slugs[slug]}')
        if slug in local_slugs:
            errors.append(f'{slug}: slug repetido neste arquivo')
        local_ids.add(entry_id)
        local_slugs.add(slug)
    return errors, len(entries)


def unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1]
    return value


def parse_front_matter(fm):
    fields = {}
    for line in fm.splitlines():
        if not line.strip() or line.startswith(' ') or ':' not in line:
            continue
        key, value = line.split(':', 1)
        fields[key.strip()] = unquote(value)
    return fields


def parse_post(path):
    with open(path, 'r', encoding='utf-8') as handle:
        text = handle.read()
    if not text.startswith('---'):
        return None
    parts = text.split('---', 2)
    if len(parts) < 3:
        return None
    fm = parse_front_matter(parts[1])
    if 'Diário de Desenvolvimento' not in fm.get('subtitle', ''):
        return None
    body = parts[2]
    id_match = re.search(r'Registro #(DEV-\d{4}-\d{3})', fm.get('subtitle', ''))
    if not id_match:
        id_match = re.search(r'Registro #(DEV-\d{4}-\d{3})', body)
    if not id_match:
        return None

    def section(marker, stops):
        start = body.find(marker)
        if start < 0:
            return ''
        start = body.find('\n', start)
        rest = body[start + 1:]
        cuts = [rest.find(stop) for stop in stops if rest.find(stop) >= 0]
        chunk = rest[:min(cuts)] if cuts else rest
        return chunk.strip()

    learnings_block = section('Principais Lições', ('\n---', '### '))
    learnings = []
    for line in learnings_block.splitlines():
        if '💡' in line:
            learnings.append(line.split('💡', 1)[1].strip())

    code_block = section('Especificação Técnica', ('\n---', '### '))
    code_match = re.search(r'```[a-zA-Z0-9_+-]*\n(.*?)```', code_block, re.S)
    snippet = code_match.group(1).strip('\n') if code_match else ''

    impact_block = section('Impacto no Ecossistema', ('* **Projetos', '---'))
    impact = impact_block.split('* **Projetos', 1)[0].strip()

    related_match = re.search(r'Projetos Relacionados\*\*:\s*(.*)', body)
    related = re.findall(r'`([^`]+)`', related_match.group(1)) if related_match else []

    filename = os.path.basename(path)
    entry_date = fm.get('date', '')[:10]
    slug = filename[len(entry_date) + 1:-3] if filename.startswith(entry_date) else ''
    tags_raw = fm.get('tags', '').strip('[]')
    tags = [item.strip() for item in tags_raw.split(',') if item.strip()]

    entry = {
        'id': id_match.group(1),
        'date': entry_date,
        'title': fm.get('title', ''),
        'category': fm.get('category', ''),
        'tags': tags,
        'slug': slug,
        'summary': fm.get('description', ''),
        'problem_statement': Literal(section('O Desafio Técnico', ('\n---', '### '))),
        'key_learnings': learnings,
        'impact_value': impact,
        'related_projects': related,
    }
    if snippet:
        entry['code_snippet'] = Literal(snippet)
    return entry


def cmd_indice():
    entries = []
    for entry, volume in load_entries():
        post_name = f"{entry.get('date')}-{entry.get('slug')}.md"
        entries.append({
            'id': entry.get('id'),
            'date': str(entry.get('date')),
            'slug': entry.get('slug'),
            'title': entry.get('title'),
            'category': entry.get('category'),
            'volume': volume,
            'post': f'_posts/{post_name}',
        })
    year, last_seq, last_volume = next_numbers()
    payload = {
        'metadata': {
            'generated_at': date.today().isoformat(),
            'source': 'volumes',
            'total_entries': len(entries),
            'last_id': f'DEV-{year}-{last_seq:03d}' if last_seq else '',
            'next_id': f'DEV-{year}-{last_seq + 1:03d}',
            'next_volume': f'_data/daily.dev-{last_volume + 1:02d}.yml',
        },
        'entries': entries,
    }
    dest = os.path.join(EXPORT_DIR, 'diario.indice.yml')
    dump_yaml(dest, payload)
    print(f'Índice: {dest}')
    print(f"Registros: {len(entries)} · próximo id: {payload['metadata']['next_id']}")
    print(f"Próximo volume: {payload['metadata']['next_volume']}")


def cmd_exportar_posts():
    entries = []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, '*.md'))):
        entry = parse_post(path)
        if entry:
            entries.append(entry)
    entries.sort(key=lambda item: item['id'])
    payload = {
        'metadata': {
            'generated_at': date.today().isoformat(),
            'source': 'posts',
            'total_entries': len(entries),
            'status': 'exportado dos artigos; a fonte de novos textos continua sendo _data/daily.dev-*.yml',
        },
        'entries': entries,
    }
    dest = os.path.join(EXPORT_DIR, 'diario.desde-posts.yml')
    dump_yaml(dest, payload)
    print(f'Exportação: {dest}')
    print(f'Artigos de diário lidos: {len(entries)}')


def cmd_validar(path):
    full = path if os.path.isabs(path) else os.path.join(BASE_DIR, path)
    if not os.path.exists(full):
        print(f'Arquivo não encontrado: {full}')
        return 1
    errors, count = validate_file(full)
    print(f'{os.path.basename(full)}: {count} entrada(s)')
    if errors:
        for error in errors:
            print(f'  - {error}')
        return 1
    print('Válido.')
    return 0


def cmd_proximo():
    year, last_seq, last_volume = next_numbers()
    print(f'último id: DEV-{year}-{last_seq:03d}' if last_seq else 'nenhum id')
    print(f'próximo id: DEV-{year}-{last_seq + 1:03d}')
    print(f'próximo volume: _data/daily.dev-{last_volume + 1:02d}.yml')


def cmd_novo():
    _year, _seq, last_volume = next_numbers()
    number = last_volume + 1
    dest = os.path.join(DATA_DIR, f'daily.dev-{number:02d}.yml')
    if os.path.exists(dest):
        print(f'Já existe: {dest}')
        return 1
    today = date.today().isoformat()
    text = f'''# Volume novo do Diário de Desenvolvimento.
# Cole entradas a partir de _data/templates/diario.entrada.modelo.yml
# Roteiro: docs/roteiro-automacao-diario-dev.md

metadata:
  year: {date.today().year}
  author: "Araguaci Carlos de Andrade"
  ecosystem: "Artes do Sul & Araguaci Dev Hub"
  volume: {number}
  total_entries: 0
  generated_at: "{today}"
  status: "rascunho"
  source_note: ""

entries: []
'''
    with open(dest, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(text)
    print(f'Criado: {dest}')
    cmd_proximo()
    return 0


def cmd_importar(target):
    from import_daily_dev import run_import
    run_import(target)


def cmd_verificar():
    failed = 0
    for path in volume_paths():
        failed |= cmd_validar(path)
    cmd_indice()
    cmd_exportar_posts()
    index = load_yaml(os.path.join(EXPORT_DIR, 'diario.indice.yml'))
    exported = load_yaml(os.path.join(EXPORT_DIR, 'diario.desde-posts.yml'))
    index_ids = sorted(item['id'] for item in index['entries'])
    export_ids = sorted(item['id'] for item in exported['entries'])
    if index_ids != export_ids:
        missing = sorted(set(index_ids) - set(export_ids))
        extra = sorted(set(export_ids) - set(index_ids))
        print('Índice e artigos divergem.')
        if missing:
            print('  só no YAML:', ', '.join(missing))
        if extra:
            print('  só no post:', ', '.join(extra))
        failed = 1
    else:
        print(f'Índice e artigos batem: {len(index_ids)} registros.')
    return failed


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    command = argv[1]
    if command == 'indice':
        cmd_indice()
        return 0
    if command == 'exportar-posts':
        cmd_exportar_posts()
        return 0
    if command == 'validar':
        if len(argv) < 3:
            print('Uso: python diario_dev.py validar _data/daily.dev-NN.yml')
            return 1
        return cmd_validar(argv[2])
    if command == 'proximo':
        cmd_proximo()
        return 0
    if command == 'novo':
        return cmd_novo()
    if command == 'importar':
        target = argv[2] if len(argv) > 2 else 'all'
        cmd_importar(target)
        return 0
    if command == 'verificar':
        return cmd_verificar()
    print(f'Comando desconhecido: {command}')
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
