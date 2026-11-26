---
layout: post
title: "Ponteiros de stack passados para ui.text no nanoui geram blocos pretos na fase de layout"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-162"
description: "Copiar uma struct com buffer interno na pilha e passar sua fatia para ui.text no nanoui corrompia o desenho de texto em blocos pretos no wslpanel. Manter o ponteiro apontando para o item na lista ou arena e reservar grow para a célula do nome resolveu a renderização e o truncamento."
date: 2026-11-18 00:00:00-03:00
categories: devlog
category: frontend
tags: [zig, nanoui, gtk3, memoria, layout, testes]
---

# Ponteiros de stack passados para ui.text no nanoui geram blocos pretos na fase de layout

> [!NOTE]
> **Resumo Executivo (DEV-2026-162)**: Copiar uma struct com buffer interno na pilha e passar sua fatia para ui.text no nanoui corrompia o desenho de texto em blocos pretos no wslpanel. Manter o ponteiro apontando para o item na lista ou arena e reservar grow para a célula do nome resolveu a renderização e o truncamento.

---

### 🚨 O Desafio Técnico / Contexto
Na construção da aba Processos do wslpanel com nanoui, o método ui.text retém o ponteiro da string até a etapa de layout, depois que a função de view já retornou. Ao copiar um item Proc contendo um array [16]u8 para a pilha local, o ponteiro ficava inválido e renderizava um bloco preto por caractere. Também ocorreram regressões de layout quando um espaçador com grow vinha após o nome (reduzindo o texto a ellipsis) e falhas em testes automatizados por causa de hasText (comparação de nó inteiro) e clickText (primeiro nó correspondente).

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 ui.text guarda apenas o ponteiro do texto até o layout; strings oriundas de arrays em structs devem apontar para o elemento estável na lista ou arena de estado, nunca para uma cópia local na pilha.
* 💡 Em linhas tabulares, o atributo grow deve ficar na célula do nome enquanto PID, CPU, RSS e estado usam largura fixa; adicionar um espaçador com grow depois do nome comprime a célula e força ellipsis (...).
* 💡 Em testes com nanoui, hasText compara o conteúdo inteiro do nó (rodapés compostos exigem containsText) e clickText aciona o primeiro nó igual, exigindo que um botão '200' nasça antes de uma linha de log com o mesmo texto.
* 💡 Listas virtuais constroem apenas as linhas visíveis na janela, logo os testes devem consultar o primeiro item ordenado efetivamente renderizado na tela.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
A renderização das abas Processos, Programas e Logs ficou estável sem artefatos de memória e a suíte de testes headless do wslpanel parou de falhar por seletores ambíguos.

* **Projetos Relacionados**: `wslpanel`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
