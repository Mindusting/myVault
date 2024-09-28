# returning-clause

- [returning-clause](<https://www.sqlite.org/syntax/returning-clause.html>)

```txt
              ┌───────────────(,)<───────────────┐
o─>(RETURNING)┴>┬>[expr]┬────────────>──────────┬┴>o
                │       ├>(AS)┬>(column-alias)─>┤
                │       └──>──┘                 │
                └─────────────>(*)──────────────┘
```
