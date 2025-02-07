---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Class/Inheritance
title: Herencia de clases en Python
---

## HERENCIA

ATENCIÓN: Este apartado está incompleto, intentaremos completarlo lo antes posible, disculpen las molestias.

[Curso de Python. POO VI. Herencia. Vídeo 29](https://youtu.be/u_VbLsIyzRk?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

[Curso de Python. POO VII Herencia II. Vídeo 30](https://youtu.be/jMQQN9OxwVc?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

[Curso de Python. POO VIII. Herencia III. Vídeo 31](https://youtu.be/oe04X1B14YY?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

La herencia entre clases conlleva un comportamiento similar al de la herencia en la vida real, donde las clases hijo (subclase) hereda las características de la clase padre (superclase), esto se puede entender mejor viendo un ejemplo.

Para que una clase sea hija de otra, se debe poner entre los paréntesis de la subclase, el nombre de la superclase como se ve en la sintaxis y el ejemplo.

|   |
|---|
|SINTAXIS|
|class [Nombre de subclase]([Nom. de superclase 1], [Nom. de superclase 2], …):<br><br>    [Código de la clase]|

|   |
|---|
|Ej:|
|Define la clase padre (superclase).<br><br>class Persona:<br><br>   def __init__(self, nombre, edad):<br><br>       self.nombre = nombre<br><br>       self.edad = edad<br><br>   def saludar(self):<br><br>       print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")<br><br>  <br><br>Define la clase hijo (subclase).<br><br>class Estudiante(Persona):<br><br>   def __init__(self, nombre, edad, matricula):<br><br>       Llamamos al constructor de la superclase para inicializar los atributos de nombre y edad.<br><br>       super().__init__(nombre, edad)<br><br>       self.matricula = matricula<br><br>   def saludar(self):<br><br>       Llamamos al método saludar de la superclase.<br><br>       super().saludar()<br><br>       print(f"Soy estudiante con matrícula {self.matricula}.")<br><br>  <br><br>Creamos un objeto de la subclase.<br><br>estudiante = Estudiante("Juan", 20, "123456")<br><br>estudiante.saludar()<br><br>  <br><br>Imprime:<br><br>"""<br><br>Hola, soy Juan y tengo 20 años.<br><br>Soy estudiante con matrícula 123456.<br><br>"""|