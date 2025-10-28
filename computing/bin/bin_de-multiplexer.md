---
author: Mindusting
corrected: false
tags:
  - Binary
title: De-Multiplexador
---

<h1 style="text-align:center;">DE-MULTIPLEXER</h1>

---

# CHIP

```txt
   ╔══════╗
A>─╣      ║
B>─╣ DMOX ╠─>Y
S>─╣      ║
   ╚══════╝
```

# ESQUEMA

%%
```txt
A>────────────╦═════╗
              ║ AND ╠─┐
   ┌──────────╩═════╝ └─╦════╗
   │                    ║ OR ╠─>Y
B>─┼──────────╦═════╗ ┌─╩════╝
   │ ╔═════╗  ║ AND ╠─┘
S>─╩─╣ NOT ╠──╩═════╝
     ╚═════╝
```
%%
