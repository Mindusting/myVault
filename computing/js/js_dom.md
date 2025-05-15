---
author: Mindusting
corrected: false
tags:
  - Programming/JS/DOM
title: DOM en JS
---

# DOM

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como obtener elementos del documento con un [selector de CSS](../css/css_selectors.md).
> > - [ ] Explicar qué es el DOM.
> > - [ ] Explicar que usos tiene el DOM:
> >     - Modificar el HTML.
> >         - Añadir nuevos elementos.
> >         - Modificar elementos.
> >         - Eliminar elementos.
> >     - Modificar el CSS.
> >     - Crear eventos.
> > - [x] Documentar la selección de elementos.
> > - [ ] Documentar los elementos.
> >     - [ ] Poner ejemplos de las propiedades.
> >     - [ ] Poner ejemplos de la navegación.
> >     - [ ] Documentar la modificación.

> [!important] IMPORTANTE
> Los **nodos** son los objetos que contiene el documento.
> Los **elementos** son *nodos* de tipo etiqueta de HTML.

## SELECCIÓN DE ELEMENTOS

- getElementById(***\[id\]***):
    - Devuelve el elemento que coincida con el *id*.
    - Si no lo encuentra devuelve `NULL`.
- getElementsByClassName(***\[class\]***):
    - Devuelve los elementos con la *clase* indicada.
    - Si no encuentra ninguno devuelve un [array](js_array.md) vacío.
- getElementsByName(***\[name\]***):
    - Devuelve los elementos con el *nombre* indicada.
    - Si no encuentra ninguno devuelve un [array](js_array.md) vacío.
- getElementsByTagName(***\[tag\]***):
    - Devuelve los elementos con la *etiqueta* indicada.
    - Si no encuentra ninguno devuelve un [array](js_array.md) vacío.
- querySelector([***\[query\]***](../css/css_selectors.md)):
    - Devuelve el elemento que coincida con el [*selector*](../css/css_selectors.md) de [CSS](../css/css.md) indicado.
    - Si no lo encuentra devuelve `NULL`.
- querySelectorAll([***\[query\]***](../css/css_selectors.md)):
    - Devuelve los elementos que coincidan con el [*selector*](../css/css_selectors.md) de [CSS](../css/css.md) indicado.
    - Si no encuentra ninguno devuelve un [array](js_array.md) vacío.
[css_selectors](../css/css_selectors.md)
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div>
        <h1>MI TÍTULO</h1>
        <!-- p1 -->
        <p id="parrafoPrincipal">
            Este es el párrafo principal.
        </p>
        <!-- p2 -->
        <p class="marcado">
            Este es el párrafo secundario.
        </p>
    </div>
    <!-- p3 -->
    <p class="marcado">
        Este es el párrafo terciario.
    </p>
    <button name="enviar">Enviar</button>
</body>
</html>
```

```js
let p1     = document.getElementoById("parrafoPrincipal");
let p2_p3  = document.getElementoByClassName("marcado");
let button = document.getElementoByName("enviar");
let h1     = document.getElementoByTagName("h1");
let p1     = document.querySelector("body div p");
let p1_p2  = document.querySelectorAll("body div p");
```

## NODOS

Para obtener el elemento [`body`](../html/html_basic_structure.md#ETIQUETA%20BODY) se usa la propiedad `body` de la [variable](js_variables.md) `document`.

### PROPIEDADES

Todos los *elementos* contienen **propiedades**, estas se usan tanto para obtener información de estos, como para modificarlos.

| Propiedades   | Descripción                                                       |
|:------------- |:----------------------------------------------------------------- |
| `nodeName`    | Nombre del nodo. (*Solo lectura*)                                 |
| `textContent` | Contenido de texto del elemento.                                  |
| `innerText`   | Versión no estándar de `textContent`. (==*Evitar*==)              |
| `otherText`   | Versión no estándar de `textContent`/`outherHTML`. (==*Evitar*==) |
| `innerHTML`   | Contenido HTML del elemento.                                      |
| `outerHTML`   | Es el `innerHTML` pero incluyendo el HTML del elemento.           |

#### NAVEGACIÓN

Para navegar entre los distintos nodos, podemos usar una serie de propiedades que tienen los propios nodos:

- `parentNode`: contiene el nodo padre.
- `cildNodes`: contiene un [array](js_array.md) con los nodos hijos.
- `firstNode`: contiene el primer hijo.
- `lastNode`: contiene el último hijo.
- `nextSibling`: contiene el siguiente hermano.
- `previousSibling`: contiene el anterior hermano.
- `nodeName`: contiene el nombre del nodo.
- [`nodeType`](#TIPOS%20DE%20NODOS): contiene el tipo del nodo, pudiendo ser uno de los siguientes:
    - (1) Elemento.
    - (2) Atributo.
    - (3) Texto.
    - (8) Comentario.
    - (9) Documento.
- `tagName`: contiene el nombre de la etiqueta.

### CREACIÓN

```js
// Creación de nodo elemento.
let p = document.createElement("p");

// Creación de nodo de texto.
let t = document.createTextNode("Hola mundo!");
```

### MODIFICACIÓN

```js
// Añadir hijo.
p.appendChild(t);

// Eliminar nodo.
p.parentNode.removeChild(p);

// Remplazar nodo hijo.
p.replaceChild(p, p);
```

### PROPERTIES

```js
// Propiedades de elemento.
var enlace = document.getElementById("enlace");
console.log(enlace.href);
console.log(enlace.className);

// Estilo de elemento.
var img = document.getElementById("img");
console.log(img.style.margin);
console.log(img.style.fontWeight);
```
