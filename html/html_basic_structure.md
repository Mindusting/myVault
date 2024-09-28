---
author: Mindusting
corrected: false
tags:
  - Programming/HTML
title: Estructura básica de HTML5
---

<h1 align="center">ESTRUCTURA BÁSICA DE HTML</h1>

---

# ESTRUCTURA BÁSICA DE HTML

## TIPO DE DOCUMENTO

Especificar el tipo de documento le permite saber desde el primer a nuestro **navegador web** (*browser*) el tipo de documento que está manejado, por lo que lo interpretará de dicha forma, esto se usa para evitar errores a la hora de visualizar el contenido.

%%
SINTAXIS

```html
<!DOCTYPE [document_type]>
```
%%

>[!abstract] SINTAXIS
>\<!<span class="key-word-color">DOCTYPE</span> <span class="italic variable-color">[document_type]</span>\>

Este es un ejemplo de como se especifica el tipo de documento HTML5:

```html
<!DOCTYPE html>
```

## ETIQUETA HTML

> [!help] REFERENCIAS WEB
> - [W3 (html tag)](https://www.w3schools.com/tags/tag_html.asp)

La etiqueta `html` permite indicar el contendido de nuestra página web entre otras cosas como puede ser el idioma.

```html
<!DOCTYPE html>
<html lang="es">
    <!--
        Todo el contenido que se encuentre dentro
        de las etiquetas de apertura y cierre de
        `html` formará parte del contenido de nuestra
        página, a su vez, podremo sindicar el idioma
        de nuestra página con el atributo `lang`
        que viene del ingles (language), dandole el
        valor de `es` (español). 
    -->
</html>
```

## ETIQUETA HEAD

> [!help] REFERENCIAS WEB
> - [W3 (head tag)](https://www.w3schools.com/tags/tag_head.asp)

La etiqueta `head` permite indicar información de la página que no se va a ver en ella, como son por ejemplo los [metadatos](html_meta.md) entre otras cosas.

```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <!--
            Aquí pondremos la información de la
            página que no se verá.
        -->
    </head>
</html>
```

### ETIQUETA TITLE

> [!help] REFERENCIAS WEB
> - [W3 (title tag)](https://www.w3schools.com/tags/tag_title.asp)

La etiqueta `title` permite cambiar como su nombre indica, el título de la página, este hace referencia al texto que se muestra en la pestaña del **navegador web** (*browser*).

```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Esta es mi página.</title>
    </head>
</html>
```

## ETIQUETA BODY

> [!help] REFERENCIAS WEB
> - [W3 (body tag)](https://www.w3schools.com/tags/tag_body.asp)

La etiqueta `body` permite indicar que queremos que se muestre en nuestra página web.


```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Esta es mi página.</title>
    </head>
    <body>
        Este texto aparece en mi página web.
    </body>
</html>
```

En este caso he puesto como ejemplo un simple texto (*Aun que para añadir textos no es así como se debería hacer, si no con un [párrafo](html_text_format.md)*), pero también podremos poner por ejemplo [títulos](html_headers.md), [imágenes](html_img.md), [vídeos](html_videos.md) y [tablas](html_tables.md) entre otras cosas.
