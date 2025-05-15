---
author: Mindusting
corrected: false
tags:
  - Programming/HTML
title: Formularios en HTML5
---

# FORMULARIO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar los tipos de `input`.
> > - [ ] Documentar los `label`.
> > - [ ] Documentar los `textarea`.
> > - [ ] Documentar los `button`.
> > - [ ] Documentar los `select`.

> [!help]- REFERENCIAS WEB
> - [W3 (`form`)](https://www.w3schools.com/tags/att_form_method.asp)
>     - [W3 (`method`)](https://www.w3schools.com/tags/ref_httpmethods.asp)

Para crear un formulario usamos la etiqueta `form`, este tiene una etiqueta de apertura y otra de cierre, entre estas dos etiquetas pondremos todo el contenido del formulario, pero de momento veremos que atributos tiene:

- `action`:
    En este atributo indicamos a la página a la que queramos redirigir al usuario una vez haya enviado el formulario.
- `method`:
    En este atributo indicamos el método que queremos usar para enviar los datos del formulario.

    Las opciones son las siguientes:
    - `get`:
        Este escribirá la información de los usuarios en la URL de la página, esto hace a este método poco seguro, ya que se podrá ver toda la información y la URL tiene una limitación de 2048 caracteres.
    - `post`:
        Este está pensado para mandar información a un servidor, ya que se lo manda de forma directa, por lo que no es tan fácil de acceder a la información como pasa con el `get`.

```html
<form action="[URL]" method="[get|post]">
    [form_content]
</form>
```

Atributos globales de `form`:

La propiedad `value`, contiene el valor por defecto.

La propiedad `readonly` hace que solo se pueda leer.

La propiedad `disabled` des habilita el campo.

La propiedad `required` hace le campo obligatorio.

## INPUT

La etiqueta `input` permite crear un área con la que el usuario podrá interactuar, pudiendo así trasmitir información.

La etiqueta `input` sirve para introducir datos en el formulario.

```html
<form>
    <input type="[type]"/>
</form>
```

- `text`
    - `size`: Numero de caracteres.
    - `maxlength`: Máximo de caracteres.
    - `placeholder`: Texto para ayudar al usuario a entender que tiene que meter en el campo.
    - `pattern`: Patrón del contenido.
    - `autocomplete`: Auto completa el campo.
- `password`:
    Es igual que el `text` pero no se muestra el texto, sino puntos.
- `submit`
- `reset`
- `button`
- `image`
- `number`
- `range`
- `color`
- `file`
- `hidden`
- `search`

## ETIQUETAS

El `label` es el pretexto antes de un campo.

Tiene la propiedad `for`, esta indica el `id` del sitio al que va a levar.

```html
<form>
    <label></label>
</form>
```

## BOTÓN

Permite crear un botón que puede ser pulsado por el usuario.

```html
<form>
    <button type="submit">Confirmar</button>
    <button type="reset">Limpiar</button>
</form>
```

## ÁREA DE TEXTO

Crea un área cuadrada en la que el usuario puede escribir.

```html
<form>
    <textarea></textarea>
</form>
```

- `width`
- `height`
- `warp`

## SELECT

```html
<form>
    <label for="pizzaSelector">Pizza:</label>
    <select id="pizzaSelector" name="pizza">
        <option value="4q">Cuatro quesos</option>
        <option value="bbq">Barbacoa</option>
        <option value="jyq">Jamón y queso</option>
        <option value="hwn">Hawaiana</option>
    </select>
</form>
```
