---
author: Mindusting
corrected: false
tags:
  - Programming/HTML/Table
title: Tablas en HTML5
---

# TABLAS

> [!help] REFERENCIAS WEB
> - [W3 (Tablas)](https://www.w3schools.com/html/html_tables.asp)

%%
`table`
`thead`
`tbody`
`tr`
`th`
`td`
`caption`
%%

Para crear una tabla en **HTML** se usa la etiqueta `table`, dentro de esta usaremos la etiqueta `tr` para indicar las filas de la tablas, y dentro de esta podremos usar las etiquetas `th` y `td` para las columnas de la tabla.

```html
<table>
    <tr>
        <th>Celda cabezera 1</th>
        <th>Celda cabezera 2</th>
    </tr>
    <tr>
        <td>Celda de información 1</td>
        <td>Celda de información 2</td>
    </tr>
</table>
```

> [!faq]
> - [¿Por qué la tabla no se ve?](#^why-table-not-visible)
> - [¿Qué significa `tr`?](#ETIQUETA%20TR)
> - [¿Qué diferencia hay entre `th` y `td`?](#ETIQUETAS%20TH%20Y%20TD)
> - [¿Como puedo ponerle un título a la tabla?](#ENCABEZADO%20Y%20CUERPO)

> [!note]
> La tabla, de por sí, no tiene bordes, por lo que no podremos ver la forma que tiene, si queremos darle bordes, lo tendremos que hacer mediante [CSS](../css/css.md).
> 
> De momento, si no te quieres meter demasiado con el [CSS](../css/css.md), puedes escribir lo siguiente en la [cabeza de la página](html_basic_structure#ETIQUETA%20HEAD):
>```html
><style>
>    table, th, td {
>        border: 1px solid black;
>    }
></style>
>```
^why-table-not-visible

## ETIQUETA TR

La etiqueta `tr` (*Talbe Row*), representa las lineas de la tabla, por tanto todos los [`th` y `td`](#ETIQUETAS%20TH%20Y%20TD) que introduzca dentro de un mismo `tr`, se situarán en una línea horizontal.

## ETIQUETAS TH Y TD

> [!help] REFERENCIAS WEB
> - [W3 (Encabezados en tablas)](https://www.w3schools.com/html/html_table_headers.asp)
> - [W3 (Etiqueta `th`)](https://www.w3schools.com/tags/tag_th.asp)
> - [W3 (Etiqueta `td`)](https://www.w3schools.com/tags/tag_td.asp)

La diferencia entre `th` y `td` son las siguientes:

- `th` (*Table Header cell*):
    Es usado para indicar las **cabezas de las columnas**, el texto que introduzcamos en esta celta, por defecto estará en negrita.
- `td` (*Table Data cell*):
    Es usado para meter **información** a la tabla, generalmente texto.

En cualquiera de los dos casos, lo que se debe introducir en estas celdas **no tiene por que ser texto**, puede ser cualquier otra etiqueta de **HTML**.

Si quieres saber mas a cerca de estas celdas, te recomiendo leer los apartados de [tamaño de las celdas](#TAMAÑO%20DE%20LAS%20CELDAS) y [grupos de columnas](#GRUPOS%20DE%20COLUMNAS).

### TAMAÑO DE LAS CELDAS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [W3 (Etiquetas `colspan` y `rowspan`)](https://www.w3schools.com/html/html_table_colspan_rowspan.asp)

## TROCEA LA TABLA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [W3 (Encabezado de la tabla)](https://www.w3schools.com/tags/tag_thead.asp)
> - [W3 (Cuerpo de la tabla)](https://www.w3schools.com/tags/tag_tbody.asp)
> - [W3 (Pie de la tabla)](https://www.w3schools.com/tags/tag_tfoot.asp)

## SUBTÍTULO

> [!help] REFERENCIAS WEB
> - [W3 (Subtítulo)](https://www.w3schools.com/tags/tag_caption.asp)

Para añadirle un título ha nuestra tabla, se usa la etiqueta `caption`:

```html
<table>
    <caption>Este es el subtítulo de mi tabla</caption>
    <tr>
        <th>Celda cabezera 1</th>
        <th>Celda cabezera 2</th>
    </tr>
    <tr>
        <td>Celda de información 1</td>
        <td>Celda de información 2</td>
    </tr>
</table>
```

## GRUPOS DE COLUMNAS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [W3 (Grupos de columnas)](https://www.w3schools.com/tags/tag_colgroup.asp)
