---
author: Mindusting
corrected: true
tags:
  - Programming/Python
title: Filtro en Python
---

# FILTRO EN PYTHON

La [función](py_function.md) `filter`, permite filtrar los elementos de un iterable en base a las condiciones que indiquemos, esta [función](py_function.md) recibe dos parámetros, siendo el primero una función que reciba un argumento que sería el elemento del iterable y que devuelva un valor [booleano](py_bool.md) indicando si debe pasar el filtro o no, y el segundo parámetro es el iterable en cuestión.

> [!abstract] SINTAXIS
> filter(***\[function\], \[iterable\]***)

Esta [función](py_function.md) devuelve un objeto de tipo `filter` que en esencia es un [generador](py_generator.md) con el cual podremos obtener los elementos del iterable filtrados en base al a la [función](py_function.md) ofrecida.

```py
# Creación de lista de números
raw_data = list(range(10))

# Se crea un objeto de tipo filtro
filter_obj = filter(
    lambda x: x % 2 == 0,
    raw_data
)

# Se procesa toda la información
data = list(filter_obj)

print(raw_data)
print(data)
# SALIDA:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8]
```

---

Podríamos crear nuestro propio [generador](py_generator.md) que funciones como la [función](py_function.md) `filter`, como forma didáctica para entender qué es lo que estaría ocurriendo en el interior:

```py
# Recreación de la función
# (generador) filter hecha
# en Python.
def my_filter(func, iter):
    for item in iter:
        if func(item):
            yield item

# Creación de lista de números
raw_data = list(range(10))

# Se crea un objeto de tipo filtro
filter_obj = filter(
    lambda x: x % 2 == 0,
    raw_data
)

# Se procesa toda la información
data = list(filter_obj)

print(raw_data)
print(data)
# SALIDA:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8]
```

> [!important] IMPORTANTE
> No es recomendable usar este ejemplo en un caso real, ya que al estar escrito en Python este es más lento que la [función](py_function.md) `filter`.

---

Si queremos filtrar [entidades](py_entity.md) podríamos hacer de la siguiente forma:

```py
# Declaración del POPO
class User(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age
    
    def __repr__(self):
        return f"User [nane='{self.name}', age={self.age}]"

# Declaración de función par el filtrado
def func_to_filter(user: User) -> bool:
    return user.age >= 18

# Tupla de usuarios
users = (
    User("Adelio", 20),
    User("Adelia", 22),
    User("Jon",    16),
    User("Sara",   15),
    User("Alex",   18),
    User("Ane",    25),
)

# Filtrado de usuarios
filtered_users = tuple(filter(
    func_to_filter,
    users
))

print("Users:")
for user in users:
    print(f"    {user}")

print("Filtered users:")
for user in filtered_users:
    print(f"    {user}")
# SALIDA:
# Users:
#     User [nane='Adelio', age=20]
#     User [nane='Adelia', age=22]
#     User [nane='Jon', age=16]
#     User [nane='Sara', age=15]
#     User [nane='Alex', age=18]
#     User [nane='Ane', age=25]
# Filtered users:
#     User [nane='Adelio', age=20]
#     User [nane='Adelia', age=22]
#     User [nane='Alex', age=18]
#     User [nane='Ane', age=25]
```
