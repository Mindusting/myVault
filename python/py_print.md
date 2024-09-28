---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Function
  - Programming/Python/Output
title: Output por consola en Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!todo] TODO
> - [ ] Hay que cambiar el estado de la primera impresión, ya que está todo metido en una anotación.
> - [ ] Buscar apara qué sirve el argumento `file`.
> - [ ] Buscar apara qué sirve el argumento `flush`.

Para poder aportar información al usuario, la forma más básica es a trabes de texto por consola, para poder hacer esto se usa la [función](py_function.md) `print` seguida de dos paréntesis, entre estos se indica que es lo que se quiere imprimir.

%%
SINTAXIS

```py
print([values])
```
%%

> [!abstract] SINTAXIS
> <span class="function-color">print</span>(<span class="italic grey">[values]</span>)

En el siguiente ejemplo lo primero que vemos es la función `print`  siendo usada para imprimir el texto `Hola mundo!!!` este está entrecomillado ya que esta es la forma de indicarle a *Python* que es un texto (*No tiene por qué ser comillas dobles, estas pueden ser comillas simples*).
```py
print("Hola mundo!!!")
```
---



En este ejemplo lo que vemos es la declaración de unas [variables](py_variable.md) (*Se verán en un próximo apartado*) para acto seguido ser usadas para completar el mensaje, siendo separados los diferentes valores por comas:

```py
name = "Mindusting"
age = 18

print("Aquí al habla", name, end=", ")
print("tengo", age, "años.")
```
Otra cosa que podemos ver en este anterior ejemplo es el **argumento** `end`, este indica que es lo que queremos que ponga la [función](py_function.md) `print` al final de esta misma, por defecto tiene un *salto de línea* (`\n`), el uso de los caracteres especiales como este se verá en un apartado a posteriori, en cualquier caso, si lo que quieres es poder usar varias veces la [función](py_function.md) `print` sin que se impriman los saltos de línea, lo que puedes hacer es darle al **argumento** `end` un texto vacío (`''`).

# SEPARACIÓN

El atributo `sep` (*abreviación de `separación` en inglés*) indica la separación que tendrán los elementos que hayamos indicado en el argumento `values`, por defecto el valor es `' '` (*un espacio*), pero podemos cambiarlo al [`string`](variables/py_str.md) que queramos:

```py
words: tuple[str] = ('Hola', 'mundo!!!')

print(*words)
print(*words, sep='-')
# SALIDA:
# Hola mundo!!!
# Hola-mundo!!!
```

> [!info] INFO
> En este ejemplo se hace uso de las [tuplas](collections/Collections_tuple.md) y su desempaquetamiento.

# FIN

El atributo `end` (*`fin` e[](collections/Collections_tuple.md)l final de la impresión de los  que hayamos indicado en el argumento `values`, por defecto el valor es `'\n'` (*un salto de línea*), pero podemos cambiarlo al [`string`](variables/py_str.md) que queramos:

```py
print('Hola mundo!!!', end='')
print('Hola mundo!!!')
print('Hola mundo!!!')
# SALIDA:
# Hola mundo!!!Hola mundo!!!
# Hola mundo!!!
```

Como se puede ver en el primer `print` tras escribir el `'Hola mundo!!!'` no salta el cursor a la siguiente línea, si no que se queda en donde está, por lo que al escribir el segundo `'Hola mundo!!!'` este se imprime seguido al anterior, como este segundo `print` sí tiene el salto de línea al final, el tercer `print` sí que imprime el texto en una línea nueva.

# ARCHIVO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

# FLUSH

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
