---
author: Mindusting
corrected: false
tags:
  - Programming/HTML/Video
title: Vídeos en HTML5
---

# VÍDEOS EN HTML

> [!help]- REFERENCIAS WEB
> - [W3 (video)](https://www.w3schools.com/html/html5_video.asp)

Para insertar un vídeo, haremos uso de las etiquetas `video` y `source`, veremos que es posible usar solo la etiqueta `video`, pero para tener un mayor control de las especificaciones usaremos `source`.

## ESTRUCTURA BÁSICA

Veremos primero como podemos insertar un vídeo, esta no es la mejor forma en la que podemos hacerlo, recomiendo ver la [documentación avanzada](#ESTRUCTURA%20AVANZADA) para ver como lo tendríamos que hacer.

%%
```html
<video [atributes]></video>
```
%%

> [!abstract] SINTAXIS
> \<video ***\[atributes\]***\>\</video\>

Los atributos son los siguientes:
- `src`: sirve para indicar la URL o directorio en donde se encuentra el vídeo.
- `type`: nos permite indicar el [tipo de vídeo](#TIPOS%20DE%20VÍDEOS).
- `controls`: crea unos controles en el vídeo para que el usuario, pueda subir o bajar el volumen, maximizar el vídeo, avanzar o retroceder entre otras serie de cosas.
- `width`: permite indicar el ancho del vídeo.
- `heigth`: permite indicar el alto del vídeo.
- `autoplay`: hace que se empiece a reproducir automáticamente el vídeo.
- `muted`: hace que el vídeo comience con el volumen a cero.

## ESTRUCTURA AVANZADA

La forma avanzada de insertar vídeos es la más correcta de usar, esta es mediante la etiqueta `source` que pondremos entre la apertura y cierre de las etiquetas de vídeo.

%%
```html
<video [atributes]>
    <source src="[URL]" type="[type]">
</video>
```
%%

> [!abstract] SINTAXIS
> \<video ***\[atributes\]***\>
> <span class="transparency">····</span>\<source src="***\[URL\]***" type="***\[type\]***"\>
> \</video\>

La idea detrás de escribirlo de esta forma es que podemos indicar varios vídeos distintos, generalmente siendo realmente el mismo pero con formatos distintos, de esta forma, si el primero no es compatible, se hará uso del segundo y así sucesivamente.

```html
<video controls mute>
    <source src="./video.mp4" type="video/mp4">
    <source src="./video.ogg" type="video/ogg">
</video>
```

## TIPOS DE VÍDEOS

Para indicar el tipo de vídeo se escribe `video/` seguido del tipo:

| Formato de vídeo | Typo         |
|:---------------- |:------------ |
| MP4              | `video/mp4`  |
| WebM             | `video/webm` |
| Ogg              | `video/ogg`  |
