---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Condicionales en programación
rating: 0.5
---

# CONDICIONALES EN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## IF ELIF ELSE

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/python/python_conditions.asp)

> [!faq]- FAQ
> - [¿Qué son los condicionales en programación?](../pc/pc_conditionals.md)

Para crear una condición en Python se usa la palabra clave `if` seguido de la condición que se debe cumplir para ejecutar el código que indiquemos:

Para que el código de una condición se ejecute este tiene que recibir un valor `True` como condición, este le puede otorgar mediante una [variable](py_variable.md) [booleana](py_bool.md) o un [operador relacional](py_operators.md#RELACIONAL)

> [!abstract] SINTAXIS
> <span class="flow-word-color">if</span> <span class="italic grey">[condition]</span>:<br><span class="transparency">····</span><span class="italic grey">[code_if_true]</span>

```python
age: int = 18

if age >= 18:
    print("Eres mayor de edad.")
```

---

Por otro lado, si queremos que ejecute algo solo cuando la condición no se cumple, podremos hacerlo mediante la palabra clave `else`, esta no requiere de ningún **condicional**, pero sí debe estar precedida por uno.

> [!abstract] SINTAXIS
> <span class="flow-word-color">if</span> <span class="italic grey">[condition]</span>:<br><span class="transparency">····</span><span class="italic grey">[code_if_true]</span><br><span class="flow-word-color">else</span>:<br><span class="transparency">····</span><span class="italic grey">[code_if_false]</span>

```python
age: int = 18

if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

---

En caso de que queramos encadenar varias condiciones que sean excluyentes entre ellas, podremos hacerlo mediante la palabra clave `elif`, tiene la misma función que el `if`, con al diferencia a de que este debe estar precedido por otro condicional.

> [!abstract] SINTAXIS
> <span class="flow-word-color">if</span> <span class="italic grey">[condition]</span>:<br><span class="transparency">····</span><span class="italic grey">[code_if_true]</span><br><span class="flow-word-color">elif</span> <span class="italic grey">[condition]</span>:<br><span class="transparency">····</span><span class="italic grey">[code_if_true]</span><br><span class="flow-word-color">else</span>:<br><span class="transparency">····</span><span class="italic grey">[code_if_false]</span>

```python
age: int = 18

if age < 0:
    print("No puedes tener edad negativa.")
elif age >= 18:
    print("Eres mayor de edad.")
elif age >= 80:
    print("Qué afortunado de vivir tanto.")
else:
    print("Eres menor de edad.")
```

### CONDICIÓN

Una condición puede ser creada mediante los [operadores](py_operators.md), principalmente los [operador relacional](py_operators.md#RELACIONAL) y [operador lógicos](py_operators.md#LÓGICOS).

![](py_operators.md#^relational-operators-table)

![](py_operators.md#^logical-operators-table)

> [!example] Ejemplo
> ```python
> age:    int  = 18
> sleepy: bool = False
> 
> if age >= 16 and not sleepy:
>     print("Puedes trabajar.")
> else:
>     print("No estás en condiciones de trabajar.")
> ```
> 
> En este caso, la condición es que para trabajar debes tener 16 años o más y no debes tener sueño.

### IF-TERNARIO

Un **IF-Ternario** se lo mismo que un `if`, `else` con la diferencia de que este se escribe en una sola línea, se utiliza para sentencias simples.

> [!abstract] SINTAXIS
> <span class="italic grey">[code_if_true]</span> <span class="flow-word-color">if</span> <span class="italic grey">[condition]</span> <span class="flow-word-color">else</span> <span class="italic grey">[code_if_false]</span>

> [!example] Ejemplo
> ```python
> age: int = 18
> 
> # EJEMPLO 1
> text: str = 'mayor' if age >= 18 else 'menor'
> 
> print(f"Eres {text} de edad.")
> 
> # EJEMPLO 2
> print(f"Eres {'mayor' if age >= 18 else 'menor'} de edad.")
> ```
> 
> En este caso, simplemente decide entre un [string](sqlite3/py_sqlite3.md) y otro dependiendo de la condición.

> [!example] Ejemplo del uso
> Yo suelo usarlo para limpiar el terminal a través de una [función](py_func.md) y el [módulo](py_module.md) [`os`](os/py_os.md):
> ```python
> def clear() -> None:
>     os.system("cls" if "nt" == os.name else "clear")
> ```
> Antes de usar el `IF-Ternario` lo hacía con un `if` normal, pero no queda tan limpio:
> ```python
> def clear() -> None:
>     if "nt" == os.name:
>         os.system("cls")
>     else:
>         os.system("clear")
> ```

## MATCH

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que cambiar esto, ya que no es un switch como tal.

Los switch en Python usan dos palabras clave, `match` (*coincidir*) y `case` (*caso*).

%%
SINTAXIS

```python
match [value_to_match]:
    case [value_case]:
        [value_case_code]
    case _:
        [default_code]
```
%%

> [!abstract] SINTAXIS
> <span class="flow-word-color">match</span> <span class="italic variable-color">[value_to_match]</span>:<br><span class="transparency">····</span><span class="flow-word-color">case</span> <span class="italic variable-color">[value_case]</span>:<br><span class="transparency">········</span><span class="italic grey">[value_case_code]</span><br><span class="transparency">····</span><span class="flow-word-color">case</span> _:<br><span class="transparency">········</span><span class="italic grey">[default_code]</span>

Un ejemplo sencillo del uso del switch podría ser el siguiente:

```python
num_day: int = 4
match num_day:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Feliz Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Savado")
    case 7:
        print("Domingo")
    case _:
        print("Ese día no existe.")
```

%%
[Stack over flow](https://stackoverflow.com/questions/67961895/how-do-if-statements-differ-from-match-case-statments-in-python)
[Otro](https://learnpython.com/blog/python-match-case-statement)
%%
