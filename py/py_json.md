---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Module
  - Programming/Python/JSON
title: Módulo JSON en Python
---

# JSON

> [!help] REFERENCIAS WEB
> - [Tech With Tim](https://www.youtube.com/@TechWithTim)
>     - [How To Use JSON In Python](https://youtu.be/-51jxlQaxyA)

Para poder manejar archivos [json](../../json/json.md) en Python se hace uso del módulo `json`.

```python
import json
```

# LEER Y ESCRIBIR ARCHIVOS

Para poder [leer y escribir archivos](py_file_manager.md) de [json](../../json/json.md), primero debes saber cómo [leer y escribir archivos](py_file_manager.md) en general.

## ESCRIBIR ARCHIVOS JSON

Para poder escribir en un archivo de [json](../../json/json.md), primero deberemos [abrir o crear un archivo](py_file_manager.md), para luego poder trabajar sobre él como un archivo [json](../../json/json.md).

Para poder guardar datos en un archivo [json](../../json/json.md) tendremos que hacer uso de la [función](py_function.md) `dump` (vertedero).

```python
data: dict = {
    "users": [
        {"name": "Mindusting", "age": 18, "height": 1.75},
        {"name": "Adelio", "age": 32, "height": 1.8}
    ],
    "products": [
        {"name": "Apple", "price": 3.5},
        {"name": "Banana", "price": 5}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file)
```

Tras ejecutar el ejemplo anterior, se crea el archivo `data.json` y se guarda en él el contenido del [diccionario](py_dict.md) `data`.

### SANGRÍA EN LOS ARCHIVOS

Si abres el archivo te encontrarás con que toda la información está escrita en una sola línea y es difícil de seguir el hilo, para poder guardar la información de una forma más estética (Consumiendo más espacio en el proceso), podemos hacer de la siguiente forma:

```python
data: dict = {
    "users": [
        {"name": "Mindusting", "age": 18, "height": 1.75},
        {"name": "Adelio", "age": 32, "height": 1.8}
    ],
    "products": [
        {"name": "Apple", "price": 3.5},
        {"name": "Banana", "price": 5}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

El parámetro `indent` (sangría) indica la sangría que queremos que tenga el archivo [json](../../json/json.md), este parámetro puede ser tanto un [`str`](py_str.md) como un [`int`](py_int.md).

En el caso de indicar un [`str`](py_str.md), por lo general, este suele ser `"\t"` para que la sangría se haga con una tabulación.

En el caso de indicar un [`int`](py_int.md), este indicará el número de espacios que queremos que tenga la sangría.

### SEPARADORES

En el caso de que quieras comprimir al máximo el contenido de los archivos [json](../../json/json.md), existe al posibilidad de usar el parámetro `separators`, este contiene una [tupla](py_tuple.md) con dos separadores, por defecto son `(", ", ": ")`, si te fijas, hay un espacio después del la coma y los dos puntos, estos también ocupan espacio a la hora de guardar el contenido, para ahorrarnos esos espacios podemos cambiar el valor de este parámetro para quitarle los espacios.

```python
data: dict = {
    "users": [
        {"name": "Mindusting", "age": 18, "height": 1.75},
        {"name": "Adelio", "age": 32, "height": 1.8}
    ],
    "products": [
        {"name": "Apple", "price": 3.5},
        {"name": "Banana", "price": 5}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, separators=(",", ":"))
```

Si te fijas en el antes y después, el espacio que ocupa el archivo cambia, ten en cuenta que cuanto más grande es el archivo más espacios se van a ahorrar, notando sé cada vez más la diferencia.

### ORDENAR EL CONTENIDO

Para ordenar alfabéticamente el contenido dentro del archivo se usa el parámetro `sort_keys`, este es de tipo [`bool`](py_bool.md), si lo indicamos con el valor de `True`, el contenido estará ordenado, si es `False`, lo guardará como en el orden en el que esté.

```python
data: dict = {
    "users": [
        {"name": "Mindusting", "age": 18, "height": 1.75},
        {"name": "Adelio", "age": 32, "height": 1.8}
    ],
    "products": [
        {"name": "Apple", "price": 3.5},
        {"name": "Banana", "price": 5}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, sort_keys=True)
```

## LEER ARCHIVOS JSON

Para poder leer el contenido de un archivo [json](../../json/json.md), se usa la [función](py_function.md) `load` (cargar), esta función devuelve en forma de [dictionario](py_dict.md) o [lista](py_list.md) (Esto depende del contenido del archivo [json](../../json/json.md)) el contenido del archivo.

```python
with open("data.json", "r") as file:
    data: dict = json.load(file)

print(data)
# SALIDA:
# {'users': [{'name': 'Mindusting', 'age': 18}, {'name': 'Adelio', 'age': 32}], 'products': [{'name': 'Apple', 'price': 3.5}, {'name': 'Banana', 'price': 5}]}
```

# CONVERSIÓN A STRING

Los métodos que se muestran en los próximos apartados son para transformar contenido de [json](../../json/json.md) en [`str`](py_str.md) y viceversa.

## DE STRING A JSON

Para transformar contenido [json](../../json/json.md) en [`str`](py_str.md) se usa la [función](py_function.md) `dumps`:

```python
with open("data.json", "r") as file:
    data: dict = json.load(file)

str_json: str = json.dumps(data)

print(str_json)
print(type(str_json))
```

El texto estará escrito en una sola línea al igual que pasa de forma predeterminada al [escribir el contenido en un archivo](#ESCRIBIR%20ARCHIVOS%20JSON), y al igual que este, también podemos usar los mismos parámetros para formatear el texto.

Gracias a esto último si sustituimos la línea en la hacemos la conversión por la siguiente, podremos imprimir el contenido de una forma más visual:

```python
str_json: str = json.dumps(data, indent=2)
```

## DE JSON A STRING

Para transformar contenido [`str`](py_str.md) o [`bytes`](py_byte.md) en contenido [json](../../json/json.md) se usa la [función](py_function.md) `loads`:

```python
str_data: str = '{"name": "Mindusting", "age": 18}'

data: dict = json.loads(str_data)

print(data["name"])
print(type(data))
```

Como se puede ver al final, se puede usar el diccionario perfectamente.
