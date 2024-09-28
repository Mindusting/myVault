---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/Clipboard
title: Módulo Clipboard en Python
---

Para poder usar el porta papeles se debe importar el módulo `clipboard` (***portapapeles***).

Así es como se importa el módulo `clipboard`:

```py
import clipboard
```

Este módulo es muy simple, ya que solo tiene dos métodos:

- `copy`
- `paste`

# COPIAR AL PORTAPAPELES

En el portapapeles se puede guardar un solo valor y debe ser de tipo [string](variables/py_str.md).

Para poder copiar texto al portapapeles se puede hacer de la siguiente forma:

```py
import clipboard

clipboard.copy("Este texto está en el portapapeles.")
```

>[!warning] CUIDADO AL COPIAR
>Cuidado cuando copies al portapapeles, el valor que esté guardado en ese momento, será sobre escrito por el nuevo.

# PEGAR DESDE EL PORTAPAPELES

Al pegar el contenido del portapapeles este siempre será de tipo [string](variables/py_str.md).

Para poder obtener el texto guardado en el porta papeles se hace de la siguiente forma:

```py
import clipboard

print(clipboard.paste())
```
