# Configuración del entorno

Generamos 3 archivos para trabajar llamados `index.html`, `index.css` y `index.js`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./index.css">
    <title>javaScript for React</title>
</head>
<body>
    <h1>JavaScript</h1>
    <script src="./index.js"></script>
</body>
</html>
```

```css
body {
    background-color: #202020;
    color: white;
}
```

```js
console.log('Hola Mundo')
```

# Funciones

## Funciones

Las funciones permiten reutilizar lógica. Son capaces de retornar un valor. el valor que devuelve puede ser de cualquier tipo: number, string, array u object. También pueden retornar otra función.

```js
// declaramos la función
function hello(){
    // lo que la función va a devolver
    return function () {
		return 'hola mundo'}
}
// llamamos a la función
const result = hello()
// llamamos a la función que retornó la función anterior
console.log(result())

// podemos no guardar el valor que devuelve
console.log(hello()())
```

## Parámetros de funciones

Las funciones pueden recibir parámetros. Los parámetros son valores que la función puede esperar para procesarlos.

```js
// Pasamos como parámetro un valor para name
function hello(name){
    return 'hola ' + name
}
const result = hello('Miguel')
console.log(result)

function add(x, y){
    return x + y
}
console.log(add(5, 9))
```

## Parámetros por defecto

Las funciones se pueden declarar con parámetros con valores por defecto.

```js
function add(x, y){
    return x + y
}
console.log(add(5)) // muestra NaN

// el segundo parámetro tiene que valor por defecto 0
function add_2(x, y = 0){
    return x + y
}
console.log(add_2(5)) // muestra 20 -> 20 + 0
console.log(add_2(5, 9)) // muestra 14
```

# Objetos

## Declaración de objetos

Los objetos en javascript se representan con `{}` y se guardan en variables o constantes. Están compuestos de valores representados por pares clave: valor. Los valores de un objeto se conocen como propiedades o atributos. Los atributos pueden ser de cualquier tipo: number, string, array u object. También podemos asignar a un atributo una función, a la que llamamos método.

```js
const user = {
    // name es la clave (key) y Miguel el valor (value)
    name: 'Miguel',
    last_name: 'Quinteros',
    age: 30,
    address: {
        country: 'Argentina',
        city: 'Tucumán',
    },
    skills: ['HTML', 'CSS', 'JS'],
    active: true,
    sed_mail: function (mail){
        return 'send mail to ' + mail
    }
}

console.log(user)
```

Para acceder a los atributos o métodos de un objeto podemos utilizar la notación de punto `.` o la notación de `[]` con el nombre del atributo entre `''`.

```js
const user = {
    // name es la clave (key) y Miguel el valor (value)
    name: 'Miguel',
    last_name: 'Quinteros',
    age: 30,
    address: {
        country: 'Argentina',
        city: 'Tucumán',
    },
    skills: ['HTML', 'CSS', 'JS'],
    active: true,
    send_mail: function (name){
        return 'send mail to ' + name
    }
}

console.log(user)
console.log(user.name)
console.log(user['name'])
console.log(user.skills) // muestra el array
console.log(user.skills[1]) // muestra CSS
console.log(user.send_mail) // muestra la definición de la función
console.log(user.send_mail('Miguel')) // ejecuta la función
```

Otra forma de declarar funciones como métodos de un objeto.

```js
const user = {
    name: 'Miguel',
	// ...
    send_mail(name){
        return 'send mail to ' + name
    }
}
```

## Shorthand property names

Entendemos por _Shorthand property names_ a que los key de los atributos de un objeto tomen por valor el nombre de la variable que contiene su value.

```js
const name = 'Laptop'
const price = 3000

const product = {
    // el name antes de : es la propiedad y el name después de los : es el valor Laptop
    name: name,
    price: price
}
console.log(product)

const product_2 = {
    // por defecto el key toma como valor el nombre de la variable que tiene el value
    name,
    price
}
console.log(product_2)
```

# Manipulación del DOM

Editamos el archivo html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./index.css">
    <title>javaScript for React</title>
</head>
<body>
    <script src="./index.js"></script>
</body>
</html>
```

Podemos agregar elementos html al documento mediante métodos de javascript.

```js
// creamos un elemento html desde js
const title = document.createElement('h1')

// agregamos texto al content del elemento
title.innerText = 'Hola mundo desde JS'

// agregamos el elemento al documento
document.body.append(title)

const button = document.createElement('button')
button.innerText = 'Click'
document.body.append(button)
```

Podemos agregar manejadores de eventos (event handlers) a los elementos que creamos o a elementos que ya existan en el documento.

```js
const title = document.createElement('h1')
title.innerText = 'Hola mundo desde JS'
document.body.append(title)

const button = document.createElement('button')
button.innerText = 'Click'

// el evento que agregamos es click. Cuando se hace click en el botón se ejecuta la función del segundo parámetro de addEventListener
button.addEventListener('click', function () {
	title.innerText = 'Texto actualizado por el click'
})

document.body.append(button)
```

# Destructuring

Podemos desestructurar el el objeto que recibimos por parámetro en una función y utilizar, de ese objeto, los atributos que necesitemos para ejecutar la misma.

```js
const user = {
    name: 'Miguel',
    age: 39,
    zodiac: 'Virgo'
}
function print_info(data){
    return '<h1>Hola ' + data.name + '</h1>'
}

// crea el elemento h1 en body como se define en el return de la función
document.body.innerHTML = print_info(user) 

// podemos declarar la función indicando cual es el atributo que necesitamos del objeto que nos van a pasar por parámetro
function print_info_2({age}){
    return '<h2>Tu edad es ' + age + '</h2>'
}

// vuelve a crear el h1 y suma el h2 al documento
// pasamos el objeto user pero la función solo va a usar el atributo age del objeto que pasamos
document.body.innerHTML = print_info(user) + print_info_2(user)

function print_info_3(data){
    // creamos tres constantes desestructurando el objeto que llega por parámetro
    const {name, age, zodiac} = data
    return '<p>Tu nombre es ' + name + ', tu edad es '+age+' y tu signo es ' + zodiac + '</p>'
}
document.body.innerHTML = print_info(user) + print_info_2(user) + print_info_3(user)
```

# Funciones anónimas
