---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/TIME
title: Módulo TIME en Python
---

# TIME

Para importar el [módulo](py_module.md) `time` lo haremos de la siguiente forma:

```python
import time
```

Este módulo tiene tres funciones en especial:
- `time`:
    Esta función devuelve un valor [float](py_float.md) con el número de segundos transcurridos desde `1970-01-01 00:00:00`.
- `perf_counter`:
    Esta función devuelve un valor [float](py_float.md) con el número de segundos transcurridos desde que se encendió el equipo.
- `process_time`:
    Esta función devuelve un valor [float](py_float.md) con el número de segundos transcurridos desde que se inicio el proceso.
    Esta función no la recomiendo se se está usando múltiples núcleos, ya que el resultado no será el correcto, en su ligar usaría `perf_counter`.
- `time_ns`:
    El tiempo actual en nanosegundos.
