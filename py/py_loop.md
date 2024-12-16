---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Loop
title: Bucles en Python
---

# BUCLES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #todo
> > - [ ] Rehacer la documentación del `while`.
> > - [ ] Documentar el `for`.
> > - [ ] Documentar el `do-while`.
> > - [ ] Documentar el `for-each`.
> > - [ ] Documentar el `break`.
> > - [ ] Documentar el `continue`.
> > - [ ] Documentar el `else`.
> > - [ ] Rehacer la documentación de bucle infinito.

> [!faq] FAQ
> - [¿Qué son lo bucles en programación?](../pc/pc_loop.md)
>     - [¿Qué es un bucle WHILE en programación?](../../pc/pc_loop.md)

## WHILE

Para crear un bucle `while` simplemente usamos la palabra `while` seguida de la [**operación lógica**](py_operators.md#LÓGICOS), tras terminar la [**operación lógica**](py_operators.md#LÓGICOS) ponemos dos puntos (`:`), a partir de este punto, todo lo que pongamos dentro de la [**sangría**](../py_indentation.md) se repetirá mientras la [**operación lógica**](py_operators.md#LÓGICOS) se cumpla.

%%
SINTAXIS

```python
while [condition]:
    [while_code]
```
%%

> [!abstract] SINSTAXIS
> <span class="flow-word-color">while</span> <span class="italic grey">[condition]</span>:<br><span class="transparency">····</span><span class="italic grey">[while_code]</span>

Un ejemplo de uso de bucle `while` podría ser el siguiente:

```python
answer = ""
while not answer:
    answer = input("Escribe tu nombre: ")
print(f"Tu nombre es: {answer}.")
```

## FOR

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## DO-WHILE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## FOR-EACH

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## BREAK

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## CONTINUE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## ELSE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## BUCLE INFINITO

Para hacer un bucle que se esté repitiendo de forma indefinida tendremos que hacer un bucle [`while`](#WHILE) con la condición valiendo siempre [`True`](py_bool.md):

```python
while True:
    print("Hola mundo!!!")
```

Por supuesto este bucle siempre se puede romper con un [`break`](#BREAK), o forzando el fin del programa, el crear un bucle infinito no implica que se nos vaya a quedar colgado el ordenador.

