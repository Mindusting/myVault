```txt
o─>┬───────────────────────────────┬>o
   └>(ON)─>(CONFLICT)┬>(ROLLBACK)─>┤
                     ├>(ABORT)────>┤
                     ├>(FAIL)─────>┤
                     ├>(IGNORE)───>┤
                     └>(REPLACE)──>┘
```