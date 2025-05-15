---
author: Mindusting
corrected: false
tags:
  - Programming/Git
title: Crear repositorios en Git
---

# INICIO DEL REPOSITIORIO

Para indicar que queremos que GIT realize el seguimiento de nuestro proyecto, tendremos que situarnos en el directorio raíz de este y ejecutar el comando `git init`, este creará una carpeta oculta dentro del directorio raíz llamada `.git`, en esta es en donde se guardará todos los cambios que vayamos realizando en nuestro proyecto junto con su [configuración](git_config.md).

> [!abstract] SINTAXIS
> git init

%%
```txt
/(HOME)
└─/Documentos
  └─/my_git
    ├─ __init__.py
    └─ console.py
```
%%

> [!example] EJEMPLO
> Vamos a nuestra carpeta `Documentos`, dentro de esta creamos otra carpeta a la que llamaremos (*por ejemplo*) `my_git`, nos situaremos dentro de esta última y ejecutaremos el comando `git init`, esto nos dejará con el siguiente árbol:
> ```txt
> /<user_name>
> └─/Documentos
>   └─/my_git
>     └─/.git
> ```

> [!important] IMPORTANTE
> Si no puedes ver el carpeta `.git` es por que no tienes puesto en tu [OS](../os/os.md) que se muestren los archivos ocultos.

%%
```bash
hint: Using 'master' as the name for the initial branch. This default branch name  
hint: is subject to change. To configure the initial branch name to use in all  
hint: of your new repositories, which will suppress this warning, call:  
hint:    
hint:   git config --global init.defaultBranch <name>  
hint:    
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and  
hint: 'development'. The just-created branch can be renamed via this command:  
hint:    
hint:   git branch -m <name>
```
%%
