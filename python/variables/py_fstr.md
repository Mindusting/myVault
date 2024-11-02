---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/Str
title: F-String en Python
---

<h1 align="center">F-STRING EN PYTHON</h1>

---

# F-STRING EN PYTHON

## ESPACIADO

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[spacing\]***}"

```py
title: str = "ESTE ES MI TÍTULO"

print(f"Inicio:{title:30}:Fin.")
# SALIDA:
# Inicio:ESTE ES MI TÍTULO             :Fin.
```

Como se puede ver en este ejemplo, se puede reservar espacio para el valor que se quiera incrustar, en este caso se incrusta un título con una reserva de `30` caracteres, es por esto que el final de [string](py_str.md), donde pone `:Fin.` está tan apartado una vez se imprime el resultado.

---

```py
title: str = "ESTE ES MI TÍTULO"

spacing: int = 30

print(f"Inicio:{title:{spacing}}:Fin.")
# SALIDA:
# Inicio:ESTE ES MI TÍTULO             :Fin.
```

Como se puede ver en el ejemplo no es necesario escribir de forma directa el número de caracteres de espaciado que queremos reservar, si lo quisiéramos hacer más dinámico, podemos declarar una [variable](../py_variable.md) que contendrá el espaciado, y luego, a la hora de formatear el valor, indicamos entre otras llaves el formato que queremos darle, en este caso es a través de la [variable](../py_variable.md) `spacing` con el valor de `30`.

## ALINEACIÓN

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[aling\]\[spacing\]***}"

```py
title: str = "ESTE ES MI TÍTULO"

print(f"Inicio:{title:<30}:Fin.")
print(f"Inicio:{title:^30}:Fin.")
print(f"Inicio:{title:>30}:Fin.")
# SALIDA:
# Inicio:ESTE ES MI TÍTULO             :Fin.
# Inicio:      ESTE ES MI TÍTULO       :Fin.
# Inicio:             ESTE ES MI TÍTULO:Fin.
```

Como se puede ver, este ejemplo es muy parecido al anterior con la diferencia que a este le hemos añadido en donde queremos que se sitúe el elemento incrustado dentro del espacio reservado para él.

Para esto existen tres tipos de aliniación:
- `<` = Alinear a la izquierda.
- `^` = Centrar.
- `>` = Alinear a la derecha.

