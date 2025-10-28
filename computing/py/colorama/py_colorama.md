---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Colorama en Python
---

# COLORAMA EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [PyPi (colorama)](https://pypi.org/project/colorama/)
> - [geeksforgeeks (colorama)](https://www.geeksforgeeks.org/introduction-to-python-colorama/)
> 
> YouTube:
> - [Tech With Tim](https://youtu.be/u51Zjlnui4Y)

> [!faq]- FAQ
> - [¿Qué es el control del terminal?](../../os/tc/tc.md)

## OBJETO FORE

Por defecto el color del texto `RESET` = 39

| NOMBRE    | COLOR    | NUM |
|:--------- |:-------- | ---:|
| `BLACK`   | Negro    |  30 |
| `RED`     | Rojo     |  31 |
| `GREEN`   | Verde    |  32 |
| `YELLOW`  | Amarillo |  33 |
| `BLUE`    | Azul     |  34 |
| `MAGENTA` | Magenta  |  35 |
| `CYAN`    | Cían     |  36 |
| `WHILE`   | Blanco   |  37 |

| NOMBRE            | COLOR          | NUM |
|:----------------- |:-------------- | ---:|
| `LIGHTBLACK_EX`   | Negro claro    |  90 |
| `LIGHTRED_EX`     | Rojo claro     |  91 |
| `LIGHTGREEN_EX`   | Verde claro    |  92 |
| `LIGHTYELLOW_EX`  | Amarillo claro |  93 |
| `LIGHTBLUE_EX`    | Azul claro     |  94 |
| `LIGHTMAGENTA_EX` | Magenta claro  |  95 |
| `LIGHTCYAN_EX`    | Cían claro     |  96 |
| `LIGHTWHILE_EX`   | Blanco claro   |  97 |

## OBJETO BACK

Por defecto el color del fondo `RESET` = 49

| NOMBRE    | COLOR    | NUM |
|:--------- |:-------- | ---:|
| `BLACK`   | Negro    |  40 |
| `RED`     | Rojo     |  41 |
| `GREEN`   | Verde    |  42 |
| `YELLOW`  | Amarillo |  43 |
| `BLUE`    | Azul     |  44 |
| `MAGENTA` | Magenta  |  45 |
| `CYAN`    | Cían     |  46 |
| `WHILE`   | Blanco   |  47 |

| NOMBRE            | COLOR          | NUM |
|:----------------- |:-------------- | ---:|
| `LIGHTBLACK_EX`   | Negro claro    | 100 |
| `LIGHTRED_EX`     | Rojo claro     | 101 |
| `LIGHTGREEN_EX`   | Verde claro    | 102 |
| `LIGHTYELLOW_EX`  | Amarillo claro | 103 |
| `LIGHTBLUE_EX`    | Azul claro     | 104 |
| `LIGHTMAGENTA_EX` | Magenta claro  | 105 |
| `LIGHTCYAN_EX`    | Cían claro     | 106 |
| `LIGHTWHILE_EX`   | Blanco claro   | 107 |

## OBJETO STYLE

Por defecto el formato y colores `RESET_ALL` = 0

| NOMBRE   | FORMATO           | NUM |
|:-------- |:----------------- | ---:|
| `BRIGHT` | Negrita           |   1 |
| `DIM`    | Oscurecido        |   2 |
| `NORMAL` | Estilo por normal |  22 |

## OBJETO CURSOR

| NOMBRE    | ACCIÓN      |
|:--------- |:----------- |
| `POS`     | Mover a ... |
| `FORWARD` | Avanzar     |
| `BACK`    | Retroceder  |
| `UP`      | Subir       |
| `DOWN`    | Bajar       |
