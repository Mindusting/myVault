---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Uso de la tabla sqlite_master en SQLite3
---

# TABLA MASTER EN SQLITE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [Documentación oficial de SQLite](https://www.sqlite.org/schematab.html)

Cuando creamos una base de datos se genera una tabla interna a esta automáticamente, esta es `sqlite_master` y contiene información del resto de tablas (entro otras cosas) de la base de datos.

Esta tabla contiene cinco campos:

- `type`:
    Indica el tipo de objeto al que hace referencia el registro, este puede ser uno de los siguientes: (`table`, `index`, `view`, `trigger`).
<br>
- `name`:
    Contiene el nombre de la (`table`, `index`, `view`, `trigger`).
<br>
- `tbl_name`:
    Contiene el nombre de una tabla o vista a la que está asociado el objeto. Para una tabla o vista, la columna `tbl_name` es una copia de la columna de nombre. Para un índice, `tbl_name` es el nombre de la tabla que está indexada. Para un trigger, la columna `tbl_name` almacena el nombre de la tabla o vista que hace que se active el trigger.
<br>
- `rootpage`:
    Indica el número del registro en el [árbol binario](../../../pc/pc_btree.md) de la tabla `sqlite_master`.
<br>
- `sql`
    Este campo contiene la sentencia SQL que ha creado el objeto al que hace referencia el registro.

Para consultar esta tabla, implemente podemos hacerlo a través de una consulta normal.

```sql
SELECT * FROM sqlite_master;
```
