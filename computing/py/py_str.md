---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/Str
title: Strings en Python
rating: 0.75
---

# STRING EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Depurar el código de este apartado para separarlo en diferentes ejemplos y documentarlos.
> > - [ ] Explicar que un string es un iterable de caracteres.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/python/python_strings.asp)
> - [W3 (Métodos)](https://www.w3schools.com/python/python_ref_string.asp)

```python
#print("101".zfill(8))
'''
Rellena con ceros a la izquierda
hasta llegar al número de dígitos
indicado.
'''

#print(f"|{'A'.center(9)}|")
'''
Centra el string en el espacio
reservado, siendo este de un ancho
igual al número indicado.
'''

#print("Fabricación".encode())
'''
Devuelve un array de bytes.
Es el equivalente a usar:
print(bytes("Fabricación", "UTF-8"))
'''

#print(" ".join(["Hola", "mundo!!!"]))
'''
Crea un str con los str del iterable,
estos los separa con el str del cual
se saca el método.
'''

"""
TAB = "	"

text = TAB + "Hola mundo!!!"

print(text)
print(text.expandtabs(4))
'''
Combierte el caracter de tabulación
en los espacios especificados, si
no se indica nada, el número por
defecto es 8.
'''
#"""

"""
TEXT = "Hola"
JUST = 9

print(f"|{TEXT.ljust(JUST)}|")
print(f"|{TEXT.rjust(JUST)}|")

print("".lstrip())
print("".rstrip())
#"""

#print("Hola mundo!!!\nHola mundo!!!".split())
#print("Hola mundo!!!\nHola mundo!!!".split("a"))
'''
Devuelve una lista separando cada
elemento por los espacios, \n, \t o \r.

Si se indica un argumento este separará
el texto en ese caracter.
'''

#print("Hola mundo!!!\nHola mundo!!!".splitlines())
'''
Devuelve una lista separando cada
elemento por los saltos de línea.
'''

#print("      Hola mundo!!!      ".strip())
'''
Devuelve el mismo str, pero
quitando todos los espación que
tenga por delante y por dentrás.
'''
```

```python
"""
Cuando queremos hacer un string de múltiples
líneas tenemos el incombeniente de que si
queremos que todo nos quede en el mismo nivel
probocaríamos que se genere un salto de línea
la principio de del string, para evitar esto
podemos poner una contrabara al principio del
todo para que no tenga en cuenta el salto de
línea.

Ahora veremos dos ejemplo, uno en el que se
aplica el cambio y otro en el que no, para 
poder ver la diferencia.
"""

normal: str = """
Hola
Mundo!!!
"""

corregido: str = """\
Hola
mundo!!!\
"""

print("-" * 10)
print(normal)
print("-" * 10)
print(corregido)
print("-" * 10)

"""
Como se puede ver con estos ejemplos, el salto
de línea se cancela si al final de esta
escribimos 
"""
```

```python
my_list: list = [char for char in "Hola"]
my_list: list = [*"Hola"]

print(my_list)
print(*my_list, sep="")
print("".join(my_list))
print(".".join(my_list))
```


## F-STRING

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hacer una explicación a cerca de el uso y utilidad que tiene el f-str.

### ESPACIADO

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[spacing\]***}"

```python
title: str = "ESTE ES MI TÍTULO"

print(f"Inicio:{title:30}:Fin.")
# SALIDA:
# Inicio:ESTE ES MI TÍTULO             :Fin.
```

Como se puede ver en este ejemplo, se puede reservar espacio para el valor que se quiera incrustar, en este caso se incrusta un título con una reserva de `30` caracteres, es por esto que el final de [string](#STRING), donde pone `:Fin.` está tan apartado una vez se imprime el resultado.

---

```python
title: str = "ESTE ES MI TÍTULO"

spacing: int = 30

print(f"Inicio:{title:{spacing}}:Fin.")
# SALIDA:
# Inicio:ESTE ES MI TÍTULO             :Fin.
```

Como se puede ver en el ejemplo no es necesario escribir de forma directa el número de caracteres de espaciado que queremos reservar, si lo quisiéramos hacer más dinámico, podemos declarar una **variable** que contendrá el espaciado, y luego, a la hora de formatear el valor, indicamos entre otras llaves el formato que queremos darle, en este caso es a través de la **variable** `spacing` con el valor de `30`.

### ALINEACIÓN

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[aling\]\[spacing\]***}"

```python
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

La alineación debe estar por delante del [espaciado](#ESPACIADO).

---

```python
title: str = "ESTE ES MI TÍTULO"

aling: str = "^"
spacing: int = 30

print(f"Inicio:{title:{aling}{spacing}}:Fin.")
# SALIDA:
# Inicio:      ESTE ES MI TÍTULO       :Fin.
```

Como se puede ver en este ejemplo la alineación no tiene porqué estar en directamente en el formato, si no que se puede declarar una variable con el tipo de alineación que queremos e indicar entre llaves la **variable** que contiene el formato.

### RELLENO

El relleno no es más que los caracteres que se usan para llenar el espacio que quede en el formato si se usa el [espaciado](#ESPACIADO), este debe colocarse por delante del [espaciado](#ESPACIADO).

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[stuffed\]\[spacing\]***}"

```python
title: str = "ESTE ES MI TÍTULO"

