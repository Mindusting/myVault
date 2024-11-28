---
author: Mindusting
corrected: false
tags:
  - Programming/Python/FlowControl
title: Match en Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> Hay que cambiar esto, ya que no es un switch como tal.

[¿Qué es un switch en la programación?](../pc/pc_switch.md)

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
