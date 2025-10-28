---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Struct
title: Módulo Struct en Python
---

# STRUCT EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar como empaquetar información.
> > - [ ] Documentar como desempaquetar información.
> > - [ ] Documentar el string de formato.
> > - [ ] Documentar como trabajar sobre booleanos.

> [!help]- REFERENCIAS WEB
> - [Python doc](https://docs.python.org/3/library/struct.html)
> 
> YouTube:
> - [NeuralNine](https://youtu.be/gViM3ZuDQrw)

El módulo **struct** es usado para transformar datos de [**Python**](../py.md) a una secuencia de [`bytes`](../py_bytes.md) y viceversa, imitando de esta forma las [*estructuras*](../../c/c_struct.md) de [**C**](../../c/c.md), esto permite que guardemos información de forma binaria bien en [archivos](../py_open.md) o para [mandar a través de la red](../socket/py_socket.md).

En esta documentación veremos a rasgos generales las cosas que se necesita saber para su uso y algunos ejemplos, pero si lo que quieres es unos casos más reales en los que se busca la eficiencia, a la hora de tratar los datos, consulta la documentación de la clase [`Struct`](py_struct_struct.md), para poder entender bien su uso, primero debes entender leer esta documentación.

```md
Este módulo es usado para transformar los valores de Python en [`bytes`](py_bytes.md) y viceversa, permitiendo así guardar información de forma compacta en archivos
```

## STRING DE FORMATO

| Character | Byte order             | Size     | Alignment |
| --------- | ---------------------- | -------- | --------- |
| `@`       | native                 | nativew  | native    |
| `=`       | native                 | standard | none      |
| `<`       | little-endian          | standard | none      |
| `>`       | big-endian             | standard | none      |
| `!`       | network (= big-endian) | standard | none      |

| Format | C Type             | Python type       | TAMAÑO EN BYTES |
|:------:|:------------------ |:----------------- |:---------------:|
|  `x`   | pad byte           | no value          |                 |
|  `c`   | char               | bytes of length 1 |        1        |
|  `b`   | signed char        | integer           |        1        |
|  `B`   | unsigned char      | integer           |        1        |
|  `?`   | _Bool              | bool              |        1        |
|  `h`   | short              | integer           |        2        |
|  `H`   | unsigned short     | integer           |        2        |
|  `i`   | int                | integer           |        4        |
|  `I`   | unsigned int       | integer           |        4        |
|  `l`   | long               | integer           |        4        |
|  `L`   | unsigned long      | integer           |        4        |
|  `q`   | long long          | integer           |        8        |
|  `Q`   | unsigned long long | integer           |        8        |
|  `n`   | `ssize_t`          | integer           |                 |
|  `N`   | `size_t`           | integer           |                 |
|  `e`   | (6)                | float             |        2        |
|  `f`   | float              | float             |        4        |
|  `d`   | double             | float             |        8        |
|  `s`   | char\[\]           | bytes             |                 |
|  `p`   | char\[\]           | bytes             |                 |
|  `P`   | void*              | integer           |                 |

## ENPAQUETAR

> [!abstract] SINTAXIS
> pack(***\[format\]***, ***\[data\]***)

## DESEMPAQUETAR

> [!abstract] SINTAXIS
> unpack(***\[format\]***, ***\[data\]***)

## FUNCIONES PROPIAS

### EMPAQUETACIÓN Y DESEMPAQUETACIÓN DE BOOLEANOS

```python
def pack_bool(
        bools: list[bool],
        offset_at_end: bool = True
    ) -> bytes:

    offset: int = len(bools) % 8

    if offset:
        offset = 8 - offset

    n_bytes: int = (len(bools) + offset) // 8

    if not n_bytes:
        return bytes()

    data: list[int] = [0] * n_bytes

    byte_index: int = 0

    if not offset_at_end:
        bools = ([False] * offset) + bools

    for bool_index in range(len(bools)):
        data[byte_index] <<= 1

        if bools[bool_index]:
            data[byte_index] += 1

        if bool_index % 8 == 7:
            byte_index += 1

    if offset_at_end:
        data[len(data) - 1] <<= offset

    return bytes(data)


def unpack_bool(bools: bytes) -> list[bool]:

    data: list[bool] = [False] * (len(bools) * 8)

    for byte_index in range(len(bools)):
        byte: int = bools[byte_index]

        for byte_bit_index in range(7, -1, -1):
            bit_index: int = byte_index * 8 + byte_bit_index

            data[bit_index] = bool(byte % 2)
            byte >>= 1

    return data
```
