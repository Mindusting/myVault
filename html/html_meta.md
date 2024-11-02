---
author: Mindusting
corrected: false
tags:
  - Programming/HTML
title: Etiqueta meta en HTML5
---

<h1 align="center">ETIQUETA META EN HTML5</h1>

---

# META

La etiqueta `meta` permite implementar meta-datos a nuestra página web, veamos unos ejemplos:

## CONJUNTO DE CARACTERES

Si queremos usar un conjunto de caracteres en específico, podremos hacerlo de la siguiente manera:

```html
<!DOCTYPE html>
<html>
    <head>
        <meta cahrset="UTF-8"/>
    </head>
</html>
```

En el caso del español se suele usar el `UTF-8` ya que es bastante completo, pudiendo usar las tildes en las bocales y la "ñ", el conjunto de caracteres que deberemos de usar dependerá del idioma en el que escribamos nuestra página.

## DESCRIPCIÓN

Si queremos darle a nuestra página una descripción, podremos hacerlo de la siguiente forma:

```html
<!DOCTYPE html>
<html>
    <head>
        <meta name="description"
            content="Esta es la descripcón de mi web."/>
    </head>
</html>
```

## PALABRAS CLAVE

Añadir palabras clave a nuestra página web permite que las personas cuando busquen a trabes de internet información, su buscador priorizará las páginas con las etiquetas que más se adecuen a lo que está buscando, por tanto es importante hacer uso de esta herramienta, ahora, no es recomendable poner más de cinco palabras clave, ya que esto hace que la página se califique como de poca calidad, esto es debido a que si no la gente podría en sus páginas todas las etiquetas posibles para que aparezca su página siempre que busque sin importar lo que sea.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta name="keywords"
            content="programación html"/>
    </head>
</html>
```

## REFRESCAR EL ENLACE

Si queremos que la página cambie automáticamente a una URL nueva cada X segundo, podemos hacerlo de la siguiente forma:

```
SINTAXIS:

<meta http-equiv="refresh"
content="[seconds]"
url="[newUrl]"/>
```

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="refresh"
            content="60"
            url="my_web.com"/>
    </head>
</html>
```

Esta etiqueta por lo genera el uso que se le da es para ganar más dinero, a costa de enfadar a la gente, esto ocurre ya que si tenemos anuncios en nuestra página, nosotros cobraremos por número de personas que entren en la página, si constantemente actualizamos la página y redirigimos al usuario a exactamente la misma página, lo que hará será contar como si hubiese entrado de nuevo, y así cobraremos dos veces los anuncios, ahora, esto no es muy agradable ya que dirigirá al usuario a la parte superior de la página, provocando que no sea fácil de leer. 
