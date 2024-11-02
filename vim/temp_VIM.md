# MOVERSE POR UN ARCHIVO

Para poder moverse por un archivo en el modo normal se puede usar la siguiente distribución de obtones:

```txt
    k
h     l
  j
```

```txt
    ^
<     >
  v
```

# INSERTAR

Para poder escribir texto, en el modo *normal* usamos el comando `i` (insert).

Este comando activará el codo *inserción*, este permitirá escribir en el archivo.

Para volver al modo *normal* se usa la tecla `<Esc>`.

# AÑADIR

Para poder escribir texto después del caracter seleccionado con el cursor se usa en el modo *normal* el comando `a` (append).

Este comando es muy parecido al de *inserción* con la diferencia de qué este hace que escribamos una posión por delante del cursor y no en la misma posición que este.

# INSERTAR NUEVA LÍENA

Para insertar una nueva línea se puede usar en el modo normal el comando `o`.

Esto implica que si tenemos dos líneas y el cursor se encuentra en la primera al escribir el comando `o`, creará una línea nueva entre estas dos y posicionará el curor en esa nueva posición en el como *inserción*.

```txt
Esta es mi primera línea.
Esta es mi segunda línea.
```

Tras escribir el comando `o` teniendo el cursor en la primera línea y seguido a esto, escribimos `Esta es mi nueva línea.` el resultado es el siguiente.

```txt
Esta es mi primera línea.
Esta es mi nueva línea.
Esta es mi segunda línea.
```

De la misma forma, el comando `O` hade lo mismo pero la nueva línea la inserta por encima de la línea en la que se encuentre el cursor.

# DESHACER

Para desacer se usa en el modo *normal* el comando `u` (undo).

# REHACER

Para reacer un cambio que hemos desecho se usa en el modo *normal* el comando `CTRL-R` (redo).

# DESHACER LA ÚLTIMA LÍNEA

Para poder deshacer todos los cambios de la última línea, en el modo *normal*, se usa el comando `U` (undo line).

Si escribimos este mismo comando un asegunda vez consecutiva, volverá a dejar la línea como estava antes de deshacer los cambios.

# BORRAR LÍENAS

Para borrar líneas se usa en el modo *normal* el comando `dd`.

A este comando le puede preceder un número, indicando este las línas que se quieren borrar, estas líneas extra serán las siguientes a la líneas a la indicada por el cursor.

# BORRAR CARACTERES

Para borrar caracteres se usa en el modo *normal* el comando `x`.

A este comando le puede preceder un número, indicando este los caracteres que se quieren borrar, los caracteres extra que se indiquen para borar, serás los siguientres al caracter indicado por el cursor.

# JUNTAR DOS LÍNEAS

Para poder juntar dos líneas se usa en el modo *normal* el comando `J`, este sustituirá el caracter de salto delínea por un espación entre la línea indicada por le cursor y la siguiente.

# ACORTACIONES DE COMANDOS

Cuando queramos repetir un mismo comando varias veces, en vez de escribirlo varias veces, podemos primero indicar el número de veces que queremos ejecutarlo seguido del comando.

Un ejemplo de esto sería el de borrar un carácter, si escribimos el comando `3x` borrará tres caracteres desde la posición del cursor.

# GUARDAR Y CERRA UN ARCHIVO

Para poder guardar y cerrar un archivo se puede usar en el modo *normal* el comando `:x` o `ZZ`.

>[!warning]
>VIM no guarda a automaticamente los archivos, por lo que tendremos que ir guardando nosotro periodicamente los cambios que nosotros hagamos.

# CERRAR UN ARCHIVO

Para cerrar un archivo que no tenga cambios se usa en el modo *normal* el comando `:q` (quit).

# SALIR SIN GUARDAR

Para cerrar un archivo que ha sufrido cambios y no queremos guardarlos, se usa en el modo *normal* el comando `:q!`.

# CARGAR LA ÚLTIMA VERSIÓN GUARDADA DEL ARCHIVO

Para cargar la última versión guardada del archivo se usa en el modo *normal* el comando `:e!`.

>[!warning]
>Este comando borrará todos los cambios que haya sufrido el archivos desde la última vez que fue guardado.

# SALTAR ENTRE ETIQUETAS

