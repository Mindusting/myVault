---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Ventanas en Tkinter
---

Para crear una ventana con `Tkinter` tenemos que crear un [objeto](../../py_class.md) de tipo `Tk`:

```py
root: tk.Tk = tk.Tk()

root.mainloop()
```

Como se puede ver en el ejemplo superior, primero creamos el [objeto](../../py_class.md) de tipo `Tk` y luego llamamos al [método](../../classes/py_method.md) `mainloop`, este indica que queremos que la ventana se mantenga activa hasta que se cierre.

Cuando empecemos a crear *elementos* (`widget`) para nuestra ventana, estos se declararán entre la declaración de la ventana y la llamada al `mainloop`.

# GEOMERÍA DE LA VENTANA

Para cambiar el tamaño de la ventana se usa al [método](../../classes/py_method.md) `geometry`, esta recibe un argumento de tipo [str](../../variables/py_str.md) con las medidas y la posición de la ventana.

```py
root: tk.Tk = tk.Tk()

root.geometry("360x240")

root.mainloop()
```

Como se puede ver en el ejemplo superior, hemos indicado que queremos que la ventana sea `360` pixeles de ancho y `240` pixeles de alto.

---

Si queremos indicar también la posición de la ventana lo haremos de la siguiente forma:

```py
root: tk.Tk = tk.Tk()

root.geometry("360x240+300+200")

root.mainloop()
```

Las coordenadas de la ventana funcionan desde su punto origen, este se encuentra arriba a la izquierda de esta, por lo que en este caso, la ventana se situará a `300` pixeles desde la izquierda de la pantalla y a `200` pixeles desde el techo de la pantalla.

---

Esto se puede combinar con el [f-string](../../Variables/py_str.md#F-STRING%20(Format) (Format)>) de la siguiente forma:

```py
root: tk.Tk = tk.Tk()

pos_x, pos_y  = (300, 200)
width, height = (360, 240)

root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

root.mainloop()
```

# REDIMENSIONABLE

De forma predeterminada, las ventanas de `Tkinter` son redimensionables, esto quiere decir que el usuario puede cambiar el tamaño de esta manteniendo el clic y arrastrando en uno de sus bordes, si queremos que esto no sea posible tendremos que usar el [método](../../classes/py_method.md) `resizable`, este recibe dos argumentos de tipo [booleano](../../variables/py_bool.md) siendo el primero para el eje en `x` y el segundo en `y`, si el valor que indicamos es `False`, ese eje no se podrá redimensionar, si es `True` si se podrá.

```py
root: tk.Tk = tk.Tk()

root.geometry("360x240")
root.resizable(False, False)

root.mainloop()
```
