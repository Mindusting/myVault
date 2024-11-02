# conflict-clause

- [conflict-clause](<https://www.sqlite.org/syntax/conflict-clause.html>)

```txt
o─>┬───────────────────────────────┬>o
   └>(ON)─>(CONFLICT)┬>(ROLLBACK)─>┤
                     ├>(ABORT)────>┤
                     ├>(FAIL)─────>┤
                     ├>(IGNORE)───>┤
                     └>(REPLACE)──>┘
```
