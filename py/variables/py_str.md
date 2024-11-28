---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Variable/Str
title: Strings en Python
---

# STRING EN PYTHON

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [W3](https://www.w3schools.com/python/python_strings.asp)
> - [W3 (Métodos)](https://www.w3schools.com/python/python_ref_string.asp)

>[!todo]
>### TEMPORALES
>- [ ] Depurar el código de este apartado para separarlo en diferentes ejemplos y documentarlos.
>- [ ] Hay que explicar el `r-str` (row-string).

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

## OTROS

- [F-STRING (Format-String)](py_fstr.md)
- [R-STRING (Row-String)](py_rstr.md)
