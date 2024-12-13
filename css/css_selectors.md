---
author: Mindusting
corrected: false
tags:
  - Programming/CSS
title: Selectores en CSS3
---

# SELECTORES

> [!help] REFERENCIAS WEB
> - [W3 (Selectores)](https://www.w3schools.com/cssref/css_selectors.php)
> - [W3 (Combinadores)](https://www.w3schools.com/cssref/css_ref_combinators.php)

Los **selectores**, como su nombre indica, nos permite seleccionar a que elementos queremos aplicarle el formato que especifiquemos.

![](css.md#^css-syntax)

| Selector                    | Descripción                                  | CSS |
|:--------------------------- |:-------------------------------------------- |:---:|
| .*\[class]*                 | Elem. con la **clase** especificada.         |  1  |
| #*\[id]*                    | Elem. con la **id** especificada.            |  1  |
| \*                          | Todos los elementos.                         |  2  |
| *\[lmnt]*                   | **Elemento** concreto.                       |  1  |
| *\[lmnt1]*, *\[lmnt2]*      | Multiples **elementos**.                     |  1  |
| *\[lmnt1]* *\[lmnt2]*       | Elem. `2` **dentro** del `1`.                |  1  |
| *\[lmnt1]* > *\[lmnt2]*     | Elem. `2` **hijo de** `1`.                   |  2  |
| *\[lmnt1]* + *\[lmnt2]*     | Elem. `2` **inmediatamente seguidos** a `1`. |  2  |
| *\[lmnt1]* ~ *\[lmnt2]*     | Elem. `2` **precedidos por** `1`.            |  3  |
| \[*\[attr.]*]               | **Atributo** especificado.                   |  2  |
| \[*\[attr.]* = *\[val.]*]   | Atributo **igual a**.                        |  2  |
| \[*\[attr.]* ~= *\[val.]*]  | Atributo **conteniendo**.                    |  2  |
| \[*\[attr.]* \|= *\[val.]*] | Atributo **coincide con**.                   |  2  |
| \[*\[attr.]* ^= *\[val.]*]  | Atributo **comenzando por**.                 |  3  |
| \[*\[attr.]* $= *\[val.]*]  | Atributo **terminado por**.                  |  3  |
| \[*\[attr.]* \*= *\[val.]*] | Atributo **cont. sub str**.                  |  3  |
| :not(*\[lmnt]*)             | Todos los elem. excepto el especificado.     |  3  |
^selectors-table

Unos ejemplos de sin formato de los selectores podrían ser los siguientes, en estos se muestras los más básicos:

 ```css
 h1, h2, h3, h4, h5, h6 {} /* Todos los headers */
 #myId {}                  /* El que contenga ID */
 .myClass {}               /* Los que tengan class */
 h2.myClass {}             /* Los h2 con esa class */
 p small {}                /* Los small dentro del un p */
 ```