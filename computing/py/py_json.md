---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/JSON
title: Módulo JSON en Python
rating: 0.5
---

# JSON EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Rehacer toda la documentación (*No me gusta como ha quedado, he vuelto a leerla porque no me acordaba como se hacía una cosa y no me ha gustado como se ve, es poco clara*).

> [!help]- REFERENCIAS WEB
> - [Tech With Tim](https://www.youtube.com/@TechWithTim)
>     - [How To Use JSON In Python](https://youtu.be/-51jxlQaxyA)

Para poder manejar archivos [json](../../dump/json.md) en Python se hace uso del módulo `json`.

```python
import json
```

Funciones 

- [`dump`](#GUARDAR%20EN%20ARCHIVO)
- [`dumps`](#COMBERTIR%20A%20TEXTO)
- [`load`](#CARGAR%20DESDE%20ARCHIVO)
- [`loads`](#COMBERTIR%20DESDE%20TEXTO)

## GUARDAR EN ARCHIVO

> [!abstract] SINTAXIS
> dump(***\[data\]***, ***\[file\]***)

```txt
dump(
    obj,
    fp,
    *,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
    **kw
)
Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
``.write()``-supporting file-like object).

If ``skipkeys`` is true then ``dict`` keys that are not basic types
(``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
instead of raising a ``TypeError``.

If ``ensure_ascii`` is false, then the strings written to ``fp`` can
contain non-ASCII characters if they appear in strings contained in
``obj``. Otherwise, all such characters are escaped in JSON strings.

If ``check_circular`` is false, then the circular reference check
for container types will be skipped and a circular reference will
result in an ``RecursionError`` (or worse).

If ``allow_nan`` is false, then it will be a ``ValueError`` to
serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)
in strict compliance of the JSON specification, instead of using the
JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).

If ``indent`` is a non-negative integer, then JSON array elements and
object members will be pretty-printed with that indent level. An indent
level of 0 will only insert newlines. ``None`` is the most compact
representation.

If specified, ``separators`` should be an ``(item_separator, key_separator)``
tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
``(',', ': ')`` otherwise.  To get the most compact JSON representation,
you should specify ``(',', ':')`` to eliminate whitespace.

``default(obj)`` is a function that should return a serializable version
of obj or raise TypeError. The default simply raises TypeError.

If *sort_keys* is true (default: ``False``), then the output of
dictionaries will be sorted by key.

To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
``.default()`` method to serialize additional types), specify it with
the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
```

## COMBERTIR A TEXTO

> [!abstract] SINTAXIS
> dumps(***\[data\]***) -> str

```txt
dumps(
    obj,
    *,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
    **kw
)
Serialize ``obj`` to a JSON formatted ``str``.

If ``skipkeys`` is true then ``dict`` keys that are not basic types
(``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
instead of raising a ``TypeError``.

If ``ensure_ascii`` is false, then the return value can contain non-ASCII
characters if they appear in strings contained in ``obj``. Otherwise, all
such characters are escaped in JSON strings.

If ``check_circular`` is false, then the circular reference check
for container types will be skipped and a circular reference will
result in an ``RecursionError`` (or worse).

If ``allow_nan`` is false, then it will be a ``ValueError`` to
serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in
strict compliance of the JSON specification, instead of using the
JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).

If ``indent`` is a non-negative integer, then JSON array elements and
object members will be pretty-printed with that indent level. An indent
level of 0 will only insert newlines. ``None`` is the most compact
representation.

If specified, ``separators`` should be an ``(item_separator, key_separator)``
tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
``(',', ': ')`` otherwise.  To get the most compact JSON representation,
you should specify ``(',', ':')`` to eliminate whitespace.

``default(obj)`` is a function that should return a serializable version
of obj or raise TypeError. The default simply raises TypeError.

If *sort_keys* is true (default: ``False``), then the output of
dictionaries will be sorted by key.

To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
``.default()`` method to serialize additional types), specify it with
the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
```

## CARGAR DESDE ARCHIVO

> [!abstract] SINTAXIS
> load(***\[file\]***) -> *data*

```txt
load(
    fp,
    *,
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
    **kw
)
Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
a JSON document) to a Python object.

``object_hook`` is an optional function that will be called with the
result of any object literal decode (a ``dict``). The return value of
``object_hook`` will be used instead of the ``dict``. This feature
can be used to implement custom decoders (e.g. JSON-RPC class hinting).

``object_pairs_hook`` is an optional function that will be called with the
result of any object literal decoded with an ordered list of pairs.  The
return value of ``object_pairs_hook`` will be used instead of the ``dict``.
This feature can be used to implement custom decoders.  If ``object_hook``
is also defined, the ``object_pairs_hook`` takes priority.

To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
kwarg; otherwise ``JSONDecoder`` is used.
```

## COMBERTIR DESDE TEXTO

> [!abstract] SINTAXIS
> loads(***\[str\]***) -> *data*

```txt
loads(
    s,
    *,
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
    **kw
)
Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
containing a JSON document) to a Python object.

``object_hook`` is an optional function that will be called with the
result of any object literal decode (a ``dict``). The return value of
``object_hook`` will be used instead of the ``dict``. This feature
can be used to implement custom decoders (e.g. JSON-RPC class hinting).

``object_pairs_hook`` is an optional function that will be called with the
result of any object literal decoded with an ordered list of pairs.  The
return value of ``object_pairs_hook`` will be used instead of the ``dict``.
This feature can be used to implement custom decoders.  If ``object_hook``
is also defined, the ``object_pairs_hook`` takes priority.

``parse_float``, if specified, will be called with the string
of every JSON float to be decoded. By default this is equivalent to
float(num_str). This can be used to use another datatype or parser
for JSON floats (e.g. decimal.Decimal).

``parse_int``, if specified, will be called with the string
of every JSON int to be decoded. By default this is equivalent to
int(num_str). This can be used to use another datatype or parser
for JSON integers (e.g. float).

``parse_constant``, if specified, will be called with one of the
following strings: -Infinity, Infinity, NaN.
This can be used to raise an exception if invalid JSON numbers
are encountered.

To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
kwarg; otherwise ``JSONDecoder`` is used.
```

---
---
---
---
---

# LEER Y ESCRIBIR ARCHIVOS

Para poder [leer y escribir archivos](py_open.md) de [json](../../dump/json.md), primero debes saber cómo [leer y escribir archivos](py_open.md) en general.

## ESCRIBIR ARCHIVOS JSON

Para poder escribir en un archivo de [json](../../dump/json.md), primero deberemos [abrir o crear un archivo](py_open.md), para luego poder trabajar sobre él como un archivo [json](../../dump/json.md).

Para poder guardar datos en un archivo [json](../../dump/json.md) tendremos que hacer uso de la [función](py_func.md) `dump` (vertedero).

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

El parámetro `indent` (sangría) indica la sangría que queremos que tenga el archivo [json](../../dump/json.md), este parámetro puede ser tanto un [`str`](py_str.md) como un [`int`](py_int.md).

En el caso de indicar un [`str`](py_str.md), por lo general, este suele ser `"\t"` para que la sangría se haga con una tabulación.

En el caso de indicar un [`int`](py_int.md), este indicará el número de espacios que queremos que tenga la sangría.

### SEPARADORES

En el caso de que quieras comprimir al máximo el contenido de los archivos [json](../../dump/json.md), existe al posibilidad de usar el parámetro `separators`, este contiene una [tupla](py_tuple.md) con dos separadores, por defecto son `(", ", ": ")`, si te fijas, hay un espacio después del la coma y los dos puntos, estos también ocupan espacio a la hora de guardar el contenido, para ahorrarnos esos espacios podemos cambiar el valor de este parámetro para quitarle los espacios.

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

Para poder leer el contenido de un archivo [json](../../dump/json.md), se usa la [función](py_func.md) `load` (cargar), esta función devuelve en forma de [dictionario](py_dict.md) o [lista](py_list.md) (Esto depende del contenido del archivo [json](../../dump/json.md)) el contenido del archivo.

```python
with open("data.json", "r") as file:
    data: dict = json.load(file)

print(data)
# SALIDA:
# {'users': [{'name': 'Mindusting', 'age': 18}, {'name': 'Adelio', 'age': 32}], 'products': [{'name': 'Apple', 'price': 3.5}, {'name': 'Banana', 'price': 5}]}
```

# CONVERSIÓN A STRING

Los métodos que se muestran en los próximos apartados son para transformar contenido de [json](../../dump/json.md) en [`str`](py_str.md) y viceversa.

## DE STRING A JSON

Para transformar contenido [json](../../dump/json.md) en [`str`](py_str.md) se usa la [función](py_func.md) `dumps`:

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

Para transformar contenido [`str`](py_str.md) o [`bytes`](py_bytes.md) en contenido [json](../../dump/json.md) se usa la [función](py_func.md) `loads`:

```python
str_data: str = '{"name": "Mindusting", "age": 18}'

data: dict = json.loads(str_data)

print(data["name"])
print(type(data))
```

Como se puede ver al final, se puede usar el diccionario perfectamente.
