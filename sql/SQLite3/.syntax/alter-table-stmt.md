# alter-table-stmt

- [alter-table-stmt](<https://www.sqlite.org/syntax/alter-table-stmt.html>)

```txt
                     ┌─────────>──────────┐
o─>(ALTER)─>(TABLE)─>┴>(schema-name)─>(.)─┴>(table-name)┐
┌─────────────────────────────<─────────────────────────┘
├>(RENAME)─>(TO)─>(new-table-name)──────────────────────────────┬>o
├>(RENAME)─>┬>(COLUMN)┬>(column-name)─>(TO)─>(new-column-name)─>┤
│           └────>────┘                                         │
├>(ADD)─>┬>(COLUMN)┬>[column-def]──────────────────────────────>┤
│        └────>────┘                                            │
└>(DROP)─>┬>(COLUMN)┬>(column-name)────────────────────────────>┘
          └────>────┘
```
