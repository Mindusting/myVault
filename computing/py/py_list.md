---
author: Mindusting
corrected: false
tags:
  - Programming/Python/DataStructure
title: Listas en Python
---

# LISTAS EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como declarar de forma literal una lista con elementos.
> > - [ ] Explicar como declarar una lista rellena de forma eficiente (`[None] * 128`).
> > - [ ] Explicar la compresión de listas (`[2 ** i for i in range(8)]`).

> [!help]- REFERENCIAS WEB
> - [Python doc (List)](https://docs.python.org/3/tutorial/datastructures.html)
> - [W3 (List)](https://www.w3schools.com/python/python_lists.asp)

> [!faq]- FAQ
> - [¿Qué es una lista en programación?](../pc/pc_list.md)

Para declarar una **lista** en Python se puede hacer de dos forma, de forma *literal* o a través de la [clase](py_class.md) `list`.

## DECLARACIÓN LITERAL

```python
# Se declara la lista de forma literal.
#               V
my_list: list = []
```

---

Para crear una **lista** en Python se puede hacer de las siguientes formas:

```python
list1 = []
list2 = list()

list3: list = []
list4: list = list()
```

La [clase](py_class.md) `list` únicamente puede recibir un argumento, este no es necesario y debe ser un *iterable*, en el caso en el que no se especifique ningún valor para el argumento, devolverá una **lista** bacía, en el caso de crear un *iterable* ([`tuple`](py_tuple.md), [`set`](py_set.md), [`dict`](py_dict.md)) creará una **lista** a partir del *iterable* indicado.

Las **listas** 

```python
l0: list = [0] * 3
l1: list = list(range(3)) # [range(3)]
l2: list = [i for i in range(3)]
```

## AÑADIR ELEMENTOS

Para añadir elementos a una **lista** se usa el [método](class/py_methods.md) `append`

## MÉTODOS

append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
