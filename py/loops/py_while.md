---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Loop
title: Bucle WHILE en Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

[¿Qué es un bucle WHILE en programación?](../../pc/pc_loop.md)

Para crear un bucle `while` simplemente usamos la palabra `while` seguida de la [**operación lógica**](../operators/Operators_Logical.md), tras terminar la [**operación lógica**](../operators/Operators_Logical.md) ponemos dos puntos (`:`), a partir de este punto, todo lo que pongamos dentro de la [**sangría**](../py_indentation.md) se repetirá mientras la [**operación lógica**](../operators/Operators_Logical.md) se cumpla.

%%
SINTAXIS

```python
while [condition]:
    [while_code]
```
%%

> [!abstract] SINSTAXIS
> <span class="flow-word-color">while</span> <span class="italic grey">[condition]</span>:<br><span class="transparency">····</span><span class="italic grey">[while_code]</span>

[Operators_Logical](../operators/Operators_Logical.md)

Un ejemplo de uso de bucle `while` podría ser el siguiente:

```python
answer = ""
while not answer:
    answer = input("Escribe tu nombre: ")
print(f"Tu nombre es: {answer}.")
```

# SUBCATEGORÍAS

Este tipo de bucle tiene las siguientes subcategorías:

- [DO-WHILE 👉](py_do_while.md)
- [Bucle infinito](py_loop_fnfinite.md)
