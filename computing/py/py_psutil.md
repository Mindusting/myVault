---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/psutil
title: Módulo psutil en Python
---

# PSUTIL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar `getLoadavg`.
> > - [ ] Documentar `users`.
> > - [ ] Documentar `win_service_iter`.
> > - [ ] Documentar `win_service_get`.
> > - [ ] Documentar `wait_procs`.
> > - [ ] Documentar `boot_time`.
> > - [ ] Documentar `cpu_count`.
> > - [ ] Documentar `cpu_freq`.
> > - [ ] Documentar `cpu_percent`.
> > - [ ] Documentar `cpu_stats`.
> > - [ ] Documentar `cpu_times`.
> > - [ ] Documentar `cpu_times_percent`.
> > - [ ] Documentar `Process`.
> > - [ ] Documentar `pids`.
> > - [ ] Documentar `pid_exists`.
> > - [ ] Documentar `process_iter`.
> > - [ ] Documentar `disk_io_counters`.
> > - [ ] Documentar `disk_partitions`.
> > - [ ] Documentar `disk_usage`.
> > - [ ] Documentar `swap_memory`.
> > - [ ] Documentar `virtual_memory`.
> > - [ ] Documentar `net_connections`.
> > - [ ] Documentar `net_if_addrs`.
> > - [ ] Documentar `net_if_stats`.
> > - [ ] Documentar `net_io_counters`.
> > - [ ] Documentar `sensors_battery`.

> [!help]- REFERENCIAS WEB
> - [psutil doc](https://psutil.readthedocs.io/en/latest/)
> - [PYPI (psutil)](https://pypi.org/project/psutil/)

- `getloadavg`

- `users`

- `win_service_iter`
- `win_service_get`

- `wait_procs`

## TIEMPO DE INICIO

- `boot_time`

Devuelve medido en segundos la fecha en la que se encendió en ordenador respecto al [*epoch*](../pc/pc_epoch.md).

## CPU

- `cpu_freq`
- `cpu_percent`
- `cpu_stats`
- `cpu_times`
- `cpu_times_percent`

### NÚMERO DE NÚCLEOS

Para obtener el número de procesadores de la máquina se usa la [función](py_func.md) `cpu_count`, esta función tiene el argumento `logical`, este por defecto está establecido a `True`, en el podremos indicar con un valor [booleano](py_bool.md) si queremos que sean los lógicos o no.

> [!abstract] SINTAXIS
> cpu_count(***\[logical\]***)

```python
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(False))
# SALIDA:
# 16
# 8
```

## PROCESS

- `Process`
- `pids`
- `pid_exists`
- `process_iter`

## DISK

- `disk_io_counters`
- `disk_partitions`
- `disk_usage`

## MEMORY

- `swap_memory`
- `virtual_memory`

## NET

- `net_connections`
- `net_if_addrs`
- `net_if_stats`
- `net_io_counters`

## BATTERY

- `sensors_battery`
