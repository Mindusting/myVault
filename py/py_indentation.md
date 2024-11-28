---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Sangría en Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Sangría en Python se utiliza para agrupar bloques de código indicando a qué parte del resto del código pertenece, esto puede sonar confuso, por ello ahora veremos un ejemplo:

%%
```txt
╔═══╦═╗
║   ║ ║
╠═══╬═╣
╚═══╩═╝

┌───┬─┐
│   │ │
├───┼─┤
└───┴─┘
```
%%

```txt
┌─────────────────────────┐
│ 1: [code-1]             │
│ 2: [code-2]:            │
│ 3:     [code-2.1]       │
│ 4:     [code-2.2]       │
│ 5:     [code-2.3]       │
│ 6: [code-3]             │
│ 7: [code-4]:            │
│ 8:     [code-4.1]       │
│ 9:     [code-4.2]:      │
│10:         [code-4.2.1] │
│11:         [code-4.2.2] │
│12:         [code-4.2.3] │
│13:     [code-4.3]       │
│14: [code-5]             │
└─────────────────────────┘
```
