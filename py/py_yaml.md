---
author: Mindusting
corrected: true
tags:
  - Programming/Python/YAML
title: YAML en Python
---

# YAML EN PYTHON

> [!help] REFERENCIAS WEB
> - [Pypi](https://pypi.org/project/PyYAML/)
> - [Python Land](https://python.land/data-processing/python-yaml)
> - [GitHub (yaml/pyyaml)](https://msg.pyyaml.org/load)

> [!faq] FAQ
> - [¿Qué es el formato YAML?](../dump/yaml.md)

Para poder manejar tanto texto como archivos de formato `YAML`, haremos uso del módulo `yaml`.

## INSTALACIÓN

En caso de que no tengamos este módulo instalado, tendremos que usar el [instalador de paquetes de Python](py_pip.md) de la siguiente forma:

```bash
pip install PyYAML
```

## DE YAML A PYTHON

Para transformar un [`str`](py_str.md) con información en formato `YAML` en un [diccionario](py_dict.md) y/o [lista](py_list.md), tendremos que hacer uso de la [función](py_function.md) `safe_load.

```python
import yaml

text = """
cake: false
name: Mindusting
tag:
- Python
- YAML
"""

data = yaml.safe_load(text)

print(data)
# SALIDA:
# {'cake': False, 'name': 'Mindusting', 'tag': ['Python', 'YAML']}
```

---

En el siguiente ejemplo veremos como hacer lo mismo que en el anterior con la diferencia que en este no usamos un [`str`](py_str.md) sino un archivo.

***data.yml***:
```yaml
cake: false
name: Mindusting
tag:
- Python
- YAML
```

```python
import yaml

with open("data.yml", "r") as file:
    data = yaml.safe_load(file)

print(data)
# SALIDA:
# {'cake': False, 'name': 'Mindusting', 'tag': ['Python', 'YAML']}
```

## DE PYTHON A YAML

Para transformar un [diccionario](py_dict.md) y/o [lista](py_list.md) en un [`str`](py_str.md) con información en formato `YAML`, tendremos que hacer uso de la [función](py_function.md) `dump.

```python
import yaml

data = {
    'cake': False,
    'name': 'Mindusting',
    'tag': [
        'Python',
        'YAML'
    ]
}

text = yaml.dump(data)

print(text)
# SALIDA:
# cake: false
# name: Mindusting
# tag:
# - Python
# - YAML
```

---

En el siguiente ejemplo veremos como hacer lo mismo que en el anterior con la diferencia que en este no usamos un [`str`](py_str.md) sino un archivo.

```python
import yaml

data = {
    'cake': False,
    'name': 'Mindusting',
    'tag': [
        'Python',
        'YAML'
    ]
}

with open("data.yml", "w") as file:
    file.write(yaml.dump(data))
```

***data.yml***:
```yaml
cake: false
name: Mindusting
tag:
- Python
- YAML
```
