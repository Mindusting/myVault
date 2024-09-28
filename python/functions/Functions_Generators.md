---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Fuction/Generator
title: Generadores en Python
---

# VÍDEO TUTORIALES

[Tech With Tim](https://youtu.be/u3T7hmLthUU)
[mCoding](https://youtu.be/tmeKsb2Fras)

Los generadores funcionan como una [función](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.4ved63vk9qq0) que usa la palabra clave “return”, con la diferencia de que este, al volver a ejecutarse, en vez de comenzar desde el principio, vuelve al estado en el que terminó de ejecutarse la última vez y continúa ejecutándose, para ello en vez de usar la palabra clave “return” usa “yield”.

### YIELD

[Curso de Python. Generadores I. Vídeo 19](https://youtu.be/TLVnoqXGWpY)

|   |
|---|
|Ej:|
|# Método del generador<br><br>def generador_binario():<br><br>  <br><br>    # Devuelve el valor "1"<br><br>    yield 1<br><br>    num = 2<br><br>  <br><br>    while True:<br><br>  <br><br>        # Devuelve el valor<br><br>        # de la variable "num"<br><br>        yield num<br><br>        num *= 2<br><br>  <br><br>  <br><br># Creación del generador<br><br>mi_generador = generador_binario()<br><br>  <br><br>for i in range(8):<br><br>  <br><br>    # Uso del generador<br><br>    print( next(mi_generador) )|

Como se puede ver en el ejemplo, el generador devuelve el valor “1”, después irá devolviendo el valor que contenga la variable “num” la cual irá aumentando en cada ciclo que se ejecute el generador, también se puede ver como se declara el generador, guardandolo en la variable “mi_generador”, este es usado en el [bucle for](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.w8e58zeesan7), haciendo uso de la [función](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.4ved63vk9qq0) “next”, está devolverá el próximo valor indicado con la palabra clave “yield”.

#### YIELD FROM

[Curso de Python. Generadores II. Vídeo 20](https://youtu.be/ucaHqGII350)

|   |
|---|
|Ej:|
|# Método del generador<br><br>def generador_matriz(matriz: list):<br><br>  <br><br>    for lista in matriz:<br><br>  <br><br>        yield from lista<br><br>  <br><br>  <br><br>mi_matriz = [<br><br>    ["manzana", "pera", "plátano"],<br><br>    ["pollo", "cerdo", "vaca"],<br><br>    ["cobre", "hierro", "oro"]<br><br>]<br><br>  <br><br># Creación del generador<br><br>generador_from = generador_matriz(mi_matriz)<br><br>  <br><br>for i in range(9):<br><br>  <br><br>    # Uso del generador<br><br>    print(f"{1 + i:3} : {next(generador_from)}")|

Como se puede ver en este ejemplo, la sintaxis de este [generador](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.ym3qqjya0j8c) es la misma que la del apartado [yield](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.5qe1q5s4l4wt), con la diferencia de que tras la palabra clave “yield” usa la palabra clave “from”, de forma que si seguido a esto indicamos una [colección](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.yxtkjlvtgt8z), siempre y cuenco no sea un [diccionario](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.7m7qt717qo3), irá devolviendo los valores guardados en la [colección](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.yxtkjlvtgt8z) de uno en uno, dando el efecto que tendría un [bucle](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.sbqufa7vxdts) [for-each](https://docs.google.com/document/d/1bfVIpraB3qlcHawNTioFMllMpYmXXwx_zfCFDvGoWDY/edit#heading=h.antpx05f3o8f).
