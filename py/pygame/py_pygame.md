---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/PyGame
title: PyGame en Python
---

# PYGAME

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> - [Real Python - PyGame](<https://realpython.com/pygame-a-primer/>)

Este módulo funciona de forma que sus clases son estáticas, pero se pueden asignar dentro de variables para poder usar estas a modo de álias.

%%
Ay que tener en cuenta que cuando el programa se termina la ventana se cierra automaticamente, para poder mantener la ventana activa, el programa debe segir en ejecución, por lo que es recomendable hacer un bucle al final para que se mantenga avierto, más adelante veremos como hacer para que detecte cuando pulsamos el botón de cerrar ventana para que este funcione.
%%

>[!quote] Así es como se importa `pygame`:
>```python
>import pygame as pg
>```

>[!example] Ej. de como iniciar y cerrar `pygame`:
>```python
>import pygame as pg
>
>pg.init()
>
>pg.quit()
>```
>En este ejemplo se puede ver como se importa el módulo `pygame` luego se inicia gracias al método `init`, para terminar cerrándolo con el método `quit`.

## CONFIGURACIÓN DE VENTANA

En este apartado veremos como

>[!example] Ej. de como asignar un tamaño a la ventana:
>```python
>import pygame as pg
>
>pg.init()
>
>screen_size: tuple[int] = (360, 240)
>
>root_window = pg.display.set_mode(screen_size)
>
>pg.quit()
>```
>En este ejemplo se puede ver como se declaran una tupla con las dimensiones de la ventana y luego se le asigna las dimensiones a la ventana, para ello, hemos llamado a al módulo `pygame`, dentro de este llamamos al módulo `display` y en este llamamos al método `set_mode`, todo esto lo guardamos en la variable `root_window` para poder usarlo posteriormente.
>
>Cabe resaltar, que estas nuevas instrucciones las hemos puesto entre el inicio y el cierre de la ventana.

### MANTENIMIENTO DE VENTANA

Debido a que cuando se termina de ejecutar el programa la ventana que hemos creado se cierra, lo que debemos hacer para que esta no se cierre es no permitir que el programa termine, esto se puede hacer con un simple [bucle while](<## WHILE ♾️>), esto probocaría que nuestra ventana se mantiviera abierta de forma constante, si lo que queremos es que se cierre cuando pulsemos la `x` de la ventana, para ello tendremos que obtener el **evento** `QUIT` esto de los eventos lo veremos más a fondo en un proximo apartado, de momento lo que tienes que saber es lo que se explica en el siguiente ejemplo.

>[!example] Ej. de como mantener la ventana abierta de forma indefinida:
>```python
>import pygame as pg
>
>pg.init()
>
>screen_size: tuple[int] = (360, 240)
>root_window = pg.display.set_mode(screen_size)
>
>loop_game: bool = True
>while loop_game:
>    events = pg.event.get()
>    for event in events:
>        if event.type == pg.QUIT:
>            loop_game = False
>
>pg.quit()
>```
>Como se puede ver en este ejemplo se crea un bucle el cual se ejecuta mientras la [variable](<# VARIABLES 💾>) `loop_game` sea igual a `True`, por cada iteración de este blucle, guardamos una [lista](<# LISTAS>) como todos los eventos que han transcurrido en ese ciclo, despues de esto creamos un [bucle for](<## FOR ➿>) el cual va recorrer todos los eventosque han ocurrido, y por cada uno de ellos comprueba si el tipo de evento es de `QUIT`, si es así establece la [variable](<# VARIABLES 💾>) `loop_game` a `False` para que no se siga repitiendo el bucle y se cierre la ventana.
>
>---
>
>```python
>import pygame as pg
>
>pg.init()
>
>screen_size: tuple[int] = (360, 240)
>root_window = pg.display.set_mode(screen_size)
>
>loop_game: bool = True
>while loop_game:
>    events = pg.event.get()
>    loop_game = not(pg.QUIT in tuple(map(lambda event: event.type, events)))
>
>pg.quit()
>```
>Otra forma de hacer esto mismo es a trabés de la clase [map](<# CLASE MAP 🗺️>).

### TÍTULO E ICONO

Las ventanas suelen tener un título y un icono, estos se pueden modificar para que se ajusten más al contenido de nuestro programa.

>[!example] Ej. de como cambiar el título e icono de la ventana:
>```python
>import pygame as pg
>
>pg.init()
>
>SCREEN_SIZE: tuple[int] = (360, 240)
>
>root_window = pg.display.set_mode(SCREEN_SIZE)
>
>pg.display.set_caption("Mindusting")
>img = pg.image.load("Mindusting.png")
>pg.display.set_icon(img)
>
>loop_game: bool = True
>while loop_game:
>    events = pg.event.get()
>    loop_game = not(pg.QUIT in tuple(map(lambda event: event.type, events)))
>
>pg.quit()
>```
>En este ejemplo se puede ver como se le cambia el subtítulo a la ventana haciendo uso del método `set_caption` del módulo `display` y para poder cambiarle la imagen al programa, primero deberemos de cargarla, para ello, desde el módulo `pygame` referenciamos el módulo `image` y de este usamos el método `load`, este método requiere de la ruta y el nombre de la imágen como argumento, esta imagen se guarda en la [variable](<# VARIABLES 💾>) `img` y luego esta [variable](<# VARIABLES 💾>) se pasa como argumento en el método `set_icon` en el módulo `display`.

## DIBUJADO EN VENTANA 🖌️

Para que poder visualizar cualquier cambio que hagamos en la venta, tendremos que indicar al módulo `display` que queremos que se apliquen los cambios, esto se hace con el método `flip`.

>[!quote] Ahí se aplican los cambios en la ventana:
>```python
>pg.display.flip()
>```
>Si queremos que se esté actualizando constantemente los cambios que vayamos haciendo en la ventana, tendremos que meter este método dentro de un [bucle](<# BUCLES>).

### PINTAR VENTACA COMPLETA

Para poder pintar toda la ventana por completo (*Normalmente para linpiar el contenido de la ventana*) se usa el método `fill`, este se encuentra en el objeto `display`.

>[!example] Ej. de como pitar la ventana de gris:
>```python
>import pygame as pg
>
>pg.init()
>
>SCREEN_SIZE: tuple[int] = (360, 240)
>
>root_window = pg.display.set_mode(SCREEN_SIZE)
>
>loop_game: bool = True
>while loop_game:
>    events = pg.event.get()
>    loop_game = not(pg.QUIT in tuple(map(lambda event: event.type, events)))
>
>    root_window.fill("#888888")
>
>    pg.display.flip()
>
>pg.quit()
>```
>Como se puede ver en este ejeplo, dentro del [bucle](<# BUCLES>) escribimos la línea `root_window.fill("#88888888")`, esto lo que proboca es que cada vez que se ejecute el [bucle](<# BUCLES>), toda la ventana pasará a tener el mismo **color gris** después de esto se escribe `pg.display.flip()` para aplicar los cambios.
>
>En este caso el color es indicado con un [string](<## STRIG 🔤>), otorgando los valores `RGB` en [hexadecimal](<## MANEJO DEL HEXADECIMAL>), pero también existe la posiblididad de pasar como argumento una [tupla](<## TUPLAS 📃>), con tres valores [enteros](<## INTEGER 🔢>) indicando los valores `RGB`.

### DIBUJAR LÍNA

Para dibujar una línea se puede usar el método `line` del módulo `draw`.

>[!abstract] SINTAXIS
>line(***\[surface\], \[color\] \[start_pos\] \[end_pos\] \[width\]***)
>
>##### ARGUMENTOS:
>
>- **surface**:
>    Indicamos el objeto `display` (*ventana*) en la que queremos dibujar la línea.
>- **color**:
>    Indicamos el color de la línea (`"#ff0000"` or `(255, 0, 0)`).
>- **start_pos**:
>    Coordenadas en las que inicia la línea (`(10, 20)`).
>- **end_pos**:
>    Coordenadas en las que ternima la línea (`(10, 20)`).
>- **width**:
>    Grosor en pixeles de la línea (`1`).

>[!example] Ej. de como dibujar una línea:
>```python
>import pygame as pg
>
>pg.init()
>
>SCREEN_SIZE: tuple[int] = (360, 240)
>
>root_window = pg.display.set_mode(SCREEN_SIZE)
>
>loop_game: bool = True
>while loop_game:
>    events = pg.event.get()
>    loop_game = not(pg.QUIT in tuple(map(lambda event: event.type, events)))
>
>    root_window.fill("#888888")
>
>    pg.draw.line(root_window, "#ffffff", (180, 120), (190, 140), 2)
>
>    pg.display.flip()
>
>pg.quit()
>```
>En este ejemplo se puede ver como se le llama al método `pg.draw.line()` para dibujar la línea.

---

Si lo qué queremos es dibujar múltiples líneas consecutivas, podemos usar el método `lines()` del módulo `draw`.

## AUDIO

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
> - https://youtu.be/ITk2QMjCMao

%%
```python
import numpy as np
import os
import random
import opensimplex as ops
import pygame as pg
from numba import njit
import time


def main() -> None:
    clear()

    screen_size = np.array((0xFF, 0xFF))

    pg.init()

    root = pg.display.set_mode(screen_size)

    arr = np.random.random((16, 16, 3))

    surf = pg.surfarray.make_surface(arr * 255)

    surf = pg.image.load("Mindusting.png")

    p_player = np.zeros(2)
    v_player = np.zeros(2)
    player_radious = np.array(np.array(surf.get_size()) / 2, dtype=np.uint8)

    old_time: float = time.perf_counter()

    while True:
        delta: float = time.perf_counter() - old_time
        old_time: float = time.perf_counter()

        events = pg.event.get()
        if pg.QUIT in tuple(map(lambda event: event.type, events)): break

        key_presed = pg.key.get_pressed()

        v_player[0] = key_presed[pg.K_d] - key_presed[pg.K_a]
        v_player[1] = key_presed[pg.K_s] - key_presed[pg.K_w]

        p_player += v_player * 100 * delta

        root.fill("#000000")

        root.blit(surf, p_player - player_radious)

        pg.display.flip()

    pg.quit()


def clear() -> None:
    os.system("cls" if "nt" == os.name else "clear")


if "__main__" == __name__:
    main()

```
%%
