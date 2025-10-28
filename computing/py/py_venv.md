---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Entorno virtual en Python
---

# ENTORNO VIRTUAL EN PYTHON

> [!fail]- ESTE APATADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar que es un `venv`.
> > - [ ] Documentar como crear un `venv`.
> > - [ ] Documentar como activar un `venv`.
> > - [ ] Documentar como borrar un `venv`.

> [!help]- REFERENCIAS WEB
> - [Python (doc)](https://docs.python.org/3/library/venv.html)

Los entornos virtuales en Python en esencia son carpetas que se guardan dentro del directorio de nuestros proyectos para guardar la información de las librerías que queremos usar dentro de estas, evitando así problemas de compativilidad entre versiones de distintos proyectos y ganando mayor facilidad para compartir proyectos sin que estos fallen.

## CREACIÓN DE ENTORNO VIRTUAL

> [!abstract] SINTAXIS
> python3 -m venv ***\[venv\_name\]***

El nombre que se le suele dar a los entornos virtuales es `venv` o algún otro relacionado con el proyecto ensí.

> [!example] Por ejemplo:
> ```bash
> python3 -m venv .venv
> ```

## ACTIVACIÓN DE ENTORNO VIRTUAL

> [!abstract] SINTAXIS (Ubuntu)
> source ***\[venv\_name\]***/bin/activate

```bash
source .venv/bin/activate
```

---

> [!abstract] SINTAXIS (Windows)
> .\\***\[venv\_name\]***\\bin\\activate.bat

```powershell
.\.venv\bin\activate.bat
```

---

Tras activar el entorno virtual la línea de commandos cambiará mostrando entre paréntensis el nombre del entorno virtual.

> [!abstract] SINTAXIS (Ubuntu)
> (***\[venv\_name\]***) \$

```bash
(venv) $
```

## DESACTIVAR EL ENTORNO VIRTUAL



## BORRAR EL ENTORNO VIRTUAL
