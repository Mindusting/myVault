# update-stmt-limited

- [update-stmt-limited](<https://www.sqlite.org/syntax/update-stmt-limited.html>)

```txt
o┬>(WHIT)┬─────>────────┬─┬>[common-table-expression]┐
 v       └>(RECURSIVE)─>┘ └───────────(,)<───────────┤
 ├───────────────────────────────────────────────────┘
 └>(UPDATE)┬──────────────────>┬>[qualified-table-name]┐
           ├>(or)─>(ABORT)────>┤                       │
           ├>(or)─>(FAIL)─────>┤                       │
           ├>(or)─>(IGNORE)───>┤                       │
           ├>(or)─>(REPLACE)──>┤                       │
           └>(or)─>(ROLLBACK)─>┘                       │
 ┌─────────────────────────────────────────────────────┘
 └>(SET)┬┬>(column-name)─────┬>(=)─>[expr]┐
        │└>[column-name-list]┘            │
        └───────────(,)<──────────────────┤
 ┌────────────────────────────────────────┘
 ├(FROM)┬┬>[table-or-subquery]┬┬>┐
 │      │└─────────(,)<───────┘│ │
 │      └────>[join-clause]────┘ │
 ├────────────────────<──────────┘
 ├>(WHERE)─>[expr]┐
 ├────────<───────┘
 ├>[returning-clause]┐
 ├────────<──────────┘
 ├>(ORDER)─>(BY)┬>[ordering-term]┐
 │              └───────(,)<─────┤
 ├───────────────────────────────┘
 ├>(LIMIT)─>[expr]┬──────────────────>┐
 │                ├>(OFFSET)─>[expr]─>┤
 │                └>(,)─>[expr]──────>┤
 └───────────────>────────────────────┴>o
```