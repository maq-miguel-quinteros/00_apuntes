# BASIC

Los elementos HTML tienen etiquetas (tags) de apertura y cierre con el contenido en medio de estas.

```html
<openingTag>content</closingTag>
```

## Títulos `h1` a `h6`

Para los títulos utilizamos elementos desde `h1` a `h6`, siendo el `h1` el de mayor nivel.

```html
<h1>most important heading element</h1>
<h2>second most important heading element</h2>
<h3>third most important heading element</h3>
<h4>fourth most important heading element</h4>
<h5>fifth most important heading element</h5>
<h6>least important heading element</h6>
```

## Párrafos `p`

El elemento `p` se utiliza para crear párrafos.

```html
<h2>Cat Photos</h2>
<p>See more cat photos in our gallery.</p>
```

## Comentarios `<!-- -->`

Para comentarios utilizamos `<!-- comment -->`.

```html
<!-- TODO: Add link to cat photos -->
<p>See more cat photos in our gallery.</p>
```

## Contenido principal `main`

Algunos elementos identifican diferentes areas de contenido en la página. El elemento `main` se utiliza para representar el contenido principal de la página. El contenido dentro del elemento `main` tiene que ser único para el documento y no se debe repetir en otra parte del documento.

```html
<main>
    <h1>Most important content of the document</h1>
    <p>Some more important content...</p>
</main>
```

## nesting

_nesting_ es la práctica de mover dos espacios o un tab los elementos que se encuentran dentro de otros elementos para facilitar la lectura.

## Imágenes `img` y atributos HTML

Para agregar imágenes utilizamos el elemento `img`. Este elemento no tiene etiqueta de cierre. Los elementos sin etiqueta de cierre se denominan _void elements_.

Para poder cargar la imagen utilizamos _atributos HTML_. Los atributos HTML son palabras reservadas que se usan dentro de la etiqueta de apertura del elemento, mediante las mismas indicamos modificadores que se van a aplicar en el elemento donde se declaran.

En el caso del elemento `img` el atributo `src` indica la ruta desde donde vamos a traer la imagen que vamos a mostrar mediante ese elemento. El atributo `alt` indica que texto se debe mostrar si falla la carga de la imagen.



```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt='A cute orange cat lying on its back'>
```

## Link `a`

Para crear un link a otra página o a otra parte del documento utilizamos el elemento `a`. El atributo `href` del elemento indica la dirección a la que apunta el link. Entre las etiquetas del elemento podemos escribir un texto sobre el cual, al hacer click, cambiamos a la página del link. 

```html
<a href="https://freecatphotoapp.com">link to cat pictures</a>
```

Podemos sumar el link al contenido de otros elementos, por ejemplo, de un elemento `p`.

```html
<p>See more <a href='https://freecatphotoapp.com'>cat photos</a> in our gallery.</p>
```

Para que el link se abra en una nueva pestaña cuando hacemos click en el mismo utilizamos el atributo `target='_blank'`.

```html
<p>See more <a href="https://freecatphotoapp.com" target='_blank'>cat photos</a> in our gallery.</p>
```

En el contenido del elemento `a` podemos tener otros elementos, por ejemplo un elemento `img`.

```html
<a href='https://freecatphotoapp.com'>
    <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute orange cat lying on its back.">
</a>
```

## Secciones `section`

El elemento `section` es un elemento semántico que se utiliza para dividir el documento en secciones, cada una con su temática o función, que se diferencia de las otras secciones. Otras secciones son los `header` o `footer`.

```html
<main>
    <h1>CatPhotoApp</h1>
    <section>
        <h2>Cat Photos</h2>
        <!-- TODO: Add link to cat photos -->
        <p>See more <a target="_blank" href="https://freecatphotoapp.com">cat photos</a> in our gallery.</p>
        <a href="https://freecatphotoapp.com"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute orange cat lying on its back."></a>
    </section>
</main>
```

# Listas `ul`, `ol` y `li`

Para crear una lista desordenada de items utilizamos el elemento `ul`. Los items dentro de la lista se crean con elementos `li`.

```html
<ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
</ul>
```

Para crear listas ordenadas utilizamos el elemento `ol`.

```html
<h3>Top 3 things cats hate:</h3>
<ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
</ol>
```

# Imágenes con `figure` y `figcaption `

El elemento `figure` representa una imagen autocontenida. Permite asociar un elemento `img` con un elemento `figcaption `, que es un texto que brinda información sobre la imagen.

```html
<figure>
    <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
    <figcaption>Cats love lasagna.</figcaption>
</figure>
```

# Énfasis con `em` y `strong`

Podemos hacer énfasis en las palabras que queramos que resalten mediante el elemento `em`.

```html
<figure>
    <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
    <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>

```

Podemos hacer énfasis en las palabras que queramos con el elemento `strong`. Se utiliza `strong` para indicar que un texto es muy importante o urgente.

```html
<figure>
    <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field.">
    <figcaption>Cats <strong>hate</strong> other cats.</figcaption>
</figure>
```

# Formularios `form`

El elemento `form` se utiliza para solicitar información al usuario. El atributo `action` indica a donde se va a enviar la información que cargamos en el formulario.

El elemento `input`, que encerramos entre las etiquetas del elemento `form`, lo utilizamos para recolectar la información.

El atributo `type` del elemento `input` indica el tipo de dato que va a recibir ese input. En el ejemplo el tipo de datos es `text`, es decir, texto.

Para poder identificar, cuando los datos se envían, cual es el input que estamos recibiendo utilizamos el atributo `name`.

```html
<form action="https://freecatphotoapp.com/submit-cat-photo">
    <input type="text" name='catphotourl'>
</form>
```
