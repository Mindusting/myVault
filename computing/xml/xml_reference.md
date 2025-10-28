---
author: Mindusting
corrected: true
tags:
  - Programming/XML
title: Referencias en XML
---

# REFERENCIAS EN XML

Debido a que **XML** usa una serie de caracteres para poder interpretar la estructura de los datos, si queremos usar alguno de estos como texto y no como formato de **XML** tendremos que referenciar lo de una forma distinta.

| CHAR | TEXT     | DECIMAL | HEX     |
|:----:|:-------- |:------- |:------- |
| `<`  | `&lt;`   | `&#60`  | `&#x3C` |
| `>`  | `&gt;`   | `&#63`  | `&#x3E` |
| `&`  | `&amp;`  | `&#38`  | `&#x26` |
| `'`  | `&apos;` | `&#39`  | `&#x27` |
| `"`  | `&quot;` | `&#34`  | `&#x22` |
