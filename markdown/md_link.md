---
author: Mindusting
corrected: false
tags:
  - MarkDown
title: Links en Markdown
---

<h1 style="text-align:center;">LINKS EN MARKDOWN</h1>

---

[Obsidian doc](<https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#External+links>)

Para asociar texto con un enlace este tiene que estar escrito entre corchetes y al final de estos tiene que haber unos paréntesis, dentro de estos paréntesis es donde se indicará el enlace del texto.

> [!abstract] SINTAXIS
> \[***\[text\]***\](***\[link\]***)

> [!example] Ej. de texto linkado con la sintaxis de MD:
> ```md
> [Mindusting Drive](https://drive.google.com/drive/folders/1swnODIsjZXUugHT9RhZvriEoluiGSe8E)
> ```
> > [!quote] Así es como se ve:
> > [Mindusting Drive](https://drive.google.com/drive/folders/1swnODIsjZXUugHT9RhZvriEoluiGSe8E)

> [!info] INFO
> También se puede poner la ruta y nombre de un archivo, de esta forma, el link nos llevará al archivo en vez de a una página web.

La forma de hacer enlaces es abriendo dos corchetes, escribimos el link y cerramos los dos corchetes, esto escribirá traslúcidas el link permitiendo usarlo como enlace.

> [!abstract] SINTAXIS
> \[\[***\[link\]***\]\]

## ENLACES INTERNOS

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR
> - [ ] El ejemplo de este apartado no funciona.

[Documentación oficial](<https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Internal+links>)

%%
Los enlaces internos funcionan de la misma forma que los enlaces normales, con la diferencia, que estos se hacen a través de los [encabezados](md_header.md), esto se hace escribiendo entre los paréntesis el nombre del encabezado (*Poniendo por delante una almohadilla*).

> [!error] COMPROBAR SI FUNCIONA EL SIGUIENTE EJEMPLO

> [!example] Ej. de enlace a encabezado:
> ```md
> # ENCABEZADO 1
> ## ENCABEZADO 1.1
>
> [E1](#ENCABEZADO%201)
> [E1.1](#ENCABEZADO%2011)
> [[#ENCABEZADO%201]]
> [[#ENCABEZADO%2011]]
> ```
>
> > [!quote] Así es como se ve:
> > # ENCABEZADO 1
> > ## ENCABEZADO 1.1
> >
> > [E1](<#ENCABEZADO 1>)
> > [E1.1](<#ENCABEZADO 11>)
> > [[#ENCABEZADO%201]]
> > [[#ENCABEZADO%2011]]

> [!info]
> Si te fijas en el ejemplo podrás ver cómo usa el `%20` como sustituto des espacio, esto es por qué el enlace hay que ponerlo de una pieza, por lo que para representa el espacio se hace con el `%` que indica que lo siguiente es un carácter especial y luego el `20`, este es el número en hexadecimal del espacio en la tabla ASCII.
%%

## LINK LITERAL

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR

https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Escape+blank+spaces+in+links

## ALIAS DE ENLACES

> [!error] ESTE APARTADO ESTÁ SIN TERMINAR
