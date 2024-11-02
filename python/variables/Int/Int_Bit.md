---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable
title: Uso del bits de los ints en Python
---

# CONTAR BITS

El método `bit_count` cuenta el número de bits `True` qué usa un número en [binario](../py_binary.md).

```py
header: str = "| NUM | BIN | COUNT |"

print(header)
print("-" * len(header))
for i in range(8):
    binary: str = f"{bin(i)[2:]:>03}"
    count: int = i.bit_count()
    print(f"|{i:^5}|{binary:^5}|{count:^7}|")
```

| NUM |  BIN  | COUNT |
|:---:|:-----:|:-----:|
|  0  |  000  |   0   |
|  1  |  001  |   1   |
|  2  |  010  |   1   |
|  3  |  011  |   2   |
|  4  |  100  |   1   |
|  5  |  101  |   2   |
|  6  |  110  |   2   |
|  7  |  111  |   3   |

```py
num: int = 8

print(f"bin({num}) = {bin(num)[2:]}")
print(f"bit_count({num}) = {num.bit_count()}")
# SALIDA:
# bin(8) = 1000
# bit_count(8) = 1
```

# LONGITUD DE BITS

El método `bit_length` cuenta el número de bits qué usa un número en [binario](../py_binary.md).

```py
header: str = "| NUM | BIN | LENGTH |"

print(header)
print("-" * len(header))
for i in range(8):
    binary: str = f"{bin(i)[2:]:>03}"
    count: int = i.bit_length()
    print(f"|{i:^5}|{binary:^5}|{count:^8}|")
```

| NUM |  BIN  | COUNT |
|:---:|:-----:|:-----:|
|  0  |  000  |   0   |
|  1  |  001  |   1   |
|  2  |  010  |   2   |
|  3  |  011  |   2   |
|  4  |  100  |   3   |
|  5  |  101  |   3   |
|  6  |  110  |   3   |
|  7  |  111  |   3   |

```py
num: int = 8

print(f"bin({num}) = {bin(num)[2:]}")
print(f"bit_length({num}) = {num.bit_length()}")
# SALIDA:
# bin(8) = 1000
# bit_length(8) = 4
```
