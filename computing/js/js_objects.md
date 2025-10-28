---
author: Mindusting
corrected: false
tags:
  - Programming/JavaScript/Object
title: Objetos en JS
---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar que es un objeto.
> > - [ ] Documentar las propiedades.
> > - [x] Documentar los métodos.
> > - [x] Documentar los constructores.
> > - [x] Documentar la impresión.
> > - [ ] Documentar los getter y setter.
> > - [ ] Documentar la herencia.

> [!help]- REFERENCIAS WEB
> - [W3 Schools (JS Objects)](https://www.w3schools.com/js/js_objects.asp)
>     - [W3 Schools (JS Objects Properties)](https://www.w3schools.com/js/js_object_property.asp)
>     - [W3 Schools (JS Objects Methods)](https://www.w3schools.com/js/js_object_method.asp)
>     - [W3 Schools (JS Objects Display)](https://www.w3schools.com/js/js_object_display.asp)
>     - [W3 Schools (JS Objects Constructos)](https://www.w3schools.com/js/js_object_constructors.asp)

> [!faq]- FAQ
> - [¿Qué son los objetos en programación?](../pc/pc_objects.md)

Los **objetos** en [**JS**](js.md)

## PROPIEDADES

Para acceder a las **propiedades** (*bien para leer o escribir*) de un **objeto** lo podemos hacer de dos formas:

> [!abstract] SINTAXIS
> ***\[objName\]***.***\[propertyName\]***

> [!abstract] SINTAXIS
> ***\[objName\]***\[***\[propertyName\]***\]

Se puede usar las dos formas indistintamente:

```js
let user = Object();

// Forma directa.
user.name = "Adelio";
console.log(user.name);
// SALIDA:
// Adelio

// Forma indirecta.
user["age"] = 20;
console.log(user["age"]);
// SALIDA:
// 20
```

Con la segunda forma de especificar las *propiedades* tenemos la ventaja que podemos acceder a ellas de forma dinámica, ya que no tenemos por qué poner el nombre entre comillas, sino que podemos ofrecerle ese valor mediante una [variable](js_variables.md):

```js
let user = {
    name: "Adelio",
    age: 20
}

let property = "name";

console.len(user[property]);
// SALIDA:
// Adelio
```

## MÉTODOS

Los **métodos** son en esencia [funciones](js_func.md) las cuales se encuentran dentro de un **objeto**; estas debido a que se ejecutan desde el interior de un **objeto** pueden usar la palabra clave `this`, este hace referencia al propio **objeto**, permitiendo acceder de esta forma a sus [**propiedades**](#PROPIEDADES) e incluso otros **métodos**.

Como se puede ver en el siguiente ejemplo, un **método** se declara como una [**propiedad**](#PROPIEDADES) del **objeto** la cual contiene una [función](js_func.md):

```js
let user = {
    name: name,
    age: age,

    greeting: function() {
        //            Referencia al propio objeto.
        //                                v
        console.log(`Hola mi nombre es ${this.name}`);
    }
};
```

## IMPRESIÓN

Para poder imprimir un **objeto** se puede hacer de diversas formas; en este caso usaremos el [`JSON`](js_json.md), transformando con él el **objeto** en texto para poder ser impreso:

```js
let user = {
    name: name,
    age: age
};

console.log(JSON.stringify(user));
// SALIDA:
// {"name":"Adelio","age":20}
```

## CONSTRUCTOR

Los **constructores** son para poder crear un **objeto** de forma más sencilla y estructurada; existen dos formas de crear constructores, la primera que veremos es la antigua y está en desuso, la siguiente que veremos será la moderna.

La forma antigua de hacer un **constructor** es mediante una [**función**](js_func.md) la cual recibirá los argumentos que serán usado para establecer las [**propiedades**](#PROPIEDADES) del **objeto**; para distinguir esta [**función**](js_func.md) (*constructor*) del resto de [**funciones**](js_func.md) se escribe su nombre capitalizado (*la primera letra en mayúsculas*):

```js
function User(name, age) {
    this.name = name;
    this.age = age;

    this.greeting = function() {
        console.log(`Hola mi nombre es ${this.name}`);
    };
}
```

La forma moderna de hacer un **constructor** es mediante las palabras clave `class` y `constructor`:

```js
class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;

        this.greeting = function () {
            console.log(`Hola mi nombre es ${this.name}`);
        };
    }
}
```
