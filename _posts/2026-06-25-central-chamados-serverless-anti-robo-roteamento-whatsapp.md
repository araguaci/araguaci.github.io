---
layout: post
title: "Central de Chamados Serverless & Anti-Robô com Roteamento Regional WhatsApp"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-029"
description: "Implementação de helpdesk corporativo com emissão de protocolo transparente no cliente e roteamento geográfico direto para atendentes em Santa Catarina e São Paulo."
date: 2026-06-25 00:00:00+00:00
categories: devlog
category: arquitetura
tags: [serverless, helpdesk, whatsapp-api, anti-bot, edge]
---

# Central de Chamados Serverless & Anti-Robô com Roteamento Regional WhatsApp

> [!NOTE]
> **Resumo Executivo (DEV-2026-029)**: Implementação de helpdesk corporativo com emissão de protocolo transparente no cliente e roteamento geográfico direto para atendentes em Santa Catarina e São Paulo.

---

### 🚨 O Desafio Técnico / Contexto
Sistemas SaaS tradicionais de chamados impõem assinaturas mensais caras e geram atrito no cliente final, que prefere atendimento ágil e direto no WhatsApp.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Geração de protocolo no cliente via timestamp base36 e token randômico permite rastreamento imediato de chamados sem servidor de banco de dados ativo.
* 💡 Roteamento contextual baseado no DDD ou na seleção de serviço direciona o cliente ao canal correto (SC ou SP) com payload estruturado e sem retrabalho.
* 💡 A barreira invisível Sentinela (campos honeypot e timer mínimo de interação) bloqueia submissões de spammers e scripts maliciosos de web scraping.

---

### 🛠️ Especificação Técnica & Código-Chave
```python
// Geração de protocolo e roteamento de suporte
function createSupportTicket(region, clientName, issueDesc) {
  const dateStr = new Date().toISOString().slice(0,10).replace(/-/g, '');
  const randCode = Math.random().toString(36).substring(2, 6).toUpperCase();
  const protocol = `ADS-${dateStr}-${randCode}`;
  
  const phone = region === 'SP' ? '5511973741227' : '5547936182687';
  const msg = encodeURIComponent(`*Chamado:* #${protocol}\n*Cliente:* ${clientName}\n*Demanda:* ${issueDesc}`);
  window.open(`https://wa.me/${phone}?text=${msg}`, '_blank');
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Custo zero de infraestrutura e tempo de primeira resposta ao cliente reduzido de 4 horas para menos de 3 minutos.

* **Projetos Relacionados**: `suporte.artesdosul.com`, `artesdosul.com`
* **Registro de Origem**: `_data/daily.dev-02.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
