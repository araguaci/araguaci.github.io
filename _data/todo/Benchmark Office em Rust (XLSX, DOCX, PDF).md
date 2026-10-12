# Benchmark: Office em Rust (XLSX, DOCX, PDF)

Oct 12, 2026 · @Araguaci Carlos de Andrade

## Resumo executivo

Para produção hoje, o ecossistema Rust só é maduro em planilhas e em PDF; documentos Word ainda dependem de bibliotecas jovens (versões 0.x ou 1.0 recente) e nenhuma exporta DOCX para PDF.

| Necessidade | Escolha principal | Alternativa | Maturidade |
| --- | --- | --- | --- |
| Ler XLSX/XLS/ODS em volume | calamine | office\_oxide (inclui XLS legado) | Alta |
| Gerar XLSX com formatação e gráficos | rust\_xlsxwriter | umya-spreadsheet | Alta |
| Editar XLSX existente (abrir, mudar, salvar) | umya-spreadsheet | betteroffice-xlsx | Média |
| Recalcular fórmulas sem Excel | IronCalc | betteroffice-xlsx | Média |
| Gerar DOCX | docx-rs (bokuweb) | office-toolkit | Média |
| Ler/editar DOCX e converter DOC legado | office\_oxide | betteroffice-docx | Baixa a média |
| Gerar PDF de relatórios | Typst | printpdf | Alta |
| Manipular PDF (merge, split, edição) | lopdf | oxidize-pdf | Alta |
| Extrair texto/estrutura de PDF (RAG, busca) | pdf\_oxide | oxidize-pdf, pdf-extract | Média |
| Renderizar PDF em imagem | pdfium-render (precisa do binário Pdfium) | hayro (Rust puro) | Alta / baixa |

Os dois líderes em adoção medida são do mesmo mantenedor, John McNamara: calamine soma 14,9 milhões de downloads (5,0 milhões nos últimos 90 dias) e rust\_xlsxwriter 5,2 milhões (2,3 milhões em 90 dias), segundo o crates.io.

## Critérios

Cada projeto foi comparado por formatos, operações (ler, escrever, editar, renderizar, converter), licença, versão e data do último lançamento, dependências nativas e bindings para outras linguagens. Versões e datas vêm das páginas do docs.rs e do crates.io consultadas em 12/10/2026; downloads só aparecem onde foi possível conferi-los.

Não houve teste de desempenho: as afirmações de velocidade e taxa de sucesso citadas são dos próprios projetos. Maturidade é uma avaliação qualitativa que combina versão, tempo de mercado, adoção e cobertura de documentação.

## Planilhas (XLSX/XLS)

Planilha é a categoria mais madura: há leitor e escritor de referência, com lançamentos mensais em 2026, mas nenhuma biblioteca única faz bem leitura rápida, edição completa e cálculo de fórmulas ao mesmo tempo.

