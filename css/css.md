---
author: Mindusting
corrected: false
tags:
  - Programming/CSS
title: CSS3
---

<h1 style="text-align:center;color:#48f;">CSS3</h1>

![#logo](css.png)

---

# VARIABLES


# CSS3

> [!help] REFERENCIAS WEB
> - [Mozilla](https://developer.mozilla.org/es/docs/Web/CSS/Using_CSS_custom_properties)
>
> YouTube:
> - [Web Dev Simplified](https://youtu.be/l1mER1bV0N0)

- [BootsTrap](css_bootstrap.md)

%%
Para aplicar variables globales se hace desde `:root`:

```css
:root {
    --my-var: #f00;
}

h1 {
    color: var(--my-var);
}
```

---

```css
img {
    image-rendering: pixelated;
}
```

---

```html
<style>
    h1[color='rojo'] {
        color: red;
    }
</style>
<h1>Header normal</h1>
<h1 color='rojo'>Header rojo</h1>
```

---
```html
<!doctype html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="style.css"/>
    </head>
    <body>
        <div class="difuminado element">
            <h1>MI TÍTULO</h1>
        </div>
    </body>
</html>

```

```css
body {
    background-color: #090909;
    color: #f9f9f9;
    font-family: Arial;
    background-image: url(ObsidianX10.png);
}

.difuminado {
    align-self: center;

    background-color: rgba(255, 255, 255, 0.0);
    border: solid 3px rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(16px);

    margin: 100px;
    padding-top: 100px;
    padding-bottom: 100px;
    border-radius: 16px;
}

h1 {
    text-align: center;
}

.element {
    border-radius: 5px;
    animation-name: desombrear;
    animation-duration: 0.5s;
}

@keyframes desombrear {
    from {box-shadow: 12px 12px 12px rgba(0, 0, 0, 0.1);}
    to {box-shadow: 12px 12px 12px rgba(0, 0, 0, 0.0);}
}


.element:hover {
    box-shadow: 12px 12px 12px rgba(0, 0, 0, 0.1);
    box-shadow: -12px -12px -12px white;
    animation-name: sombrear;
    animation-duration: 0.5s;
}

@keyframes sombrear {
    from {box-shadow: 12px 12px 12px rgba(0, 0, 0, 0.0);}
    to {box-shadow: 12px 12px 12px rgba(0, 0, 0, 0.1);}
}
```
%%