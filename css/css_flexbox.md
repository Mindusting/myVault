---
author: Mindusting
corrected: false
tags:
  - Programming/CSS/FlexBox
title: FlexBox en CSS3
---

# FLEXBOX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar el fin de esta propiedad.
> > - [ ] Explicar que son las propiedades de los padres.
> >     - [x] Documentar `display`.
> >     - [x] Documentar `flex-direction`.
> >     - [x] Documentar `flex-wrap`.
> >     - [x] Documentar `justify-content`.
> >     - [x] Documentar `align-items`.
> >     - [ ] Documentar `align-content`.
> > - [ ] Explicar que son las propiedades de los hijos.
> >     - [ ] Documentar `order`.
> >     - [ ] Documentar `flex-grow`.
> >     - [ ] Documentar `flex-shrink`.
> >     - [ ] Documentar `flex-basis`.
> >     - [ ] Documentar `align-self`.

## PROPIEDADES DE LOS PADRES

### DISPLAY

Para poder usar el *flexbox* tendremos que a la *etiqueta* **padre** la propiedad `display` con el valor `flex` o `inline-flex`.

> [!abstract] SINTAXIS
> display: flex;

%%
```html
<nav>
    <a href=""></a>
    <a href=""></a>
    <a href=""></a>
</nav>
```
%%

```css
/*
Hacemos que a las etiquetas nav
se les apliceque el flexbox.
*/
nav {
    display: flex;
}
```

### DIRECCIÓN

La **dirección** indica como se van a colocar los elementos **hijos**, la idea es que podemos indicar si queremos que se coloquen de izquierda a derecha o de arriba a bajo.

> [!abstract] SINTAXIS
> flex-direction: ***\[direction\]***;

- `row`: (*valor por defecto*) coloca los elementos de izquierda a derecha.
- `column`: coloca los elementos de arriba a abajo.
- `row-reverse`: es igual que `row` pero invirtiendo el orden.
- `column-reverse`: es igual que `column` pero invirtiendo el orden.

![#center](img/flexbox/flexbox_direction.md)

### WRAP

Esta propiedad permite indicar que los elementos **hijos** en caso de no caber dentro del elemento **padre** dentro de una misma línea, estos se reorganizarán en múltiples líneas.

> [!abstract] SINTAXIS
> flex-wrap: ***\[option\]***;

- `nowrap`: (*valor por defecto*) añade todos los elementos en la misma línea.
- `wrap`: si los elementos no entran en una línea, los que no entren saltarán a la siguiente, este proceso se puede repetir varias veces, dividiéndose en múltiples líneas.
- `wrap-reverse`: es lo mismo que `wrap`, pero de forma inversa.

![#center](img/flexbox/flexbox_wrap.md)

> [!note] Nota
> En la [imagen](img/flexbox/flexbox_wrap.md) se muestra como se reorganizan los elementos cuando la [dirección](#DIRECCIÓN) es de tipo `row` (*horizontal*).
> 
> Si la [dirección](#DIRECCIÓN) es de tipo `column`, funcionaría igual, con la diferencia que iría de arriba a abajo, y cuando ya no caben más elementos, estos irían a la siguiente columna.

> [!warning] Atención
> Para poder ver los efectos del `wrap` en el eje vertical, el elemento *padre* tendrá que tener una altura fija, ya que sino esta crecerá a más elementos *hijo* tenga, provocando que nunca haga el efecto de `wrap`.

### JUSTIFICADO

Esta propiedad permite indicar como queremos que se alineen los elementos *hijo* dentro del *padre*.

> [!abstract] SINTAXIS
> justify-content: ***\[option\]***;

- `flex-start`: coloca los *hijos* en el principio del *padre*.
- `flex-end`: coloca los *hijos* al final del *padre*.
- `center`: coloca los *hijos* en el centro del *padre*.
- `space-between`: separa los *hijos* al máximo, dejando los que se encuentran en los extremos pegados al margen del *padre*.
- `space-around`: pone dos separaciones igual a cada lado de cada *hijos*, haciendo que entre cada *hijo* haya dos separaciones y entre cada *hijo* extremo y el margen del *padre* haya una separación.
- `space-evenly`: separa todos los *hijos* de forma uniforme entre los propios *hijos* y los márgenes del *padre*.

![#center](img/flexbox/flexbox_justify.md)

### ALINEAR ELEMENTOS

Esta propiedad permite indicar como se deben alinear los elementos *hijos* sobre la línea en la que están colocados, debido a esto, es más fácil entender como funciona cuando se muestran elementos de distintos tamaños y en varias líneas gracias al [`wrap`](#WRAP).

> [!abstract] SINTAXIS
> align-items: ***\[option\]***;

- `flex-start`: alinea todos los elementos en la parte superior.
- `flex-end`: alinea todos los elementos en la parte inferior.
- `center`: alinea todos los elementos en el centro.
- `stretch`: deforma los elementos para que cubran todo el espacio.
- `baseline`: alinea los elementos en la base del texto.

![#center](img/flexbox/flexbox_align.md)

### ALINEAR CONTENIDO

Esta propiedad alinea todos los *hijos* del *padre* en bloque:

> [!abstract] SINTAXIS
> align-content: ***\[option\]***;

## PROPIEDADES DE LOS HIJOS
