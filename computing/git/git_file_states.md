---
author: Mindusting
corrected: false
tags:
  - Programming/Git
title: Estados de los archivos en Git
---

# ESTADOS DE LOS ARCHIVOS EN GIT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para comprobar en qué estado se encuentran los archivos consulta el comando [`status`](git_status.md).

![#fillall](img/file_life_cicle_state.md)

- **Untraked**: 
    El archivo no está siendo vigilado por **Git**; este es en el estado en le que se encuentran todos los archivos nuevo a los que no le hemos indicado a **Git** que debe vigilar; para pasar desde este estado a **Staged** se puede hacer mediante el comando [`add`](git_add.md).
- **Unmodified**:
    El archivo no ha cambiado desde el último [`commit`](commands/git_commit.md); los archivo que se encuentren en este estado no se mostrarán con el comando [`status`](git_status.md)
- **Modified**:
    El archivo ha sido modificado desde el último [`commit`](commands/git_commit.md) y no se le ha indicado a **Git** que debe tener lo en cuenta par el próximo [`commit`](commands/git_commit.md).
- **Staged**:
    El archivo está preparado para ser guardado en el próximo [`commit`](commands/git_commit.md); este puede pasar al estado **Unmodified** tras hacer un [`commit`](commands/git_commit.md)
