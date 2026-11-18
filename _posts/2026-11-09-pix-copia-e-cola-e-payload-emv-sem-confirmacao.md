---
layout: post
title: "O copia e cola do Pix é um payload EMV, e o app não fica sabendo se o valor caiu"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-147"
description: "A pré-venda entrega um código que o banco consegue ler, sem conta recebedora no app. O texto segue o arranjo EMV do Pix, e a divisão acima de trezentos reais é regra do próprio app."
date: 2026-11-09 00:00:00-03:00
categories: devlog
category: backend
tags: [pix, emv, crc16, frontend]
---

# O copia e cola do Pix é um payload EMV, e o app não fica sabendo se o valor caiu

> [!NOTE]
> **Resumo Executivo (DEV-2026-147)**: A pré-venda entrega um código que o banco consegue ler, sem conta recebedora no app. O texto segue o arranjo EMV do Pix, e a divisão acima de trezentos reais é regra do próprio app.

---

### 🚨 O Desafio Técnico / Contexto
O plano de pré-venda precisava de um código para colar no banco. Não havia confirmação de pagamento nem webhook. Nome com acento ou longo demais faz o banco recusar o payload.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 buildPixPayload monta TLV: dois dígitos de id, dois de tamanho e o valor. O campo 26 leva o GUI br.gov.bcb.pix e a chave. Moeda 986, país BR, valor no campo 54 com duas casas.
* 💡 pixText tira acento e o que não é letra, número ou espaço. O nome de quem recebe fica em 25 caracteres e a cidade em 15. Abaixo disso o banco não aceita o nome.
* 💡 O CRC16-CCITT entra depois do marcador 6304, calculado sobre o corpo que já inclui esse marcador.
* 💡 parcelasPix, a partir de 300, gera três payloads estáticos: na confirmação, em 30 dias e em 60 dias. Cada um é um copia e cola. O app não recebe o valor e não sabe se caiu.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
function tlv(id, value) {
  const text = String(value);
  return id + String(text.length).padStart(2, "0") + text;
}
body += "6304";
return body + crc16(body);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A pré-venda publica um código que o banco lê, e o painel continua dependendo da venda que a pessoa anota.

* **Projetos Relacionados**: `ideia`
* **Registro de Origem**: `_data/daily.dev-25.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
