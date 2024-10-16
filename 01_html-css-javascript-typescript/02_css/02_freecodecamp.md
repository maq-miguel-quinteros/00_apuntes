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

# Selector hijo

Podemos encadenar los selectores llegando a un en particular a traves de sus hijos. En el ejemplo seleccionamos todos los elementos de tipo `p` que estén dentro de elementos con clase `item`.

```css
.item p {
    display:inline-block;
}
```

# Pseudo selector `:`

Podemos utilizar el pseudo selector : para seleccionar, por ejemplo, un estado de un elemento. En el ejemplo, los elementos `a` tienen un estado llamado `visited` que indica si ya se hizo click sobre el enlace. Para modificar el estilo del elemento en ese estado utilizamos el pseudo selector.

```css
a:visited {
    color: grey;
}
```

# Ejemplo completo

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cafe Menu</title>
    <link href="styles.css" rel="stylesheet" />
</head>

<body>
    <div class="menu">
        <main>
            <h1>CAMPER CAFE</h1>
            <p class="established">Est. 2020</p>
            <hr>
            <section>
                <h2>Coffee</h2>
                <img src="https://cdn.freecodecamp.org/curriculum/css-cafe/coffee.jpg" alt="coffee icon" />
                <article class="item">
                    <p class="flavor">French Vanilla</p>
                    <p class="price">3.00</p>
                </article>
                <article class="item">
                    <p class="flavor">Caramel Macchiato</p>
                    <p class="price">3.75</p>
                </article>
                <article class="item">
                    <p class="flavor">Pumpkin Spice</p>
                    <p class="price">3.50</p>
                </article>
                <article class="item">
                    <p class="flavor">Hazelnut</p>
                    <p class="price">4.00</p>
                </article>
                <article class="item">
                    <p class="flavor">Mocha</p>
                    <p class="price">4.50</p>
                </article>
            </section>
            <section>
                <h2>Desserts</h2>
                <img src="https://cdn.freecodecamp.org/curriculum/css-cafe/pie.jpg" alt="pie icon" />
                <article class="item">
                    <p class="dessert">Donut</p>
                    <p class="price">1.50</p>
                </article>
                <article class="item">
                    <p class="dessert">Cherry Pie</p>
                    <p class="price">2.75</p>
                </article>
                <article class="item">
                    <p class="dessert">Cheesecake</p>
                    <p class="price">3.00</p>
                </article>
                <article class="item">
                    <p class="dessert">Cinnamon Roll</p>
                    <p class="price">2.50</p>
                </article>
            </section>
        </main>
        <hr class="bottom-line">
        <footer>
            <p>
                <a href="https://www.freecodecamp.org" target="_blank">Visit our website</a>
            </p>
            <p class="address">123 Free Code Camp Drive</p>
        </footer>
    </div>
</body>

</html>
```

```css
body {
    background-image: url(https://cdn.freecodecamp.org/curriculum/css-cafe/beans.jpg);
    font-family: sans-serif;
    padding: 20px;
}

h1 {
    font-size: 40px;
    margin-top: 0;
    margin-bottom: 15px;
}

h2 {
    font-size: 30px;
}

.established {
    font-style: italic;
}

h1,
h2,
p {
    text-align: center;
}

.menu {
    width: 80%;
    background-color: burlywood;
    margin-left: auto;
    margin-right: auto;
    padding: 20px;
    max-width: 500px;
}

img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

hr {
    height: 2px;
    background-color: brown;
    border-color: brown;
}

.bottom-line {
    margin-top: 25px;
}

h1,
h2 {
    font-family: Impact, serif;
}

.item p {
    display: inline-block;
    margin-top: 5px;
    margin-bottom: 5px;
    font-size: 18px;
}

.flavor,
.dessert {
    text-align: left;
    width: 75%;
}

.price {
    text-align: right;
    width: 25%;
}

/* FOOTER */

footer {
    font-size: 14px;
}

.address {
    margin-bottom: 5px;
}

a {
    color: black;
}

a:visited {
    color: black;
}

a:hover {
    color: brown;
}

a:active {
    color: brown;
}
```
