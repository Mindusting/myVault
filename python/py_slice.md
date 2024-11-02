---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Slice
title: Slices en Python
---

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

>[!todo]
>### TEMPORALES
>---
>### CONSTANTES
>- [ ] Faltas de ortografía corregidas.

<https://www.w3schools.com/python/ref_func_slice.asp>

Los `slice` permiten obtener una porción de un [string](<## STRIG 🔤>) o como veremos más adelante, también funcionan con las [colecciones](<# COLECCIONES>), pero eso ya lo veremos más adelante.

La clase `slice` permite crear objetos de este los cuales indicara una secuencia basandose en tres reglas:

- Empezar (`start`)
- Parar (`stop`)
- Paso (`step`)

%%
SINTAXIS
slice([start], [stop], [step])
%%

> [!abstract] SINTAXIS
> <span class="class-color">slice</span>(<span class="italic grey">[start]</span> <span class="italic grey">[stop]</span>, <span class="italic grey">[step]</span>)

Esta clase requiere como mínimo un argumento (`star`), este indica el índice del elemento por el que se debe empezar a obtener el resultado

>[!example] Ej. de uso del `slice`:

```py
alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

my_slice: slice = slice(2, 8, 2)

print(alphabet[my_slice])
# SALIDA:
# CEG
```