Para poder entrar en una etiqueta se usa en el modo *normal* el comando `CTRL-]`, para volver a la anterior `CTRL-T` (pop tag).

También se puede saltar a la etiqueta anterior con el comando `CTRL-O` (jum to older position).
También se puede saltar a la etiqueta posterior con el comando  `CTRL-I`.

# MOVIMIENTO

## MOVERSE AL PRINCIPIO DE LA SIGUIENTE PALABRA

Para ir saltando al comienzo de la siguiente palabra al cursor, se usa el comando `w`.

## MOVERSE AL PRINCIPO DE LA ANTERIOR PALABRA

Para ir saltando al comienzo de la anterior palabra al cursor, se usa el comando `b`.

## MOVERSE AL FINAL DE LA SIGUIENTE PALABRA

Para ir saltando al final de la siguiente palabra al cursor, se usa el comando `e`.

## MOVERSE AL FINAL DE LA ANTERIOR PALABRA

Para ir saltando al final de la anterior palabra al cursor, se usa el comando `g`.

## MOVERSE AL PRINCIPIO DE LA LÍNEA

Para posicionar el cursor al principio de la línea se usa en el modo normal el comando `0`.

## MOVERSE AL PRIMER CARACTER QUE NO SEA UN ESPACIO O TABULACIÓN

Para posicionar el cursor en el primer caracter que no sea *blank* de la línea se usa el comando `^`.

## MOVERSE AL FINAL DE LA LÍNEA

Para posicionar el cursor al final de la línea, se usa el comando `$`. 

## MOVERSE AL PROXIMO CARÁCTER INDICADO

Para posicionar el cursor en el proximo caracter que indiquemos se usa el comando `f` (find) seguido del caracter que queremos buscar.

Si usamos el comando `F` busca el caracter hacia atras.

## MOVERSE ENTRE LOS BORDES DE LOS PARÉNTESIS

Si situamos nuestro cursor en un parentesis de apertura y usamos el comando `%` este nos situará el cursor en el cierre de paréntesis que le corresponde, tanbién funciona de forma inversa, podemos ir al parentesis de apertura.

Este mismo comando funciona con los corchetes `[]` y las llaves `{}`.

Si el cursor no está posicionado sobre unos de estos carácteres, al usar este comando, el cursor se posicionará sobre el primer carácter de este tipo que encuentre.

## GOTO

Si queremos ir a alguna línea en concreto podemos usar el comanod `G`, este debe estar precedido por el número de la línea a la que queremos ir.

Si escribimos el comando `G` sin especificar una línea, el cursor se posicionará al final del archivo.

Si queremos ir al principio del archivo podemo usar el comando `gg`.

### GOTO POR PORCENTAGE

Si escribimos un núero entre `1` y `100` seguido de un `%`, estaremos indicado que queremos posicionar el cursor en el porcetage del archivo, esto quiere decir que si escribimos el comando `50%`, el cursor se posicionará en el centro del archivo.

## MOVERSE ENTRE LAS LÍENAS VISIBLES

Si queremos mosvernos entre las líenas que tenemos en pantalla, tenemos res comandos para poder desplazarnos.

El comando `H` posicionará el cursor en la parte superior de las líneas visibles.
El comando `M` posicionará el cursor en la parte media de las líneas visibles.
El comando `L` posicionará el cursor en la parte baja de las líneas visibles.

## DONDE ESTOY?

Para saver la posición en la que nos encontramos podemos usar el comando `CTRL-G`, este nos inprimirá en la parte inferior de la pantalla la posición actual de nuestro cursor.

## MOVER MEDIANTE SCROLL

### UNA PÁGINA

Para mover el scroll una página hacia arriba se usa el comando `CTRL-B`.

Para mover el scroll una página hacia abajo se usa el comando `CTRL-F`.

### MEDIA PÁGINA

Para mover el scroll media página hacia arriba se usa el comando `CTRL-U`.

Para mover el scroll media página hacia abajo se usa el comando `CTRL-D`.

### UNA LÍNEA

Para mover el scroll una línea hacia arriba se usa el comando `CTRL-E`.

Para mover el scroll una línea hacia abajo se usa el comando `CTRL-Y`.

### CENTRAR SCROLL AL CURSOR

Para que el scroll se sitúe centrando al cursor, se usa el comando `zz`.
