---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/HashLib
title: Módolo HashLib en Python
---

# HASHLIB EN PYTHON

> [!fail]- ESTA APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [PyPi (hashlib)](https://pypi.org/project/hashlib/)
> - [geeksforgeeks (hashlib)](https://www.geeksforgeeks.org/hashlib-module-in-python/)

## FUNCIONES PROPIAS

### HASH DE CONTENIDO DE ARCHIVO

```python
import hashlib
import math
import os


def fhash_sha256(
        path: str | bytes,
        bf_size: None | int = None,
        bf_max_exp: int = 16777216 # 16MiB
    ) -> str:
    """
    Makes a hash with sha256 function of the content of the file especified.

    Parameters:
        path (str | bytes):
            Path to the file to make the hash.
        bf_size (None | int):
            Size of the buffer in bytes or None to auto buffer size.
        bf_max_exp (int):
            Max buffer size in bytes.

    Returns:
        sha256 (str):
            Is the hash value is hex.
    """
    
    if bf_size is None:
        f_size: int = os.path.getsize(path)
        chunk_size: int = f_size // 1024 # 1KiB

        if chunk_size < 1024:
            bf_size = 1024 # 1KiB
        else:
            log = math.log2(chunk_size)
            bf_size = 2 ** int(log)

        if bf_size > bf_max_exp:
            bf_size = bf_max_exp


    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        data = file.read(bf_size)

        while data:
            data = file.read(bf_size)
            
            sha256.update(data)

    return sha256.hexdigest()
```
