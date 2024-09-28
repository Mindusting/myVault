---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/Byte
title: Bytes en Python
---

- [Bytearray](py_bytearray.md)
- [memoryview](py_memoryview.md)

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

>[!todo]
>### TEMPORALES
>- [ ] Depurar código, hacer ejemplos y documentarlos.

```py
bs = bytes("Adiós", "UTF-8")
print(bs)
print(bs.decode())
```

```py
num_bytes: int = 1

for i in range(2 ** (num_bytes * 8)):
    print(list(map(lambda x: f"{bin(x)[2:]:>08}", int.to_bytes(i, num_bytes))))


num: int = 3

bs: bytes = bytes([1 for _ in range(2)])

print(bs)
print(int.from_bytes(bs))
print(0b0000000100000001)

rand_bytes: bytes = bytes(list(map(lambda x: x % 256, [random.randint(0, 256) for _ in range(2)])))

print(rand_bytes)
print(f"{int.from_bytes(rand_bytes):_}")

print(int.to_bytes(65))
```
