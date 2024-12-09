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

## FUNCIONES

| Función                     | Descripción                                     |
|:--------------------------- |:----------------------------------------------- |
| [findall](py_re_findall.md) | Devuelve una lista con todas las coincidencias. |
| search                      | Devuelve un objeto `Match`.                     |
| split                       | Devuelve una lista con el texto troceado.       |
| sub                         | Remplaza las coincidencias.                     |

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
