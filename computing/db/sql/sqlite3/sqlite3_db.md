---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Bases de datos en SQLite3
---

# BASES DE DATOS EN SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Corregir ortografía.

> [!help]- REFERENCIAS WEB
> - [DDBB en memoria](https://sqlite.org/inmemorydb.html)

Las [bases de datos](../../db.md) en SQLite3 son guardadas en forma de un único archivo dentro de nuestro dísco duro en local.

También existe la posibilidad de trabajar sobre una [base de datos](../../db.md) en memoria, esto se consigue cuando a la hora de indicar la ruta del archivo de la [base de datos](../../db.md), indicamos la dirección `:memory:`; al hacer esto no se trabajara sobre el disco sino sobre la memoria, haciendo que esta [base de datos](../../db.md) sea temporal, y se borrara en el momento en que se cierre la conexión con esta.
