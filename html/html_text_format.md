---
author: Mindusting
corrected: true
tags:
  - Programming/HTML
title: HTML5
---

# FORMATO DE TEXTO EN HTML

## PÁRRAFOS

> [!help] REFERENCIAS WEB
> - [W3 (Paragraphs)](https://www.w3schools.com/html/html_paragraphs.asp)

Para escribir un párrafo en HTML se suele usar la etiqueta `p` (*Paragraph*), aunque no es necesario usar esta etiqueta para escribir un texto, simplemente es una forma de agrupar el texto.

%%
SINTAXIS

```html
<p>[content]</p>
```
%%

>[!abstract] SINTAXIS
>\<<span class="key-word-color">p</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">p</span>\>

```html
<p>
    Este es mi
    párrafo
    escrito en
    múltiples
    líneas.
</p>
```

Si escribes un párrafo en múltiples líneas como ocurre en este ejemplo, el resultado final será con todo en la misma línea, por lo menos hasta que llegue al final de la pantalla.

Por otra parte, también podemos usar la etiqueta "`pre`" (*PRE made*).

%%
SINTAXIS

```html
<pre>[content]</pre>
```
%%

>[!abstract] SINTAXIS
>\<<span class="key-word-color">pre</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">pre</span>\>

```html
<pre>
Este es mi
pre hecho
escrito en
múltiples
líneas.
</pre>
```

En este caso el texto saldrá con cada salto de línea indicado.

## SALTO DE LÍNEA

> [!help] REFERENCIAS WEB
> - [W3 (`br`)](https://www.w3schools.com/tags/tag_br.asp)

Para poder indicar un salto de línea en HTML usamos la etiqueta `br` (*line BReack*).

%%
SINTAXIS

```html
<br>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">br</span>\>

Un ejemplo de esto es el siguiente:

```html
<br>
```

Siguiendo el anterior ejemplo no se diferencia de un archivo HTML vacío, pero si ponemos tres [encabezados](html_headers.md) y entre dos de estos ponemos un salto de línea verás la diferencia:

```html
<h1>Hola mundo!!!</h1>
<br>
<h1>Hola mundo!!!</h1>
<h1>Hola mundo!!!</h1>
```

## LÍNEA HORIZONTAL

> [!help] REFERENCIAS WEB
> - [W3 (`hr`)](https://www.w3schools.com/tags/tag_hr.asp)

Para poder crear una línea horizontal usamos la etiqueta `hr` (*HoRizontal line*).

%%
SINTAXIS

```html
<hr>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">hr</span>\>

Un ejemplo de esto es el siguiente:

```html
<p>Esto es línea,<hr>y esta es la segunda.</p>
```

## NEGRITA

> [!help] REFERENCIAS WEB
> - [W3 (`b`)](https://www.w3schools.com/tags/tag_b.asp)

Para hacer un texto en negrita se usa la etiqueta `b` (*Bold*).

%%
SINTAXIS

```html
<b>[content]</b>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">b</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">b</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte en <b>negrita</b>.</p>
```

## ITÁLICA

> [!help] REFERENCIAS WEB
> - [W3 (`i`)](https://www.w3schools.com/tags/tag_i.asp)

Para hacer un texto en cursiva (itálica) se usa la etiqueta `i` (*Italic*).

%%
SINTAXIS

```html
<i>[content]</i>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">i</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">i</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte en <i>itálica</i>.</p>
```

## TEXTO GRANDE

> [!help] REFERENCIAS WEB
> - [W3 (`big`)](https://www.w3schools.com/tags/tag_big.asp)

> [!attention] NO ESTÁ PENSADO PARA USARSE EN HTML5
> Esta etiqueta se usaba en **HTML4** para hacer el texto grande, en **HTML5** se usa [CSS](../css/css.md) para hacer el texto más grande.

Para hacer un texto grande se usa la etiqueta `big` (*BIG*).

%%
SINTAXIS

```html
<big>[content]</big>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">big</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">big</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte en <big>grande</big>.</p>
```

## TEXTO PEQUEÑO

> [!help] REFERENCIAS WEB
> - [W3 (`small`)](https://www.w3schools.com/tags/tag_small.asp)

Para hacer un texto grande se usa la etiqueta `small` (*SMALL*).

%%
SINTAXIS

```html
<small>[content]</small>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">small</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">small</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte en <small>pequeño</small>.</p>
```

## SUB-TEXTO

> [!help] REFERENCIAS WEB
> - [W3 (`sub`)](https://www.w3schools.com/tags/tag_sub.asp)

Para hacer un texto grande se usa la etiqueta `sub` (*SUBtext*).

%%
SINTAXIS

```html
<sub>[content]</sub>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">sub</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">sub</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte en <sub>subtexto</sub>.</p>
```

## SUPER-TEXTO

> [!help] REFERENCIAS WEB
> - [W3 (`sup`)](https://www.w3schools.com/tags/tag_sup.asp)

Para hacer un texto grande se usa la etiqueta `sup` (*SUPertext*).

%%
SINTAXIS

```html
<sup>[content]</sup>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">sup</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">sup</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte en <sup>super texto</sup>.</p>
```

## SUBRAYADO

> [!help] REFERENCIAS WEB
> - [W3 (`ins`)](https://www.w3schools.com/tags/tag_ins.asp)

Para para subrayar un texto se usa la etiqueta `ins` (*INSert*).

%%
SINTAXIS

```html
<ins>[content]</ins>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">ins</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">ins</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte <ins>subrayada</ins>.</p>
```

## TACHADO

> [!help] REFERENCIAS WEB
> - [W3 (`del`)](https://www.w3schools.com/tags/tag_del.asp)

Para tachar un texto se usa la etiqueta `del` (*DELete*).

%%
SINTAXIS

```html
<del>[content]</del>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">del</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">del</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte <del>tachada</del>.</p>
```

## MARCADO

> [!help] REFERENCIAS WEB
> - [W3 (`mark`)](https://www.w3schools.com/tags/tag_mark.asp)

Para para marcar un texto se usa la etiqueta `mark` (*MARKed*).

%%
SINTAXIS

```html
<mark>[content]</mark>
```
%%

> [!abstract] SINTAXIS
> \<<span class="key-word-color">mark</span>\><span class="italic grey">[content]</span>\</<span class="key-word-color">mark</span>\>

Un ejemplo del uso de esta etiqueta es el siguiente:

```html
<p>Este texto tiene una parte <mark>marcada</mark>.</p>
```
