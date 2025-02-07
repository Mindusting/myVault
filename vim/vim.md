---
author: Mindusting
corrected: false
tags:
  - Programming
title: VIM
---

<h1 style="text-align:center;color:#11AA11;">VIM</h1>

---

# VIM

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hacer imagen de portada.
> > - [ ] Explicar que es VIM.

```vimrc
syntax on

set number
set relativenumber

set autoindent
set expandtab
set tabstop=4
set shiftwidth=4

set mouse=a
```

- [Archivo temporal de VIM](temp_VIM.md)

VIM es un editor de texto plano diseñado para editar de forma eficiente.

---

Los directorios de configuración de VIM son los siguientes:

- Unix:
    - `~$HOME/.vimrc` o `~$HOME/.vim/vimrc`
- Windows:
    - `~$HOME/_vimrc` o `~$HOME/vimfiles/vimrc` o `~$VIM/_vimrc`

VIM no crea de forma automática estos archivos por lo que se debe crear.

---

# SPLIT SCREEN

## SPLIT

- `:sp` o `:split`: Split horizontal.
- `:vsp` o `:vsplit`: Split vertical.

## MOVE BETWEEN SPLITS

Se pulsa `<CTRL>` + `w` + tecla de movimiento (`h`, `j`, `k`, `l`).

## CLOSE SPLIT

- `:clo` o `:close`: Cerrar ventana.
- `:q`: Cerrar ventana y VIM.

## ONLY ONE WINDOW

Para cerrar todas las ventanas menos una: `:only`.

%%
# BUSQUEDA

To divide the Vim screen, you can use the following commands:

**Horizontal Split**

- `:split` or `:sp` - splits the screen horizontally
- `:vsp` or `:vsplit` - splits the screen vertically

**Moving Between Splits**

- `Ctrl + w + h` - move to the window on the left
- `Ctrl + w + j` - move to the window below
- `Ctrl + w + k` - move to the window above
- `Ctrl + w + l` - move to the window on the right

**Closing a Split**

- `:close` or `:clo` - close the current window
- `:q` - close the current window and quit Vim

**Other Options**

- `:only` - close all other windows and keep the current one
- `:only` + `Ctrl + w + w` - close all other windows and keep the current one, and then move to the next window

**Tips**

- You can also use the `:tabnew` command to open a new tab and split it horizontally or vertically.
- You can use the `:terminal` command to open a terminal in a split window.
- You can use the `:vsplit` command to split the screen vertically and open a file in the new window.
- You can use the `:split` command to split the screen horizontally and open a file in the new window.

**Example**

Here is an example of how to divide the Vim screen:

1. Open a file in Vim: `vim file.txt`
2. Split the screen horizontally: `:split`
3. Move to the new window: `Ctrl + w + j`
4. Open a new file in the new window: `:edit newfile.txt`
5. Split the screen vertically: `:vsp`
6. Move to the new window: `Ctrl + w + l`
7. Open a new file in the new window: `:edit anotherfile.txt`

Note: You can customize the behavior of the splits by adding commands to your `.vimrc` file.
%%

---

# SCROOL

## ONE LINE

- `<CTRL>` + `y`: Desplazar una línea hacia arriba.
- `<CTRL>` + `e`: Desplazar una línea hacia abajo.

## SCROLL HALF PAGE

En cualquiera de las dos opciones el cursor se centra en la ventana.

- `<CTRL>` + `u`: Media página hacia arriba.
- `<CTRL>` + `d`: Media página hacia abajo.

## CENTER

Para centra la ventana en el cursor se usa `zz`.
