---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Class/Method
title: Métodos en Python
---

# MÉTODOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Revisar todo el documento y hacer un TODO de las cosas que hay que cambiar.

> [!help] REFERENCIAS WEB
> YouTube:
> - [pildorasinformaticas](https://youtu.be/Y_SiIgxc-xI?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

Un **método** es una [función](../py_function.md) que se encuentra en el interior de una [clase](../py_class.md), al estar dentro de esta, el nombre que se le da es “**método**”, esto es debido a que así es más fácil diferenciar cuando nos referimos a si está dentro o fuera de una [clase](../py_class.md), por tanto para crear un método deberemos seguir la misma sintaxis que con las [funciones](../py_function.md).

Siguiendo con el ejemplo del [vector](../../math/math_vectors.md) de 

```python
class Vector:
    x: float = 0.0
    y: float = 0.0

    def distance(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

v = Vector()

v.x = 3.0
v.y = 4.0

print(v.distance())
# SALIDA:
# 5.0
```

Argumento

Como se puede ver en el ejemplo, dentro de la [clase](../py_class.md) `Vector` declaramos el **método** `distance`, 

%%
Como se puede ver en este ejemplo, la clase “user” contiene un [constructor](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.9s3d3f1sd07) “\_\_init\_\_” y dos métodos “get_name” y “set_name”, estos dos últimos sirven para interactuar con el objeto, pudiendo cambiar u obtener el nombre del mismo, de esta forma no interactuamos de forma directa con el valor de las [variables](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.1b13qrr2gfco) como sucede en el segundo ejemplo del apartado [clases y objetos](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.t8yympz7nzi8), más adelante, en el apartado [encapsulación](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.i1s1jqwbzgn3) veremos cómo evitar que se puede manipular [variables](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.1b13qrr2gfco) y métodos desde fuera de la clase.

Otra cosa que podemos observar en el ejemplo es el argumento “self” tanto en los métodos como en el [constructor](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.9s3d3f1sd07) la función que tiene este es la misma que la palabra clave “this” en otros lenguajes de programación, y es hacer referencia a la propia clase, si conoces cómo funciona los argumentos en las [funciones](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.4ved63vk9qq0) sabrás que tras terminar de ejecutarse la [función](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.4ved63vk9qq0), los valores almacenados en las [variables](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.1b13qrr2gfco) o [colecciones](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.yxtkjlvtgt8z) declarados dentro de la [función](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.4ved63vk9qq0) se borran, por lo que si queremos que se quede guardado en el objeto que estemos manejando, primero hacemos referencia al mismo con el argumento “self” seguido por un punto y el nombre de la [variable](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.1b13qrr2gfco) o [colección](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.yxtkjlvtgt8z) que queramos que forme parte del objeto o que ya forme parte del objeto y queramos obtener su valor o modificarlo.

Como se puede ver en el [constructor](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.9s3d3f1sd07), tiene el argumento “name”, esta [variable](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.1b13qrr2gfco) es completamente distinta a la que se declara dentro del [constructor](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.9s3d3f1sd07) “self.name”, debido a que la primera forma parte del [constructor](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.9s3d3f1sd07) mientras que la segunda forma parte de la clase, esta misma lógica se le aplica a los método, no solo a los [constructores](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.9s3d3f1sd07).
%%

# MÉTODOS ESTÁTICOS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

# MÉTODOS MÁGICOS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

[YT- mCoding (`__new__` vs `__init__`)](https://youtu.be/-zsV0_QrfTw)

> [!warning] WARNING
> Existe una diferencia sustancial entre los métodos `__div__`, `__truediv__` y `__floordiv__`.
> 
> La diferencia es que `__div__` es el usado para Python2, mientras qué `__truediv__` y `__floordiv__` son para Python3.
> 
> [FUENTES](https://stackoverflow.com/questions/29155829/operator-overloading-for-truediv-in-python)

<https://www.geeksforgeeks.org/dunder-magic-methods-python/>

## Initialization and contruction

- `__new__`
- `__init__`
- `__del__`

## Numeric

- `__trunc__` (`math.trunc()`)
- `__ceil__` (`math.ceil()`)
- `__floor__` (`math.floor()`)
- `__round__` (`round()`)
- `__invert__` (`~`)
- `__abs__` (`abs()`)
- `__neg__` (`-[class]`)
- `__pos__` (`+[class]`)

## Aritmetic

- `__add__` (`[class] + [class]`)
- `__sub__` (`[class] - [class]`)
- `__mul__` (`[class] * [class]`)
- `__div__` (`[class] / [class]` in `Python2`)
- `__truediv__` (`[class] / [class]` in `Python3`)
- `__floordiv__` (`[class] // [class]` in `Python3`)
- `__mod__` (`[class] % [class]`)
- `__divmod__` (`divmod([class], [class])`)
- `__pow__` (`[class] ** [class]`)
- `__lshift__` (`[class] << [class]`)
- `__rshift__` (`[class] >> [class]`)
- `__and__` (`[class] & [class]`)
- `__or__` (`[class] | [class]`)
- `__xor__` (`[class] ^ [class]`)

Todos estos tienen su propia variante con una `r` por delante para transformar el `[class] + [class]` en `[class] += [class]`.

## String

- `__str__` (`str([class])`)
- `__repr__` (`repr([class])`)
- `__unicode__` (`__str__` unicode version)
- `__format__` (New style of string)
- `__hash__` (`hash([class])`)
- `__nonzero__` (`bool([class])`)
- `__dir__` (Return a list of atributes of the class)
- `__sizeof__` (It returns the size of the object)

## Comparation

- `__eq__` (`[class] == [class]`)
- `__ne__` (`[class] != [class]`)
- `__lt__` (`[class] < [class]`)
- `__gt__` (`[class] > [class]`)
- `__le__` (`[class] <= [class]`)
- `__ge__` (`[class] >= [class]`)
