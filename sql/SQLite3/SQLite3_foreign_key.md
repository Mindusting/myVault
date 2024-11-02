---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Llave extrangera en SQLite3
---

```txt
CREATE TABLE emails (
    id INTEGER PRAIMARY KEY,
    id_user INTEGER,
    email TEXT,
    FOREIGN KEY(id_user) REFERENCES users(id)
);
```
