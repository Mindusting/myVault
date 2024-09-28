---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Fuction/Decorator
title: Decoradores en Python
---

%%
```py
def decorator(func):
    def w():
        print("Inicio")
        func()
        print("Fin")
    return w

def bucle():
    for i in range(1_000_000):
        pass

bucle = decorator(bucle)

bucle()
```
%%
