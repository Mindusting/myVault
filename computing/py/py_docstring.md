---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Doc-String en Python
---

# DOC-STRING EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## FUNCIONES PROPIAS

### GUARDAR AYUDA

```python
import sys

def save_help(path: str | bytes, element) -> None:
    with open(path, "w") as file:
        sys.stdout = file
        help(element)
        sys.stdout = sys.__stdout__
```
