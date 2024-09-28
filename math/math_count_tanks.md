---
author: Mindusting
corrected: false
tags:
  - Math
title: Contar tankes
---

<h1 style="text-align:center;">CONTAR TANQUES</h1>

---

# VÍDEOS

- [Numberphile](https://youtu.be/WLCwMRJBhuI)

# CONTAR TANQUES

Este archivo explica una forma de aproximar cuántos elementos hay en una lista numerada conociendo únicamente unos pocos elementos de la lista.

Este método es conocido por haber sido usado en la segunda guerra mundial para aproximar el número de tanques que tenían los alemanes, en el vídeo del inicio del archivo lo explica más a fondo.

Este método consiste en que hay una lista de objetos enumerados de forma ordenada y no sabemos cuántos objetos son (*En el caso original fue el número de tanques, aunque esto se puede usar en por ejemplo el número de coches que se han fabricado ya que todos tienen un número de fabricación*).

Cuando obtenemos varios de estos objetos y revisamos sus números sabremos que por lo menos hay tantos objetos como el número más grande que hayamos encontrado, veamos un ejemplo:

> Si una empresa fabrica `10` coches y nosotros comprados `2`, y resulta que estos tienen el identificador `3` y `7`, sin saber cuántos coches ha fabricado la empresa, podremos deducir que ha fabricado `7` coches como mínimo, ya que es el identificador más alto que hemos encontrado.

Como hemos visto en el ejemplo anterior el resultado que obtenemos tiene un margen de error de `30%`, ahora si usamos la siguiente fórmula podremos tener una aproximación más precisa, para ello necesitaremos dos datos, el identificador más grande que hayamos obtenido (*Siguiendo con el ejemplo este será `7`*) en forma de variable llamada `MAX` y el número de objetos identificados que hayamos obtenido (*Siguiendo con el ejemplo este serán `2`*) en forma de variable llamada `k` y aplicaremos la siguiente fórmula, donde `N` es la aproximación de objetos que hay en total:

<br>

$$N = MAX + \frac{MAX - k}{k}$$

<br>

También podemos transformar esta fórmula en una función (*En este caso en [Python](../python/py.md)*) para obtener la aproximación:

```py
def count_tanks(tanks_found: list[int]) -> float:
    k:   int = len(tanks_found)
    MAX: int = max(tanks_found)
    return MAX + ((MAX - k) / k)
```

Aplicando esta fórmula a al ejemplo anterior obtenemos que el número aproximado de coches fabricados es `9.5` y sí lo redondeamos obtenemos que el resultado es `10`, siendo esta aproximación mucho más cercana, obviamente en este caso a dado de lleno en el resultado correcto, pero no tiene por qué coincidir así y también hay que tener en cuenta que como en todas las aproximaciones cuanta más información tengamos el resultado será más certero.

---

Ahora veremos un ejemplo de cómo se puede usar esta fórmula en [py](../python/py.md), ten en cuenta que si ejecutas este ejemplo el número de tanques creado es `3000` mientras que el número de tanques a los que hemos podido acceder a sus identificadores son `10` por lo que vamos a deducir el número de tanques que hay en base al `0.33%` de los tanques, es muy poca información por lo que la aproximación puede ser distante, si quieres puedes probar a ir cambiando los valores para ver cómo de precisa es la aproximación en base a la cantidad de información que le otorgamos a la fórmula:


```py
from random import random

def count_tanks(tanks_found: list[int]) -> float:
    k:   int = len(tanks_found)
    MAX: int = max(tanks_found)
    return MAX + ((MAX - k) / k)

# Esta lista contiene los identificadores
# de todos los tanques (Se supone que
# nosotros no conocemos el número de tanque
# y vamos a sacar una aproximación del
# número en base a la información que
# obtengamos).
tanks: list[int] = list(range(3_000))

# En esta lista guardaremos los identificadores
# de los tanques ya hayamos obtenido.
tank_data: list[int] = list()

# Este bucle simula que se ha obtenido
# la información de 10 tanques.
for _ in range(10):
    tank_data.append(tanks.pop(int(random() * len(tanks))))

print(count_tanks(tank_data))
# El resultado debería ser aproximadamente 3000
```
