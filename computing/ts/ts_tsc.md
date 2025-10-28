---
author: Mindusting
corrected: true
tags:
  - Programming/TypeScript
title: Compilador de TypeScript
---

# COMPILADOR DE TYPESCRIPT

El compilador de **TypeScript** es el encargado de transformar el código escrito en **TypeScript** a [**JavaScript**](../js/js.md).

## INSTALACIÓN

Para instalar el compilador de TypeScript se hace uso del [**gestor de paquetes de NodeJS**](../node/node_npm.md); en este caso veremos como instalar (*en linux*) de forma global (*el parámetro `-g` indica que es global, esto significa que el compilador de TypeScript no va a estar limitado solo al proyecto, sino que se instalará a nivel de sistema, por lo que podremos compilar TypeScript desde donde queramos*) con el siguiente comando:

```bash
sudo npm install -g typescript
```

Una vez ha terminado la instalación podremos comprobar que se ha instalado correctamente tratando de ver la versión de esta:

```bash
tsc -v
```

## CÓMO COMPILAR

Una vez tenemos instalada una versión del compilador de **TypeScript** podremos empezar a hacer uso de él; este es muy simple ya que únicamente tendremos que escribir el nombre del comando (`tsc`) seguida de la ruta del archivo que **TypeScript** que queramos compilar a [**JavaScript**](../js/js.md).

> [!abstract] SINTAXIS
> tsc ***\[ts\_path\]***

Este creará un nuevo archivo con el mismo nombre que el archivo que tratamos de compilar, con la diferencia que este tendrá la extensión `.js` (*siendo esta la extensión de [**JavaScript**](../js/js.md)*).

---

Como ejemplo supongamos que tenemos el siguiente archivo (*se llama `main.ts`*) de **TypeScript** con el siguiente contenido:

```ts
let message: string = "Este es mi primer programa de TS.";
console.log(message);
```

Al ejecutar el siguiente comando:

```bash
tsc main.ts
```

Se creará el siguiente archivo (*se llama `main.js`*) de [**JavaScript**](../js/js.md):

```js
var message = "Este es mi primer programa de TS.";
console.log(message);
```

Este último a su vez ya podrá ser ejecutado con [**NodeJS**](../node/node.md) o ser [incluido de una página web](../js/js_file.md).
