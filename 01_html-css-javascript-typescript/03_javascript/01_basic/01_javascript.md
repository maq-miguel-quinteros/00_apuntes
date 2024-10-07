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

## Operadores aritméticos

Suma

```js
let a = 3, b = 2;
let z = a + b;
console.log("Resultado de la suma: " + z);
```

Resta

```js
let a = 3, b = 2;
z = a - b;
console.log("Resultado de la resta: " + z);
```

Multiplicación

```js
let a = 3, b = 2;
z = a * b;
console.log("Resultado de la multiplicación: " + z);
```

División

```js
let a = 3, b = 2;
z = a / b;
console.log("Resultado de la división: " + z);
```

Módulo o resto de la división

```js
let a = 3, b = 2;
z = a % b;
console.log("Resultado del módulo (resto): " + z);
```

Exponente

```js
let a = 3, b = 2;
z = a ** b;
console.log("Resultado del exponente: " + z);
```

## Operadores de incremento y decremento

Pre-incremento. El operador `++` va antes de la variable `++variable`.

```js
a = 3;
z = ++a; // se incrementa a en 1 y despues se asigna a z
console.log("a: " + a);
console.log("z: " + z);
```

Post-incremento. El operador `++` va después de la variable `variable++`.

```js
b = 2;
z = b++; // se asigna b a z y después se hace el incremento de 1 en b
console.log("b: " + b);
console.log("z: " + z);
```

Pre-decremento. El operador `--` va antes de la variable `--variable`.

```js
a = 3;
z = --a; // se decrementa a en 1 y despues se asigna a z
console.log("a: " + a);
console.log("z: " + z);
```

Post-decremento. El operador `--` va después de la variable `variable--`.

```js
b = 2;
z = b--; // se asigna b a z y después se hace el decremento de 1 en b
console.log("b: " + b);
console.log("z: " + z);
```

## Precedencia de operadores

Las expresiones se evalúan de izquierda a derecha. Siempre se evalúan primero las expresiones que están dentro de los paréntesis, desde los más internos hasta los más externos. El orden de prioridad de los operadores es el siguiente:
1.   Paréntesis: `()`
2.   División y multiplicación: `/ *`
3.   Suma y resta: `+ -`

```js
a = 3, b = 2, c = 1, d = 4;

z = a * b + c / d;
console.log(z);

z = c + a * b / d;
console.log(z);

z = (c + a) * b / c;
console.log(z);
```

## Operadores de asignación

Operador de asignación común.

```js
a = 1;
console.log(a);
```

Operadores de asignación compuesto. Son operadores de asignación que además de asignar el valor realizan una operación aritmética antes de la asignación.

```js
a = 1;

a += 3; // a = a + 3
console.log(a);

a -= 2; // a = a - 2
console.log(a);

a *= 5; // a = a * 5
console.log(a);

a /= 2; // a = a / 2
console.log(a);

a %= 3; // a = a % 2
console.log(a);

a **= 2; // a = a ** 2
console.log(a);
```

## Operadores de comparación

El operador de comparación de igualdad `==` revisa el valor de las dos variables a comparar sin importar el tipo.

```js
a = 3, b = 2, c = "3";

z = a == c; // convierte la cadena '3' a número y los compara
console.log(z);
```

El operador de comparación de igualdad `===` revisa el valor de las dos variables a comparar y también su tipo. Ambos tienen que ser iguales para que la comparación de `true`.

```js
a = 3, b = 2, c = "3";

z = a == c; // convierte la cadena '3' a número y los compara
console.log(z);
```

El operador de comparación de desigualdad `!=` revisa el valor de las dos variables a comparar sin importar el tipo.

```js
a = 3, b = 2, c = "3";

z = a != c; // convierte la cadena '3' a número y los compara
console.log(z);
```

El operador de comparación de igualdad `!==` revisa el valor de las dos variables a comparar y también su tipo. Ambos tienen que ser iguales para que la comparación de true.

```js
a = 3, b = 2, c = "3";

z = a !== c; // convierte la cadena '3' a número y los compara
console.log(z);
```

## Operadores relacionales

Son operadores que devuelven valores de verdad (`true` o `false`) dependiendo de la expresión que se evalúa. Los operadores son menor que `<`, menor igual que `<=`, mayor que `>` y mayor igual que `>=`.

```js
a = 3, b = 2, c = "3";

z = a < b;
console.log(z);

z = a <= b;
console.log(z);

z = a > b;
console.log(z);

z = a >= b;
console.log(z);
```

## Operadores lógicos

El operador lógico and (`&&`) solo devuelve `true` cuando las dos expresiones que se evalúan son `true`.

```js
valMin = 0, valMax = 10;

a = 15;

if( a >= valMin && a <= valMax ){
    console.log("Dentro de rango"); 
}else{
    console.log("Fuera de rango"); // devuelve este mensaje
}

a = 9;

if( a >= valMin && a <= valMax ){
    console.log("Dentro de rango"); // devuelve este mensaje
}else{
    console.log("Fuera de rango"); 
}
```

El operador lógico or (`||`) solo devuelve `false` cuando las dos expresiones que se evalúan son `false`.

```js
vacaciones = false, diaDescanso = true;

if( vacaciones || diaDescanso ){
    console.log("Padre puede asistir al juego del hijo"); // devuelve este mensaje
}else{
    console.log("El padre está ocupado");
}

vacaciones = false, diaDescanso = false;

if( vacaciones || diaDescanso ){
    console.log("Padre puede asistir al juego del hijo"); 
}else{
    console.log("El padre está ocupado"); // devuelve este mensaje
}
```

## Operador ternario

El operador ternario revisa la condición dentro del `()` y devuelve lo que está después de `?` si la condición dio `true` o lo que está después de los `:` si la condición dio `false`. No es necesario poner la condición entre paréntesis.

```js
resultado = (1>2) ? "verdadero" : "falso";
console.log(resultado);

numero = 110;
resultado = numero % 2 == 0 ? "Número par" : "Número impar"; 
console.log( resultado );
```

## Funciones especiales `Number` e `isNaN`

Mediante la función `Number` convertimos el valor de una variable de `string` a un `number`.

```js
miNumero = "18";
console.log(typeof miNumero); // devuelve string
 
edad = Number(miNumero);
console.log(typeof edad);
console.log(edad); 
 
if(edad >= 18){
 console.log("Puede votar");
}else{
 console.log("Muy joven para votar");
}
 
resultado = (edad >= 18)? "Puede votar" : "Muy joven para votar";
console.log( resultado );
```

Utilizamos la función `isNaN` para saber si la variable es un número antes de trabajar con ella. La función isNaN devuelve `true` si la variable no contiene un número y `false` en caso contrario.

```js
miNumero = "17x";

/** al tener caracteres el string no se puede convertir en número */
edad = Number(miNumero); 

/** devuelve NaN que significa not a number */
console.log(edad);

edad = 18;

if( isNaN(edad)){
  console.log("No es un número");
}else{
  if(edad >= 18){
    console.log("Puede votar");
  }else{
    console.log("Muy joven para votar");
  }
}

if( isNaN(edad)){
  console.log("No es un número");
}
else{
  let resultado = (edad >= 18)? "Puede votar" : "Muy joven para votar";
  console.log( resultado ); 
}
```

# Estructuras de control
