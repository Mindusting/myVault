---
author: Mindusting
corrected: false
tags:
  - OS/TerminalControl
title: Color en el terminal
---

Para poder indicar un color en forma de `RGB`, tendremos que seguir la siguiente sintaxis:

%%
```txt
SINTAXIS

\033[[target];2;[r];[g];[b]m
```
%%

> [!abstract] SINTAXIS
> \033[<span class="italic grey">[target]</span>;2;<span class="italic" style="color:f66;">[r]</span>;<span class="italic" style="color:#6f6;">[g]</span>;<span class="italic" style="color:#66f;">[b]</span>m

`\033[38;2;255;255;255m`
