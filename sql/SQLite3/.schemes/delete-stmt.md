```txt
o─>┬>(WITH)┬─────>────────┬─┬>[common-table-expression]┐
   v       └>(RECURSIVE)─>┘ └───────────(,)<───────────┤
   ├────────────────────────<──────────────────────────┘
   └>(DELETE)─>(FROM)─>[qualified-table-name]┐
               ┌───────────────────<─────────┘
               ├>(WHERE)─>[expr]┐ ┌>[returning-clause]┐
               └────────────────┴>┴───────────────────┴>o
```