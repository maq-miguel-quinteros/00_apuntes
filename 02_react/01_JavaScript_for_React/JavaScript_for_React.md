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

Podemos declarar una función de varias formas y en varios contextosEn javascript no es necesario que una función tenga un nombre.

```js
// forma común con nombre
function start(){
    return 'starting...'
}
console.log(start())

// declaramos la función dentro de la función console.log(). Para ejecutar la misma requiere el segundo par de paréntesis
console.log((function start_2(){
    return 'starting...'
})())

// no es necesario indicar el nombre de la función si la utilizamos al momento de declararla
console.log((function () {
    return 'starting...'
})())
```

El uso más común de estas funciones es en los manejadores de eventos.

```js
// creamos la función con nombre y la pasamos al método addEventListener
const button = document.createElement('button')
button.innerText = 'Click me'
function handleClick(){
    console.log('clicked')
}
button.addEventListener('click', handleClick)
document.body.append(button)

// pasamos la función anónima al método addEventListener
const button_2 = document.createElement('button')
button_2.innerText = 'Click me 2'
button_2.addEventListener('click', function (){
    console.log('clicked 2')
})
document.body.append(button_2)
```

# Funciones flecha

Otra forma de crear funciones es mediante las funciones flecha. 

```js
// forma común de declarar una función
function add(x, y){
    return x + y
}

// forma de declarar una función flecha con nombre
const add_1 = (x, y) => {
    return x + y
}

// si el return está en la misma línea de la declaración de la función no requiere el return ni las llaves
const add_2 = (x, y) =>  x + y

// si lo que devolvemos es un objeto, tenemos en encerrarlo entre paréntesis
const show_object = () => ({name:'Miguel', age:39})

// pasamos la función flecha anónima al método addEventListener
const button = document.createElement('button')
button.innerText = 'Click me'
button.addEventListener('click', () => console.log({name:'Miguel', age:39}))
document.body.append(button)
```

# Condicionales con return

Podemos utilizar el return de una función en un condicional para establecer lo que hace la misma.

```js
const is_authorized = false

// forma normal de trabajar con condicionales
const button = document.createElement('button')
button.innerText = 'Click me'

button.addEventListener('click', () => {
    // forma común de trabajar con condicionales
    if (is_authorized) {
        console.log('Autorizado')
    }else {
        console.log('No autorizado')
    }
})
document.body.append(button)

// forma altenativa de trabajar con condicionales
const button_1 = document.createElement('button')
button_1.innerText = 'Click me'
button_1.addEventListener('click', () => {
    // como alternativa utilizamos return para salir de la función si es true. Si es false pasa de largo el if y ejecuta el segundo console.log
    if (is_authorized) {
        return console.log('Autorizado')
    }
    console.log('No autorizado')
    
})
document.body.append(button_1)
```

# String literales

Strings literals permite concatenar variables con strings interpretando el valor de la variable dentro del mismo string. Los strings literales los definimos dentro de backsticks que son las comillas \` \`.

```js
// definimos variables con strings
const background = 'grey'
const color = 'red'

const button = document.createElement('button')
button.innerText = 'Click me'

// podemos agregar estilos a los elementos html que creamos utilizando strings literals
button.style = `background: ${background}; color: ${color}`
document.body.append(button)
```

# Operador ternario

Mediante el operador ternario podemos generar un condicional en una sola línea. La sintaxis es `condition ? do true : do false`

```js
const background = 'grey'
const color = 'red'
const is_authorized = false

const button = document.createElement('button')
button.innerText = 'Click me'

// si is_authorized es true devuelve el valor de background, si es false devuelve un string blue
button.style = `background: ${is_authorized ? background : 'blue'}; color: ${color}`
document.body.append(button)
```

# Métodos de array

## `forEach`

El método `forEach` espera como parámetro una función. Ejecuta sobre cada uno de los elementos del array lo que la función indica. `forEach` solo recorre el arreglo y ejecuta lo que indica la función que recibe como parámetro.

```js
const names = ['Miguel', 'Ángel', 'Daniela']

// cada elemento del array names va a llamarse name y se va a ejecutar lo que indica la función sobre cada uno
names.forEach( name => {
    console.log(name)
})
```

## `map`

El método `map`  espera como parámetro una función. Ejecuta sobre cada uno de los elementos del array lo que la función indica. El método `map` no solo recorre el array y ejecuta lo que indica la función que recibe como parámetro sino que además devuelve un nuevo arreglo. `map` no modifica el arreglo original.

```js
const names = ['Miguel', 'Ángel', 'Daniela']

// cada elemento del array names va a llamarse name y se va a ejecutar lo que indica la función sobre cada uno
names_1 = names.map( name => {    
    console.log(name)
    return `${name}_1`
})
console.log(names_1)
```

## `find`

Utilizamos el método `find` para buscar un elemento dentro de un array. Recorre cada uno de los elementos del array y devuelve un valor si se cumple con la condición dentro de la función que pasamos por parámetro.

```js
const names = ['Miguel', 'Ángel', 'Daniela']