| Biblioteca | Versão (data) | Licença | Ler | Escrever | Editar existente | Fórmulas | Formatos | Destaques |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [calamine](https://docs.rs/calamine) | 0.36.1 (27/07/2026) | MIT | Sim | Não | Não | Lê valores | xlsx, xlsm, xlsb, xls, ods | Leitor padrão do ecossistema; 14,9 mi downloads |
| [rust\_xlsxwriter](https://rustxlsxwriter.github.io) | 0.99.1 (14/09/2026) | MIT ou Apache-2.0 | Não | Sim | Não | Grava | xlsx | Gráficos, formatação, WASM, Polars, Serde, modo de memória constante |
| [umya-spreadsheet](https://docs.rs/crate/umya-spreadsheet/latest) | 3.1.0 (17/08/2026) | MIT | Sim | Sim | Sim | Grava | xlsx, xlsm, csv (saída) | Estilos, gráficos, imagens, senha, carga preguiçosa, WASM opcional |
| [IronCalc](https://docs.rs/crate/ironcalc/latest) | 0.8.3 (31/07/2026) | MIT ou Apache-2.0 | Sim | Sim | Parcial | Calcula | xlsx | Motor de fórmulas testado contra resultados do Excel |
| [betteroffice-xlsx](https://docs.rs/crate/betteroffice-xlsx/latest) | 0.3.0 (28/09/2026) | Apache-2.0 | Sim | Sim | Sim | Calcula | xlsx | Edição colaborativa (CRDT Yrs), renderização, preserva partes não tocadas; alguns tipos de gráfico recusados |
| [office\_oxide](https://docs.rs/office_oxide) | 0.1.13 (30/09/2026) | MIT ou Apache-2.0 | Sim | Sim | Sim | Não informado | xlsx, xls (só leitura) | Converte XLS em XLSX; bindings Python, Node, Go, C#, C, CLI e servidor MCP |
| [office-toolkit](https://docs.rs/crate/office-toolkit/latest) | 1.0.0 (22/07/2026) | MIT | Sim | Sim | Sim | Não informado | xlsx | API única para Word, Excel e PowerPoint; projeto recente |

O par calamine + rust\_xlsxwriter cobre a maior parte dos fluxos de backend (importar planilha de cliente, exportar relatório). Quando é preciso abrir um arquivo, mudar algumas células e devolver o mesmo arquivo, umya-spreadsheet é a opção estável; betteroffice-xlsx preserva melhor o original, mas ainda está na versão 0.3.

## Documentos (DOCX/DOC)

Documento de texto é o ponto fraco: gerar DOCX novo é viável, mas editar com fidelidade, ler DOC legado e exportar para PDF ainda dependem de projetos com menos de um ano ou de ferramentas fora do Rust.

| Biblioteca | Versão (data) | Licença | Ler | Escrever | Editar existente | DOC legado | Destaques |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [docx-rs (bokuweb)](https://docs.rs/crate/docx-rs/latest) | 0.4.22 (21/07/2026) | MIT | Não | Sim | Não | Não | Gerador mais usado; pacote npm docx-wasm para navegador e Node |
| [docx-rust](https://docs.rs/crate/docx-rust/latest) | 0.1.11 (22/01/2026) | MIT | Sim | Sim | Sim | Não | Fork de PoiScript/docx-rs; lança com menos frequência |
| [office\_oxide](https://docs.rs/office_oxide) | 0.1.13 (30/09/2026) | MIT ou Apache-2.0 | Sim | Sim | Sim | Só leitura | Converte DOC em DOCX; saída em texto, Markdown, HTML e JSON |
| [betteroffice-docx](https://docs.rs/crate/betteroffice-docx/latest) | 0.3.0 (28/09/2026) | Apache-2.0 | Sim | Sim | Sim (limitado) | Não | Modelo tipado, paginação, render em PNG, limites para arquivos não confiáveis |
| [office-toolkit](https://docs.rs/crate/office-toolkit/latest) | 1.0.0 (22/07/2026) | MIT | Sim | Sim | Sim | Não | Criar, ler e modificar com a mesma API do XLSX e PPTX |

O betteroffice-docx é o único que pagina e renderiza o documento, base necessária para uma futura exportação a PDF. Hoje, porém, a substituição de texto só funciona em parágrafos de um único trecho de formatação, e a documentação cobre 4 de 59 itens. O office\_oxide é a escolha para ingestão (busca, RAG, migração de acervo .doc), não para diagramação.

Para DOCX → PDF não há solução em Rust puro. O caminho comum é gerar o PDF diretamente com Typst a partir dos mesmos dados, em vez de converter o .docx.

## PDF

Em PDF o Rust já cobre todo o ciclo, mas com uma biblioteca por tarefa: gerar, manipular, extrair e renderizar. A única exceção é renderização fiel, que ainda passa pelo Pdfium (C++).

| Biblioteca | Versão (data) | Licença | Gerar | Manipular / editar | Extrair texto | Renderizar | Destaques |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Typst](https://docs.rs/crate/typst/latest) | 0.15.1 (17/07/2026) | Apache-2.0 | Sim, por markup | Não | Não | Não | Compilador de diagramação; melhor saída tipográfica para relatórios e documentos |
| [printpdf](https://docs.rs/crate/printpdf/latest) | 0.12.8 (05/09/2026) | MIT | Sim, por API | Leitura básica | Experimental | Para SVG, experimental | Fontes com subconjunto, imagens, SVG, HTML → PDF experimental |
| [krilla](https://docs.rs/crate/krilla/latest) | 0.8.2 (04/06/2026) | MIT ou Apache-2.0 | Sim, por API | Não | Não | Não | Primitivas de alto nível (preenchimentos, gradientes, glifos) sobre pdf-writer |
| [lopdf](https://docs.rs/crate/lopdf/latest) | 0.45.0 (08/09/2026) | MIT | Sim, baixo nível | Sim: merge, localizar e substituir texto | Indireto | Não | Base de vários outros crates; streams de objetos para reduzir tamanho |
| [oxidize-pdf](https://docs.rs/crate/oxidize-pdf/latest) | 4.9.0 (30/08/2026) | MIT | Sim | Sim: split, merge, rotação, criptografia | Sim, com estrutura | Não | Recuperação de arquivos corrompidos, verificação de assinatura, validação PDF/A, chunks para RAG |
| [pdf\_oxide](https://docs.rs/crate/pdf_oxide/latest) | 0.3.78 (08/09/2026) | MIT ou Apache-2.0 | Sim | Sim: anotações, formulários, marcadores | Sim, por caractere, palavra e linha | Não informado | Saída em Markdown e HTML; bindings para 19 linguagens, CLI e MCP |
| [pdf-extract](https://docs.rs/crate/pdf-extract/latest) | 0.12.1 (16/09/2026) | Não informado | Não | Não | Sim | Não | Extração simples sobre lopdf |
| [pdfium-render](https://docs.rs/crate/pdfium-render/latest) | 0.9.4 (06/09/2026) | Não informado | Sim | Sim: formulários, edição | Sim | Sim, fiel | Wrapper do Pdfium do Chromium; exige o binário nativo; compila para WASM |
| [hayro](https://docs.rs/crate/hayro/latest) | 0.8.0 (04/10/2026) | MIT ou Apache-2.0 | Não | Não | Não | Sim, em CPU | Rust puro sem unsafe; sem PDF criptografado; sem otimização de desempenho ainda |

oxidize-pdf diz ter 99,3% de sucesso na leitura de mais de 9.000 PDFs; o número é do próprio projeto. Para renderizar miniaturas ou páginas sem dependência nativa, hayro já funciona, mas falha em arquivos protegidos por senha.

## Suítes completas

Nenhuma suíte em Rust substitui o Microsoft Office ou o LibreOffice hoje; as três candidatas têm menos de seis meses e servem para avaliar, não para produção.

| Suíte | Interface | Rust em quê | Formatos | Licença | Estágio |
| --- | --- | --- | --- | --- | --- |
| [BetterOffice](https://github.com/openooxml/betteroffice) | Web (Next.js), motores em WASM | Todos os motores (DOCX, XLSX, PPTX) | docx, xlsx, pptx; vsdx em núcleo fechado | Apache-2.0 | Crates 0.3.0 (set/2026); repositório sem releases |
| [GenOffice](https://github.com/genspark-ai/genoffice) | Seis apps Electron | Só o sidecar de XLSX (calamine + IronCalc) | docx, xlsx, pptx, pdf, md | Apache-2.0 (código); IA não aberta | Publicado em 31/07/2026 |
| [ArtCraft (PdfCraft)](https://www.gadgetpilipinas.net/2026/10/artcraft-adobe-alternatives-rust/) | Desktop nativo e navegador | Tudo, sem Electron | pdf | MIT ou Apache-2.0 | Alfa (out/2026) |

BetterOffice é a única suíte construída inteiramente sobre motores Rust, e os mesmos crates podem ser usados isoladamente em backend. GenOffice entrega mais funções ao usuário final (tabelas dinâmicas, segmentação, edição por IA), mas o Rust nele é periférico. O PdfCraft se destaca por expor cada ação como comando via CLI, JSON e MCP, o que permite automação por agentes.

## Stack por cenário

A combinação mais segura hoje é calamine + rust\_xlsxwriter + Typst + lopdf, deixando DOCX para quando o cliente exigir o formato.

| Cenário | Stack | Por quê |
| --- | --- | --- |
| Relatórios gerados no servidor (tabelas, gráficos, PDF e Excel) | Typst para PDF + rust\_xlsxwriter para XLSX | Os dois têm saída de qualidade e lançamentos frequentes; Typst embute gráficos em SVG e rust\_xlsxwriter cria gráficos nativos do Excel |
| Importação de planilhas enviadas por usuários | calamine; office\_oxide se houver .xls antigo para converter | calamine lê xlsx, xls, xlsb e ods; office\_oxide converte XLS em XLSX |
| Editar modelos (template) e devolver o arquivo | umya-spreadsheet para XLSX; office\_oxide ou docx-rust para DOCX | Abrem, alteram e salvam sem recriar o documento |
| Ingestão para busca ou RAG | pdf\_oxide ou oxidize-pdf para PDF; office\_oxide para Office | Saída em Markdown/estruturada, com página e posição |
| Editor no navegador | BetterOffice (WASM + React) ou rust\_xlsxwriter/docx-rs compilados para WASM | Processamento local, sem enviar arquivo para servidor |
| Backend em PHP, Python ou Node | Serviço Rust isolado chamado por HTTP ou fila; ou bindings prontos de office\_oxide e pdf\_oxide | Evita FFI direto no PHP; os dois crates já trazem CLI, C FFI e bindings |
| Pipeline com agentes de IA | Servidores MCP de office\_oxide, pdf\_oxide e PdfCraft | O agente opera arquivos por comandos, com rastreabilidade |

## Riscos e lacunas

- Quase tudo está em versão 0.x: atualizações podem quebrar a API entre versões menores, então fixe versões no Cargo.lock.
- Não existe conversão DOCX → PDF nem XLSX → PDF em Rust puro com fidelidade de layout.
- Renderização fiel de PDF depende do binário Pdfium, o que complica builds estáticos e WASM.
- Projetos de 2026 (office\_oxide, pdf\_oxide, office-toolkit, betteroffice) têm pouco histórico público de uso; vale testar com arquivos reais antes de adotar.
- Falta medir desempenho e consumo de memória com os seus próprios arquivos; este comparativo não fez isso.

## Fontes

- Páginas do docs.rs consultadas em 12/10/2026: [calamine](https://docs.rs/calamine), [umya-spreadsheet](https://docs.rs/crate/umya-spreadsheet/latest), [ironcalc](https://docs.rs/crate/ironcalc/latest), [betteroffice-xlsx](https://docs.rs/crate/betteroffice-xlsx/latest), [betteroffice-docx](https://docs.rs/crate/betteroffice-docx/latest), [office\_oxide](https://docs.rs/office_oxide), [office-toolkit](https://docs.rs/crate/office-toolkit/latest), [docx-rs](https://docs.rs/crate/docx-rs/latest), [docx-rust](https://docs.rs/crate/docx-rust/latest), [typst](https://docs.rs/crate/typst/latest), [printpdf](https://docs.rs/crate/printpdf/latest), [krilla](https://docs.rs/crate/krilla/latest), [lopdf](https://docs.rs/crate/lopdf/latest), [oxidize-pdf](https://docs.rs/crate/oxidize-pdf/latest), [pdf\_oxide](https://docs.rs/crate/pdf_oxide/latest), [pdf-extract](https://docs.rs/crate/pdf-extract/latest), [pdfium-render](https://docs.rs/crate/pdfium-render/latest), [hayro](https://docs.rs/crate/hayro/latest)
- API do crates.io (downloads e versões): [calamine](https://crates.io/crates/calamine), [rust\_xlsxwriter](https://crates.io/crates/rust_xlsxwriter)
- Suítes: [BetterOffice no GitHub](https://github.com/openooxml/betteroffice), [BetterOffice wiki](https://github.com/openooxml/betteroffice/wiki), [GenOffice no GitHub](https://github.com/genspark-ai/genoffice), [Powerdrill sobre o GenOffice](https://powerdrill.ai/blog/what-is-genoffice), [Gadget Pilipinas sobre o ArtCraft](https://www.gadgetpilipinas.net/2026/10/artcraft-adobe-alternatives-rust/), [Teknoblog sobre o ArtCraft](https://www.teknoblog.com/artcraft-yedi-yaratici-uygulama-gelistiriyor/)
