---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/GetPass
title: Módulo GetPass en Python
---

# GETPASS

Para poder obtener contraseñas por parte del usuario de una forma más segura podemos usar el módulo `getpass`, este permitirá que el usuario escriba la contraseña por el terminal sin que se muestre lo que esté escribiendo.

Así es como se importa el [módulo](py_module.md) `getpass`:

```python
import getpass
```

## CONTRASEÑA

Para poder obtener una contraseña se hace uso del método `getpass`, este puede ejecutarse sin argumento, o se le puede indicar un [string](variables/py_str.md) para que sea este mensaje el que se imprima a la hora de obtener la contraseña.

```python
import getpass

password = getpass.getpass("Contraseña: ")
print(password)
```

## NOMBRE DE USUSARIO

Si queremos obtener el nombre del usuario del sistema podemos usar el método `getuser`.

```python
import getpass

user_name = getpass.getuser()
print(f"user: {user_name}")
```