// cada elemento del array names va a llamarse name y se va a ejecutar lo que indica la función sobre cada uno
names_2 = names.find( name => {    
    console.log(name)
    if (name === 'Daniela'){
        return name
    }
})
console.log(`Encontramos el nombre: ${names_2}`)
```

## `filter`

Utilizamos el método `find` para devolver elementos filtrados de un array. Recorre cada uno de los elementos del array y devuelve el elemento si el mismo cumple con la condición del filtro que pasamos en la función que recibe como parámetro. `filter` devuelve un nuevo array.

```js
const names = ['Miguel', 'Ángel', 'Daniela']

// cada elemento del array names va a llamarse name y se va a ejecutar lo que indica la función sobre cada uno
names_3 = names.filter( name => {    
    console.log(name)
    if (name !== 'Ángel'){
        return name
    }
})
console.log(names_3)
```

## `concat`

Utilizamos el método `concat` para concatenar dos array. El método `concat` devuelve un nuevo array.

```js
const names = ['Miguel', 'Ángel', 'Daniela']
const names_1 = ['Braja', 'Santy', 'Maite']

const names_2 = names.concat(names_1)
console.log(names_2)
```

# spread operator

Otra forma de concatenar elementos de un array es mediante el spread operator. 

```js
const names = ['Miguel', 'Ángel', 'Daniela']
const names_1 = ['Braja', 'Santy', 'Maite']

console.log([...names, ...names_1])
```

Podemos usar el spread operator con objetos.

```js
const user = {
    name: 'Miguel',
    last_name: 'Quinteros'
}
const address = {
    street: 'Avenida Siempre Viva 123',
    city: 'Tucumán'
}
const user_info = {
    ...user, ... address
}

console.log(user_info)
```

# EcmaScript modules

Podemos dividir una aplicación de javascript en multiples archivos que se conocen como módulos. Desde estos módulos podemos exportar variables o funciones hacia otros archivos o módulos.

Primero tenemos que configurar `index.html` para que reconozca nuestro archivo `index.js` como módulo.

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
	<!-- mediante el atributo html type indicamos que index.js es un módulo -->
    <script type="module" src="./index.js"></script>
</body>
</html>
```

Desde un mismo módulo podemos exportar más de una función. Podemos indicar o no una función por defecto. Si indicamos una función por defecto solo se exportará esa función aunque otras también tengan la palabra reservada export.

`add_subtraction.js`

```js
// función por defecto que se exporta
export default function add(x, y) {
    return x + y
}

// para acceder a está función usamos notación de . como en los objetos o desestructuración
export function subtraction(x, y){
    return x - y
}


```

Importando la función indicada por defecto.

`index.js`

```js
// sin importar el nombre que indiquemos en el import, va a traer la función que declaramos por defecto
import add_1 from './add_subtraction.js'
import subtraction  from './add_subtraction.js'

// en ambos casos realiza una suma
console.log(add_1(30,7))
console.log(subtraction(30,7))
```

En el caso de querer exportar más de una función en el mismo archivo.

`add_subtraction.js`

```js
export function add(x, y) {
    return x + y
}

export function subtraction(x, y){
    return x - y
}
```

El total de las funciones, aunque solo sea una, se exportan como si fueran atributos de un objeto. Si no indicamos una función por defecto podemos exportar varias y desestructurarlas.

`index.js`

```js
// traemos ambas funciones renombrando la función subtraction como sub mediante la palabra reservada as
import {add , subtraction as sub} from './add_subtraction.js'

console.log(add(30,7))
console.log(sub(30,7))
```

# optional chaining

En ocasiones tratamos de acceder a valores de un objeto que puede que no existan. Podemos resolver esto con un condicional pero una manera mas sencilla de hacerlo es mediante optional chaining.

```js
const user = {
    name: 'Miguel',
    address: {
        city: 'Tucumán'
    }
}
console.log(user.address.city)
console.log(user.location.city) // devuelve un error
```

Podemos resolverlo de dos formas.

```js
const user = {
    name: 'Miguel',
    address: {
        city: 'Tucumán'
    }
}
console.log(user.address.city)
// console.log(user.location.city) // devuelve un error

// forma normal de resolverlo. Si location no está definido no ingresa en el condicional
if (user.location){
    console.log(user.location.city)
}

// mediante optional chaining indicamos con ? cual es la variable que tiene que evaluar si existe
console.log(user.location?.city) // devuelve undefined
```

En el caso de que el atributo del objeto exista.

```js
const user = {
    name: 'Miguel',
    address: {
        city: 'Tucumán'
    },
    location: {
        city: 'San Miguel de Tucumán'
    }
}
console.log(user.address.city)
console.log(user.location.city)

if (user.location){
    console.log(user.location.city)
}

console.log(user.location?.city) // devuelve undefined
```
