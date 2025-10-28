---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/CSV
title: Python
---

# CSV EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar para qué sirve el módulo.
> > - [ ] Hacer referencia a la documentación de los archivos `CSV`.
> > - [ ] Documentar como cambiar la separación, salto de línea, etc de las funciones.

> [!help]- REFERENCIAS WEB
> - [Python doc (csv)](https://docs.python.org/3/library/csv.html)

```csv
id,name,age
1,Adelio,20
2,Adelia,22
```

## LEER COMO LISTA

```python
import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)

    head = next(reader)
    users = list(reader)

    print(*head, sep="\t")
    print("-" * 24)
    for user in users:
        print(*user, sep="\t")
    # SALIDA:
    # id      name    age
    # ------------------------
    # 1       Adelio  20
    # 2       Adelia  22
```

## ESCRIBIR COMO LISTA

```python
import csv

head = ["id", "name", "age"]

users = [
    [1, "Adelio", 20],
    [2, "Adelia", 22]
]

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(head)
    writer.writerows(users)
```

## LEER COMO DICCIONARIO

```python
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)

    for user in reader:
        print(user)
        # SALIDA:
        # {'id': '1', 'name': 'Adelio', 'age': '20'}
        # {'id': '2', 'name': 'Adelia', 'age': '22'}
```

## ESCRIBIR COMO DICCIONARIO

```python
import csv

head = ["id", "name", "age"]

users = [
    {"id": 1, "name": "Adelio", "age": 20},
    {"id": 2, "name": "Adelia", "age": 22}
]

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, head)

    writer.writeheader()
    writer.writerows(users)
```
