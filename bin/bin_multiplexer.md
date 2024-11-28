---
author: Mindusting
corrected: false
tags:
  - Binary
title: Multiplexador
---

<h1 style="text-align:center;">MULTIPLEXER</h1>

---

# CHIP

```txt
   ╔═════╗
A>─╣     ║
B>─╣ MOX ╠─>Y
S>─╣     ║
   ╚═════╝
```

# ESQUEMA

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
