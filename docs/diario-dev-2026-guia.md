# 📓 Diário de Desenvolvimento 2026 (Daily.Dev) • Guia de Estrutura & Pipeline de Artigos

> **Documento de Governança Editorial & Engenharia**  
> **Fontes de Dados:**  
> • Volume 1: [`D:\app_aragua\araguaci.github.io\_data\daily.dev-01.yml`](file:///D:/app_aragua/araguaci.github.io/_data/daily.dev-01.yml) (DEV-2026-001 a DEV-2026-016)  
> • Volume 2: [`D:\app_aragua\araguaci.github.io\_data\daily.dev-02.yml`](file:///D:/app_aragua/araguaci.github.io/_data/daily.dev-02.yml) (DEV-2026-017 a DEV-2026-032)  
> **Script de Ingestão:** [`D:\app_aragua\araguaci.github.io\import_daily_dev.py`](file:///D:/app_aragua/araguaci.github.io/import_daily_dev.py)  
> **Destino dos Artigos:** [`D:\app_aragua\araguaci.github.io\_posts\`](file:///D:/app_aragua/araguaci.github.io/_posts/)  
> **Data:** 01 de Outubro de 2026  
> **Status:** Ativo & Sincronizado (32 Registros de Engenharia)

---

## 📌 Sumário Executivo

Ao longo do ano de 2026, o ecossistema **Artes do Sul & Araguaci** desenvolveu, consolidou e colocou em produção mais de 56 plataformas digitais, micro-SaaS, observatórios cívicos de inteligência OSINT, hardware conectado (IoT/ESP32) e arquiteturas resilientes de homelab e computação em borda.

Para registrar metadados detalhados de aprendizado contínuo derivados diretamente dos históricos de commits e da bancada diária de desenvolvimento, foram criadas as bases estruturadas [`_data/daily.dev-01.yml`](file:///D:/app_aragua/araguaci.github.io/_data/daily.dev-01.yml) e [`_data/daily.dev-02.yml`](file:///D:/app_aragua/araguaci.github.io/_data/daily.dev-02.yml).

Ambas as bases são transformadas automaticamente em artigos técnicos completos no blog pessoal do desenvolvedor ([`araguaci.github.io`](https://araguaci.github.io)), prontos para indexação, leitura pública e distribuição em redes técnicas.

---

## 📐 Esquema de Dados YAML (`daily.dev-*.yml`)

Cada entrada do diário segue uma taxonomia estrita e semântica:

```yaml
- id: "DEV-2026-XXX"
  date: "YYYY-MM-DD"
  title: "[Título Técnico e Editorial do Aprendizado]"
  category: "[devops | frontend | osint | iot | saas | ia | datascience | seguranca | infraestrutura | arquitetura | conteudo]"
  tags: [tag1, tag2, tag3]
  slug: "[slug-amigavel-para-url]"
  summary: "[Resumo executivo de 1 a 2 linhas para SEO e feeds]"
  problem_statement: >
    [Descrição detalhada do desafio de engenharia ou contexto do problema]
  key_learnings:
    - "[Lição aprendida 1: Causa raiz ou princípio técnico descoberto]"
    - "[Lição aprendida 2: Prática recomendada adotada]"
    - "[Lição aprendida 3: Métrica de ganho de desempenho ou estabilidade]"
  code_snippet: |
    [Trecho de código executável, configuração de CI/CD, CSS ou algoritmo]
  impact_value: "[Impacto prático nos produtos e valor para o ecossistema]"
  related_projects: ["projeto1", "projeto2"]
```

---

## 📋 Catálogo Completo dos 32 Registros de Aprendizado de 2026

### 🔹 Volume 1: Infraestrutura Básica, CI/CD, Shaders e Primeiros Micro-SaaS (`daily.dev-01.yml`)

| ID | Data | Categoria | Título do Aprendizado Técnico | Slug do Artigo Gerado |
| :-: | :---: | :---: | :--- | :--- |
| **DEV-2026-001** | 2026-10-01 | `devops` | Resolução de Conflitos no GitHub Actions: Ruby 2.6 para 3.3 e a Falha FFI | `2026-10-01-resolucao-conflitos-github-actions-ruby3-gem-ffi.md` |
| **DEV-2026-002** | 2026-10-01 | `devops` | A Armadilha do `vendor/bundle` no Jekyll: Exclusão Obrigatória no `_config.yml` | `2026-10-01-armadilha-vendor-bundle-jekyll-exclude.md` |
| **DEV-2026-003** | 2026-10-01 | `frontend` | Engenharia de Contraste em Headers Heróicos: Stacking Context e Overlay Gradiente | `2026-10-01-engenharia-contraste-headers-heroicos-stacking-context.md` |
| **DEV-2026-004** | 2026-09-28 | `arquitetura` | Arquitetura PWA Offline-First para Aplicações Devocionais e Espirituais | `2026-09-28-arquitetura-pwa-offline-first-aplicacoes-devocionais.md` |
| **DEV-2026-005** | 2026-09-25 | `frontend` | Síntese Sonora Procedural em 432Hz & Ressonância Schumann com Web Audio API | `2026-09-25-sintese-sonora-procedural-432hz-web-audio-api.md` |
| **DEV-2026-006** | 2026-09-15 | `iot` | Comunicação IoT de Ultrabaixa Latência (<5ms) com Protocolo ESP-NOW | `2026-09-15-comunicacao-iot-ultrabaixa-latencia-esp-now.md` |
| **DEV-2026-007** | 2026-09-08 | `osint` | Cartografia Cronológica de Lawfare: Modelagem de Dossiês com Visx e D3 | `2026-09-08-cartografia-cronologica-lawfare-visx-d3.md` |
| **DEV-2026-008** | 2026-08-20 | `frontend` | Processamento Visual com Shaders WebGL (GLSL) e Gravação Nativa WebM | `2026-08-20-processamento-visual-shaders-webgl-glsl-webm.md` |
| **DEV-2026-009** | 2026-08-15 | `osint` | Auditoria Jurimétrica de Supersalários e Captura com Corpus CC0 | `2026-08-15-auditoria-jurimetrica-supersalarios-corpus-cc0.md` |
| **DEV-2026-010** | 2026-08-08 | `frontend` | Arquitetura de Design System Cyber-Growth: Tokens HSL e Alta Conversão | `2026-08-08-design-system-cybergrowth-tokens-hsl-conversao.md` |
| **DEV-2026-011** | 2026-08-06 | `datascience` | Data Science em Saúde Pública: Mineração DATASUS (SIM) 2014–2025 | `2026-08-06-data-science-saude-publica-datasus-sim-2014-2025.md` |
| **DEV-2026-012** | 2026-07-28 | `ia` | Engenharia de Prompt Avançada e Agentes Autônomos em Pair Programming | `2026-07-28-engenharia-prompt-agentes-autonomos-pair-programming.md` |
| **DEV-2026-013** | 2026-07-15 | `segurança` | Blindagem de Formulários Anti-Bot em 4 Camadas sem Fricção de Captchas | `2026-07-15-blindagem-formularios-antibot-4-camadas-sem-captcha.md` |
| **DEV-2026-014** | 2026-06-30 | `saas` | Modelagem Financeira e Unit Economics para Micro-SaaS: Do Zero ao Breakeven | `2026-06-30-modelagem-financeira-unit-economics-micro-saas.md` |
| **DEV-2026-015** | 2026-06-10 | `datascience` | Auditoria Tarifária Energética B2B com Parser de Faturas e IA de Dados | `2026-06-10-auditoria-tarifaria-energetica-b2b-parser-faturas.md` |
| **DEV-2026-016** | 2026-05-20 | `infraestrutura`| Infraestrutura Soberana de Homelab: Proxmox VE, Docker e Mesh WireGuard | `2026-05-20-infraestrutura-soberana-homelab-proxmox-docker-wireguard.md` |

---

### 🔹 Volume 2: PWAs Sagrados & Táticos, WebGL Generativo, MCP e Deploy Híbrido (`daily.dev-02.yml`)

| ID | Data | Categoria | Título do Aprendizado Técnico | Slug do Artigo Gerado |
| :-: | :---: | :---: | :--- | :--- |
| **DEV-2026-017** | 2026-09-30 | `devops` | Deploy Híbrido Resiliente: Sincronização Atômica via FTPS e Preservação Jekyll | `2026-09-30-deploy-hibrido-resiliente-sincronizacao-ftps-jekyll.md` |
| **DEV-2026-018** | 2026-09-29 | `frontend` | Engenharia de Hero Images de Alto Impacto: Conversão WebP e Formato 5:2 para X Articles | `2026-09-29-engenharia-hero-images-webp-proporcao-5-2-x-articles.md` |
| **DEV-2026-019** | 2026-09-29 | `frontend` | Design de Interface Devocional & Decodificação Interativa: Medalha São Bento (CSSML) | `2026-09-29-interface-devocional-decodificacao-interativa-cssml-pwa.md` |
| **DEV-2026-020** | 2026-09-28 | `frontend` | Engenharia Reversa Psicológica: O Playbook do Manipulador como PWA Offline-First | `2026-09-28-engenharia-reversa-psicologica-playbook-manipulador-pwa.md` |
| **DEV-2026-021** | 2026-09-27 | `frontend` | Cartografia de Saúde Holística & Medicina Integrativa: Mapa da Cura PWA & Rife | `2026-09-27-cartografia-saude-holistica-pwa-mapa-da-cura-frequencias.md` |
| **DEV-2026-022** | 2026-09-26 | `frontend` | Design Memorial & Telemetria F1: Trilogia Ayrton Senna Lotus 98T em Web Experience | `2026-09-26-design-memorial-telemetria-f1-trilogia-ayrton-senna-lotus-98t.md` |
| **DEV-2026-023** | 2026-09-24 | `devops` | Pipeline Unificado de Currículo Soberano: De YAML Único para JSON, Markdown e PDF | `2026-09-24-pipeline-unificado-curriculo-soberano-yaml-json-markdown-pdf.md` |
| **DEV-2026-024** | 2026-08-25 | `frontend` | Engenharia de Micro-Aplicações Criativas: Delaunay e Canvas Generativo (Polygonize 3D) | `2026-08-25-micro-aplicacoes-criativas-delaunay-canvas-polygonize.md` |
| **DEV-2026-025** | 2026-08-22 | `frontend` | Visualização Sonora Reativa em Tempo Real: FFT e Web Audio API (AudioVisualizer 3D) | `2026-08-22-visualizacao-sonora-reativa-fft-web-audio-api.md` |
| **DEV-2026-026** | 2026-08-14 | `devops` | Governança de Metadados e Prevenção de Erros 404 em Tag Clouds no Jekyll Estático | `2026-08-14-governanca-metadados-prevencao-erros-404-tag-clouds-jekyll.md` |
| **DEV-2026-027** | 2026-07-20 | `ia` | Orquestração de Agentes com MCP (Model Context Protocol): O Fim dos Scripts Ad-Hoc | `2026-07-20-orquestracao-agentes-mcp-model-context-protocol.md` |
| **DEV-2026-028** | 2026-07-10 | `conteudo` | Estratégia Editorial para X Articles: Long-Forms Técnicos sem Ruído de Threads | `2026-07-10-estrategia-editorial-x-articles-long-forms-sem-ruido.md` |
| **DEV-2026-029** | 2026-06-25 | `arquitetura` | Central de Chamados Serverless & Anti-Robô com Roteamento Regional WhatsApp | `2026-06-25-central-chamados-serverless-anti-robo-roteamento-whatsapp.md` |
| **DEV-2026-030** | 2026-06-05 | `frontend` | Portais Geográficos & Ecoturismo: Vetores SVG e Leaflet com Performance 100 PageSpeed | `2026-06-05-portais-geograficos-ecoturismo-vetores-svg-leaflet-pagespeed.md` |
| **DEV-2026-031** | 2026-05-15 | `iot` | Hardware Maker & Telemetria Portátil com M5Stack Cardputer e ESP32-S3 em FreeRTOS | `2026-05-15-hardware-maker-telemetria-portatil-m5stack-cardputer-esp32-s3.md` |
| **DEV-2026-032** | 2026-04-20 | `osint` | Governança de Dados Cívicos e OSINT: Cadeia de Custódia Digital com Hash SHA-256 e IPFS | `2026-04-20-governanca-dados-civicos-osint-cadeia-custodia-sha256-ipfs.md` |

---

## ⚡ Como Executar a Ingestão / Atualização de Artigos

O pipeline [`import_daily_dev.py`](file:///D:/app_aragua/araguaci.github.io/import_daily_dev.py) suporta processamento seletivo ou total:

```powershell
# 1. Processar todos os volumes (daily.dev-01.yml e daily.dev-02.yml)
python import_daily_dev.py all

# 2. Processar apenas o volume recém-adicionado
python import_daily_dev.py daily.dev-02.yml

# 3. Execução padrão (varre todos os arquivos daily.dev-*.yml na pasta _data/)
python import_daily_dev.py
```

O script lê as bases YAML, aplica realce de sintaxe dinâmico de linguagens (Python, HTML, CSS, JavaScript, C++, YAML, JSON), compõe a estrutura canônica de frontmatter Jekyll e gera/atualiza os arquivos `.md` dentro de `_posts/`.

---

*Documento mantido pela Engenharia de Software Artes do Sul & Araguaci Hub.*