La alineación debe estar por delante del [espaciado](<py_fstr.md## ESPACIADO>).

---

```py
title: str = "ESTE ES MI TÍTULO"

aling: str = "^"
spacing: int = 30

print(f"Inicio:{title:{aling}{spacing}}:Fin.")
# SALIDA:
# Inicio:      ESTE ES MI TÍTULO       :Fin.
```

Como se puede ver en este ejemplo la alineación no tiene porqué estar en directamente en el formato, si no que se puede declarar una variable con el tipo de alineación que queremos e indicar entre llaves la [variable](../py_variable.md) que contiene el formato.

## RELLENO

El relleno no es más que los caracteres que se usan para llenar el espacio que quede en el formato si se usa el [espaciado](<py_fstr.md## ESPACIADO>), este debe colocarse por delante del [espaciado](<py_fstr.md## ESPACIADO>).

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[stuffed\]\[spacing\]***}"

```py
title: str = "ESTE ES MI TÍTULO"

print(f"{title:_^30}")
# SALIDA:
# ______ESTE ES MI TÍTULO_______
```

Como se puede ver en este ejemplo, el título está [centrado](<py_fstr.md## ALINEACIÓN>) dentro del [espaciado](<py_fstr.md## ESPACIADO>), siendo este rellenado con el carácter *barra baja*.

El relleno se pone por delante de la [alineación](<py_fstr.md## ALINEACIÓN>), en caso de que la haya.

---

```py
title: str = "ESTE ES MI TÍTULO"

stuffed = "~"

print(f"{title:{stuffed}^30}")
# SALIDA:
# ~~~~~~ESTE ES MI TÍTULO~~~~~~~
```

Como ya se a visto un los apartados anteriores, otra forma de indicar, en este caso el relleno, es a través una variable, dándole a ésta el valor del relleno y indicando la entre corchetes, esto también permite indicar caracteres que por lo general no se pueden hacer de la forma que se muestra en el primer ejemplo, como es este caso, en donde se usa la virgulilla (`~`).

## SEPARADOR DE MILLARES

El separador de millares permite ver los números grandes un una forma más sencilla.

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[thousands_sep]***}"

```py
num = 2 ** 64

print(f"{num}")
# SALIDA:
# 18446744073709551616

print(f"{num:,}")
# SALIDA:
# 18,446,744,073,709,551,616
```

Como se puede ver en este ejemplo, en la primera impresión se ve como todos los dígitos están pegados, de forma que es difícil leer el número, mientras que si especificamos que se aplique el separador de millares, como es el caso de la segunda impresión, los dígitos se agrupan de tres en tres, para ello, el formato se especifica con una *coma* (`,`), poniendo esta por detrás del [espaciado](<py_fstr.md## ESPACIADO>), también es posible usar un *barra baja* (`_`).

Por supuesto, esto mismo también se puede hacer de la misma forma que se a explicado en los apartados anteriores, pudiendo guardar el formato en una [variable](../py_variable.md).

## SIGNO

Si quieres que aparezca el signo *más* (`+`) en los número positivos se puede hacer poniendo un signo *más* (`+`) por delante del [espaciado](<py_fstr.md## ESPACIADO>) y por detrás de la [alineación](<py_fstr.md## ALINEACIÓN>).

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[signes\]\[thousands_sep]***}"

```py
num =  10

print(f"Número: {num:3}")
print(f"Número: {num:+3}")
# SALIDA:
# Número:  10
# Número: +10
```

Como se puede ver en este ejemplo en la primera impresión el número no tiene signo ya que es positivo, sin embargo, en la segunda impresión se le indica en el formato que queremos que se muestre el signo con el carácter *más* (`+`) provocando que si el número es positivo este se imprima con el signo *más* (`+`) por delante.

## PRECISIÓN

La precisión indica en qué dígito queremos que se redondee un número, para esto, primero ponemos *un punto* (`.`), seguido del dígito en el que queremos redondear y para finalizar, una *efe* (`f`).

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[precision\]***}"

```py
PI = 3.141592653589793

print(f"{PI:.4f}")
```
Como se puede ver en este ejemplo, el número *PI* es redondeado en el cuarto decimal ya que se ha especificado una precisión de cuatro.

Si la precisión es `0` se redondea a la unidad, si es `1` se redondea a la décima, si es `2` a la centésima y así constantemente, pero si es igual a `-1` redondea a la decena, si es `-2` redondea a la centena, y sí constantemente.

## INCRUSTACIÓN

También podemos imprimir [variables](../py_variable.md) y operaciones con estas, seguidas de se valor o resultado, para ello, deberemos escribir el nombre u operación seguida de un igual, esto imprimirá el nombre o la operación y al final el resultado, esto se puede entender mejor con el ejemplo.

```py
salario = 1_000.0
pagas = 12

print(f"{salario = :,} €")
print(f"{pagas = }")
print(f"{salario * pagas = :,} €")
# SALIDA:
# salario = 1,000.0 €
# pagas = 12
# salario * pagas = 12,000.0 €
```

Como se puede ver en el ejemplo, si escribimos el nombre de una [variable](../py_variable.md), seguido de un *igual* (`=`) o una operación [aritmética](../operators/Operators_Arithmetic.md).

```py
x = True
y = False

print(f"{x = }")
print(f"{y = }")
print(f"{not x = }")
print(f"{not y = }")
print(f"{x and y = }")
print(f"{x or y = }")
print(f"{(x != y) = }")
# SALIDA:
# x = True
# y = False
# not x = False
# not y = True
# x and y = False
# x or y = True
# (x != y) = True
```

Como se puede ver en este ejemplo, también se puede hacer con operadores [relacionales](../operators/Operators_Relational.md) y [lógicos](../operators/Operators_Logical.md).
