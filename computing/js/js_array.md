---
author: Mindusting
corrected: false
tags:
  - Programming/JavaScript/Array
title: Array en JS
---

# ARRAYS EN JS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar como crear un array.
> > - [ ] Documentar las funciones del array.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/js/js_arrays.asp)

> [!faq]- FAQ
> - [¿Qué son los arrays in programación?](../pc/pc_array.md)

Un **array** en **JS** se guarda dentro de una [variable](js_variables.md), este se expresa con unos *corchetes* (`[]`), entre estos pondremos los diferentes elementos que queramos que tenga en el momento de la declaración.

> [!abstract] SINTAXIS
> let ***\[arr_name]*** = \[***\[element]***, ...];

```js
// Declaramos el array con valores establecidos.
let arr = [3, 2, 5];

// Imprimimos el array en consola.
console.log(arr);
// SALIDA:
// [3, 2, 5]
```

Si queremos signar valores o acceder a ellos, podemos hacerlo mediante el nombre del **array** y unos *corchetes* (`[]`):

```js
// Declaramos el array bacio.
let arr = [];

// Asignamos valores a las posiciones.
arr[0] = 3;
arr[1] = 2;
arr[2] = 5;

// Imprimimos el array en consola.
console.log(arr);
// SALIDA:
// [3, 2, 5]
```

```txt
unsift -> [arr] <- push
  sift <- [arr] -> pop
```
