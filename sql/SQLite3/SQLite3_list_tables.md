---
author: Mindusting
corrected: false
tags:
  - Programming
title: Listar tablas en SQLite3
---

Para listar las tablas que tenemos creadas en nuestra base de datos podemos usar le comando `.tables`.

%%
```sql
PRAGMA table_info(sqlite_master);
```

```sql
SELECT name
FROM sqlite_master
WHERE type='table';
```
%%
