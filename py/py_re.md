---
aliases:
  - Expresión Regular
  - Regular Expresion
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/RE
title: Módolo RE en Python
---

# RE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [Python RE Doc](https://docs.python.org/es/3/library/re.html)
> - [W3 scools](https://www.w3schools.com/python/python_regex.asp)
>
> YouTube:
> - [Corey Schafer](https://youtu.be/K8L6KVGG-7o)
> - [FRIKIdelTO](https://youtu.be/7QUmK6cW_Rg)
> - [NeuralNine](https://youtu.be/wnuBwl2ekmo)

> [!faq] FAQ
> - [¿Qué son las expresiones regulares?](../regex/regex.md)

---

| Función                     | Descripción                                     |
|:--------------------------- |:----------------------------------------------- |
| [findall](py_re_findall.md) | Devuelve una lista con todas las coincidencias. |
| search                      | Devuelve un objeto `Match`.                     |
| split                       | Devuelve una lista con el texto troceado.       |
| sub                         | Remplaza las coincidencias.                     |

## REGEX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como se escriben los regex en Python.
> > - [ ] Añadir un enlace al archivo de regex.

## COINCIDE

> [!help] REFERENCIAS WEB
> - [RE (match)](https://docs.python.org/3/library/re.html#re.match)

> [!abstract] SINTAXIS
> match(***\[pattern\]***, ***\[string\]***, ***[\{flags\}](#BANDERAS)***)

- ***pattern***: (*obligatorio*) es la [expresión regular](#REGEX) para dividir el [*strings*](py_str.md).
- ***string***: (*obligatorio*) es el [texto](py_str.md) que va a ser dividido.
- ***flags***: [banderas](#BANDERAS) a aplicar sobre el proceso.

## ENCONTRAR TODO

La [función](py_function.md) `findall` devuelve una [lista](py_list.md) con [strings](py_str.md), siendo estos un extracto del [strings](py_str.md) original, el criterio para encontrarlo se indica en *pattern* con una [expresión regular](#REGEX).

- Es el inverso de [`split`](#TROCEADO).
- Si no se encuentra ninguna coincidencia, devuelve una [lista](py_list.md) vacía.

> [!abstract] SINTAXIS
> findall(***\[pattern\]***, ***\[string\]***, ***[\{flags\}](#BANDERAS)***)

- ***pattern***: (*obligatorio*) es la [expresión regular](#REGEX) para dividir el [*strings*](py_str.md).
- ***string***: (*obligatorio*) es el [texto](py_str.md) que va a ser dividido.
- ***flags***: [banderas](#BANDERAS) a aplicar sobre el proceso.

```python
pattern:  str = r"\d{4}(?:(?:/|-)\d{2}){2}(?: |T)\d\d(?::\d\d){2}"
string:   str = """\
2015/05/21
2008/06/07 11:49:16
2007-05-01T01:16:41
2002-02-19
"""

matches = re.findall(pattern, string)

for match in matches:
    print(match)
# SALIDA:
# 2008/06/07 11:49:16
# 2007-05-01T01:16:41
```

## TROCEADO

La [función](py_function.md) `split` devuelve una [lista](py_list.md) con [strings](py_str.md), siendo estos un extracto del [strings](py_str.md) original, el criterio para dividirlo se indica en *pattern* con una [expresión regular](#REGEX).

- Es el inverso de [`findall`](#ENCONTRAR%20TODO).

> [!abstract] SINTAXIS
> split(***\[pattern\]***, ***\[string\]***, ***\{maxsplit\}***, ***[\{flags\}](#BANDERAS)***)

- ***pattern***: (*obligatorio*) es la [expresión regular](#REGEX) para dividir el [*strings*](py_str.md).
- ***string***: (*obligatorio*) es el [texto](py_str.md) que va a ser dividido.
- ***maxsplit***: (*por defecto es 0*) indica el número de veces que se de aplicar el corte, di forma que si indicamos 1, solo se aplicará al primer *pattern* que coincida, aunque después haya otros, si se indica 0, se aplica a todos los *pattern* que se encuentren.
- ***flags***: [banderas](#BANDERAS) a aplicar sobre el proceso.

```python
import re

pattern:  str = r"\n\n"
string:   str = """\
Este es un texto de prueba
creado por Mindusting.

Esto es un segundo párrafo
creado para demostar que se
separan.
"""
maxsplit: int = 0

paragraphs = re.split(pattern, string, maxsplit)

print(paragraphs)

for i, paragraph in enumerate(paragraphs):
    print(f"El párrafo {i + 1} es:")
    print(f"{paragraph}\n")
# SALIDA:
# El párrafo 1 es:
# Este es un texto de prueba
# creado por Mindusting.
# 
# El párrafo 2 es:
# Esto es un segundo párrafo
# creado para demostar que se
# separan.
```

## SUSTITUCIÓN

La [función](py_function.md) `sub` sustituye los patrones que encuentre en el texto que le proveamos por otro que también le tendremos que proveer.

> [!abstract] SINTAXIS
> sub(***\[pattern\]***, ***\[repl\]***, ***\[string\]***, ***\{counts\}***, ***[\{flags\}](#BANDERAS)***)

- ***pattern***: (*obligatorio*) es al [expresión regular](#REGEX).
- ***repl***: (*obligatorio*) es el [string](py_str.md) que por el que va a ser sustituida las coincidencias del ***pattern***.
- ***string***: (*obligatorio*) es el texto sobre el que se va a trabajar.
- ***counts***: (*por defecto es 0*) indica el número de veces que debe aplicar la sustitución, de forma que si ponemos un 1, solo se aplicará a la primera coincidencia que se encuentre, si se pone 0, se aplica a todas las opciones.
- ***flags***: [banderas](#BANDERAS) a aplicar sobre el proceso.

```python
import re

pattern: str = r"\d{4}(?:(?:/|-)\d{2}){2}"
repl:    str = "2024-12-27"
string:  str = """\
Este es un texto de prueba creado por Mindusting
este va a ser usado para sustituir la fecha actual,
siendo esta 1984/01/01.

Sin embargo, somo he indicado que solo se debe hacer
con la primera coincidencia, la fecha 1969/07/21 no
va a ser modificada.
"""
counts:  int = 1

string = re.sub(pattern, repl, string, counts)

print(string)
# SALIDA:
# Este es un texto de prueba creado por Mindusting
# este va a ser usado para sustituir la fecha actual,
# siendo esta 2024-12-27.
# 
# Sin embargo, somo he indicado que solo se debe hacer
# con la primera coincidencia, la fecha 1969/07/21 no
# va a ser modificada.
```

## BANDERAS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar las banderas.

https://docs.python.org/3/library/re.html#flags

## META CARACTERES

![py_re_mc](Meta_Characteres/py_re_mc.md)

## SECUENCIAS ESPECIALES

---

# EXPLICACIÓN DE CHAT GPT 3.5

Claro, con gusto te explico el uso del módulo `re` en Python. El módulo `re` proporciona herramientas para trabajar con expresiones regulares (regex), que son patrones utilizados para buscar y manipular cadenas de texto de forma eficiente.

Aquí tienes una guía sobre las funciones y métodos más comunes del módulo `re`:

### 1. `re.match()`

Busca un patrón al comienzo de la cadena.

```python
import re

pattern = r'\d+'  # patrón para uno o más dígitos
text = "123abc"
match = re.match(pattern, text)

if match:
    print("Match encontrado:", match.group())
else:
    print("No hay match")
```

### 2. `re.search()`

Busca el patrón en toda la cadena y devuelve el primer match.

```python
import re

pattern = r'\d+'  # patrón para uno o más dígitos
text = "abc123xyz"
match = re.search(pattern, text)

if match:
    print("Match encontrado:", match.group())
else:
    print("No hay match")
```

### 3. `re.findall()`

Devuelve una lista con todos los matches del patrón en la cadena.

```python
import re

pattern = r'\d+'  # patrón para uno o más dígitos
text = "abc123xyz456"
matches = re.findall(pattern, text)

print("Matches encontrados:", matches)
```

### 4. `re.finditer()`

Devuelve un iterador con todos los matches del patrón en la cadena, donde cada match es un objeto `Match`.

```python
import re

pattern = r'\d+'  # patrón para uno o más dígitos
text = "abc123xyz456"
matches = re.finditer(pattern, text)

for match in matches:
    print("Match encontrado:", match.group(), "en la posición", match.start())
```

### 5. `re.split()`

Divide la cadena en una lista donde el patrón actúa como delimitador.

```python
import re

pattern = r'\d+'  # patrón para uno o más dígitos
text = "abc123xyz456"
split_text = re.split(pattern, text)

print("Texto dividido:", split_text)

```

### 6. `re.sub()`

Reemplaza todas las ocurrencias del patrón en la cadena con una cadena de reemplazo.

```python
import re

pattern = r'\d+'  # patrón para uno o más dígitos
text = "abc123xyz456"
replaced_text = re.sub(pattern, "NUM", text)

print("Texto reemplazado:", replaced_text)

```

### Expresiones Regulares Básicas

- `.`: Cualquier carácter excepto nueva línea.
- `^`: Inicio de la cadena.
- `$`: Fin de la cadena.
- `*`: Cero o más repeticiones.
- `+`: Una o más repeticiones.
- `?`: Cero o una repetición.
- `{n}`: Exactamente n repeticiones.
- `{n,m}`: Entre n y m repeticiones.
- `[abc]`: Cualquier carácter entre los corchetes (a, b o c en este caso).
- `[^abc]`: Cualquier carácter que no esté entre los corchetes.
- `(a|b)`: a o b.

### Ejemplo Completo

```python
import re

# Definir una cadena de ejemplo
text = "Mi número de teléfono es 123-456-7890 y mi correo es ejemplo@correo.com"

# Buscar un número de teléfono
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_match = re.search(phone_pattern, text)

if phone_match:
    print("Número de teléfono encontrado:", phone_match.group())

# Buscar una dirección de correo electrónico
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
email_match = re.search(email_pattern, text) 

if email_match:
    print("Correo electrónico encontrado:", email_match.group())
```

Espero que esta explicación te haya sido útil. Las expresiones regulares pueden ser muy poderosas y útiles para manejar cadenas de texto de manera avanzada.
