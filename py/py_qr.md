---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/QRCode
title: Módulo QRCode en Python
---

<h1 style="text-align:center;">QR</h1>

---

Este [módulo](py_module.md) permite crear una imagen de un `QR`, albergando este un texto, enlace o imagen que queramos.

Primero tendremos qué importar el [módulo](py_module.md) `qrcode`:

```python
import qrcode
```

Luego podemos crear un [objeto](py_class.md) de tipo `qrcode` y guardarlo, para ello se usa la [función](py_function.md) `make`, éste requiere de como mínimo un [`string`](py_str.md) o [`bytes`](py_byte.md) que será la información que se guardará en el `QR`, después este para guardar el [objeto](py_class.md) usamos el [método](classes/py_method.md) `save`, este requiere de un [`string`](py_str.md) o [`bytes`](py_byte.md) que indique la ruta y el nombre del archivo.

```python
import qrcode

qrcode.make("Hola mundo!!!").save("qr.jpg")
```

La [función](py_function.md) `make` también tiene dos argumentos, `box_size` y `border`, el primero por defecto es `10` e indica el tamaño en píxeles que tiene cada cuadro del `QR`, el segundo indica el número de cuadros de margen que tiene el `QR` alrededor:

```python
import qrcode

qrcode.make("Hola mundo!!!", box_size=1, border=1).save("qr.jpg")
```
