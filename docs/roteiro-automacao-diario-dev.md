# Roteiro — automação do Diário de Desenvolvimento

A ferramenta publica aprendizado técnico no blog `D:\app_aragua\araguaci.github.io`. A fonte é o YAML. O artigo em `_posts/` é gerado. O índice serve para não repetir o que já entrou.

## Arquivos

| Papel | Caminho |
|---|---|
| Volume publicado | `_data/daily.dev-01.yml`, `02`, `03`, … |
| Modelo de volume | `_data/templates/diario.volume.modelo.yml` |
| Modelo de uma entrada | `_data/templates/diario.entrada.modelo.yml` |
| Forma do índice | `_data/templates/diario.indice.modelo.yml` |
| Contrato JSON | `_data/templates/diario.entrada.schema.json` |
| Índice gerado | `_data/export/diario.indice.yml` |
| Cópia lida dos artigos | `_data/export/diario.desde-posts.yml` |
| Artigos | `_posts/AAAA-MM-DD-slug.md` |
| Comandos | `diario_dev.py` |

`_data/export/` é gerado. Não editar e não versionar.

## O que a ferramenta faz, em ordem

1. Rodar `python diario_dev.py indice` e abrir `_data/export/diario.indice.yml`.
2. Juntar fatos novos (commits, changelog, código). Um tema por entrada. Sem métrica que o fato não sustente.
3. Descartar tema cujo `id` ou `slug` já está no índice, ou cujo título conta o mesmo incidente.
4. Se o último volume está `status: rascunho`, acrescentar nele. Se está pronto ou já foi importado, rodar `python diario_dev.py novo`.
5. Copiar o bloco de `_data/templates/diario.entrada.modelo.yml`. Preencher com o próximo id (`python diario_dev.py proximo`). Atualizar `total_entries`.
6. Rodar `python diario_dev.py validar _data/daily.dev-NN.yml`. Corrigir até sair `Válido.`
7. Importar só esse arquivo: `python diario_dev.py importar _data/daily.dev-NN.yml`.
8. Conferir o `_posts/AAAA-MM-DD-slug.md` novo. Não reimportar `all` se a intenção é não reescrever os artigos antigos.
9. Marcar o volume `status: pronto` quando o lote fechar. Rodar `indice` de novo.

`python diario_dev.py verificar` valida os volumes publicados e confere se cada id do YAML tem artigo.

## Campos de cada entrada

Obrigatórios, na ordem do modelo:

- `id` — `DEV-AAAA-NNN`, sequencial, ano igual ao de `date`. `000` é só o modelo.
- `date` — dia do aprendizado, `AAAA-MM-DD`.
- `title` — uma frase, até 140 caracteres.
- `category` — uma da lista do schema (`devops`, `telefonia`, `arquitetura`, …).
- `tags` — 2 a 8, sem espaço.
- `slug` — kebab-case, único, até 80 caracteres. Vira o nome do arquivo.
- `summary` — duas frases: o que estava em jogo e o que passou a valer.
- `problem_statement` — o que quebrou.
- `key_learnings` — 2 a 6 lições, com mecanismo (arquivo, porta, comando, versão).
- `impact_value` — o que mudou na prática, uma frase.
- `related_projects` — repositórios ou pastas.

`code_snippet` é opcional. Trecho curto. Se não houver código, omitir a chave.

## O que não entra no texto

- Senha, token, chave privada, connection string.
- IP de produção, hostname de cliente, nome de cliente.
- Valor padrão de AMI, SMTP ou banco.
- Um artigo por commit. Vários commits do mesmo incidente viram uma entrada.
- Volume já importado não se reabre para assunto novo. Correção factual no mesmo id é a exceção, e o import desse arquivo reescreve o post.

## Exportar

Há duas saídas, as duas no formato do índice ou no formato de entrada:

```bat
cd /d D:\app_aragua\araguaci.github.io
python diario_dev.py indice
python diario_dev.py exportar-posts
```

`indice` lista o que os volumes já documentam. É a lista que a ferramenta consulta antes de escrever.

`exportar-posts` lê os artigos cujo subtítulo é `Diário de Desenvolvimento` e devolve YAML de entrada. Serve de cópia e de conferência. Aprendizado novo não nasce desse arquivo: nasce de um `daily.dev-NN.yml`.

## Comandos

```bat
cd /d D:\app_aragua\araguaci.github.io
python diario_dev.py proximo
python diario_dev.py novo
python diario_dev.py validar _data\daily.dev-04.yml
python diario_dev.py importar _data\daily.dev-04.yml
python diario_dev.py verificar
```

`importar` sem argumento processa todo `daily.dev-*.yml` e regrava os posts existentes.

Dependência: `pyyaml`.
