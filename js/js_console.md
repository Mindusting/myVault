---
author: Mindusting
corrected: true
tags:
  - Programming/JS
title: Consola en JS
---

# CONSOLA EN JS

Existen cuatro tipos de impresión por consola, para poder acceder a ellos se debe llamar al objeto `console`, seguido de un punto para poder acceder a uno de sus métodos.

> [!abstract] SINTAXIS
> console.***\[metod\]***(***\[args\]***);

```js
console.log("Hola mundo!!!");   // Impresión normal.
console.info("Hola mundo!!!");  // Impresión de información.
console.warn("Hola mundo!!!");  // Impresión de alerta.
console.error("Hola mundo!!!"); // Impresión de error.
```

> [!info]
> Es posible que no haya diferencia estética entre la impresión del `log` e `info`.

---

Si quisiéramos limpiar la consola, podemos hacerlo a través del método `clear`, esto borrará todo lo que se haya impreso antes de esta instrucción.

```js
console.clear();
```

## GRUPOS

Para poder hacer grupos de mensajes en la consola, se hace uso de los métodos `group` y `guoupEnd`, indicando estos el inicio y el final de cada uno de ellos.

```js
console.group("Primer grupo:");
console.log("Hola");
console.log("mundo!!!");
console.groupEnd();

console.group("Segundo grupo:");
console.log("Adiós");
console.log("mundo!!!");
console.groupEnd();
```

---

Un ejemplo más complejo de ello podría ser el siguiente:

```js
var elements = document.getElementsByTagName("p");

console.group("Grupos:");

for (let idxGrupo = 0; idxGrupo < 3; idxGrupo++) {

    console.group("Grupo %d", idxGrupo)

    for (let idxElemento = 0; idxElemento < 3; idxElemento++) {

        console.log(
            "Elemento %d del grupo %d",
            idxElemento,
            idxGrupo
        )
    }
    console.groupEnd();
}
console.groupEnd();
```
