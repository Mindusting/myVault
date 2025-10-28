---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Module
  - Programming/Python/QRCode
title: Módulo QRCode en Python
rating: 0.75
---

# QR EN PYTHON

Este [módulo](py_module.md) permite crear una imagen de un `QR`, albergando este un texto, enlace o imagen que queramos.

Primero tendremos qué importar el [módulo](py_module.md) `qrcode`:

```python
import qrcode
```

Luego podemos crear un [objeto](py_class.md) de tipo `qrcode` y guardarlo, para ello se usa la [función](py_func.md) `make`, éste requiere de como mínimo un [`string`](py_str.md) o [`bytes`](py_bytes.md) que será la información que se guardará en el `QR`, después este para guardar el [objeto](py_class.md) usamos el [método](class/py_methods.md) `save`, este requiere de un [`string`](py_str.md) o [`bytes`](py_bytes.md) que indique la ruta y el nombre del archivo.

```python
import qrcode

qrcode.make("Hola mundo!!!").save("qr.jpg")
```

La [función](py_func.md) `make` también tiene dos argumentos, `box_size` y `border`, el primero por defecto es `10` e indica el tamaño en píxeles que tiene cada cuadro del `QR`, el segundo indica el número de cuadros de margen que tiene el `QR` alrededor:

```python
import qrcode

qrcode.make("Hola mundo!!!", box_size=1, border=1).save("qr.jpg")
```
