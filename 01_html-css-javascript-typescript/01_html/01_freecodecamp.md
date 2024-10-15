# BASIC

Los elementos HTML tienen etiquetas (tags) de apertura y cierre con el contenido en medio de estas.

```html
<openingTag>content</closingTag>
```

## Títulos `h1` a `h6` (_block element_)

Para los títulos utilizamos elementos desde `h1` a `h6`, siendo el `h1` el de mayor nivel.

```html
<h1>most important heading element</h1>
<h2>second most important heading element</h2>
<h3>third most important heading element</h3>
<h4>fourth most important heading element</h4>
<h5>fifth most important heading element</h5>
<h6>least important heading element</h6>
```

## Párrafos `p` (_block element_)

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

## Contenido principal `main` (_block element_)

Algunos elementos identifican diferentes areas de contenido en la página. El elemento `main` se utiliza para representar el contenido principal de la página. El contenido dentro del elemento `main` tiene que ser único para el documento y no se debe repetir en otra parte del documento.

```html
<main>
    <h1>Most important content of the document</h1>
    <p>Some more important content...</p>
</main>
```

## nesting

_nesting_ es la práctica de mover dos espacios o un tab los elementos que se encuentran dentro de otros elementos para facilitar la lectura.

## Imágenes `img` y atributos HTML (_block element_)

Para agregar imágenes utilizamos el elemento `img`. Este elemento no tiene etiqueta de cierre. Los elementos sin etiqueta de cierre se denominan _void elements_.

Para poder cargar la imagen utilizamos _atributos HTML_. Los atributos HTML son palabras reservadas que se usan dentro de la etiqueta de apertura del elemento, mediante las mismas indicamos modificadores que se van a aplicar en el elemento donde se declaran.

En el caso del elemento `img` el atributo `src` indica la ruta desde donde vamos a traer la imagen que vamos a mostrar mediante ese elemento. El atributo `alt` indica que texto se debe mostrar si falla la carga de la imagen.



```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt='A cute orange cat lying on its back'>
```

## Link `a` (_inline element_)

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

## Secciones `section` (_block element_)

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

# Listas `ul`, `ol` y `li` (_block element_)

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

# Imágenes con `figure` y `figcaption ` (_block element_)

El elemento `figure` representa una imagen autocontenida. Permite asociar un elemento `img` con un elemento `figcaption `, que es un texto que brinda información sobre la imagen.

```html
<figure>
    <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
    <figcaption>Cats love lasagna.</figcaption>
</figure>
```

# Énfasis con `em` y `strong` (_inline element_)

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

# Atributo `id`

Utilizamos el atributo `id` para identificar de forma única un elemento, es decir, no puede existir más de un elemento con el mismo valor en el elemento `id`.

```html
<section id="comments">
    ...
</section>
```

# Formularios `form` (_block element_)

El elemento `form` se utiliza para solicitar información al usuario. El atributo `action` indica a donde se va a enviar la información que cargamos en el formulario.

## Elemento `input` (_inline element_)

El elemento `input`, que encerramos entre las etiquetas del elemento `form`, lo utilizamos para recolectar la información.

El atributo `type` del elemento `input` indica el tipo de dato que va a recibir ese input. En el ejemplo el tipo de datos es `text`, es decir, texto.

Para poder identificar, cuando los datos se envían, cual es el input que estamos recibiendo utilizamos el atributo `name`.

Podemos indicar un texto que aparezca dentro del input antes de que nosotros carguemos un dato. Para hacerlo utilizamos el atributo `placeholder`.

Si necesitamos que el dato del `input` sea indicado si o si utilizamos el atributo `required`.

Los tipos de elemento `input` que podemos tener son:
* `radio`: elementos de selección única. Para que, al enviar el formulario, solo sea considerado el que fue seleccionado utilizamos el elemento `name`. Todos los `input` de tipo `radio` deberán tener el mismo `name`.
* `checkbox`: elemento de selección múltiple. Es importante que cada elemento de tipo `checkbox` tenga el mismo `name` que los otros elementos que pertenecen a esa selección múltiple. El atributo `value` es opcional, pero es una buena práctica indicarlo con el mismo valor que `id`.



## Atributo `checked`

Mediante el atributo `checked` podemos indicar que un `input` de tipo `radio` o `checkbox` aparezcan seleccionados por defecto.

## Elemento `label` (_inline element_)

Utilizamos el elemento `label` para relacionar elementos `input` con textos. Podemos crear el elemento `label` y en su `content`, es decir entre sus etiquetas, indicar el elemento input y si lo tiene, el texto que acompaña la mismo. La otra opción es utilizar el atributo `for` del elemento `label` y relacionar el elemento con el atributo `id` del elemento `input`.

## Elemento `button` (_inline element_)

El elemento `button`, dentro del elemento `form`, se utiliza para enviar los datos que cargamos en el formulario. Si el elemento no tiene atributos que indiquen algo diferente al tocar en el botón los datos del formulario se van a enviar a la dirección que figura en el atributo `action` del elemento `form`.

