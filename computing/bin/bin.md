---
alias: Binario
author: Mindusting
corrected: false
tags:
  - Binary
title: Binary
---

<h1 style="text-align:center;">BINARY</h1>

![#logo](../../img/retro_monitor.png)

---

# BINARIO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Core Dumped](https://youtu.be/HjneAhCy2N4)
> - [Josh's Channel](https://youtu.be/PMpNhbMjDj0)

El binario no es más que sistema de enumeración.

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## UNIDADES

| Nombre    | Sím. | Nombre   | Sím. | Nombre   | Sím. | Nombre  | Sím. |
|:--------- |:----:|:-------- |:----:|:-------- |:----:|:------- |:----:|
| KiloByte  |  kB  | KibiByte | kiB  | Kilobit  |  kb  | Kibibit | kib  |
| MegaByte  |  MB  | MebiByte | MiB  | Megabit  |  Mb  | Mebibit | Mib  |
| GigaByte  |  GB  | GibiByte | GiB  | Gigabit  |  Gb  | Gibibit | Gib  |
| TeraByte  |  TB  | TebiByte | TiB  | Terabit  |  Tb  | Tebibit | Tib  |
| PetaByte  |  PT  | PebiByte | PiB  | Petabit  |  Pb  | Pebibit | Pib  |
| ExaByte   |  EB  | ExbiByte | EiB  | Exabit   |  Eb  | Exbibit | Eib  |
| ZettaByte |  ZB  | ZebiByte | ZiB  | Zettabit |  Zb  | Zebibit | Zib  |
| YottaByte |  YB  | YobiByte | YiB  | Yottabit |  Yb  | Yobibit | Yib  |

## PUERTAS LÓGICAS

### NOT

La puerta lógica **NOT** está compuesta por una entrada y una salida.

| A | S |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

### AND

| A | B | S |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### OR

| A | B | S |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### XOR

![](../../img/logic_gate_xor.png)

>[!note]
>Si el número de inputs es par, las reglas son las siguientes:
>1. Si los inputs son todos iguales el resultado es False.
>2. Si el número de Falses es igual al número de Trues el resulado es False.
>3. Si el número de Falses es diferente del número de Trues, el resulado es True.
>
>Si el número de inputs es inpar, las reglas son las siguientes:
>1. Si todos los inputs son Trues el resulado es True.
>2. Si todos los inputs son Falses el resulado es False.
>3. Si el número de Trues es mayor que Falses, el resultado es False.
>4. Si el número de Falses es mayor que Trues, el resultado es True.

| A | B | S |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## FORMAS DE INTERPRETAR EL BINARIO

- [ENTERO](bin_int.md)
- [DECIMALES](bin_float.md)

## OPERAR EN BINARIO

- [SUMA](bin_add.md)

# OTROS

- [Multiplexer](bin_multiplexer.md)
- [De-Multiplexer](bin_de-multiplexer.md)
