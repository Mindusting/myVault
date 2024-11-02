---
author: Mindusting
corrected: false
tags:
  - Programming/HTML
title: Listas en HTML
---

<h1 style="text-align:center;">LISTAS EN HTML5</h1>

---

# REFERENCIAS WEB

- [W3](https://www.w3schools.com/html/html_lists.asp)
    - [W3 (Listas ordenadas)](https://www.w3schools.com/html/html_lists_ordered.asp)
    - [W3 (Listas desordenadas)](https://www.w3schools.com/html/html_lists_unordered.asp)
    - [W3 (Listas de definición)](https://www.w3schools.com/html/html_lists_other.asp)
# LISTAS

## LISTAS ORDENADAS

Las listas ordenadas se hacen usando la etiqueta `ol` (**Ordered List**), esta se usa poniendo la apertura y el cierra, entre estas etiquetas podremos indicar los diferentes punto que queremos añadir a la lista con la etiqueta `li` (**List Item**), también podemos meter otros elementos como puede ser un párrafo, esto nos puede servir por ejemplo cuando vamos ha poner una serie de preguntas enumeradas y sus respuestas.

> [!fail] HAY QUE CAMBIAR ESTOS EJEMPLOS DE ELEMENTOS INDEXADOS

```html
<ol>
    <li>Primer punto.</li>
    <p>Este es el texto del primer punto.</p>
    <li>Segundo punto.</li>
    <p>Este es el texto del segundo punto.</p>
    <li>Tercer punto.</li>
    <p>Este es el texto del tercer punto.</p>
</ol>
```

### TIPOS DE LISTAS ORDENADAS

El atributo `type` permite cambiar la forma en la que se van a ordenar los elementos, pudiendo usar números, letras mayúsculas o minúsculas y números romanos en mayúsculas o minúsculas:

| TIPO | DEFINICIÓN                 |
|:----:|:-------------------------- |
| `1`  | Números.                   |
| `a`  | Letras minúsculas.         |
| `A`  | Letras mayúsculas.         |
| `i`  | Número romanos minúsculos. |
| `I`  | Número romanos mayúsculos. |

```html
<ol type="I">
    <li>Primer punto.</li>
    <li>Segundo punto.</li>
    <li>Tercer punto.</li>
</ol>
```

### ORDEN DE LA LISTA

Si queremos hacer que la lista con el orden invertido, podemos hacerlo con el **atributo** `reversed`:

```html
<ol reversed>
    <li>Primer punto.</li>
    <li>Segundo punto.</li>
    <li>Tercer punto.</li>
</ol>
```

### PUNTO DE INICIO DE LA LISTA

Para indicar un punto de inicio distinto, se usa el atributo `start` el valor indicará desde que posición debe comenzar la lista a enumerarse:

```html
<ol start="3">
    <li>Primer punto.</li>
    <li>Segundo punto.</li>
    <li>Tercer punto.</li>
</ol>
```

## LISTAS DESORDENADA

Las listas desordenadas permite 

```html
<ul>
    <li>Primer punto.</li>
    <p>Este es el texto del primer punto.</p>
    <li>Segundo punto.</li>
    <p>Este es el texto del segundo punto.</p>
    <li>Tercer punto.</li>
    <p>Este es el texto del tercer punto.</p>
</ul>
```

### TIPOS DE LISTAS DESORDENADAS

| TIPO     | DEFINICIÓN |
|:-------- |:---------- |
| `disc`   | Punto.     |
| `circle` | Círculo.   |
| `square` | Cuadrado.  |
| `none`   | Sin icono. |

## LISTAS DE DEFINICIÓN

Las listas de definición se usan como su nombre indica para hacer una lista de palabras con sus definiciones, primero tendremos que indicar la lista, para ello usamos la apertura y cierre de la etiqueta `dl` (**Definition List**), dentro de esta podremos indicar dos etiquetas, `dt` (**Definition Term**) permite indicar la palabra que vamos a definir mientras que la etiqueta `dd` (**Definition Definition**) permite indicar la definición de la palabra indicada en el anterior "`dt`".

```html
<dl>Mi lista de términos:
    <dt>Gato.
        <dd>Animal.</dd>
        <dd>Herramienta</dd>
    </dt>
</dl>
```

## LISTAS ANIDADAS

Las listas anidadas consisten en hacer lo mismo que hemos estado haciendo 
