---
author: Mindusting
corrected: true
tags:
  - Programming/SQL
title: Valor default in SQLite3
---

En la creación de una tabla, si indicamos un valor `DEFAULT` este será el que asigne en ese campo cuando creemos un nuevo registro y el valor de este no sea especificado, por defecto el valor es `NULL`, pero podemos cambiarlo de esta forma.

```sql
CREATE TABLE "users" (
    "id"         INTEGER NOT NULL UNIQUE,
    "first_name" TEXT NOT NULL DEFAULT "No-Name",
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

Como se puede ver en este ejemplo, en el caso de que se cree un registro en esta tabla y no se especifique ningún nombre, este obtendrá el valor por defecto, siendo en este caso `"No-Name"`.
