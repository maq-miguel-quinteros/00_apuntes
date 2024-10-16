# Elemento `style`

Para controlar los estilos agregamos el elemento `style` dentro del elemento `head`.

```html
<head>
    <meta charset="utf-8" />
    <style></style>
    <title>Cafe Menu</title>
</head>
```

Para agregar estilos a un elemento utilizamos la sintaxis.

```css
element {
    property: value;
}
```

# Selector de tipo

Mediante los selectores de tipo podemos modificar el estilo de los elementos HTML como `h1`, `p`, `spam`, `section`, etc. Modificamos la alineación del texto del elemento `h1` indicando que se ubiquen en el centro.

```css
h1 {
    text-align: center;
}
```

Si el estilo que vamos a aplicar es el mismo para varios selectores podemos indicar que se aplique ese estilo a una lista de selectores separados por coma.

```css
h1, h2, p {
    text-align: center;
}
```

# Hoja de estilos en un archivo separado

Podemos indicar los estilos en un documento separado del documento HTML. Para hacerlo tenemos que indicar en el elemento `head` cual es la dirección donde encontramos la hoja de estilos que vamos a utilizar.

```html
<head>
    <meta charset="utf-8" />
    <link rel='stylesheet' href='styles.css'>
    <title>Cafe Menu</title>
</head>
```

# Responsive

Para que la página se vea similar en un navegador de escritorio y en un navegador de teléfono utilizamos el siguiente meta.

```html
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel='stylesheet' href='styles.css'>    
    <title>Cafe Menu</title>
</head>
```

# Elemento `div`

Utilizamos el elemento `div` para indicar una separación entre distintas partes de nuestro documento. `div` es un elemento comodín que podemos utilizar siempre que necesitemos diferenciar una parte de nuestro documento del resto.

```html
<body>
    <div id='menu'>
        <main>
            <h1>CAMPER CAFE</h1>
            <p>Est. 2020</p>
            <section>
                <h2>Coffee</h2>
            </section>
        </main>
    </div>
</body>
```

# Selector de `id` de elementos `#`

Mediante el selector `#` podemos seleccionar un elemento en particular por el valor de su atributo `id`.

```css
#menu {
    width:300px;
}
```

# Comentarios con `/* */`

Para hacer comentarios utilizamos `/* */`

# Ancho y margenes

```css
#menu {
    width: 80%; /* ocupa el 80% del total del tamaño del padre (body) */
    background-color: burlywood;
    margin-left: auto; /* alinea al centro el div con id menu */
    margin-right: auto; /* alinea al centro el div con id menu */
}
```

# Selector de clase .

Podemos utilizar el selector de clase, este permite seleccionar los elementos que tienen el mismo valor en el atributo `class`. En css para indicar una clase se hace mediante el punto.

```css
.menu {
    width: 80%;
    background-color: burlywood;
    margin-left: auto;
    margin-right: auto;
}
```

# Elemento `article`

El elemento `article` es un elemento semántico que se utiliza dentro del elemento `section`, un documento puede tener una o varias `section` y una `section` puede tener uno o varios `article`.

```html
<section>
    <h2>Coffee</h2>
    <article></article>
</section>

```

seguir https://www.freecodecamp.org/learn/2022/responsive-web-design/learn-basic-css-by-building-a-cafe-menu/step-36
