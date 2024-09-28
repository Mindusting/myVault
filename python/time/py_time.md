---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/TIME
title: Módulo TIME en Python
---

> [!fail] ESTA APARTADO ESTÁ INCOMPLETO

Este módulo tiene tres funciones en especial:
- `time`:
    Esta función devuelve un valor float con el número de segundos transcurridos desde `1970-01-01 00:00:00`.
<br>
- `perf_counter`:
    Esta función devuelve un valor float con el número de segundos transcurridos desde que se encendió el equipo.
<br>
- `process_time`:
    Esta función devuelve un valor float con el número de segundos transcurridos desde que se inicio el proceso.

    Esta función no la recomiendo se se está usando múltiples núcleos, ya que el resultado no será el correcto, en su ligar usaría `perf_counter`.

---

- [time_time_ns](time_time_ns.md)
