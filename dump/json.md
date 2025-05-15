---
author: Mindusting
corrected: false
tags:
  - Programming/JS/JSON
title: JSON
---

# JSON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que JSON es JavaScript Object Notation.
> > - [ ] Revisar todo el contenido para valorar que se puede mejorar.
> > - [ ] Comprobar faltas de ortografía.

Los archivos JSON están pensados para guardar información de forma sencilla, vienen por parte de [JavaScript](../computing/js/js.md), pero se puede usar en otros lenguajes con ayuda de librerías.

El objetivo de estos es guardar información de forma permanente en un archivo externo para poder acceder a la información en el futuro.

## ARCHIVOS

Los archivos de JSON tienen la extensión `.json` y el formato interno que usa es texto plano.

## ESTRUCTURA DE LA INFORMACIÓN

La información dentro de los archivos JSON se escribe al igual que en [JavaScript](../computing/js/js.md) se escriben los [array](../computing/js/js_array.md) y los [objetos](../computing/js/js_objects.md), este último tiene un matiz y es que no se pueden guardar funciones, únicamente información.

Por lo general los archivos JSON suelen empezar con un [objetos](../computing/js/js_objects.md), pero también puede comenzar con [array](../computing/js/js_array.md).

En el próximo ejemplo podemos ver como el primer nivel del archivo tiene un [objetos](../computing/js/js_objects.md), este contiene dos *llaves* (`key`), con cada uno su respectivo *valor* (`value`):

```json
{
    "PI": 3.14159236535,
    "E" : 2.71828182845
}
```

En el próximo ejemplo, a diferencia del anterior, este comienza con un [array](../computing/js/js_array.md), conteniendo este dos elementos.

```json
[
    3.14159236535,
    2.71828182845
]
```

>[!note]
>Cada archivo JSON solo puede tener un [array](../computing/js/js_array.md) u [objeto](../computing/js/js_objects.md) en el primer nivel, de lo contrario nos dará un error.

---

La información puede tener forma de *matriuska*, de forma que un [array](../computing/js/js_array.md) u [objeto](../computing/js/js_objects.md) se puede encontrar dentro de otro, en el próximo ejemplo se muestra como hacerlo.

```json
{
    "users": [
        {"name": "Mindusting", "age": 18, "height": 1.75},
        {"name": "Adelio", "age": 32, "height": 1.8}
    ],
    "products": [
        {"name": "Apple", "price": 3.5},
        {"name": "Banana", "price": 5}
    ]
}
```

Otra forma de guardar la misma información que en el ejemplo anterior pero con la misma estructura es la siguiente.

```json
{
    "users": {
        "name": ["Mindusting", "Adelio"],
        "age": [18, 32],
        "height": [1.75, 1.8]
    },
    "products": {
        "name": ["Apple", "Banana"],
        "price": [3.5, 5]
    }
}
```

---

Los ejemplos que has visto hasta ahora están hechos de una forma visualmente agradable, pero el contenido no tiene por qué guardarse de esa forma, por lo genera, para ahorrar espacio, se suele guardar de una forma más compacta, escribiendo lo todo en una sola línea:

```json
{"users":{"name":["Mindusting","Adelio"],"age":[18,32],"height":[1.75,1.8]},"products":{"name":["Apple","Banana"],"price":[3.5,5]}}
```

En cualquiera de los dos casos funciona de la misma forma, por lo que cuando el archivo va a guardar muchísimos datos y no vamos a acceder a la información de forma directa al archivo, no tenemos ningún interés en guardarlo de forma visualmente agradable ya que ocupa más espacio, en cambio si es un archivo por ejemplo de configuración, que es pequeño y queremos que sea fácil de manejar abriendo el archivo de forma directa, podemos usar el formato agradable a la vista, esto último os lo digo por qué cuando vamos a guardar datos en un archivo JSON desde otro archivo de código, por lo general, existe la opción de elegir en qué forma queremos guardar el archivo. si de forma visual o compacta.
