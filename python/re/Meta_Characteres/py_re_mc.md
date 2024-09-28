---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/RE
title: Meta caracteres
---

| Char | Descripción                       | Ejemplo     |
|:----:|:----------------------------------|:------------|
| \[\] | [Lista de caracteres](py_re_mc_sets.md) | "\[a-m\]"   |
|  \\  | Indicar caracteres especiales     | "\d"        |
|  .   | Cualquier carácter                | "he..o"     |
|  ^   | Comenzar con                      | "^hello"    |
|  $   | Terminar con                      | "world$"    |
|  \*  | Secuencia de caracteres o nada    | "he\*o"     |
|  +   | Secuencia de caracteres           | "he+o"      |
|  ?   | Un o ningún carácter              | "he??o"     |
|  {}  | Número de caracteres específico   | "he.{2}o"   |
|  \|  | Buscar dos valores de búsqueda    | "hello\|hi" |
|  ()  | Captura en grupo                  |             |