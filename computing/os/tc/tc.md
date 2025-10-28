---
author: Mindusting
corrected: false
tags:
  - OS/TerminalControl
title: Control del terminal
---

# REFERENCIAS WEB

[HOWTO](https://tldp.org/HOWTO/Bash-Prompt-HOWTO/index.html)
[stack overflow](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)

> [!todo] #TODO
> - [ ] [Chequear en enlace](https://fusesource.github.io/jansi/)

# PÓLOGO

> [!warning] WARNING
> Si pretendes usar estos comando en Windows, primero debes ejecutar el comando `cls`, por alguna razón, después de esto sí funciona.
> 
> En el caso de Python, se puede ejecutar de la siguiente forma:
> ```python
> import os
>
> clear = lambda: os.system("cls" if "nt" == os.name else "clear")
> clear()
> ```

Para poder controlar el terminal se usa el carácter `ESC` (***ESCAPE***) seguido de una serie de caracteres que indican una instrucción.

El carácter `ESC` se puede representar en un `Stirng` de diferentes formas:

| OCTAL  | UNICODE  |
|:------:|:--------:|
| `\033` | `\u001b` |

La gran mayoría de la gente usa el octal ya que es más corto y fácil de recordar.

# FORMATO DEL TEXTO

Una vez aplicado el formato este se mantendrá hasta que se indique lo contrario.

Para modificar el formato del texto se escribe una *apertura de corchete* `[` y una *eme* `m`, entre estos podremos indicar diferentes argumentos, si quisiéramos indicar varios simultáneamente, tendremos que separarlos con un *punto y coma* (`;`).

| FORMAT        | ARG |
|:--------------|----:|
| Default       |   0 |
| Bold          |   1 |
| Dim           |   2 |
| Italic        |   3 |
| Undercore     |   4 |
| Blick         |   5 |
| Reverse       |   6 |
| Hidden        |   7 |
| Strikethrough |   8 |
| Undercore-2   |  21 |
| Overscore     |  53 |

> [!abstract] SINTAXIS
> \\033\[***\[arg\]***m
>
> \\033\[***\[arg\]***;***\[arg\]***;...m

> [!example] Ej. de cambio de formato del texto:
> ```txt
> \033[1m
>
> \033[1;3;4m
> ```

## COLOR DEL TEXTO

Para cambiar el color del texto se usan los siguientes valores.

| COLOR  | ARG | LIGHT COLOR  | ARG |
|:-------|----:|:-------------|----:|
| Black  |  30 | Light black  |  90 |
| Red    |  31 | Light red    |  91 |
| Green  |  32 | Light gree   |  92 |
| Yellow |  33 | Light yellow |  93 |
| Blue   |  34 | Light blue   |  94 |
| Pink   |  35 | Light pink   |  95 |
| Cyan   |  36 | Light cyan   |  96 |
| White  |  37 | Light white  |  97 |

> [!example] Ej. de cambio de color del texto:
> ```txt
> \033[32m
> ```

## COLOR DEL FONDO

Para cambiar el color del fondo se usan los siguientes valores, son los mismos que los de los colores del texto, pero sumándole `10` a cada uno.

| COLOR  | ARG | LIGHT COLOR  | ARG |
|:-------|----:|:-------------|----:|
| Black  |  40 | Light black  | 100 |
| Red    |  41 | Light red    | 101 |
| Green  |  42 | Light gree   | 102 |
| Yellow |  43 | Light yellow | 103 |
| Blue   |  44 | Light blue   | 104 |
| Pink   |  45 | Light pink   | 105 |
| Cyan   |  46 | Light cyan   | 106 |
| White  |  47 | Light white  | 107 |

> [!example] Ej. de cambio de color del fondo:
> ```txt
> \033[103m
> ```

## COLOR RGB

![](tc_rgb_color.md)

# CONTROL CURSOR

## POSICIONAR EL CURSOR

Para posición el cursor se escribe una *apertura de corchete* `[` y una *hache mayúscula* `H`, entre estos podremos indicar diferentes argumentos, como son la *línea* (`row`) y la *columna* (`col`), estando estos separados por un *punto y coma* (`;`), si no indicamos ninguno, se entenderá que queremos posicionar el cursor en el punto de origen, siendo este arriba a la izquierda.

> [!abstract] SINTAXIS
> \\033\[***\[row\]***;***\[col\]***H

> [!example] Ej. de posicionamiento del cursor:
> ```txt
> \033[H
>
> \033[3;2H
> ```

> [!info]
> Existe un alias de este último, y es con la letra *jota* `j`:
>
> ```txt
> \033[j
>
> \033[3;2j
> ```

## MOVER EL CURSOR

Para mover el cursor existen cuatro instrucciones.

| INSTRUCTION | CHAR |
|:------------|:----:|
| Up          |  `A` |
| Down        |  `B` |
| Left        |  `D` |
| Right       |  `C` |

> [!abstract] SINTAXIS
> \\033\[***\[num\]\[char\]***

El número indica el número de posiciones que queremos desplazar el cursor en la dirección qué hayamos indicado.

## SAVE AND USE CURSOR POSITION

Para guardar la posición actual del cursor se usa la letra *ese* (`s`), aparentemente no cambiará nada, ahora veremos para que nos puede servir esto.

> [!example] Ej. de como guardar la posición del cursor:
> ```txt
> \033[s
> ```

Una vez hayamos guardado la posición del cursor, podros devolverlo a esa posición usando la letra *u* (`u`).

> [!example] Ej. de como guardar la posición del cursor:
> ```txt
> \033[u
> ```

> [!info]
> Únicamente se podrá guardar una posición, es algo que hay que tener en cuenta.

## HIDE AND SHOW CURSOR

`\033[?25l`
`\033[?25h`

%%
- <https://askubuntu.com/questions/831971/what-type-of-sequences-are-escape-sequences-starting-with-033>

```python
# Cambia el tamapo del terminal

# Opción 1
print("\033[8;32;80t", end="")

# Opción 2
import os
os.system("mode 80, 32")
```

## Device Status

The following codes are used for reporting terminal/display settings, and vary depending on the implementation:

**Query Device Code	\<ESC>\[c**

- Requests a **Report Device Code** response from the device.

**Report Device Code	\<ESC>\[{code}0c**

- Generated by the device in response to **Query Device Code** request.

**Query Device Status	\<ESC>\[5n**

- Requests a **Report Device Status** response from the device.

**Report Device OK	\<ESC>\[0n**

- Generated by the device in response to a **Query Device Status** request; indicates that device is functioning correctly.

**Report Device Failure	\<ESC>\[3n**

- Generated by the device in response to a **Query Device Status** request; indicates that device is functioning improperly.

**Query Cursor Position	\<ESC>\[6n**

- Requests a **Report Cursor Position** response from the device.

**Report Cursor Position	\<ESC>\[{ROW};{COLUMN}R**

- Generated by the device in response to a **Query Cursor Position** request; reports current cursor position.

---

## Terminal Setup

The **h** and **l** codes are used for setting terminal/display mode, and vary depending on the implementation. Line Wrap is one of the few setup codes that tend to be used consistently:

**Reset Device		\<ESC>c**

- Reset all terminal settings to default.

**Enable Line Wrap	\<ESC>\[7h**

- Text wraps to next line if longer than the length of the display area.

**Disable Line Wrap	\<ESC>\[7l**

- Disables line wrapping.

---

## Fonts

Some terminals support multiple fonts: normal/bold, swiss/italic, etc. There are a variety of special codes for certain terminals; the following are fairly standard:

**Font Set G0		\<ESC>(**

- Set default font.

**Font Set G1		\<ESC>)**

- Set alternate font.

---

## Cursor Control

**Cursor Home 		\<ESC>\[{ROW};{COLUMN}H**

- Sets the cursor position where subsequent text will begin. If no row/column parameters are provided (ie. **\<ESC>\[H**), the cursor will move to the _home_ position, at the upper left of the screen.

**Cursor Up		\<ESC>\[{COUNT}A**

- Moves the cursor up by _COUNT_ rows; the default count is 1.

**Cursor Down		\<ESC>\[{COUNT}B**

- Moves the cursor down by _COUNT_ rows; the default count is 1.

**Cursor Forward		\<ESC>\[{COUNT}C**

- Moves the cursor _forward_ by _COUNT_ columns; the default count is 1.

**Cursor Backward		\<ESC>\[{COUNT}D**

- Moves the cursor _backward_ by _COUNT_ columns; the default count is 1.

**Force Cursor Position	\<ESC>\[{ROW};{COLUMN}f**

- Identical to **Cursor Home**.

**Save Cursor		\<ESC>\[s**

- Save current cursor position.

**Unsave Cursor		\<ESC>\[u**

- Restores cursor position after a **Save Cursor**.

**Save Cursor & Attrs	\<ESC>7**

- Save current cursor position.

**Restore Cursor & Attrs	\<ESC>8**

- Restores cursor position after a **Save Cursor**.

---

## Scrolling

**Scroll Screen		\<ESC>\[r**

- Enable scrolling for entire display.

**Scroll Screen		\<ESC>\[{start};{end}r**

- Enable scrolling from row **{start}** to row **{end}**.

**Scroll Down		\<ESC>D**

- Scroll display down one line.

**Scroll Up		\<ESC>M**

- Scroll display up one line.

---

## Tab Control

**Set Tab 		\<ESC>H**

- Sets a tab at the current position.

**Clear Tab 		\<ESC>\[g**

- Clears tab at the current position.

**Clear All Tabs 		\<ESC>\[3g**

- Clears all tabs.

---

## Erasing Text

**Erase End of Line	\<ESC>\[K**

- Erases from the current cursor position to the end of the current line.

**Erase Start of Line	\<ESC>\[1K**

- Erases from the current cursor position to the start of the current line.

**Erase Line		\<ESC>\[2K**

- Erases the entire current line.

**Erase Down		\<ESC>\[J**

- Erases the screen from the current line down to the bottom of the screen.

**Erase Up		\<ESC>\[1J**

- Erases the screen from the current line up to the top of the screen.

**Erase Screen		\<ESC>\[2J**

- Erases the screen with the background colour and moves the cursor to _home_.

---

## Printing

Some terminals support local printing:

**Print Screen		\<ESC>\[i**

- Print the current screen.

**Print Line		\<ESC>\[1i**

- Print the current line.

**Stop Print Log		\<ESC>\[4i**

- Disable log.

**Start Print Log		\<ESC>\[5i**

- Start log; all received text is echoed to a printer.

---

## Define Key

**Set Key Definition	\<ESC>\[{key};"{string}"p**

- Associates a _string_ of text to a keyboard key. **{key}** indicates the key by its ASCII value in decimal.

---

## Set Display Attributes

**Set Attribute Mode	\<ESC>\[{attr1};...;{attrn}m**

- Sets multiple display attribute settings. The following lists standard attributes:
    
    0	Reset all attributes
    1	Bright
    2	Dim
    4	Underscore
    5	Blink
    7	Reverse
    8	Hidden

    **Foreground Colours**
    
    30	Black
    31	Red
    32	Green
    33	Yellow
    34	Blue
    35	Magenta
    36	Cyan
    37	White

    **Background Colours**
    
    40	Black
    41	Red
    42	Green
    43	Yellow
    44	Blue
    45	Magenta
    46	Cyan
    47	White

```python
t_format = {
    # DEFAULT
    "df":            "\033[0m",
    "df-t":          "\033[39m",
    "df-b":          "\033[49m",

    # TEXT FORMAT
    "bold":          "\033[1m",
    "transparent":   "\033[2m",
    "italic":        "\033[3m",
    "underlined":    "\033[4m",
    "underlined-2":  "\033[21m",
    "strikethrough": "\033[9m",
    "overlined":     "\033[53m",
    "marked":        "\033[7m",
    "invisible":     "\033[8m",

    # TEXT COLORS
    "black-t":       "\033[30m",
    "red-t":         "\033[31m",
    "green-t":       "\033[32m",
    "yellow-t":      "\033[33m",
    "blue-t":        "\033[34m",
    "pink-t":        "\033[35m",
    "cyan-t":        "\033[36m",
    "white-t":       "\033[37m",

    # TEXT LIGHT COLORS
    "black-lt":      "\033[90m",
    "red-lt":        "\033[91m",
    "green-lt":      "\033[92m",
    "yellow-lt":     "\033[93m",
    "blue-lt":       "\033[94m",
    "pink-lt":       "\033[95m",
    "cyan-lt":       "\033[96m",
    "white-lt":      "\033[97m",

    # BACKGROUND COLOR
    "black-b":       "\033[40m",
    "red-b":         "\033[41m",
    "green-b":       "\033[42m",
    "yellow-b":      "\033[43m",
    "blue-b":        "\033[44m",
    "pink-b":        "\033[45m",
    "cyan-b":        "\033[46m",
    "white-b":       "\033[47m",

    # BACKGROUND LIGHT COLOR
    "black-lb":      "\033[100m",
    "red-lb":        "\033[101m",
    "green-lb":      "\033[102m",
    "yellow-lb":     "\033[103m",
    "blue-lb":       "\033[104m",
    "pink-lb":       "\033[105m",
    "cyan-lb":       "\033[106m",
    "white-lb":      "\033[107m"
}
```
%%
