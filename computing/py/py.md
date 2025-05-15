---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Python
---

<h1 align="center">
<span style="color:#48b;">PYT</span><span style="color:#ed5;">HON</span>
</h1>

![#logo](../../img/py_logo.png)

---

# PYTHON

> [!help]- REFERENCIAS WEB
> - [Python doc](https://docs.python.org/es/3/)
> - [JavaTPoint (Python)](https://www.javatpoint.com/python-tutorial)
> 
> YouTube:
> - [Clear Code](https://youtu.be/mDKM-JtUhhc)

> [!tip] TIP
> Si es la primera vez que programas, te recomiendo que compagines la lectura de esta documentación con la de [conceptos de la programación](../pc/pc.md) ya que ay ciertas cosas que se explican mucho más a fondo en esa documentación, ya que está orientada a ello, a diferencia de esta que está más orientada al aprendizaje de la sintaxis de Python.
>
> Igualmente, iré poniendo link a lo largo de la documentación que llevarán a los apartados comunes de cada tema.

> [!note] NOTE
> Es importante especificar que esta documentación está basada en Python3 por lo que si usas otra versión de Python puedes encontrarte con la posibilidad de qué no funcione lo que estás programando.

## ÍNDICE

- [AGRADECIMIENTOS 🎉](py_thanks_to.md)
- [PRÓLOGO 🧭](py_prologue.md)
- [ARCHIVOS DE PYTHON 📄](py_files.md)
- [COMENTARIOS 💬](py_comments.md)
- [OUTPUT POR CONSOLA 🖥️](py_print.md)
- [VARIABLES 💾](py_variable.md)
- [INPUT POR CONSOLA ⌨️](py_input.md)
- [SLICES 📏](py_slice.md)
- [ESTRUCTURAS DE DATOS](py_data_structure.md)
- [CONTROL DE FLUJO 🚦](py_flow_control.md)
- [BUCLES ➰](py_loop.md)
- [FUNCIONES 📞](py_function.md)
    - [MAP 🗺](py_map.md)
    - [FILTRO](py_filter.md)
    - [ZIP](py_zip.md)
    - [ENUMERATE](py_enumerate.md)
    - [GENERADORES](py_generator.md)
    - [DECORADORES](py_decorators.md)
- [SWITCH](py_switch.md)
- [ASSERT](py_assert.md)
- [BREAKPOINT 🔴](py_breakpoint.md)
- [CLASES 📦](py_class.md)
- [EXCEPCIONES ⚠️](py_exception.md)
- [MÓDULOS 🛄](py_module.md)
    - [VENV](py_venv.md)
    - [COMANDO PIP](py_pip.md)
- [ARCHIVOS EXTERNOS](py_open.md)
- [GUI 🖼](py_gui.md)

## MÓDULOS

- [DATETIME](py_datetime.md)
- [EXCEL 🍫](openpyxl/py_openpyxl.md)
- [HILOS 🧵](py_threading.md)
- [JSON 🗃](py_json.md)
- [MANIM](py_manim.md)
- [MATH 🧮](math/py_math.md)
- [MATHPLOTLIB](py_matplotlib.md)
- [NUMPY 🧮](numpy/py_numpy.md)
- [OPENSIMPLEX](py_opensimplex.md)
- [OS](py_os.md)
- [PANDAS 📈](py_pandas.md)
- [PASSWORD 🔑](py_getpass.md)
- [PATHFINDING](py_pathfinding.md)
- [PILLOW](py_pillow.md)
- [PORTA PAPELES 📋](py_clipboard.md)
- [PSUTIL](py_psutil.md)
- [PYAUTOGUI 🖱️](py_pyautogui.md)
- [PYGAME 🕹️](pygame/py_pygame.md)
    - [MIXER](pygame/mixer/pg_mixer.md)
- [QR 🔗](py_qr.md)
- [RANDOM 🎲](py_random.md)
- [RE](py_re.md)
- [SOCKET](socket/py_socket.md)
- [SQLCIPHER3 🛢](py_pysqlcipher3.md)
- [SQLITE3 🛢](sqlite3/py_sqlite3.md)
- [STRUCT](py_struct.md)
- [SYS](py_sys.md)
- [TIME ⌛](py_time.md)
- [XML](xml/py_xml.md)
- [YAML](py_yaml.md)
- [ZIPFILE 🗄️](zipfile/py_zipfile.md)

## TODO

> [!todo] #TODO
> - [ ] Documentar las [variables](py_variable.md).
> - [ ] Documentar el [control de flujo](py_flow_control.md).

```python
import os
import sys
import platform

print(os.path)
print(os.name)
print(sys.platform)
print(os.getcwd())
#os.chdir("..") # cd command
print(os.listdir())
#os.mkdir("tmp") # mkdir command
"""
for module in sys.modules:
    print(module)
#"""
print(platform.architecture())
print(platform.machine())
print(platform.processor()) # CPU
print(platform.platform()) # OS version
print(platform.system()) # OS
```

### GLOVAL

https://youtu.be/QYUbLevwgDQ
https://youtu.be/38uGbVYICwg
https://youtu.be/UEuXQjPUwcw

---

```python
gloval
glovals()

nonlocal


import py_compile
py_compile.compile("EXCEL_Worker.py")
```

---

### EJECUTAR FUNCIONES DE C EN PYTHON

- [stack overflow](https://stackoverflow.com/questions/16647186/calling-c-functions-in-python)

### VER VÍDEOS

- [ ] [Control de red local](https://youtu.be/DFTwB2nAexs)
