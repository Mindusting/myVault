---
author: Mindusting
corrected: false
tags:
  - Programming/JS
title: Consola en JS
---

# CONSOLA EN JS

> [!warning] AVISO
> Para poder ver el resultado de todas las operaciones que hagamos con la consola, tendremos que abrir nuestra pagina en un buscador, y pulsar `F12` o click derecho e `Inspeccionar`.

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

Para poder hacer grupos de mensajes en la consola, se hace uso de los métodos `group`, `groupCollapsed` y `guoupEnd`, indicando estos el inicio y el final de cada uno de ellos.

```js
console.group("Grupo normal:");
console.log("Hola");
console.log("mundo!!!");
console.groupEnd();

console.groupCollapsed("Grupo colapsado:");
console.log("Adiós");
console.log("mundo!!!");
console.groupEnd();
```

Como se puede ver en el ejemplo, tanto el método `group` como `groupCollapsed`, permite indicar un nombre que es el que se le dará al grupo.

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

## TIEMPOS

Para poder cronometrar cuanto tiempo tarda un proceso en hacerse podemos usar los métodos `time` y `timeEnd`,

```js
console.time();
console.timeEnd();
```
