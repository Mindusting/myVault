---
aliases:
  - Documento Nacional de Identidad
author: Mindusting
corrected: true
tags:
  - NIE
title: NIE
rating: 0.75
---

# Número de Identidad Extrangero

Un **NIE** se muy parecido al [**DNI**](dni.md) con la diferencia que en este, el primer dígito numérico es sustituido con una letra; esta letra tiene tres posibilidades (*`X`, `Y` y `Z`*), estas se sustituyen por un número a la hora de calcular la última letra de seguridad, siendo estas (*`0`, `1` y `2`*).

| LETRA | NÚM | EXPLICACIÓN |
|:-----:|:---:|:----------- |
|  `X`  | `0` | Anterior a 2008            |
|  `Y`  | `1` | Posterior a 2008            |
|  `Z`  | `2` | Se usará cuando se acabe la `Y`            |

## CALCULAR NIE

Para calcular el la letra de verificación del **NIE** se usa la misma fórmula que con el [**DNI**](dni.md), por eso te dejo aquí el código de este último:

![](dni.md#^dni-funcs)

```python
def nie_prefix(nie: str) -> int:
    # Se obtiene el número que representa la primera letra.
    try:
        return "XYZ".index(nie[0])
    except:
        return -1


def valid_nie(nie: str) -> bool:
    # Debe tener una longitud de 9 caracteres.
    if len(nie) != 9:
        return False
    nie_num: int = int(str(nie_prefix(nie)) + nie[1:-1])
    if nie_num == -1:
        return False
    # La letra debe coincidir con la resultante.
    if dni_letter(nie_num) != nie[-1]:
        return False
    return True
```

## REGEX NIE

Si queremos encontrar **NIEs** con una expresión regular podríamos hacerlo con la siguiente expresión:

```regex
[X-Z]\d{8}[A-HJ-NP-TV-Z]
```
