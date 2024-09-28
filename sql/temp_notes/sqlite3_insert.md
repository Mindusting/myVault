Para poder insertar un nuevo registro en una tabla se sigue el siguiente esquema:

```txt
o┬>(WITH)┬─────>────────┬┬>[common-table-expression]┐
 v       └>(RECURSIVE)─>┘└────────────(,)<──────────┤
 ├──────────────────────<───────────────────────────┘
 ├>(REPLACE)───────────────────┬>(INFO)┐
 └>(INSERT)┬──────────────────>┤       │
           └>(OR)┬>(ABORT)────>┤       │
                 ├>(FAIL)─────>┤       v
                 ├>(IGNORE)───>┤       │
                 ├>(REPLACE)──>┤       │
                 └>(RELLBACK)─>┘       │
┌─────────────<─────┬──────────────────┘
│                   v
└>(schema-name)─>(.)┴>(table-name)┬>(AS)─>(alias)┐
                                  v              │
┌─────────────────────────────────┴─────<────────┘
├>(()┬>(column-name)┬>())┐
│    └──────(,)<────┘    │
├────────────<───────────┘
├>(VALUES)┬>(()┬>[expr]┬>())┬─────────────────>┐
│         │    └──(,)<─┘    ├>[upsert-clause]─>┤
│         └───────(,)<──────┘                  │
├>[select-stmt]─────────────┬─────────────────>┤
│                           └>[upsert-clause]─>┤
└>(DEFAULT)─>(VALUES)─────────────────────────>┤
                          ┌──────────<─────────┤
                          └>[returning-clause]─┴─o
```

Un ejemplo de ello es el siguiente:

```sql
INSERT INTO users (
    name,
    last_name,
    email
) values (
    'Adelio',
    'Gonzalez',
    'adelio@gmail.com'
);
```