print(f"{title:_^30}")
# SALIDA:
# ______ESTE ES MI TÍTULO_______
```

Como se puede ver en este ejemplo, el título está [centrado](#ALINEACIÓN) dentro del [espaciado](#ESPACIADO), siendo este rellenado con el carácter *barra baja*.

El relleno se pone por delante de la [alineación](#ALINEACIÓN), en caso de que la haya.

---

```python
title: str = "ESTE ES MI TÍTULO"

stuffed = "~"

print(f"{title:{stuffed}^30}")
# SALIDA:
# ~~~~~~ESTE ES MI TÍTULO~~~~~~~
```

Como ya se a visto un los apartados anteriores, otra forma de indicar, en este caso el relleno, es a través una variable, dándole a ésta el valor del relleno y indicando la entre corchetes, esto también permite indicar caracteres que por lo general no se pueden hacer de la forma que se muestra en el primer ejemplo, como es este caso, en donde se usa la virgulilla (`~`).

### SEPARADOR DE MILLARES

El separador de millares permite ver los números grandes un una forma más sencilla.

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[thousands_sep]***}"

```python
num = 2 ** 64

print(f"{num}")
# SALIDA:
# 18446744073709551616

print(f"{num:,}")
# SALIDA:
# 18,446,744,073,709,551,616
```

Como se puede ver en este ejemplo, en la primera impresión se ve como todos los dígitos están pegados, de forma que es difícil leer el número, mientras que si especificamos que se aplique el separador de millares, como es el caso de la segunda impresión, los dígitos se agrupan de tres en tres, para ello, el formato se especifica con una *coma* (`,`), poniendo esta por detrás del [espaciado](#ESPACIADO), también es posible usar un *barra baja* (`_`).

Por supuesto, esto mismo también se puede hacer de la misma forma que se a explicado en los apartados anteriores, pudiendo guardar el formato en una **variable**.

### SIGNO

Si quieres que aparezca el signo *más* (`+`) en los número positivos se puede hacer poniendo un signo *más* (`+`) por delante del [espaciado](#ESPACIADO) y por detrás de la [alineación](#ALINEACIÓN).

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[signes\]\[thousands_sep]***}"

```python
num =  10

print(f"Número: {num:3}")
print(f"Número: {num:+3}")
# SALIDA:
# Número:  10
# Número: +10
```

Como se puede ver en este ejemplo en la primera impresión el número no tiene signo ya que es positivo, sin embargo, en la segunda impresión se le indica en el formato que queremos que se muestre el signo con el carácter *más* (`+`) provocando que si el número es positivo este se imprima con el signo *más* (`+`) por delante.

### PRECISIÓN

La precisión indica en qué dígito queremos que se redondee un número, para esto, primero ponemos *un punto* (`.`), seguido del dígito en el que queremos redondear y para finalizar, una *efe* (`f`).

> [!abstract] SINTAXIS
> f"{***\[var/func\]***:***\[precision\]***}"

```python
PI = 3.141592653589793

print(f"{PI:.4f}")
```
Como se puede ver en este ejemplo, el número *PI* es redondeado en el cuarto decimal ya que se ha especificado una precisión de cuatro.

Si la precisión es `0` se redondea a la unidad, si es `1` se redondea a la décima, si es `2` a la centésima y así constantemente, pero si es igual a `-1` redondea a la decena, si es `-2` redondea a la centena, y sí constantemente.

### INCRUSTACIÓN

También podemos imprimir **variables** y operaciones con estas, seguidas de se valor o resultado, para ello, deberemos escribir el nombre u operación seguida de un igual, esto imprimirá el nombre o la operación y al final el resultado, esto se puede entender mejor con el ejemplo.

```python
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

Como se puede ver en el ejemplo, si escribimos el nombre de una **variable**, seguido de un *igual* (`=`) o una operación [aritmética](py_operators.md#ARITMÉTICOS).

```python
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

Como se puede ver en este ejemplo, también se puede hacer con operadores [relacionales](py_operators.md#RELACIONAL) y [lógicos](py_operators.md#LÓGICOS).

## R-STRING

El término `R-String` es la abreviación de `Raw-String`, siendo *raw*, *crudo* en inglés, la diferencia entre este y un [`str`](#STRING), es que este, no tiene caracteres de escape, esto podemos verlo mejor con un ejemplo:

```python
print("\tHola mundo!!!")
print(r"\tHola mundo!!!")
# SALIDA:
#     Hola mundo!!!
# \tHola mundo!!!
```

Como se puede ver en el ejemplo, en el [`print`](py_print.md) que hemos usado el [`str`](#STRING) normal al haber indicado la tabulación con el `\t` se ha impreso en el resultado la tabulación como corresponde, sin embargo, en el caso del [`print`](py_print.md) con el `R-String` se ha impreso tal cual los caracteres de **contrabarra** y **te** (`\t`).

Para este punto ya te habrás dado cuenta gracias al ejemplo, y es que para indicar que queremos que un [`str`](#STRING) se interprete de forma cruda, simplemente tendremos que poner una `r` por delante de las comillas que conformen el [`str`](#STRING).

> [!note] Nota
> Este tipo de `string` se suele usar en las [expresiones regulares](py_re.md).
