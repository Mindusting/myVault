---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Exception
title: Clases y Ojetos en Python
---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

# CONTROL DE EXCEPCIONES

Una excepción es un error que ocurre mientras se está ejecutando nuestro programa, un ejemplo de esto sería cuando hacemos una división entre cero.

```py
1 / 0
```

Si intentamos ejecutar un archivo de Python con el contenido del anterior ejemplo obtendremos el siguiente resultado:

```txt
Traceback (most recent call last):
  File "/home/mindusting/python/main.py", line 1, in <module>
    1 / 0
    ~~^~~
ZeroDivisionError: division by zero
```

Como se puede ver en la ultima línea del resultado, nos indica que se ha producido una excepción de tipo `ZeroDivisionError`.

Si quisieramos controlar un área (Segmento de código) ya que sabemos que puede incidir en excepciones tendremos que usar la palabra clave `try` (Del Inglés "Intentar"), dentro de la sangría de esta meteremos el código que pueda incidir en una excepción, luego tendremos que usar la palabra clave `except` (Del Inglés "Excepción"), dentro de la sangría de esta pondremos el código que queramos que se ejecute en caso de que ocurra una excepción dentro de la sangría del `try`.

```py
num1 = 1`
num2 = 0

try:
    print(num1 / num2)
except:
    print("No se puede dividir entre cero.")
```

%%
Una excepción es un error en tiempo de ejecución, esto puede ocurrir cuando el código de un programa está bien escrito, pero el usuario introduce un valor de tipo string cuando se esperaba un valor de tipo int, para solucionar esto, deberemos hacer uso de la palabra clave `try` seguido de dos puntos, todo lo que metamos en su sangría será el código que va a intentar ejecutar y el cual tiene peligro de excepción, tras esto, se debe usar la palabra clave `except`, seguida de un tipo de error o no, para que se ejecute dando igual el tipo de error y dos puntos, dentro de su sangría deberemos indicar el código que queremos que se ejecute en caso de que ocurra la excepción indicada o genérica, como añadido, podemos usar la palabra clave `finally`, la cual ejecutará el código que se encuentre dentro de su sangría ocurra una excepción o no.

```py
while True:
    try:
        # Todo lo que se encuentre en esta sangría
        # se estará "supervisado" por el "try" para
        # comprobar que no ocurra ninguna excepción.

        x = float( input("Valor de X: ") )
        y = float( input("Valor de Y: ") )

        # En el caso de que no ocurra ninguna
        # excepción en alguna de las dos líneas
        # anteriores, se romperá el bucle, saliendo
        # de él y continuando con el programa.
        break

    except ValueError:
        # Este código se ejecutará en caso de que
        # ocurra una excepción de tipo "ValueError"

        print("Alguno de los valores introducidos no es válido.")
        print("Inténtalo de nuevo...")

    except:
        # Este código se ejecutará en caso de que
        # no haya ya un "except" concreto para
        # el tipo de excepción que ha ocurrido.

        print("A ocurrido una excepción.")
        print("Inténtalo de nuevo...")

    finally:
        # El código del "finally" se ejecuta
        # haya ocurrido una excepción o no.

        print("Esta línea se imprime haya excepción o no.")

# Usa las variables obtenidas en el anterior bucle
# para hacer una operación matemática.
print(f"{x} + {y} = {x + y}")
```
%%

[LANZAMIENTO DE EXCEPCIONES](exceptions/Exceptions_Raise.md)