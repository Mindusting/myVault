---
alias: Expresión regular
author: Mindusting
corrected: false
tags: 
  - Programming/Regex
title: Regular Expression
---

# EXPRESIÓN REGULAR

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [Wikipedia](https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular)
> - [Microsoft](https://learn.microsoft.com/es-es/dotnet/standard/base-types/regular-expression-language-quick-reference)
> - [rexegg](https://www.rexegg.com/regex-quickstart.php)
>
> YouTube:
> - [MoureDev by Brais Moure](https://youtu.be/MRKpVxn5fqI)
> - [Stand-up Maths](https://youtu.be/5vbk0TwkokM)

## TABLAS

| Scape Chars | Descripción                                           |
|:-----------:|:----------------------------------------------------- |
|    `\t`     | Tabulación                                            |
|    `\r`     | Retorno de carro                                      |
|    `\n`     | Nueva línea                                           |
|    `\a`     | Campana                                               |
|    `\e`     | Escape                                                |
|    `\f`     | Salto de página                                       |
|    `\v`     | Tabulación vertical                                   |
|    `\x`     | Carácter ASCII mediante HEX                           |
|    `\u`     | Código Unicode                                        |
|    `\d`     | Dígito \[0, 9\]                                       |
|    `\w`     | Cualquier carácter alfanumérico                       |
|    `\s`     | Espacio                                               |
|    `\D`     | Cualquier carácter no dígito \[0, 9\]                 |
|    `\W`     | Cualquier carácter no alfanumérico                    |
|    `\S`     | Cualquier carácter no espacio                         |
|    `\A`     | Inicio de la cadena                                   |
|    `\Z`     | Fin de la cadena                                      |
|    `\B`     | Separación entre palabras                             |
| `\Q` y `\E` | Se toma como literal el interior de las dos etiquetas |

| Char | Descripción                     | Ejemplo     |
|:----:|:------------------------------- |:----------- |
| \[\] | Lista de caracteres             | "\[a-m\]"   |
|  \\  | Indicar caracteres especiales   | "\d"        |
|  .   | Cualquier carácter              | "he..o"     |
|  ^   | Comenzar línea con              | "^hello"    |
|  $   | Terminar línea con              | "world$"    |
|  \*  | Secuencia de caracteres o nada  | "he.\*o"     |
|  +   | Secuencia de caracteres         | "he.+o"      |
|  ?   | Un o ningún carácter            | "he??o"     |
|  {}  | Número de caracteres específico | "he.{2}o"   |
|  \|  | Buscar dos valores de búsqueda  | "hello\|hi" |
|  ()  | Captura en grupo                |             |

## LISTA DE CARACTERES

| Set            | Descripción                           |
|:-------------- |:------------------------------------- |
| \[arn\]        | Carácter específicos                  |
| \[a-n\]        | Rango de caracteres                   |
| \[\^arn\]      | Cualquier carácter excepto            |
| \[0123\]       | Dígitos específicos                   |
| \[0-9\]        | Rango de dígitos                      |
| \[0-5\]\[0-9\] | Cualquier número en entre "00" y "59" |
| \[a-zA-Z\]     | Cualquier carácter mayúsculas o no    |
| \[+\]          | Caracteres especiales                 |

## EJEMPLOS

### BÚSQUEDA DE FECHAS

Si queremos buscar fechas, podemos usar la siguiente expresión regular:

`\d{4}(?:(?:/|-)\d{2}){2}(?: |T)\d\d(?::\d\d){2}`

`(\d{4}-\d{2}-\d{2}(\s|T)\d{2}:\d{2}:\d{2}|\d{4}-\d{2}-\d{2})`

Esta expresión regular, al ser algo compleja vamos a fragmentarlo:

```regex
(
    \d{4}-\d{2}-\d{2}(\s|T)\d{2}:\d{2}:\d{2}
    |
    \d{4}-\d{2}-\d{2}
)
```

Como se puede ver, la expresión regular contiene unos paréntesis con dos bloques separados por el operador lógico `or` (`|`).

Veamos el primer bloque, ya que este a si vez está compuesto de otros tres bloques:

```regex
\d{4}-\d{2}-\d{2}
(
    \s
    |
    T
)
\d{2}:\d{2}:\d{2}
```

Como se puede ver, el primer bloque indica que debe buscar una secuencia de caracteres en la que coincida cuatro dígitos seguido de un guion, dos dígitos, seguido de otro guion y otros dos dígitos, esto haría referencia a la estructura de una fecha (*\[año\]-\[mes\]-\[día\]*), como podría ser:

`2020-03-20`

Seguido a esto aparece otros paréntesis con dos valores separados de nuevo por el operador lógico `or` (`|`), indicando que debe haber un *espacio* o una "T" mayúscula, para finalmente tener tres pares de dígitos separados por dos puntos, por tanto todo este bloque lo que representa es una fecha y hora, la cual puede tener dos formatos:

`2020-03-20 08:32:54`

`2020-03-20T08:32:54`

---

`(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$€])[a-zA-Z0-9$€]{8,}`

---

`[0-2][0-9]:[0-5][0-9]\s?(AM|PM)`

`^\s*?boolean\s+?.+?(?:\s+?=\s+?(?:true|false));\s*?$`

12:12 AM

---

`int\s+?(?:[a-zA-Z_][a-zA-Z0-9_]*?)(?:;|(?:\s+?=\s+?\d+\s*?;))`

`^\s*?int\s+?(?:[a-zA-Z_][a-zA-Z1-9_]*?)(?:;|(?:\s+?=\s+?\d+\s*?;))\s*?$`

`[a-zA-Z_][a-zA-Z0-9]*?\s+?[a-zA-Z_][a-zA-Z0-9_]*?(?:\s+?=\s+?.+?)?;`


```regex
(?:\d{4}((?:\/|-)\d{2}){2}(?:\s|T)\d{2}(?::\d{2}){2}|\d{4}(?:(?:\/|-)\d{2}){2})
```