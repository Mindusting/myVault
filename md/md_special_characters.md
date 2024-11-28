---
author: Mindusting
corrected: false
tags:
  - MarkDown
title: Caracteres especiales en Markdown
---

<h1 style="text-align:center;">CARACTERES ESPECIALES EN MARKDOWN</h1>

---

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR

> [!info] INFO
> El carácter *contrabarra* en Markdown es considerado un *carácter de escape*, esto lo que significa es que como algunos caracteres tienen funciones especiales, si quisiéramos escribir estos caracteres, no podríamos, para solucionar esto se usa un *carácter de escape*, de forma que si escribimos este carácter y seguido ponemos un carácter con una función especial, esto provoca que ese carácter especial se intérprete de forma literal, un ejemplo de esto sería el carácter *asterisco*, de forma que si escribimos `* Ejemplo` el interprete me lo va a entender como una [lista desordenada](<md_list.md#LISTAS DESORDENADAS>), de forma que si quisiéramos que se muestre tal cuál es asterisco, lo que tendríamos que poner es `\* Ejemplo`.

Ciertos caracteres nos pueden dar problemas a la hora de usarlos en un texto, ya que estos pueden tener un uso especial en el Markdown, es por esto por lo que se escribe una contra barra antes del carácter especial para indicar que queremos escribir el carácter tal cuál.

| CARÁCTER | NOMBRE                |
|:--------:|:----------------------|
|    \\    | Contrabarra           |
|    \`    | Acentuación grave     |
|    \*    | Asterisco             |
|    \_    | Barra baja            |
|   \{\}   | Llaves                |
|   \[\]   | Corchetes             |
|   \(\)   | Paréntesis            |
|    \#    | Almohadilla / Numeral |
|    \+    | Más                   |
|    \-    | Menos / Guión         |
|    \.    | Punto                 |
|    \!    | Exclamación           |
|    \|    | Pilar                 |

## CARÁCTER DE ESCAPE DE HTML

Página que recopila los caracteres [Unidoce](<https://symbl.cc/es/>).

> [!abstract] SINTAXIS
> \&\#***\[decimal_code_from_unicode\]***;

&pi;

&smile;

&copy;

&trade;

&reg;

&#124;

&#65;
