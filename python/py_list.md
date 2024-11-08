---
author: Mindusting
corrected: false
tags:
  - Programming/Python/DataStructure
title: Listas en Python
---


# LIST

> [!help] REFERENCIAS WEB
> - [Python doc (List)](https://docs.python.org/3/tutorial/datastructures.html)
> - [W3 (List)](https://www.w3schools.com/python/python_lists.asp)

- [¿Qué es una lista en programación?](../../pc/pc_list.md)

Para declarar una [**lista**](../../pc/pc_list.md) en Python se puede hacer de las siguientes formas:

```py
list1 = []
list2 = list()

list3: list = []
list4: list = list()
```

La [clase](../py_class.md) `list` únicamente puede recibir un argumento, este no es necesario y debe ser un *iterable*, en el caso en el que no se especifique ningún valor para el argumento, devolverá una **lista** bacía, en el caso de crear un *iterable* ([`tuple`](py_tuple.md), [`set`](py_set.md), [`dict`](py_dict.md)) creará una **lista** a partir del *iterable* indicado.

Las **listas** 

```py
l0: list = [0] * 3
l1: list = list(range(3)) # [range(3)]
l2: list = [i for i in range(3)]
```

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
