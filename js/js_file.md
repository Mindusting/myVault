---
author: Mindusting
corrected: false
tags:
  - Programming/JS/File
title: Archivos de JS
---

Para crear un archivo de JS simplemente tenemos que coger un archivo de texto y darle la extensión `.js`.

Para poder vincular un archivo de JS a uno de HTML, en este último se debe crear un etiqueta de tipo *script*, entre la apertura y cierre de esta se puede poner el código del archivo JS, pero por lo general se suele poner a parte, en otro archivo , para ello, hay que indicar el atributo `src` (***source***) con el nombre del archivo JS.

>[!example] Ej. de vinculación de archivo de JS a HTML:
```html
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<title>Prueba</title>
</head>
<body>
	<script src="main.js"></script>
</body>
</html>
```