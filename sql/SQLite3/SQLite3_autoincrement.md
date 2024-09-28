---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Clave primaria en SQLite3
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

El atributo `AUTOINCREMENT` es utiliza en las [claves primarias](SQLite3_primary_key.md), este, la especificarlo, cambia ligeramente el comportamiento de la [clave primaria](SQLite3_primary_key.md):

Imaginemos que tenemos una tabla sin ningún registro al meter uno nuevo, este tendrá la clave primaria con el valor `1` y la siguiente con el valor `2`, ahora, si borramos la que tiene la clave primaria `2`.

- SIN `AUTOINCREMENT`:
    E [insertamos](SQLite3_insert.md) una nueva, esta tendrá de nuevo el valor `2`, ya que simplemente busca el valor más grande que se encuentre en la columna que sea [clave primaria](SQLite3_primary_key.md) y le suma uno.
<br>
- CON `AUTOINCREMENT`:
    E [insertamos](SQLite3_insert.md) una nueva, esta tendrá el valor `3`, ya que aunque el valor `2` ya no esté en uso, la tabla tiene un contador interno para la [clave primaria](SQLite3_primary_key.md), este contador indica que valor debe obtener el siguiente registro en la [clave primaria](SQLite3_primary_key.md).
