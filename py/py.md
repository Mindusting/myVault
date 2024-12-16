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

![#logo](../img/py_logo.png)

---

# PYTHON

> [!help] REFERENCIAS WEB
> - [Python doc](https://docs.python.org/es/3/)
> - [JavaTPoint (Python)](https://www.javatpoint.com/python-tutorial)

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
- [SLICES 📏](py_slice.md)
- [INPUT POR CONSOLA ⌨️](py_input.md)
- [ESTRUCTURAS DE DATOS](py_data_structure.md)
- [CONTROL DE FLUJO 🚦](py_flow_control.md)
- [BUCLES ➰](py_loop.md)
- [FUNCIONES 📞](py_function.md)
- [MAP 🗺](py_map.md)
- [BREAKPOINT 🔴](py_breakpoint.md)
- [CLASES 📦](py_class.md)
- [EXCEPCIONES ⚠️](py_exception.md)
- [MÓDULOS 🛄](py_module.md)
- [COMANDO PIP](py_pip.md)
- [ARCHIVOS EXTERNOS](py_file_manager.md)
- [GUI 🖼](gui/py_gui.md)

## MÓDULOS

- [MATH 🧮](math/py_math.md)
- [RANDOM 🎲](py_random.md)
- [OS](py_os.md)
- [RE](re/py_re.md)
- [SYS](py_sys.md)
- [PSTIL](py_psutil.md)
- [STRUCT](py_struct.md)
- [TIME ⌛](py_time.md)
- [JSON 🗃](py_json.md)
- [YAML](py_yaml.md)
- [HILOS 🧵](py_threading.md)
- [NUMPY 🧮](numpy/py_numpy.md)
- [EXCEL 🍫](openpyxl/py_openpyxl.md)
- [PANDAS 📈](py_pandas.md)
- [SQLITE3 🛢](py_sqlite3.md)
- [PORTA PAPELES 📋](py_clipboard.md)
- [PASSWORD 🔑](py_getpass.md)
- [QR 🔗](py_qr.md)
- [OPENSIMPLEX](py_opensimplex.md)
- [PYAUTOGUI 🖱️](py_pyautogui.md)
- [PYGAME 🕹️](pygame/py_pygame.md)

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
