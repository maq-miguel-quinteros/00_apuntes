# JavaScript


Para ejecutar el archivo de ejemplos `02_JavaScript_example.js`, en la consola de Visual Studio Code navegar hasta el path donde se encuentra el archivo y ejecutar el comando `node 02_JavaScript_example.js`.

# Tipos de datos


El tipo de dato `string` (cadena de caracteres)


```js
var string = "Carlos";
console.log(string);
```

El tipo de dato `number` (numérico)


```js
var number = 1000;
console.log(number);
```

El tipo de dato `object` (objeto)


```js
var object = {
    name: "Juan",
    lastName: "Perez",
    phone: "55443322"
}
console.log(object);
```

Las variables son dinámicas, con asignarle el valor indicamos el tipo de datos que almacena, a su vez si cambiamos su valor por otro, de otro tipo de datos, la misma cambia para adaptarse a al mismo.

El tipo de dato `typeof` devuelve el tipo de datos que está almacenado en la variable al momento de usarlo.


```js
console.log ('typeof de una variable String')
var name = "Carlos";
console.log(typeof name);

console.log ('typeof de una variable number')
var age = 5;
console.log(typeof age);

console.log ('typeof de una variable object')
var person = {
    name: "Juan",
    lastName: "Perez",
    phone: "55443322"
}
console.log(typeof person);
```

El tipo de dato `boolean` puede tomar los valores de `true` o `false` (verdadero o falso). Este tipo de variable se conoce como bandera.


```js
var boolean = false;
console.log(typeof boolean);
```

El tipo de dato `function` (función) permite realizar una tarea. Lleva adelante una serie de lineas de código y, si necesitamos volver a realizar esa tarea, podemos volver a llamar a la función.


```js
function myFunction() { }
console.log(typeof myFunction);
```

El tipo de dato `Symbol` se utiliza para crear un valor único de una variable. Si necesitamos crear una variable de este tipo llamamos a la función `Symbol()` y entre los paréntesis pasamos una cadena de caracteres.


```js
var symbol = Symbol("mi simbolo");
console.log(typeof symbol);
```

El tipo de dato `class` (clase) es un tipo `function`. Por lo general se define la clase con su nombre en singular y empezando en mayúsculas. Para poder definir objetos de esta clase necesitamos un método o función, propio de la clase, llamado constructor. Con la palabra reservada `this` seguida de `.atributo` indicamos que al atributo, propio de la clase, le asignamos un `valor`, que viene por parámetros en el constructor, de la forma `this.atributo = valor`.


```js
class Person {

	/** método constructor de la clase recibe por parámetros newName, newLastName */
	constructor(newName, newLastName) {

		/** asignamos a los atributos nombre y apellido, propios de la clase, lo que llega por parámetro */
		this.name = newName;
		this.lastName = newLastName;
	}
}
console.log(typeof Person);
```

El tipo de dato `undefined` es un tipo de dato y, a la vez, un valor que puede tomar una variable cuando, por ejemplo, se la declara sin asignarle valores.

```js
var x;
console.log(typeof x);

x = undefined;
console.log(x);
```

Para el caso de `null`, este no es un tipo de datos sino que es un valor asignable a una variable, que representa la ausencia de valor.

```js
var y = null;
console.log(y);
console.log(typeof y);
```

Para el caso de los array (arreglos), su tipo de dato es `object`.

```js
var autos = ['BMW','Audi','Volvo'];
console.log(autos);
console.log(typeof autos);
```

Para el caso de las cadenas vacías su tipo de dato es `string` pero al consultar su contenido nos devuelve `empty string`, que no es un tipo de dato sino un valor (el contenido de una variable).

```js
var z = '';
console.log(z); // devuelve empty string aunque en notebooks no aparezca así
console.log(typeof z);
```

# Variables

## Concatenación de variables

Podemos concatenar variables usando el operador `+`. Al concatenar el contenido de dos o más variables o datos generamos una nueva cadena. Mediante `+ ' ' +` concatenamos un espacio en blanco entre las dos variables.

```js
var nombre = 'Juan';
var apellido = 'Perez';

var nombreCompleto = nombre + ' ' + apellido;
console.log(nombreCompleto);
```

No es necesario tener en variables los valores para concatenar.

```js
var nombreCompleto2 = 'Carlos' + ' ' + 'Lara';
console.log(nombreCompleto2);
```

La lectura de las operaciones, ya sea aritméticas o de concatenación de `string`, se hace de izquierda a derecha. Si comienza con números, realizar la operación matemática hasta que encuentra un `string`, a partir del este realiza la concatenación. Se atiende primero las operaciones que están dentro de los paréntesis, luego lo que está afuera.

```js
var nombre = 'Juan';
var x = nombre + 2 + 4;
console.log(x);

/**  realiza la suma dentro del paréntesis antes de realizar la concatenación */
x = nombre + (2 + 4);
console.log(x);

x = 2 + 4 + nombre;
console.log(x);
```

## Declaración de variables

### Literales

Un literal es un dato suelto, que podemos asignar a una variable. Un literal tiene un tipo, como las variables, el tipo de un literal puede ser `string`, `number`, `boolean`, etc. Los siguientes son literales:

```js
3;
3.5;
'Andrea';
```

Cuando asignamos un literal a una variable, podemos decir que guardamos el literal dentro de la variable.

```js
var nombre = 'Andrea';
```

### Uso de `var`, `let` y `const`

Ya no se recomienda usar la palabra reservada `var` para declarar una variable, sino la palabra reservada `let`. A su vez tampoco es necesario utilizar `let` para declarar la variable, se pueden declarar solo escribiendo el nombre, pero una buena práctica es escribir `let` antes del nombre de la variable. Podemos declarar primero la variable y asignarle el valor a la misma luego, o declarar la variable en una línea de código, y asignarle el valor en otra línea de código distinta.

```js
let nombre;
nombre = "Juan";
console.log(nombre);
nombre = "Pedro";
console.log( nombre );
```

Para declarar una constante utilizamos la palabra reservada `const`. A diferencia de las variables, a las constantes no podemos volver a asignarle un valor luego de hacerlo la primera vez.

```js
const apellido = "Perez";
console.log(apellido);
apellido = "Gomez"; // dará error
```

Podemos declarar las variables por grupos con coma y asignarles el valor en la misma línea también separadas por coma.

```js
let x, y;
x = 10, y = 20;
let z = x + y;
console.log(z);
```

Javascript es sensible a mayúsculas y minúsculas para los nombres de las variables o funciones. No se puede comenzar el nombre de una variable o función con un número. Para el inicio del nombre se permiten mayúsculas, minúsculas y los signos `_` y `$`. No se pueden utilizar las palabras reservadas como nombre de variable o función.

La palabra reservada `console` es un objeto, por su parte `log` es un método del objeto `console`, por lo que al escribir la sentencia `console.log()` estamos llamando a un método que se encarga de mostrar valores por consola. A esto solo queda indicar el argumento que va a recibir el método de la forma `console.log(argumento)`.

```js
let nombreCompleto = "Juan Perez";
console.log( nombreCompleto );
```

# Operadores
