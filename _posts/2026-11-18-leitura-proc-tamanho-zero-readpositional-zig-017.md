---
layout: post
title: "Arquivos em /proc informam tamanho zero e exigem readPositional em buffer fixo no Zig 0.17"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-161"
description: "Medidores de CPU e processos lidos via readFileAlloc em /proc retornavam vazio e travavam a interface em 0% no wslpanel. Trocar para openFile com readPositional em buffer fixo e calcular deltas entre amostras de um segundo estabilizou toda a telemetria em Zig 0.17."
date: 2026-11-18 00:00:00-03:00
categories: devlog
category: backend
tags: [zig, linux, wsl, procfs, cgroup, telemetry]
---

# Arquivos em /proc informam tamanho zero e exigem readPositional em buffer fixo no Zig 0.17

> [!NOTE]
> **Resumo Executivo (DEV-2026-161)**: Medidores de CPU e processos lidos via readFileAlloc em /proc retornavam vazio e travavam a interface em 0% no wslpanel. Trocar para openFile com readPositional em buffer fixo e calcular deltas entre amostras de um segundo estabilizou toda a telemetria em Zig 0.17.

---

### 🚨 O Desafio Técnico / Contexto
Durante o desenvolvimento do wslpanel (0.1.0 e 0.2.0) em Zig 0.17 rodando em WSL2, tentativas de ler arquivos virtuais do procfs com readFileAlloc devolviam conteúdo vazio porque o kernel reporta tamanho 0 no stat de /proc. Além disso, a primeira amostra de CPU sempre resulta em 0% sem um delta anterior, a função std.posix.getpid não existe no Zig 0.17 e o parâmetro --nanoui-wait executa antes de --nanoui-script, fazendo um clique posterior à espera ainda cair na primeira amostra.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Arquivos virtuais em /proc informam tamanho 0; readFileAlloc falha silenciosamente devolvendo vazio, exigindo openFile seguido de readPositional em um buffer de tamanho fixo.
* 💡 O percentual de CPU em /proc/stat é o delta entre duas leituras (cerca de 1 segundo) usando total menos idle e iowait; em containers, cpu.stat fornece usage_usec (microssegundos de um núcleo) e a página precisa chamar frameIn(1) enquanto aberta.
* 💡 No Zig 0.17, o PID do próprio processo vem de std.os.linux.getpid (std.posix.getpid não existe), enquanto std.posix.kill está disponível normalmente.
* 💡 Em testes automatizados com nanoui, --nanoui-wait roda antes de --nanoui-script, portanto qualquer aba aberta por clique no script ainda receberá a primeira amostra (0%) antes do segundo delta.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
const file = try std.fs.openFileAbsolute("/proc/stat", .{});
defer file.close();
var buf: [4096]u8 = undefined;
const n = try file.readPositional(&buf, 0);
const pid = std.os.linux.getpid();
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os medidores de CPU por núcleo, processos e cgroup do wslpanel passaram a atualizar com precisão a cada segundo sem leituras vazias no Linux e no WSL2.

* **Projetos Relacionados**: `wslpanel`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