Si bien por defecto el botón dentro del form indica sin atributos hace el `submit` a la dirección de `action` del `form` el ideal es indicar esto en el mismo botón mediante el atributo `type` con el valor `submit`. El valor que se envía en el formulario va a ser el valor del atributo `value`.

## Elemento `fieldset` y `legend` (_block element_)

El elemento `fieldset` se utiliza para agrupar `input` y `label` juntos dentro de un elemento `form`. Los elementos `fieldset` son elementos de bloque, es decir, van a aparecer en una nueva línea dentro del documento.

El elemento `legend` funciona como el elemento `caption` de `figure` pero este es para `fieldset`.

```html
<form action="https://freecatphotoapp.com/submit-cat-photo">
    <fieldset>
        <legend>Is your cat an indoor or outdoor cat?</legend>
        <label><input id="indoor" type="radio" name="indoor-outdoor" value="indoor"> Indoor</label>
        <label><input id="outdoor" type="radio" name="indoor-outdoor" value="outdoor"> Outdoor</label>
    </fieldset>
    <fieldset>
        <legend>What's your cat's personality?</legend>
        <input id="loving" type="checkbox" name="personality" value='loving'> <label for="loving">Loving</label>
        <input id="lazy" type="checkbox" name="personality" value='lazy'> <label for="lazy">Lazy</label>
        <input id="energetic" type="checkbox" name="personality" value='energetic'> <label for="energetic"> Energetic</label>
    </fieldset>
    <input type="text" name="catphotourl" placeholder='cat photo URL' required>
    <button type='submit'>Submit</button>
</form>
```

# Elemento `footer`

Para generar un pie de página del documento utilizamos el elemento `footer`.

```html
<footer>
    <p>No Copyright - <a href="https://www.freecodecamp.org">freeCodeCamp.org</a></p>
</footer>
```

# Elemento `head`, `title` y `meta`

Utilizamos el elemento `head` para generar la cabecera del documento. El elemento `title` indica cual es el título que va a aparecer en la barra de títulos de la ventana o en la pestaña del navegador. Mediante elementos `meta` podemos especificar una serie de metadatos que modifican la forma en que se va a mostrar la información del documento entre otros. Con `charset` indicamos cual va a ser el juego de caracteres que se van a utilizar en el documento. El valor `utf-8` sirva para la mayoría de los idiomas.

```html
<head>
    <meta charset=utf-8>
    <title>CatPhotoApp</title>
</head>
```

# Elemento `html`

Todo el documento se encuentra dentro del elemento `html`. En este elemento podemos configurar el idioma de la página.

```html
<html lang='en'>
    ...
</html>
```

# Elemento `<!DOCTYPE html>`

Mediante el elemento `<!DOCTYPE html>` indicamos a los navegadores que lo siguiente es un documento HTML. Este elemento no tiene tag de cierre. Este elemento tiene que estar en la primera línea del documento.

# El ejemplo completo

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>CatPhotoApp</title>
</head>
<body>
    <main>
        <h1>CatPhotoApp</h1>
        <section>
            <h2>Cat Photos</h2>
            <!-- TODO: Add link to cat photos -->
            <p>See more <a target="_blank" href="https://freecatphotoapp.com">cat photos</a> in our gallery.</p>
            <a href="https://freecatphotoapp.com"><img
                    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
                    alt="A cute orange cat lying on its back."></a>
        </section>
        <section>
            <h2>Cat Lists</h2>
            <h3>Things cats love:</h3>
            <ul>
                <li>cat nip</li>
                <li>laser pointers</li>
                <li>lasagna</li>
            </ul>
            <figure>
                <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg"
                    alt="A slice of lasagna on a plate.">
                <figcaption>Cats <em>love</em> lasagna.</figcaption>
            </figure>
            <h3>Top 3 things cats hate:</h3>
            <ol>
                <li>flea treatment</li>
                <li>thunder</li>
                <li>other cats</li>
            </ol>
            <figure>
                <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
                    alt="Five cats looking around a field.">
                <figcaption>Cats <strong>hate</strong> other cats.</figcaption>
            </figure>
        </section>
        <section>
            <h2>Cat Form</h2>
            <form action="https://freecatphotoapp.com/submit-cat-photo">
                <fieldset>
                    <legend>Is your cat an indoor or outdoor cat?</legend>
                    <label><input id="indoor" type="radio" name="indoor-outdoor" value="indoor" checked> Indoor</label>
                    <label><input id="outdoor" type="radio" name="indoor-outdoor" value="outdoor"> Outdoor</label>
                </fieldset>
                <fieldset>
                    <legend>What's your cat's personality?</legend>
                    <input id="loving" type="checkbox" name="personality" value="loving" checked> <label
                        for="loving">Loving</label>
                    <input id="lazy" type="checkbox" name="personality" value="lazy"> <label for="lazy">Lazy</label>
                    <input id="energetic" type="checkbox" name="personality" value="energetic"> <label
                        for="energetic">Energetic</label>
                </fieldset>
                <input type="text" name="catphotourl" placeholder="cat photo URL" required>
                <button type="submit">Submit</button>
            </form>
        </section>
    </main>
    <footer>
        <p>
            No Copyright - <a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
        </p>
    </footer>
</body>
</html>
```
