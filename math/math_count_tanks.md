---
author: Mindusting
corrected: false
tags:
  - Math
title: Contar tanques
---

# CONTAR TANQUES

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Numberphile](https://youtu.be/WLCwMRJBhuI)

Este archivo explica una forma de aproximar cuántos elementos hay en una lista numerada conociendo únicamente unos pocos elementos de la lista.

Este método es conocido por haber sido usado en la segunda guerra mundial para aproximar el número de tanques que tenían los alemanes, en el vídeo del inicio del archivo lo explica más a fondo.

Este método consiste en que hay una lista de objetos enumerados de forma ordenada y no sabemos cuántos objetos son (*En el caso original fue el número de tanques, aunque esto se puede usar en por ejemplo el número de coches que se han fabricado ya que todos tienen un número de fabricación*).

Cuando obtenemos varios de estos objetos y revisamos sus números sabremos que por lo menos hay tantos objetos como el número más grande que hayamos encontrado, veamos un ejemplo:

> Si una empresa fabrica `10` coches y nosotros comprados `2`, y resulta que estos tienen el identificador `3` y `7`, sin saber cuántos coches ha fabricado la empresa, podremos deducir que ha fabricado `7` coches como mínimo, ya que es el identificador más alto que hemos encontrado.

Como hemos visto en el ejemplo anterior el resultado que obtenemos tiene un margen de error de `30%`, ahora si usamos la siguiente fórmula podremos tener una aproximación más precisa, para ello necesitaremos dos datos, el identificador más grande que hayamos obtenido (*Siguiendo con el ejemplo este será `7`*) en forma de variable llamada `MAX` y el número de objetos identificados que hayamos obtenido (*Siguiendo con el ejemplo este serán `2`*) en forma de variable llamada `k` y aplicaremos la siguiente fórmula, donde `N` es la aproximación de objetos que hay en total:

$$N = MAX + \frac{MAX - k}{k}$$

También podemos transformar esta fórmula en una función (*En este caso en [Python](../computing/py/py.md)*) para obtener la aproximación:

```python
def count_tanks(tanks_found: list[int]) -> float:
    k:   int = len(tanks_found)
    MAX: int = max(tanks_found)
    return MAX + ((MAX - k) / k)
```

Aplicando esta fórmula a al ejemplo anterior obtenemos que el número aproximado de coches fabricados es `9.5` y sí lo redondeamos obtenemos que el resultado es `10`, siendo esta aproximación mucho más cercana, obviamente en este caso a dado de lleno en el resultado correcto, pero no tiene por qué coincidir así y también hay que tener en cuenta que como en todas las aproximaciones cuanta más información tengamos el resultado será más certero.

---

Ahora veremos un ejemplo de cómo se puede usar esta fórmula en [Python](../computing/py/py.md), ten en cuenta que si ejecutas este ejemplo el número de tanques creado es `3000` mientras que el número de tanques a los que hemos podido acceder a sus identificadores son `10` por lo que vamos a deducir el número de tanques que hay en base al `0.33%` de los tanques, es muy poca información por lo que la aproximación puede ser distante, si quieres puedes probar a ir cambiando los valores para ver cómo de precisa es la aproximación en base a la cantidad de información que le otorgamos a la fórmula:

```python
from random import randint


def main() -> None:
    clear_screen()

    # Número de tanques
    num_of_tanks: int = 3_000
    # Número de tanques destruidos
    tanks_demo:   int =    10

    # Esta lista contiene los identificadores
    # de todos los tanques (Se supone que
    # nosotros no conocemos el número de tanque
    # y vamos a sacar una aproximación del
    # número en base a la información que
    # obtengamos).
    tank_ids: list[int] = list(range(num_of_tanks))

    # En esta lista guardaremos los identificadores
    # de los tanques ya hayamos obtenido.
    demo_tank_ids: list[int] = list()

    # Este bucle simula que se ha obtenido
    # los ids de n tanques.
    for _ in range(tanks_demo):

        # Se elige un tanque aleatorio,
        # se elimina de la lista de tanques
        # y se añade a la lista de tanques
        # destruidos.
        rand_index: int = randint(0, len(tank_ids)-1)
        demo_tank_id: int = tank_ids.pop(rand_index)
        demo_tank_ids.append(demo_tank_id)

    # Se usa la formula para calcular el
    # aproximado y otras dos apra caulcular
    # los porcentages de cantidad de información
    # obtenida y margen de error.
    estimated_tanks: int = count_tanks(demo_tank_ids)
    perc_demo_tanks: float = tanks_demo * 100 / num_of_tanks
    error_perc: float = (num_of_tanks / estimated_tanks - 1) * 100

    # Calculo de espaciado para el f-str.
    spacing: int = len(str(num_of_tanks))

    # Impresión de datos:
    # El resultado debería ser aproximadamente
    # el mismo que el número de tanques.
    print(f"Número de tanques: {num_of_tanks:>{spacing}}")
    print(f"Tanques estimados: {estimated_tanks:>{spacing}.0f}")
    print(f"Tanques avatidos: {perc_demo_tanks:>6.2f}%")
    print(f"Margen de error:  {abs(error_perc):>6.2f}%")


def count_tanks(tanks_found: list[int]) -> float:
    k:   int = len(tanks_found)
    MAX: int = max(tanks_found)
    return MAX + ((MAX - k) / k)


def clear_screen() -> None:
    # Se limpia el terminal.
    print("\033[2J\033[H", end="")


if "__main__" == __name__:
    main()

```
