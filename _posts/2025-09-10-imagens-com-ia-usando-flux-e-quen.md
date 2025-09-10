---
title: Imagens com IA usando Flux ou Quen 
subtitle: "Duas formas gratuitas e eficientes de gerar milhares de imagens usando inteligência artificial (IA), explorando as plataformas Flux e Quen. Com o encerramento da camada gratuita do Together AI."
date: 2025-09-10T16:48:43.396Z
preview: ""
tags: [AI, Flux, Quen, Cloudflare, Image Generation]
categories: [Tecnologia, Tutorial]
cover-img: /assets/img/imagens-com-ia-usando-flux-e-quen.png
thumbnail-img: /assets/img/medapps.png
share-img: /assets/img/imagens-com-ia-usando-flux-e-quen.png
---

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto; margin-bottom: 20px;">
    <iframe src="https://www.youtube.com/embed/2tycZNP5_IA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

O vídeo apresenta duas formas gratuitas e eficientes de gerar milhares de imagens usando inteligência artificial (IA), explorando as plataformas Flux e Quen. Com o encerramento da camada gratuita do Together AI, os criadores do canal buscam alternativas que permitem aos usuários continuar produzindo imagens em grande escala sem custos. O foco principal é demonstrar o uso do Cloudflare Workers AI e do modelo.com, oferecendo um passo a passo detalhado para configurar e utilizar essas ferramentas, além de mostrar exemplos práticos de aplicação.

---

### 1. Introdução e Contextualização

O vídeo inicia destacando a mudança recente no Together AI, que encerrou sua oferta de créditos gratuitos e acesso livre a modelos Flux, obrigando os usuários a comprarem créditos mínimos para utilizar a plataforma. Apesar desse revés, o apresentador enfatiza que há alternativas gratuitas muito vantajosas, capazes de gerar quase mil imagens diárias sem custo.

Ele anuncia que o conteúdo é um agradecimento pela conquista dos 10.000 inscritos no canal, incentivando a inscrição para que mais pessoas possam aproveitar essa nova forma de gerar imagens com IA.

**Pontos-chave:**
- Together AI removeu camada gratuita em agosto.
- Era necessário comprar créditos para continuar usando.
- O vídeo apresenta duas soluções gratuitas para continuar gerando imagens.
- O público é incentivado a se inscrever no canal.

---

### 2. Método 1: Uso do Cloudflare Workers AI para gerar imagens Flux

Esta seção detalha o primeiro método, que utiliza o Cloudflare Workers AI, uma plataforma que permite criar e executar códigos na borda da rede da Cloudflare, com integração para geração de imagens via IA.

**Passos para implementação:**
- Criar ou acessar uma conta na Cloudflare.
- Navegar até o perfil e criar um novo token API usando o template de Workers AI.
- Copiar o token gerado para autenticar as solicitações.
- Baixar o subfluxo (subworkflow) do Cloudflare Workers AI e importá-lo para a ferramenta NA10.
- Configurar o token Bearer no nó do fluxo que chama a API.
- Adicionar um nó para execução do subfluxo, preenchendo o prompt, largura e altura da imagem (limitando abaixo de 1 megapixel para melhor performance).
- Executar o workflow e visualizar a imagem gerada.

**Informações técnicas e benefícios:**
- Permite gerar até 76 imagens por dia gratuitamente.
- Processo envolve configurar token, importar workflows e executar prompts.
- Ideal para quem busca facilidade e integração rápida com fluxos automatizados.

---

### 3. Método 2: Uso do Model.com para geração de imagens Flux com créditos gratuitos

A segunda abordagem explora o model.com, que oferece $30 de créditos mensais para novos usuários após cadastro e adição de cartão de crédito, permitindo gerar imagens com modelos Flux.

**Configuração detalhada:**
- Criar conta no model.com e adicionar cartão.
- No portal, acessar a área de "secrets" para adicionar uma chave chamada `flux-app-secs`.
- Opcionalmente, adicionar um token Bearer para autenticação de endpoints.
- Configurar ambiente Python no computador (Windows, Mac ou Linux), criando e ativando um ambiente virtual.
- Instalar o pacote `model` via pip.
- Autorizar o acesso via navegador após configuração inicial.
- Rodar o aplicativo com o comando `model serve` apontando para o arquivo do modelo (nunchaku flux schnell), uma versão otimizada e leve.
- Copiar a URL gerada para uso em workflows.
- Baixar os modelos e subfluxos fornecidos pelo canal.
- Configurar autenticação Bearer no nó HTTP request, caso tenha sido adicionada.
- Executar o workflow com prompt, largura e altura definidos.

**Características do método:**
- Primeira geração demora um pouco, mas as subsequentes levam cerca de 2 segundos para gerar.
- Apropriado para usuários que precisam de alta performance sem consumir muita memória.
- Aproveita créditos mensais gratuitos para gerar imagens ilimitadas dentro do limite da cota.

---

### 4. Demonstração Prática e Aplicação em Projetos

Nesta parte, o vídeo mostra testes práticos substituindo o antigo fluxo do Together AI por esses novos métodos em um projeto real, um gerador de vídeos no TikTok com histórias assustadoras.

**Testes realizados:**
- Executa o workflow do Cloudflare Workers AI com um prompt para gerar imagens de fundo.
- Reproduz o áudio e a música de fundo para validar a integração.
- Similarmente, testa o método model.com com o fluxo Flux, preenchendo os detalhes do formulário e submetendo para geração.
- Compara tempos e resultados, destacando a velocidade e estabilidade dos novos métodos.

**Importância da demonstração:**
- Valida a eficácia das soluções.
- Mostra que é possível migrar projetos existentes para ferramentas gratuitas.
- Apresenta a facilidade de integração com fluxos de trabalho automatizados e aplicações reais.

---

### 5. Convite para Comunidade e Agradecimentos Finais

Ao final, o apresentador convida os espectadores para aderirem à comunidade no No Code AI, oferecendo mais templates de geração de vídeo, servidor de mídia hospedado e suporte contínuo para otimização de custos.

**Pontos finais:**
- Agradece os 10.000 inscritos.
- Incentiva a curtir e se inscrever no canal.
- Reforça a disponibilidade de mais recursos e dicas na comunidade dedicada.

---

### Considerações Finais e Insights

Este vídeo é um guia completo e atualizado para quem deseja continuar utilizando modelos de IA para geração de imagens de forma gratuita, especialmente após o fim da camada grátis do Together AI. A abordagem dupla oferece flexibilidade para diferentes perfis de usuários — desde aqueles que preferem uma solução simples e rápida (Cloudflare Workers AI) até os que precisam de maior performance e controle (model.com).

Além disso, o vídeo destaca a importância de configuração técnica, incluindo gestão de tokens de autenticação, uso de ambientes virtuais Python, e integração em fluxos de trabalho automatizados, tornando o conteúdo valioso para criadores de conteúdo, desenvolvedores e entusiastas de IA.

**Resumo dos benefícios:**
- Geração gratuita de imagens AI sem necessidade de pagamento.
- Métodos acessíveis e configuráveis.
- Integração com ferramentas populares de workflow.
- Aplicação prática em projetos multimídia.
- Comunidade ativa para suporte e expansão.

---

Este conteúdo é fundamental para qualquer pessoa que deseja explorar a geração de imagens com IA de forma econômica, eficiente e escalável, aproveitando as últimas alternativas disponíveis no mercado.

![](/assets/img/imagens-com-ia-usando-flux-e-quen.png)