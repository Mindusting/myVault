Para poder crear una tabla deberemos seguir la siguiente estructura:

```txt
o─>(CREATE)┬────────────┬>(TABLE)┬>(IF)─>(NOT)─>(EXISTS)┐
           ├>(TEMP)─────┤        │                      │
           └>(TEMPORARY)┘        │                      │
┌─────────────────<──────────────┴─────────────<────────┘
├─>(schema-name)─>(.)┬>(table-name)┬>(AS)─>[select-stmt]───────>─────┐
└───────>────────────┘             │                                 │
┌───────────────────<──────────────┘                ┌────────>───────┼>o
└─>(()┬>[column-def]┬>┬────────────────────────┬>())┴>[table-options]┘
      └──────(,)<───┘ └[table-constraint]<─(,)<┘
```

Un ejemplo de ello sería el siguiente:

```sql
CREATE TABLE users (
    id          INTEGER NOT NULL,
    name        TEXT NOT NULL,
    email       TEXT,
    insert_date TEXT
);
```
