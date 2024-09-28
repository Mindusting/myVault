---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: SQLite3
---

<h1 style="text-align:center;">SQLite3</h1>

---

> [!note] NOTA
> En el caso de qué sea tu primera vez con SQL, te recomiendo que primero veas la [documentación general](../SQL.md).

# ABRIR EL ENTORNO DE SQLITE3

Para poder abrir el entorno de sqlite3 se debe escribir el comando `sqlite3`, tras esto entrarás en el entorno, pudiendo escribir comandos que afectarán a bases de datos.

Este comando nos permite también crear o abrir una base de datos, para ello seguido de este, se escribe al ruta y el nombre de la base de datos.

> [!abstract] SINTAXIS
> sqlite3 ***\[db_name\]***

%%
# DUMP

- [Guardar una base de datos](SQLite3_save_db.md)
- [Abrir una base de datos](SQLite3_open_db.md)
- [Ver las tablas](SQLite3_list_tables.md)
    - [Info de las tablas](SQLite3_table_info.md)
- [Consulta de datos](SQLite3_select.md)
- [Formato de salida de datos](SQLite3_output_formats.md)
- [Llave primaria](SQLite3_primary_key.md)
- [Llave extrangera](SQLite3_foreign_key.md)
- [Ejecutar archivos SQL sobre la base de datos](SQLite3_read_sql_files.md)
- [Tabla sqlite_master](SQLite3_sqlite_master.md)
- [Tipos de datos](SQLite3_data_types.md)
%%

- [CREAR TABLAS](SQLite3_tables.md)
- [INSERTAR REGISTROS](SQLite3_insert.md)
- [LEER REGISTROS](SQLite3_select.md)
- [VALOR POR DEFECTO](SQLite3_default.md)
- [OPERADORES](SQLite3_operators.md)
- [DDBB EN MEMORIA](SQLite3_memory_ddbb.md)

---

## TIPOS DE DATOS

- [Tipos de datos](https://www.sqlite.org/datatype3.html)

| TIPOS DE SQLITE3 | TIPOS DE PYTHON |
|:---------------- |:--------------- |
| NULL             | None            |
| INTEGER          | Bool            |
| INTEGER          | Int             |
| REAL             | Float           |
| TEXT             | Str             |
| BLOB             | Bytes           |
