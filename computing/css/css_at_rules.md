---
author: Mindusting
corrected: false
tags:
  - Programming/CSS/AtRule
title: At-Rules en CSS3
---

# AT-RULES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar `@media`.

> [!help]- REFERENCIAS WEB
> - [W3 (At-Rules)](https://www.w3schools.com/cssref/css_ref_atrules.php)

## MEDIA

Para indicar que estilo de CSS queremos que se aplique cuando el ancho de la pantalla es ==menor o igual== que la medida que indiquemos se usa el `max-width` de la siguiente forma:

```css
body {
    background-color: red;
}

@media screen and (max-width: 600px) {
    body {
        background-color: blue;
    }
}
```

Si queremos que se aplique cuando es ==mayor o igual== que la medida que hemos indicado se hace con `min-width`:

```css
body {
    background-color: red;
}

@media screen and (min-width: 600px) {
    body {
        background-color: blue;
    }
}
```

También es posible apilar los cambios, para tener multiples opciones dependiendo del tamaño.

```css
body {
    background-color: red;
}

@media screen and (min-width: 900px) {
    body {
        background-color: green;
    }
}

@media screen and (min-width: 600px) {
    body {
        background-color: blue;
    }
}
```