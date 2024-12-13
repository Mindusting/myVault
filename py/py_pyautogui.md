---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/PyAutoGUI
title: Módulo PyAutoGUI en Python
---

# CONTROL DEL TECLADO Y RATÓN

> [!help] REFERENCIAS WEB
> - [Documentación oficial de PyAutGUI](<https://pyautogui.readthedocs.io/en/latest/>)

Este módulo nos permite controlar el tecla y el ratón, como puede ser, pulsar tecla, mover el cursor, hacer clic, tanto izquierdo como dereche, para ello, primero deberemos importar el módulo, y tenemos que tener en cuenta que este es dependiendo de otros mósulos como `tkinter` (*Entre otros*), por lo que si queremos usar ciertas funciones necesitaremos instalar en nuestro equipo los módulos a los cuales es dependiente.

>[!quote] Así es como se importa el módulo `pyautogui`:
>```python
>import pyautogui as pag
>```

## PANTALLA

>[!example] Ej. de como obtener las dimensiones del monitor:
>```python
>import pyautogui as pag
>
># Obtener las dimensiones de la pantalla principal
>screen_width, screen_height = pag.size()
>
>print(f"{screen_width = }")
>print(f"{screen_height = }")
># SALIDA:
># screen_width = 1920 
># screen_height = 1080
>```

## CURSOR

>[!example] Ej. de obtener la posición del cursor:
>```python
># Obtener la posición x e y del cursor.
>mouse_x, mouse_y = pag.position()
>
>print(f"{mouse_x = }")
>print(f"{mouse_y = }")
># SALIDA:
># mouse_x = 100
># mouse_y = 100
>```

>[!example] Ej. de mover el cursor a una coordenada de la pantalla:
>```python
>import pyautogui as pag
>
># Mover instantaneamente el cursor
># a la posición indicada.
>pag.moveTo(100, 100)
>
># Mover el cursor a la posición indicada
># tardano medio segundo en realizar el trallecto.
>pag.moveTo(200, 200, 0.5)
>```
>Como se puede ver en este ejemplo, primero movemos el cursor a la posición `100, 100` de forma instantánea y luego movemos el cursor a la posición `200, 200` tardando medio segundo en llegar a esa posición.

>[!example] Ej. de mover el cursor respecto a su posición:
>```python
>import pyautogui as pag
>
># Mover instantaneamente el cursor
># a la posición indicada, relativa
># a la posición del cursor.
>pag.move(100, 100)
>
># Mover el cursor a la posición relativa
># a la posición del cursor, tardando medio
># segundo en realizar el trallecto.
>pag.move(100, 100, 0.5)
>```
>Como se puede ver en este ejemplo, primero movemos el cursor `100, 100` pixeles desde su posición relativa de forma instantánea y luego movemos el cursor `200, 200` pixeles desde su posición relativa, tardando medio segundo en realizar ese movimiento.

>[!example] Ej. de como usar el clic:
>```python
>pag.click(x=500,
>          y=500,
>          clicks=2,
>          interval=0.1,
>          button="left",
>          duration=1.0)
>```
>No es necesario usar los argumentos que se muestran en este ejemplo, si no indicamos ningún argumento, simplemente haremos click, pero si indicamos los siguientes argumentos podremos hacer cosas más complejas.
>
>Con los argumentos `x` e `y`, se indica las coordenadas de la pantalla en la que queremos que se haga click.
>
>El argumento `clicks` indica el número de clicks que queremos que se hagan.
>
>el argumento `interval` indica en segundos el tiempo que queremos que se transcurra entre los diferentes clicks.
>
>El argumento `button` indica el botón del ratón que queremos que se pulse, este puede tener los siguientes valores:
>
>- "left"
>- "middle"
>- "right"
>
>El argumento `duration` indica el tiempo en segundo que queremos que tarde en realizar el recorrido hasta las coordenadas indicadas.

## TECLADO

>[!fail]- ESTE APARTADO ESTÁ INCOMPLETO

```python
# Escribe el texto con un intervalo de
# 0.15 segundo por carácter.
pag.write("Hola mundo!!!", interval=0.15)
```

---

```python
import pyautogui as pag

#"""
# Pulsa la tecla indicada
# (Se mantiene pulsada)
pag.keyDown("a")
# Despulsa la tecla indicada
pag.keyUp("a")
#"""

#"""
# Pulsa el M1
pag.click()
#"""

#"""
# Presiona M2
pag.rightClick()
#"""

#"""
# El mouse se mueve respecto a origen
pag.moveTo(100, 100, 1)
#"""

#"""
# El mouse se mueve de forma relativa
pag.moveRel(100, 100, 1)
#"""

#"""
# Debuelve una tupla con las medidas de la pantalla
print(pag.size())
#"""
```