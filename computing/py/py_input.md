---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Function
  - Programming/Python/Input
title: Input por consola en Python
---

# INPUT EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Corregir faltas de ortografía.
> >     - [ ] Comprobar si la documentación está bien hecha.

> [!help]- REFERENCIAS WEB
> - [Python doc (input)](https://docs.python.org/3/library/functions.html#input)

Para obtener información por parte del usuario a través del terminal se usa la [función](py_func.md) `input`, esta recibe un solo argumento (`prompt`), en este indicaremos lo que le aparecerá al usuario en el terminal justo antes de escribir la respuesta, en el momento en el que el usuario pulse la tecla `ENTER` todo lo que haya escrito se devolverá en forma de [`string`](py_str.md) a través de esta [función](py_func.md).

%%
SINTAXIS

```python
answer: str = input([prompt])
```
%%

> [!abstract] SINTAXIS
> <span class="variable-color">answer</span>: <span class="class-color">str</span> = <span class="function-color">input</span>(<span class="italic grey">[prompt]</span>)

Un ejemplo de uso que le podemos dar sería preguntarle al usuario cual es su nombre y luego saludarle con el nombre que haya escrito:

```python
user_name: str = input('Escribe tu nombre: ')

print(f'Hola {user_name}.')
```

---

Si queremos obtener un número (*Puede ser tanto [entero](py_int.md) como [decimal](py_float.md)*) antes de operar con él, se debe convertir:

```python
x: int = int(input('x: '))
y: int = int(input('y: '))

print(f'{x + y = }')
```

> [!success] FORMA CORRECTA
> ```python
> x = 3
> y = 2
>
> print(f'{x + y = }')
> # SALIDA:
> # x + y = 5
> ```

> [!failure] FORMA INCORRECTA
> ```python
> x = '3'
> y = '2'
>
> print(f'{x + y = }')
> # SALIDA
> # x + y = '32'
> ```
