---
author: Mindusting
corrected: true
tags:
  - Programming/JavaScript/File
title: Archivos de JS
---

# ARCHIVOS DE JS

Para crear un archivo de JS simplemente tenemos que coger un archivo de texto y darle la extensión `.js`.

Para poder vincular un archivo de [JS](js.md) a uno de [HTML](../html/html.md), se debe crear un etiqueta de tipo *script* en el archivo [HTML](../html/html.md), entre la apertura y cierre de esta se puede poner el código del archivo [JS](js.md), pero por lo general se suele poner aparte, en otro archivo; para ello, hay que indicar el atributo `src` (***source***) con el nombre del archivo [JS](js.md).

```html
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<title>Prueba</title>
</head>
<body>
    <!--
        A continuación tenemos la etiqueta `script`,
        esta permite que ejecutemos el contenido de
        archivo de JavaScript, indicando la ruta de
        este archivo mediante el atributo `src`
        (fuente) y `type` indicando con este último
        el tipo de archivo.
    -->
	<script src="main.js" type="text/javascript"></script>
</body>
</html>
```