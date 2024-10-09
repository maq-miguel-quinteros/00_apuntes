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
console.log('typeof de una variable String')
var name = "Carlos";
console.log(typeof name);

console.log('typeof de una variable number')
var age = 5;
console.log(typeof age);

console.log('typeof de una variable object')
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
var autos = ['BMW', 'Audi', 'Volvo'];
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
console.log(nombre);
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
console.log(nombreCompleto);
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

if (a >= valMin && a <= valMax) {
    console.log("Dentro de rango");
} else {
    console.log("Fuera de rango"); // devuelve este mensaje
}

a = 9;

if (a >= valMin && a <= valMax) {
    console.log("Dentro de rango"); // devuelve este mensaje
} else {
    console.log("Fuera de rango");
}
```

El operador lógico or (`||`) solo devuelve `false` cuando las dos expresiones que se evalúan son `false`.

```js
vacaciones = false, diaDescanso = true;

if (vacaciones || diaDescanso) {
    console.log("Padre puede asistir al juego del hijo"); // devuelve este mensaje
} else {
    console.log("El padre está ocupado");
}

vacaciones = false, diaDescanso = false;

if (vacaciones || diaDescanso) {
    console.log("Padre puede asistir al juego del hijo");
} else {
    console.log("El padre está ocupado"); // devuelve este mensaje
}
```

## Operador ternario

El operador ternario revisa la condición dentro del `()` y devuelve lo que está después de `?` si la condición dio `true` o lo que está después de los `:` si la condición dio `false`. No es necesario poner la condición entre paréntesis.

```js
resultado = (1 > 2) ? "verdadero" : "falso";
console.log(resultado);

numero = 110;
resultado = numero % 2 == 0 ? "Número par" : "Número impar";
console.log(resultado);
```

## Funciones especiales `Number` e `isNaN`

Mediante la función `Number` convertimos el valor de una variable de `string` a un `number`.

```js
miNumero = "18";
console.log(typeof miNumero); // devuelve string

edad = Number(miNumero);
console.log(typeof edad);
console.log(edad);

if (edad >= 18) {
    console.log("Puede votar");
} else {
    console.log("Muy joven para votar");
}

resultado = (edad >= 18) ? "Puede votar" : "Muy joven para votar";
console.log(resultado);
```

Utilizamos la función `isNaN` para saber si la variable es un número antes de trabajar con ella. La función isNaN devuelve `true` si la variable no contiene un número y `false` en caso contrario.

```js
miNumero = "17x";

/** al tener caracteres el string no se puede convertir en número */
edad = Number(miNumero);

/** devuelve NaN que significa not a number */
console.log(edad);

edad = 18;

if (isNaN(edad)) {
  console.log("No es un número");
} else {
  if (edad >= 18) {
    console.log("Puede votar");
  } else {
    console.log("Muy joven para votar");
  }
}

if (isNaN(edad)) {
  console.log("No es un número");
}
else {
  let resultado = (edad >= 18) ? "Puede votar" : "Muy joven para votar";
  console.log(resultado);
}
```

# Estructuras de control

## Estructura if / else

Según una condición de verdad, examinada por la palabra reservada `if`, realiza uno u otro conjunto de sentencias. La expresión examina una condición, si la misma se cumple, es decir es `true`, realiza un conjunto de sentencias. La estructura puede quedar de esa manera pero, en caso de que no se cumpla la condición, es decir que sea `false`, podemos indicarle a la expresión realizar otro conjunto de sentencias diferente, mediante la palabra reservada `else`.

```js
condicion = true;

if (condicion) {
    console.log("Condición verdadera");
    console.log("fin del programa");
}
else {
    console.log("Condición falsa");
}

/**  en caso de tener una sola línea a continuación de if o else podemos omitir el uso de llaves */
condicion = 3;
if (condicion > 2) console.log("Condición verdadera");
else console.log("Condición falsa");
```

Podemos anidar los `if else` para poder realizar consultas que vayan descartando distintas opciones. En el ejemplo tabulamos los anidamientos para visualizar cuanto se adentra en los `if else`.

```js
let numero = 2;

if (numero == 1) {
    console.log("Número uno");
} else if (numero == 2) {
    console.log("Número dos");
} else if (numero == 3) {
    console.log("Número tres");
} else if (numero == 4) {
    console.log("Número cuatro");
} else {
    console.log("Número desconocido");
}
```

Podemos utilizar los operadores lógicos `and` (`&&`) y `or` (`||`) para evaluar las condiciones de verdad de la sentencia de control.

```js
/** Estaciones del año con if else*/
let mes = 12;
let estacion;

if (mes == 1 || mes == 2 || mes == 12) {
    estacion = "Invierno";
}
else if (mes == 3 || mes == 4 || mes == 5) {
    estacion = "Primavera";
}
else if (mes == 6 || mes == 7 || mes == 8) {
    estacion = "Verano";
}
else if (mes == 9 || mes == 10 || mes == 11) {
    estacion = "Otoño";
}
else {
    estacion = "Valor incorrecto";
}

console.log(estacion);

/** saludo segun las horas del día */

let horaDia = 23;
let mensaje;

if (horaDia >= 6 && horaDia <= 11) {
    mensaje = "Buenos días";
}
else if (horaDia >= 12 && horaDia <= 18) {
    mensaje = "Buenas tardes";
}
else if (horaDia >= 19 && horaDia <= 24) {
    mensaje = "Buenas noches";
}
else if (horaDia >= 0 && horaDia < 6) {
    mensaje = "Durmiendo";
}
else {
    mensaje = "Valor incorrecto";
}

console.log(mensaje);
```

## Estructura `switch`

Esta estructura evalúa una variable y en caso de coincidir con algunas de las opciones que tiene configuradas realiza el conjunto de sentencias asociadas a esa opción. La palabra reservada `switch` es la que se utiliza para iniciar la expresión y evaluar la variable. Cada una de las opciones se definen mediante la palabra reservada `case`. Una vez realizadas todas las sentencias del `case` correspondiente salimos de la estructura mediante la palabra reservada `break`.

```js
numero = 1;
let numeroTexto = 'Valor desconocido';

switch (numero) {
    case 1:
        numeroTexto = 'Número uno';
        break;

    /** en caso no encontrarse el break se va a ejecutar el siguiente case aunque la variable no cumpla con la opcion
     * esto sucede por que la ejecución de las sentencias es secuencias de arriba a abajo y el break, que hace saltar
      esa secuencia no esta escrito */
    case 2:
        numeroTexto = 'Número dos';
        break;
    case 3:
        numeroTexto = 'Número tres';
        break;
    case 4:
        numeroTexto = 'Número cuatro';
        break;

    /** si la variable no cumple con ninguno de los casos se ejecutan las sentencias a continuación de default
     * la opción default puede no estar, si es así y no se ejecuta ninguno de los case solo se sale de la estructura
     * podemos escribir default al comienzo de la estructura, pero en ese caso tiene que tener su correspondiente break
     * en este caso no es necesario el break por que despues de las sentencias de default salimos de la estructura switch */
    default:
        numeroTexto = 'Caso no encontrado';
}

console.log(numeroTexto);
```

```js
/** Estaciones del año con switch */
mes = 11;
estacion = 'Estación desconocida';

switch (mes) {
    case 1: case 2: case 12:
        estacion = 'Invierno';
        break;
    case 3: case 4: case 5:
        estacion = 'Primavera';
        break;
    case 6: case 7: case 8:
        estacion = 'Verano';
        break;
    case 9: case 10: case 11:
        estacion = 'Otoño';
        break;
    default:
        estacion = 'Valor incorrecto';
}
console.log(estacion);
```

# Bucles

Los bucles nos permiten repetir un conjunto de sentencias en la medida en que se cumpla una condición.

## Bucle while

Mediante la palabra reservada `while` indicamos que se evalúe la sentencia dentro de los paréntesis. Si la condición es `true` se ejecutan las sentencias que están entre las `{}`, al terminar estas sentencias vuelve a evaluar la condición entre los paréntesis, si sigue `true` vuelve a ejecutarse las sentencias entre las llaves. Cuando la condición es `false` sale de bucle o ciclo.

```js
let contador = 0;
/** la variable que evaluamos entre los parentesis la llamamos contador, por que
 *  está va a incrementarse dentro de las llaves para, eventualmente, salir del bucle
 *  */
while (contador < 3) {
    console.log(contador);
    contador++;
}
console.log("Fin ciclo while");
```

## Bucle do while

En el bucle `do while` el conjunto de sentencias que deben ejecutarse cuando la condición es `true`, se van a ejecutar al menos una vez antes de evaluar la condición. Mediante la palabra reservada `do` indicamos realizar las sentencias entre `{}` y al final de estas, mediante el `while`, evaluamos si se cumple la condición, de ser `true` volvemos a ejecutar las sentencias entre llaves y al final evaluamos de nuevo. Cuando la condición devuelve `false` salimos del bucle.

```js
let contador = 0;

do {
    console.log(contador);
    contador++;
} while (contador < 3); // es importante terminar la sentencia while con ;
console.log("Fin ciclo do while");
```

## Bucle for

En el bucle `for` definimos todas las partes del bucle, como ser la variable que se evalúa, la condición que se evalúa y el incremento de la variable, todo dentro de los paréntesis con el que lo generamos. En el ejemplo primero se ejecuta `let contador = 0`, esta sentencia se ejecuta solo la primera vez que entramos en el bucle. Después ejecutamos la condición `contador < 3`, si la misma devuelve `true` se ejecutan las sentencias dentro de las `{}`. Una vez terminadas las sentencias de las llaves ejecutamos `contador++` incrementando la variable contador. Después de eso volvemos a ejecutar la condición, si devuelve `true` de nuevo se ejecutan las sentencias dentro de las llaves y vuelve a sumarse el contador. Si la condición da `false` sale del bucle.

```js
//   def variable      condición     incremento
for (let contador = 0; contador < 3; contador++) {
    console.log(contador);
}
console.log("Fin ciclo for");
```

## Palabra reservada `break`

Mediante la palabra reservada `break` podemos indicar que se termine el bucle que se está ejecutando aunque no se hayan completado todos los casos en que la condición devuelve `true`.

```js
/** en el ejemplo mostramos el primer número par y después salimos del bucle */
for (let contador = 0; contador <= 10; contador++) {
    if (contador % 2 !== 0) {
        console.log(contador);
        break; // termina la ejecución del bucle for por completo 
    }
}
```

## Palabra reservada `continue`

Mediante la palabra reservada `continue` indicamos al bucle que, en el punto donde aparece `continue`, se termine la ejecución de sentencias dentro de los `{}` y se pase a incrementar la variable a evaluar con `contador++` y que vuelva a evaluarse la condición que, si devuelve `true`, volverá a entrar en el bucle. Es decir que con `continue` detenemos la ejecución de sentencias dentro del bucle en ese punto y pasamos a la siguiente iteración, de corresponder, o salimos del bucle si la condición devuelve `false`.

```js
for (let contador = 0; contador <= 10; contador++) {
    if (contador % 2 !== 0) {
        continue; // ir a la siguiente iteración
    }
    console.log(contador);
}
```

## Labels

Podemos indicar, dentro del código, una label o etiqueta, que es una linea en la secuencia de sentencias del código a la que podemos volver si necesitamos que las sentencias de la misma se repitan por algún motivo. En el ejemplo el label es `inicio:` y dentro del bucle indicamos mediante `continue inicio` que al ejecutarse esa linea de código la secuencia de sentencias vaya a lo que se encuentra a continuación de la etiqueta `inicio:`. Podemos indicar una etiqueta a donde redireccionar la secuencia de ejecución al usar la palabra reservada `break` de la manera `break inicio;`. En este caso en lugar de redireccionar a esa etiqueta indicamos saltar todo lo contenido a continuación de la misma. Este tipo de programación se conoce como `go to`. No es recomendado trabajar de este forma.

```js
inicio:
for (let contador = 0; contador <= 10; contador++) {
    if (contador % 2 !== 0) {
        continue inicio; // ir a la siguiente iteración
    }
    console.log(contador);
}
```

# Arreglos o `array`

Un arreglo o `array` es una variable de tipo `object` que permite almacenar, no solo uno sino varios elementos. Los elementos que almacena una arreglo pueden ser de distintos tipo como `number` o `String` o hasta `object` como otro arreglo. Podemos declarar un arreglo mediante el operador `new` y la clase `Array`. Esta es una forma antigua de declarar los arreglos que ya no se recomienda usar. Actualmente creamos una variable o constante y la hacemos igual a los valores que va a tener el arreglo. La variable almacena la referencia a la dirección en memoria donde se encuentran los datos que contiene el arreglo.

```js
/** forma antigua de declarar arreglos */
let autos1 = new Array('BMW', 'Mercedes Benz', 'Volvo');

/** forma actual de declarar arreglos usando let o const 
 *  según se vayan a agregar datos o no al arreglo */
const autos2 = ['BMW', 'Mercedes Benz', 'Volvo'];

console.log(autos1);
console.log(autos2);
```

## Recorrer elementos de un arreglo

```js
const autos = ['BMW', 'Mercedes Benz', 'Volvo'];
console.log(autos);

console.log(autos[0]);
console.log(autos[2]);

/** recorremos el arreglo e imprimimos en consola un mensaje utilizando 
 * cada uno de los elementos. Utilizamos la variable contador i como indice
 * dentro de los corchetes para trabajar con cada elemento */
for (let i = 0; i < autos.length; i++) {
    console.log(i + ' : ' + autos[i]);
}
```

Mediante al propiedad `length` podemos saber la longitud del arreglo, es decir, la cantidad de elementos que tiene el arreglo. Esta propiedad nos sirve para recorrer un arreglo, mediante un bucle `for`, y trabajar sobre cada uno de sus elementos por separado.

## Modificar elementos de un arreglo

Para modificar los datos de un elemento en un arreglo tenemos que acceder al elemento utilizando su indice y asignarle el nuevo valor que este elemento va a tener. En el ejemplo es la linea `autos[1] = 'MercedesBenz'`.

```js
const autos3 = ['BMW', 'Mercedes Benz', 'Volvo'];
console.log(autos3);

/** cambiamos el vamor 'Mercedes Benz' del elemto 1 por 'MercedesBenz' */
autos3[1] = 'MercedesBenz';
console.log(autos3[1]);
```

## Agregar elementos en un arreglo

Para agregar un nuevo elemento al arreglo utilizamos la función o método `push` del tipo de dato `array`. El nuevo elemento se va a agregar a continuación del último indice del arreglo.

```js
const autos4 = ['BMW', 'Mercedes Benz', 'Volvo'];
console.log(autos4);

/** agregamos el elemento 'Audi' al arreglo en el indice 3 */
autos4.push('Audi');
console.log(autos4);
```

También podemos agregar elementos al arreglo utilizando su longitud. 
La propiedad `autos5.length` devuelve un valor numérico, que es la longitud del arreglo pero, como los arreglos comienzan en 0, la propiedad `autos5.length` va a devolver un numero más al último indice del arreglo. Esto permite que `autos5[autos5.length] = 'Cadillac'` agregue al siguiente indice del arreglo el valor `'Cadillac'`.

```js
const autos5 = ['BMW', 'Mercedes Benz', 'Volvo'];
console.log(autos5);

console.log(autos5.length);
autos5[autos5.length] = 'Cadillac';

console.log(autos5);
```

También podemos agregar elementos dejando indices vacíos entre ellos. En el ejemplo la variable `autos5` quedó con 4 elementos en los índices del 0 al 3. Podemos agregar un elemento en el índice 7 sin tomar en cuenta los índices 4, 5 y 6. Esos dos índices quedan sin elementos, quedan vacíos. Ahora la variable `autos5` queda con 4 elementos pero con 8 índices que van del 0 al 7. No es recomendable sumar elementos a un arreglo de esta forma ni tener indices sin elementos o vacíos.

```js
autos5 = ["BMW", "Mercedes Benz", "Volvo", "Cadillac"];
autos5[7] = 'Porshe';
console.log(autos5);
```

## Consultar si una variable es un arreglo

Cuando necesitamos consultar si una variable es un arreglo, utilizando el tipo de dato `typeof` nos va a devolver que el tipo dato de la variable es `object`. Esta respuesta no es lo suficientemente específica. Para un respuesta mas certera podemos usar el método `isArray` de la clase `Array` de la forma `Array.isArray(variable)`, que nos devuelve `true` si la variable es un arreglo. También podemos usar `instanceof`, una palabra reservada de JavaScript que nos indica si la variable es una instancia de un tipo de datos, en este caso el tipo de datos es Array, si la variable es un arreglo la sentencia va a devolver `variable instanceof Array` va a devolver `true`.

```js
autos = ["BMW", "Mercedes Benz", "Volvo", "Cadillac"];

console.log(typeof autos);

console.log(Array.isArray(autos));

console.log(autos instanceof Array);
```

# Funciones

Una función es un código reutilizable que podemos llamar todas la veces que utilizamos. Llamar a una función significa solicitar, en un momento de la secuencia de sentencias, que la función se ejecute. Primero tenemos que declarar la función, para hacerlo utilizamos la palabra reservada `function` seguido del nombre de la función, de preferencia en notación camelCase (primera letra del nombre en minúscula y si consta de más de una palabra, la siguiente palabra empezando en mayúsculas sin espacio). Seguido al nombre agregamos `()` dentro de los cuales podemos o no tener argumentos de la función. Los argumentos son valores que ingresan a la función y que se van a utilizar cuando se ejecuten las sentencias dentro de la función. Seguido a esto abrimos llaves `{` escribimos el cuerpo de la función, que son las sentencias a ejecutar cada vez que llamemos a la función y finalmente cerramos llaves `}` indicando el final de la definición de la misma.

```js
function nombreFuncion(argumento1, argumento2, ...argumentoN) {
    // cuerpo de la función
}
```

```js
/** llamamos la funcion antes de definirla */
miFuncion(4, 2);

/** declaramos la función
 * si la misma tiene más de un argumento se separan por comas */
function miFuncion(a, b) {
    console.log("Suma: " + (a + b));
}

/** llamamos la función después de definirla */
miFuncion(2, 3);
```

Podemos llamar a la función, en la secuencia de sentencias, incluso antes de definir la misma. Esto se conoce como hoisting, donde JavaScript pasa, de forma automática, la definición de la función al comienzo de la ejecución de sentencias, para que esté definida al momento de llamarla.

## Palabra reservada `return`

Cuando necesitamos que la función nos devuelva un valor utilizamos, en el cuerpo de la misma, la palabra reservada `return` y a continuación el valor que queremos que devuelva. El valor que la función devuelve lo tenemos que asignar a una variable para poder trabajar con él. Si al final de la función no está la palabra `return` escrita JavaScript la agrega automáticamente, pero sin nada a continuación, por lo que la función no devuelve nada a pesar de tener `return` al final.

```js
/** declaramos la función */
function miFuncion(a, b) {
    return a + b;
}

/** llamamos a la función asignando a una variable el valor que devuelve */
resultado = miFuncion(2, 3);
console.log(resultado);
```

## Funciones de tipo expresión

Podemos asignar una función a una variable. Esto es diferente a asignar lo que la función devuelve a una variable. Cuando asignamos una función a una variable evitamos de tener que poner un nombre a la función. Para llamar a la misma utilizamos el nombre de la variable. Esto se conoce como funciones de tipo expresión o funciones anónimas.

```js
/** Declaramos la función
 * no es necesario ; al final de la declaración de la función */
function miFuncion(a, b) {
    return a + b;
}

/** Llamamos a la función */
resultado = miFuncion(2, 3);
console.log(resultado);

/** Declaramos la  función de tipo expresión 
* tenemos que finalizar la sentecia con ; por ser una expresión */
sumar = function (a, b) { return a + b };

resultado = sumar(1, 2);
console.log(resultado);
```

## Funciones de tipo self-invoking

Las funciones self-invoking son funciones que se llaman a sí mismas. Son funciones anónimas, sin nombre. Ak finalizar la declaración de la función la llamamos, una vez que lo hicimos ya no podemos volver a llamar a la misma. Declaramos la función abriendo paréntesis `(`, seguimos con la palabra reservada `function` seguida de nuevos paréntesis donde podemos tener argumentos si lo requiere. Abrimos llaves `{` y escribimos las sentencias del cuerpo de la función. Cerramos las llaves y el paréntesis `)}`. Para llamar a la función, si no tiene argumentos escribimos a continuación del final de la declaración, paréntesis `()`. Si la función tiene argumentos ponemos los valores de los argumentos dentro de los paréntesis.

```js
(function (a, b) {
    console.log('Ejecutando la función: ' + (a + b));
})(3, 4);
```

## Funciones como objetos

Las funciones tienen como tipo de dato `function`. A pesar de eso las mismas pueden ser descritas como objetos, que tienen propiedades y métodos asociados. 

```js
console.log(typeof miFuncion);

/** arguments es una propiedad que tiene la función al ser un objeto 
 * esta propiedad enumera la cantidad de argumentos de la funcion y su valor al llamarla
 * esta propiedad solo se puede usar dentro del cuerpo de la función */
function miFuncion(a, b) {
  console.log(arguments);
  console.log(arguments.length);
  return a + b;
}
miFuncion(3, 4);

/** toString es un método que tiene la función al ser un objeto 
 * este método convierte la declaración de la función en texto
 * el texto se guarda en la variable miFuncionTexto */
var miFuncionTexto = miFuncion.toString();
console.log(miFuncionTexto);
```

## Función flecha

Las funciones flecha son similares a las funciones de tipo expresión. No utilizamos `function`, directamente indicamos los argumentos o parámetros a continuación del `=`. Si la función solo tiene un argumento podemos indicarlo sin paréntesis, si tiene varios argumentos los indicamos entre paréntesis de la forma `(arg1, arg2, ... argn)`, si no tiene ningún argumento es necesario escribir los paréntesis vacíos `()`. A continuación escribimos el símbolo de flecha `=>` con lo que indicamos que continua el cuerpo de la función. Podemos omitir el uso de llaves y de la palabra reservada `return` si la función solo tiene una sentencia o linea de código. Si la función tiene más de una sentencia indicamos todo entre llaves y utilizamos `return`.

```js
/** Declaración Función de tipo Expresión */
let sumar = function (a, b) { return a + b };

resultado = sumar(1, 2);
console.log(resultado);

/** utilizamos const en lugar de let para evitar cambiar la referencia 
 * a la función que guarda la variable */
const sumarFuncionTipoFlecha = (a, b) => a + b;

/** llamamos a la función flecha */
resultado = sumarFuncionTipoFlecha(3, 5);
console.log(resultado);
```

## Parámetros y argumentos

En la mayoría de los casos podemos decir que los argumentos y los parámetros de una función son lo mismo, ya que en la práctica se manejan de forma equivalente. Se conocen como parámetros a la lista de variables que recibe la función cuando la declaramos. A su vez los argumentos son los valores que toman esas variables al momento de llamar a la función. Podemos llamar a la función con todos, algunos o ninguno de los argumentos para los parámetros con que se definió. En ese caso los argumentos que no se pasan quedan con valor `undefined o null`. A los parámetros podemos declararlos con valores por defecto cuando definimos la función, en caso de no pasar valores cuando se llama a la función el argumento de la misma va a ser el definido en la función por defecto. Podemos acceder a argumentos de la función aunque no estén declarados los parámetros correspondientes en la definición de la misma. En ese caso utilizamos el array `arguments[x]` donde x es el número de orden del parámetro si el mismo se hubiese definido `function (a = 4, b = 5, x)`. En el ejemplo x sería el valor 2.

```js
/** Declaración de una función de tipo expresión
 * al declarar la función damos valores por defecto a los parametros
 * el parametro es a y el argumento de ese parametro, por defecto, es 4 */
sumar = function (a = 4, b = 5) {
    console.log(arguments[0]); // muestra 3, valor con que llamamos a la función
    console.log(arguments[1]);
    console.log(arguments[2]);
    console.log(arguments[3]); // muestra null
    return a + b + arguments[2];
};

resultado = sumar(3, 6, 7);
console.log(resultado);
```

## Paso dinámico de argumentos a una función

```js
/** podemos pasar todos los argumentos que queramos a la función
 * mediante el array arguments vamos a ir sumando cada uno */
let resultado = sumarTodo(5, 4, 13, 10, 9, 10, 11, 3);
console.log(resultado);

function sumarTodo() {
    let suma = 0;
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i]; // suma = suma + arguments[i]
    }
    return suma;
}
```

## Paso por valor

En una asignación del tipo `x=10` el valor 10 se conoce como valor primitivo o valor de tipo primitivo, ya que no podemos asociar atributos o métodos a ese valor. Al pasar por valor el argumento de una función, no se pasa la referencia en memoria que corresponde a la variable que igualamos al parámetro, sino que pasamos el valor que contiene esa variable. Es decir, no pasamos la variable x sino el valor que tiene asignado la variable x que es 10. Pasamos una copia del valor de la variable x.

```js
x = 10;

function cambiarValor(a) {
    a = 20;
}

/** Paso por valor */
cambiarValor(x); // hacemos a = 10
console.log(x); // devuelve 10
console.log(a); // devuelve is not defined por que a existe solo dentro de la función
```

## Paso por referencia

Al contrario de los tipos primitivos tenemos los objetos. A los objetos podemos asociarles atributos y métodos. Las variables a las que igualamos estos objetos almacenan una referencia al objeto. En el ejemplo `persona` guarda una referencia al objeto con los atributos que le asignamos.

```js
/** definimos el objeto persona, para hacerlo usamos las llaves
 * despues definimos atributos y valores a esos atributos */
const persona = {
    nombre: 'Juan',
    apellido: 'Perez'
}
console.log(persona);

/** p1 = persona, es decir que p1 es igual a la referencia del objeto
 * a la que es igual persona, si modificamos los atributos de p1
 * se modifican los de persona */
function cambiarValorObjeto(p1) {

    /** mediante punto+atributo indicamos que queremos acceder a algun
     * atributo del objeto que pasamos por referencia */
    p1.nombre = 'Carlos';
    p1.apellido = 'Lara';
}

/** Paso por referencia */
cambiarValorObjeto(persona);
console.log(persona);
```

# Objetos

Casi todo lo que manejamos en JavaScript son objetos. La diferencia entre los valores de tipo primitivo y los objetos es que los primeros no tienen atributos ni métodos. Los atributos de un objeto pueden ser valores de tipo primitivo u otros objetos. El código que ingresamos entre `{}` crea un objeto en memoria. A este objeto se le asigna una referencia o dirección en memoria del lugar donde se aloja. Este valor o referencia es lo que se guarda en la variable con la que generamos el objeto, en el ejemplo `persona`. La variable persona entonces almacena la referencia en memoria donde se encuentra el objeto.

```js
/** el valor asignado a la variable x es de tipo primitivo
 * x.length devuelve undefined por que el método length no está definido
 * para la variable */
let x = 10;
console.log(x.length);

/** definimos el objeto en la variable persona
 * la variable puede llamarse perro y tener los mismos atributos
 * el nombre de la variable no define su contenido, tipo o clase */
let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,
}
/** mediante la variable persona podemos acceder a los atributos
 * y métodos del objeto utilizando la notación del punto */
console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.apellido);

console.log(persona);
```

## Agregar métodos a los objetos

Agregamos el método a la función como si fuera un atributo más de la misma. Se trabaja de forma similar a como trabajamos las funciones de tipo expresión. La función es, a su vez, un objeto, por lo que la referencia a esta función la asignamos una variable o atributo del objeto, en el ejemplo es `nombreCompleto`. Si necesitamos acceder a los atributos del objeto, dentro de una función o método que pertenecen al objeto, utilizamos la palabra reservada `this` para hacer referencia a que queremos utilizar el atributo perteneciente al objeto.

```js
let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,

    /** agregamos el método como si fuera un atributo del objeto
     * pero a la hora de declararlo no declaramos como un valor primitivo
     * sino como una función */
    nombreCompleto: function () {

        /** utilizamos this. para acceder a los atributos o métodos del objeto */
        return this.nombre + ' ' + this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.apellido);

/** llamamos a la función similar a como accedemos a los atributos
 * solo que tulizamos los () para indicar que es una función */
console.log(persona.nombreCompleto());

console.log(persona);
```

## Crear objetos

Podemos crear objetos definiendo la variable, que va a almacenar la referencia al objeto, y luego igualándola a `{}`, dentro de las llaves vamos a declarar los atributos y métodos del objeto de la forma `nombre : valor`, en el caso de ser valores de tipo primitivo u otros objetos y `nombre : function(){}`, en el caso de tratarse de un método. Podemos crear un objeto utilizando la palabra reservada `new` con esta palabra indicamos que necesitamos espacio en memoria para el objeto que estamos creando. la sintaxis para crear el objeto es `new Object()`. `Object` es un tipo de dato de JavaScript. Para agregar atributos o métodos al objeto que acabamos de crear los hacemos utilizando el punto. Los atributos o métodos se agregan de forma dinámica, es decir que se crean al momento en que los definimos.

```js
/** Definimos el objeto y asignamos su referencia a la variable persona  */
persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,
    nombreCompleto: function () {
        return this.nombre + ' ' + this.apellido;
    }
}

/** Definimos el objeto utilizando la palabra reservada new 
 * el objeto que se crea es vacío
 * la referencia en memoria al objeto se guarda en la variable persona2 */
let persona2 = new Object();

/** utilizamos punto para indicar los atributos o métodos que agregamos */
persona2.nombre = 'Carlos';
persona2.direccion = 'Saturno 15';
persona2.tel = '55443322';

console.log(persona2.tel);
```

## Acceder a atributos o métodos de objetos. Uso de `for in`

Podemos acceder a los atributos o métodos de los objetos mediante la notación de punto de la forma `objeto.atributo` u `objeto.metodo()`, donde objeto es la variable que tiene la referencia en memoria del objeto. También podemos acceder a los atributos de los objetos como si fueran un `array` de la forma `objeto['atributo']`. Podemos recorrer los atributos del objeto utilizando un ciclo `for` con la sintaxis `for (nombreAtributo in objeto){}`.

```js
persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,
    nombreCompleto: function () {
        return this.nombre + ' ' + this.apellido;
    }
}

/** accedemos al atributo del objeto utilizando el punto */
console.log(persona.nombre);

/** accedermos al atributo del objeto como si fuera un array */
console.log(persona['apellido']);

/** recorremos los atributos del objeto con el ciclo for in */
for (nombrePropiedad in persona) {
    console.log(nombrePropiedad);
    console.log(persona[nombrePropiedad]);
}
```

## Agregar o eliminar atributos y métodos de objetos

Con la notación de punto podemos agregar atributos o métodos a un objeto. El atributo o método agregado se suma a la colección de estos que ya tiene el objeto. Para eliminar un atributo o método de un objeto utilizamos la palabra reservada delete de la forma `delete objeto.atributo`. Esto borra el atributo y los valores que tenga asignados.

```js
let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,
    nombreCompleto: function () {
        return this.nombre + ' ' + this.apellido;
    }
}

/** agregamos el atributo tel que no existía en el objeto
 * y le asignamos un valor */
persona.tel = '55443322';

/** modificamos el valor del atributo tel del objeto */
persona.tel = '44332211';
console.log(persona);

/** eliminamos el atributo tel del objeto */
delete persona.tel;
console.log(persona);
```

## Formas de imprimir objetos

Una de las formas de imprimir los valores de un objeto es de la forma `console.log(objeto)` pero algunos navegadores pueden mostrar, ante ese método, la leyenda `Object Object`, sin desglosar sus atributos y métodos con sus valores. Podemos concatenar los valores de los atributos de la forma `console.log(objeto.atributo1 + ', ' + atributo2)`. Podemos recorrer el objeto mediante `for in` y mostrar sus atributos y métodos con `console.log`. Podemos utilizar el método `Object.values()` que regresa el objeto pero como un `array`. Similar a esto, pero utilizando una variable de tipo `String`, imprimimos los atributos del objeto mediante el método `JSON.stringify()` que convierte el objeto en una cadena de caracteres. Utilizamos el objeto `JSON` por que este, al igual que nuestros objetos, utiliza la notación de `atributo : valor`.

```js
let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,
    nombreCompleto: function () {
        return this.nombre + ' ' + this.apellido;
    }
}

/** concatenamos los valores asignados a cada atributo del objeto */
console.log(persona.nombre + ', ' + persona.apellido);

/** accdemos a cada uno de los atributos y métodos mediante for in */
for (nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad]);
}

/** guardamos en el array personaArray los atributos y métodos del objeto
 * el método Object.values() nos devuelve este array  */
let personaArray = Object.values(persona);
console.log(personaArray);

/** convertimos en String el objeto con JSON.stringify() 
 * guardamos lo que devuelve el método en la variable personaString */
let personaString = JSON.stringify(persona);
console.log(personaString);
```

## Método `get` y `set` en objetos

Trabajar con los métodos `get` y `set` son las mejores prácticas a la hora de programar. `get` significa obtener, y lo utilizamos para acceder a los valores asignados a nuestros atributos y métodos, es decir que usamos `get` para indicar que vamos a recuperar información del objeto. A los métodos los declaramos como `get metodo(){}`, y a la hora de llamarlo hacemos directamente `objeto.metodo` sin los `()`. Esto simplifica la sintaxis de la declaración y llamado del método, lo que hace que se asemeje al llamado de un atributo, pero es un método que devuelve valores.

```js
let persona = {
  nombre: 'Juan',
  apellido: 'Perez',
  email: 'jperez@mail.com',
  edad: 28,

  /** modificamos la declaración de la función utilizamod get
   * lo siguiente a get va a ser el nombre de la función
   * el resto se escribe como se hace normalmente con las funciones */
  get nombreCompleto() {
    return this.nombre + ' ' + this.apellido;
  }
}

/** a declarar la función con get no necesitamos indicar los parentesis
 * cuando la llamamos si la misma no necesita parámetros */
console.log(persona.nombreCompleto);
```

`set` significa establecer o modificar, y lo utilizamos para modificar los valores de los atributos de nuestro objeto. Los métodos los declaramos como `set metodo(parámetro){}` y a la hora de llamarlo hacemos `objeto.metodo = parámetro`, no lo hacemos de la forma `objeto.metodo(parametro)` para llamarlo. Esto simplifica la sintaxis de la declaración y llamado del método, lo que hace que se asemeje a la asignación de un valor a un atributo, pero es un método que asigna valores.

```js
let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@mail.com',
    edad: 28,

    /** los idiomas en general se almacenan en mayusculas de la forma ES */
    idioma: 'es',

    get lang() {

        /** utilizamos toUpperCase() para convertir a mayúsculas la cadena 
         * guardada en la variable idioma */
        return this.idioma.toUpperCase();
    },

    /** el método lag recibe un parámetro del mismo nombre */
    set lang(lang) {

        /** convertimos a mayúsculas con toUpperCase() al valor
         * del parámetro lang que recibe el método */
        this.idioma = lang.toUpperCase();
    },

    get nombreCompleto() {
        return this.nombre + ' ' + this.apellido;
    }
}

console.log(persona.lang);

/** llamamos al método set lang y el parametro de entrada es lo que 
 * continua al = que es 'en'. Como el llamado tiene un signo de = 
 * JavaScript interpreta que se trata del método set */
persona.lang = 'en';

/** llamamos al método get lang, como el llamado no tiene signo =
 * Javascript interpreta que se trata de método get */
console.log(persona.lang);

console.log(persona.idioma);
```

## Constructor de objetos

Un constructor es una función especial de los objetos que permite crear un nuevo objeto. Para llamar a la función utilizamos la palabra reservada `new`, que reserva espacio en memoria para el objeto que vamos a crear. Se acostumbra que el nombre de la función constructor empiece en mayúsculas, así mismo el nombre del constructor va a ser el nombre del tipo de objeto que estamos definiendo. En el ejemplo la función constructor se llama Persona y el tipo de objeto va a ser tipo Persona. La firma del método son los parámetros que recibe el mismo, es decir lo que está entre paréntesis en su definición. Utilizamos el operador `this` para indicar que los atributos que utilizamos dentro de la función pertenecen al objeto que creamos mediante esta. Esto funciona por que llamamos a la función con la palabra reservada `new`.

```js
/** Funcion constructor de objetos de tipo Persona */
function Persona(nombre, otro, email) {

    /** el atributo del objeto se llama nombre
     * recibe el argumento del parametro nombre que es una prática común
     * el parametro no tiene que tener el mismo nombre que el atributo   */
    this.nombre = nombre;
    this.apellido = otro;
    this.email = email;
}

/** llamamos el constructor con la palabra reservada new
 * y le asignamos valores a los atributos */
let padre = new Persona('Juan', 'Perez', 'jperez@mail.com');
console.log(padre);

let madre = new Persona('Laura', 'Quintero', 'lquintero@mail.com');
console.log(madre);

/** podemos cambiar el valor de un atributo en uno de los objetos
 * el otro objeto queda como está */
padre.nombre = 'Carlos';

console.log(padre);
console.log(madre);
```

## Agregar métodos a un constructor de objetos

Agregamos métodos en el método constructor de objetos de forma en que agregábamos métodos en un objeto ya creado, utilizando la palabra reservada `this`. Los métodos agregados en el constructor van a estar disponibles para cualquier objeto que creemos con ese constructor. Esto permite reutilizar el código ya que, definido un constructor de objetos con sus atributos y métodos, todos los objetos que creemos con ese constructor van a poder hacer uso de los mismos atributos y métodos.

```js
/** Funcion constructor de objetos de tipo Persona */
function Persona(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;

    /** creamos la función */
    this.nombreCompleto = function () {
        return this.nombre + ' ' + this.apellido;
    }
}

let padre = new Persona('Juan', 'Perez', 'jperez@mail.com');

/** llamamos a la función después de crear el objeto */
console.log(padre.nombreCompleto());

let madre = new Persona('Laura', 'Quintero', 'lquintero@mail.com');
console.log(madre.nombreCompleto());

padre.nombre = 'Carlos';

console.log(padre);
console.log(madre);
```

## Distintas formas de crear objetos

Hasta el momento vimos como crear objetos a partir de una función constructor, pero existen sintaxis que simplifican el uso de la palabra `new` a la hora de crear objetos. En los ejemplos vemos que cada tipo de dato en JavaScript se corresponde con un objeto, es decir que podemos crear variables de tipo `String`, `Number` o `Array` de manera mas formal, que es utilizando la palabra reservada `new`, o podemos indicar su valor directamente y JavaScript reconoce el tipo de objeto o dato al que corresponde.

```js
/** creamos un nuevo objeto de tipo Object. Es un objeto vacio
 * la sintaxis simplificada de eso es utilizar {} */
let miObjeto1 = new Object();
let miObjeto2 = {};

let miCadena1 = new String('Hola');
let miCadena2 = 'Hola';

let miNumero1 = new Number(1);
let miNumero2 = 1;

let miBoolean1 = new Boolean(false);
let miBoolean2 = false;

let miArreglo1 = new Array();
let miArreglo2 = [];

let miFuncion1 = new Function();
let miFuncion2 = function () { };
```

## Uso de `prototype`

Si agregamos un atributo o método a un objeto ya creado, en el ejemplo el atributo `tel` al objeto `padre` de la forma `padre.tel = '11223344';`, ese atributo está disponible solo para ese objeto. Si queremos agregar un atributo o método para todos los objetos, pero no hacerlo en la definición del constructor, utilizamos `prototype`.

```js
function Persona(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function () {
        return this.nombre + ' ' + this.apellido;
    }
}

let padre = new Persona('Juan', 'Perez', 'jperez@mail.com');

/** creamos el atributo tel en el objeto padre */
padre.tel = '11223344';
console.log(padre.tel);

let madre = new Persona('Laura', 'Quintero', 'lquintero@mail.com');

/** la propiedad tel no esta definida para el objeto madre */
console.log(madre.tel);

/** agregamos el atributo tel a todos los objetos que creamos
 * utilizando el constructor Persona */
Persona.prototype.tel = '44332211';

let padre2 = new Persona('Juan', 'Perez', 'jperez@mail.com');
console.log(padre2.tel);

let madre2 = new Persona('Laura', 'Quintero', 'lquintero@mail.com');

/** podemos cambiar el atributo tel si lo necesitamos */
madre2.tel = '66889900';
console.log(madre2.tel);
```

## Uso del método `call`

El método `call` nos permite llamar un método que está definido en un objeto desde otro objeto. El método `call` utiliza los atributos del objeto que le pasamos como parámetro como si fueran los atributos del objeto donde está definido el método que queremos utilizar.

```js
let persona1 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto: function () {
        return this.nombre + ' ' + this.apellido;
    }
}

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

/** llamamos al método nombreCompleto que pertenece a persona1 */
console.log(persona1.nombreCompleto());

/** llamamos al método nombreCompleto de persona1 y después al metodo call
 * call recibe como parametro el objeto sobre el cual queremos llamar
 * al método nombreCompleto */
console.log(persona1.nombreCompleto.call(persona2));
```

## Paso de argumentos al método `call`

Los argumentos del método, perteneciente a otro objeto, los pasamos después del objeto sobre el que llamamos al método, seguidos de coma.

```js
let persona1 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto: function (titulo, tel) {
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ', ' + tel;
    }
}

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

/** llamamos al método nombreCompleto de persona1 con sus parámetros */
console.log(persona1.nombreCompleto('Lic.', '44332288'));

/** cuando llamamos al método call, además de pasar el objeto como parámetro
 * pasamos los dos parámetros que requiere la función original nombreCompleto */
console.log(persona1.nombreCompleto.call(persona2, 'Ing', '5544332211'));
```

## Uso del método `apply`

El método `apply`, como el método `call`, nos permite utilizar un método que pertenece a un objeto en otro objeto. La diferencia está en que, a la hora de pasar argumentos al método del otro objeto, con `call` los pasamos seguidos de comas mientras que con `apply` lo hacemos mediante un `Array`.

```js
let persona1 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto: function (titulo, tel) {
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ', ' + tel;
    }
}

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona1.nombreCompleto('Lic', '66887711'));

/** pasamos los argumentos del método nombreCompleto de persona1 
 * mediante un array utilizando el método apply */
let arreglo = ['Ing', '55443322'];

console.log(persona1.nombreCompleto.apply(persona2, arreglo));
console.log(persona1.nombreCompleto.apply(persona2, ['Lic', '55448822']));
```

# Clases

## Definición de clases

Una clase es una plantilla. En esta plantilla definimos los atributos y métodos que queremos que tengan los objetos que vamos a crear a partir de ella. Un objeto es una instancia de una clase. EN general cuando definimos una clase la misma no tiene valores en sus atributos o métodos, en caso de tenerlos esos valores van a estar presente en cada uno de los objetos que creemos a partir de esa clase. Una clase tiene un nombre, tiene atributos y tiene métodos. Cada uno de los objetos creados a partir de la clase comparten los mismos atributos y métodos, pero no comparten los valores que toman estos.

```js
/** el nombre de la clase en general se escribe en mayúsculas */
class Persona {

    /** creamos el constructor de la clase escribiendo un método
     * llamado constructor */
    constructor(nombre, otro) {

        /** this nos permite indicar que nombre es un atributo de la clase */
        this.nombre = nombre;
        this.apellido = otro;
    }
}

/** utilizamos la palabra reservada new para crear un nuevo objeto
 * del tipo Persona  */
let persona1 = new Persona('Juan', 'Perez');
console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2);
```

## Métodos `get` y `set`

Podemos utilizar métodos `get` y `set` para acceder y modificar los valores de los atributos de un objeto. El método `get` no puede tener el mismo nombre que el atributo sobre el que trabaja, por ese motivo al atributo lo nombramos antepuesto a un guion bajo de la forma `_atributo`.

```js
class Persona {

    /** no son necesarias las comas despueés de definir cada método de la clase */
    constructor(nombre, apellido) {

        /** los atributos llevan un _ para poder crear el método
         * get con el mismo nombre de estos */
        this._nombre = nombre;
        this._apellido = apellido;
    }

    /** creamos el método get */
    get nombre() {
        return this._nombre;
    }

    /** cramos el método set que recibe un argumento */
    set nombre(nombre) {
        this._nombre = nombre;
    }
}

let persona1 = new Persona('Juan', 'Perez');

/** el método set no requiere ser utilizado de la forma
 * persona1.nombre('Juan Carlos') */
persona1.nombre = 'Juan Carlos';

/** el método get no tiene que ser llamado de la forma persona1.nombre() */
console.log(persona1.nombre);
```

## Hoisting y clases

Cuando trabajamos con clases no se aplica el concepto de hoisting, es decir, no es posible crear objetos antes de declarar la clase de ese objeto.

```js
/** va a devolver un error por que tratamos de crear el objeto
 * antes de definir la clase */
let persona2 = new Persona('Karla', 'Juarez');

class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
}

let persona1 = new Persona('Juan', 'Perez');
persona1.nombre = 'Juan Carlos';//set nombre('Juan Carlos')
console.log(persona1.nombre);//get nombre

let persona2 = new Persona('Karla', 'Juarez');
console.log(persona2);
```

## Herencia

Mediante la herencia podemos reutilizar código y heredar características de una clase padre a una clase hijo. Para indicar la herencia de una clase desde otra utilizamos la palabra reservada `extends` sobre la clase hijo. La clase hijo va a heredar, y por ende a tener definidos, los atributos y métodos de la clase padre, esto significa que no tenemos la necesidad de declarar los atributos presentes en la clase padre, entre las declaraciones de la clase hijo. Para llamar al constructor de la clase padre dentro de la clase hijo utilizamos la palabra reservada `super`, si no hacemos este llamado y completamos los datos del constructor de la clase padre nos dará un error indicando que no podemos crear un objeto de la clase hijo.

```js
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
}

/** la clase Empleado hereda de la clase Persona mediante la palabra reservada
 * extends. */
class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {

        /** llamamos al constructor de la clase padre con sus parámetros */
        super(nombre, apellido);
        this._departamento = departamento;

    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
}

let persona1 = new Persona('Juan', 'Perez');
console.log(persona1);

let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');
console.log(empleado1);

/** utilizamos el método get nombre heredado de la clase persona */
console.log(empleado1.nombre);
```

## Herencia de métodos

Podemos heredar métodos además de los `get` y `set` en una clase hijo desde una clase padre.

```js
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }

    /** no es necesario agregar function en la definicion de la clase
     * cuando definimos un nuevo método o función */
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
}

let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');
console.log(empleado1);

/** heredamos el método nombreCompleto */
console.log(empleado1.nombreCompleto());
```

## Sobrescribir métodos

Podemos redefinir un método de la clase heredado de la clase padre en la clase hijo, es decir, podemos editar el método heredado en la clase hijo para que realice acciones para las que no está definido en la clase padre. Esto no modifica el método en la clase padre, donde queda como está, pero lo redefine en la clase hijo que lo hereda. Cuando lo redefinimos en la clase hijo, el método tiene que tener el mismo nombre y recibir los mismos parámetros, si esto no se cumple no es sobrescribir el método heredado sino la definición de un nuevo método.

```js
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }

    /** redefinimos o sobreescribimos el método nombreCompleto() */
    nombreCompleto() {

        /** como la sobreescritura no modifica el método de la clase padre
         * podemos reutilizar este método con la palabra reservada super
         * que llama al método o a atributos definidos en la clase padre*/
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let persona1 = new Persona('Juan', 'Perez');
console.log(persona1);

let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());
```

## Clase `Object` y polimorfismo

La clase `Object` es la clase padre de todas las clases en JavaScript. No se escribe de manera explicita pero cada clase que creamos está definida de la forma `class NombreClase extends Object`. Al heredar de la clase `Object` la nueva clase también hereda los atributos y métodos de esta clase. Uno de los atributos de la clase `Object` es `prototype`. Este también tiene definidos sus propios atributos y métodos, por ende, en nuestra nueva clase podemos acceder y sobrescribir los atributos y métodos de `Object` y los atributos y métodos de sus atributos como `prototype`.

```js
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }

    /** sobreescribimos el método toString() que encontramos en la clase padre
     * Object en uno de sus atributos (que también es un objeto) prototype
     * de la forma Object.prototype.toString(); */
    toString() {

        /** se aṕlica el concepto de polimorfimso, el método toString llama a 
         * nombreCompleto() de la clase Persona (padre) si lo llamamos
         * desde un objeto de tipo Persona y llama a 
         * nombreCompleto() de la clase Empleado (hijo) si lo llamamos 
         * desde un objeto del tipo Empleado */
        return this.nombreCompleto();
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let persona1 = new Persona('Juan', 'Perez');

/** llama al método nombre completo de la clase Persona */
console.log(persona1.toString());

let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

/** el método  toString() sobreescrito se hereda de la clase padre Persona y
 * llama al método nombre completo de la clase hijo Empleado */
console.log(empleado1.toString());
```

Polimorfismo significa multiples formas en tiempo de ejecución, es decir, que el comportamiento del método varía según el objeto desde el cual lo estemos llamando.

# Palabra reservada `static`

## Métodos estáticos

Una vez definida la clase podemos agregar métodos que se asocien con los objetos que creamos a partir de esa clase y también podemos crear métodos que se asocien con la clase exclusivamente. Para definir estos métodos utilizamos la palabra reservada `static`.

```js
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
    toString() {
        return this.nombreCompleto();
    }

    /** definimos el método estático, es decir que se asocia con la clase
     * y no con los objetos que creamos a partir de la clase */
    static saludar() {
        console.log('saludos desde método static');
    }

    /** paramos un objeto como parametro del método estatico */
    static saludar2(persona) {
        console.log(persona.nombre + ' ' + persona.apellido);
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let persona1 = new Persona('Juan', 'Perez');

let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');

/** el método funciona por que lo llamamos desde la clase directamente */
Persona.saludar();

/** pasamos como argumento un objeto de tipo persona pero seguimos llamando
 * al método desde la clase y no del objeto */
Persona.saludar2(persona1);

/** el método estático se hereda a la clase hijo como método estático
 * es decir que tiene que ser llamado desde la clase hijo, no desde el 
 * objeto que creamos con la clase */
Empleado.saludar();
Empleado.saludar2(empleado1);

/** devuelve error por que no es posible llamar un método static
 * desde un objeto */
persona1.saludar(); 
```

## Atributos estáticos

Para definir atributos estáticos en nuestra clase utilizamos la palabra reservada `static`. Este atributo, así como los métodos estáticos pertenecen a la clase pero no a los objetos que creamos a partir de esa clase.

```js
class Persona {

    /** definimos el atributo contadorObjetosPersona como static
     * y le asignamos el valor inicial 0 */
    static contadorObjetosPersona = 0;

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;

        /** incrementamos el valor del atributo contadorObjetosPersona cada
         * vez que se crea un objeto. No accedemos al atributo como 
         * this.contadorObjetosPersona por que este hace referencia al atributo
         *  del objeto y contadorObjetosPersona es un atributo de la clase */
        Persona.contadorObjetosPersona++;
        console.log('Se incrementa contador:' + Persona.contadorObjetosPersona);
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
    toString() {
        return this.nombreCompleto();
    }
    static saludar() {
        console.log('saludos desde método static');
    }
    static saludar2(persona) {
        console.log(persona.nombre + ' ' + persona.apellido);
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let persona1 = new Persona('Juan', 'Perez');

let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');

/** si tratamos de llamar a una variable estática desde un objeto nos indica
 * con undefined que la variable no existe, aunque esta si existe, solo que
 * debe ser accedida desde la clase */
console.log(persona1.contadorObjetosPersona);

/** llamamos al atributo desde la clase */
console.log(Persona.contadorObjetosPersona);

/** el atributo estático se hereda y puede llamarse desde la clase hijo */
console.log(Empleado.contadorObjetosPersona);
```

## Atributos estáticos vs no estáticos

No es necesario definir todos los atributos propios de los objetos en el constructor de la clase.

```js
class Persona {

    /** atributo estático, se asocia solo con la clase */
    static contadorObjetosPersona = 0;

    /** atributo no estático, se asocia con los objetos creados a partir
     * de la clase. No requiere la palabra this en su definicio, si cuando
     * lo llamamos o asignamos valores con un método */
    email = 'Valor default email';

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        Persona.contadorObjetosPersona++;
        console.log('Se incrementa contador:' + Persona.contadorObjetosPersona);
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
    toString() {
        return this.nombreCompleto();
    }
    static saludar() {
        console.log('saludos desde método static');
    }
    static saludar2(persona) {
        console.log(persona.nombre + ' ' + persona.apellido);
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let persona1 = new Persona('Juan', 'Perez');


let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');

/** los objetos creados a partir de la clase padre e hijo 
 * tienen el atributo email */
console.log(persona1.email);
console.log(empleado1.email);

/** la clase padre e hijo no tienen el atributo email por que no
 * está definino como static */
console.log(Persona.email);
console.log(Empleado.email);
```

## Ejemplo de uso de atributos estáticos

```js
class Persona {

    /** atributo estático de la clase */
    static contadorPersonas = 0;

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;

        /** creamos el atributo de objeto idPersona y le asignamos el valor
         * del atributo de clase contadorPersonas incrementando en 1 el mismo
         * antes de la asignación */
        this.idPersona = ++Persona.contadorPersonas;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {

        /** modificamos el método para mostrar el atributo idPersona */
        return this.idPersona + ' ' + this._nombre + ' ' + this._apellido;
    }
    toString() {
        return this.nombreCompleto();
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

/** al crear un objeto de tipo Persona el atributo de clase contadorPersonas 
 * se incrementa en 1 y ese valor se asigna al atributo de objeto idPersona */
let persona1 = new Persona('Juan', 'Perez');
console.log(persona1.toString());

/** el constructor de Empleado llama al constructor de Persona, por ende
 * el atributo de clase contadorPersonas se incrementa en 1 y ese valor 
 * se asigna al atributo de objeto idPersona */
let empleado1 = new Empleado('Maria', 'Jimenez', 'Sistemas');
console.log(empleado1.toString());

console.log(Persona.contadorPersonas);

let persona2 = new Persona('Karla', 'Ramirez');
console.log(persona2.toString());
console.log(Persona.contadorPersonas);
```

## Crear constantes estáticas

Para crear un atributo de tipo `static`, pero que sea de solo lectura, similar a lo que hacemos con `const`, solo que en este caso no podemos utilizar `const`. Para esto vamos a crear un método `static` que solo va a regresar un valor. Al no ser un atributo sino un método que devuelve un valor, este valor no puede ser modificado.

```js
class Persona {

    static contadorPersonas = 0;

    /** el método MAX_OBJ, definido como get, solo devuelve un valor
     * de esa forma simula ser una constante */
    static get MAX_OBJ() {
        return 5;
    }

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;

        /** valida si la cantidad de personas creadas en contadorPersonas es 
         * menor a la constante simulada MAX_OBJ */
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas;
        }
        else {
            console.log('Se han superado el máximo de objetos permitidos');
        }
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this.idPersona + ' ' + this._nombre + ' ' + this._apellido;
    }
    toString() {
        return this.nombreCompleto();
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

/** al ser un método get no requiere los () */
console.log(Persona.MAX_OBJ);

/** no da error al tratar de hacer ejecutar el método set para MAX_OBJ ya que,
 * aunque este no existe, JavaScript está creando un atributo en persona con 
 * el nombre MAX_OBJ */
Persona.MAX_OBJ = 10;

/** seguimos llamando al método a pesar de la asignación de la linea anterior
 * y el valor que devuelve el método no cambia */
console.log(Persona.MAX_OBJ);

let persona1 = new Persona('Juan', 'Perez');
let persona2 = new Persona('Karla', 'Ramirez');
let persona3 = new Persona('Mariano', 'Lara');
let persona4 = new Persona('Armando', 'Toledo');
let persona5 = new Persona('Laura', 'Quintero');
console.log(persona5.toString());
```

# Ejercicios de ejemplo

## Ejercicio de herencia

![09-13-EjercicioHerencia-UJS.png](data:image/png;base64,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)

En el ejercicio utilizamos las `` para indicar que, lo que esta entre las tildes, va a formatearse como un `string` respetando los espacios y los saltos de línea. Lo que encontramos entre las tiles se formatea como está escrito. Para poder consultar los valores de los atributos utilizamos `${this.atributo}`, esto indica que, en lugar de mostrar es sentencia, muestre el valor guardado en el atributo al que hace referencia.

```js
class Persona {

    /** atributo de clase */
    static contadorPersonas = 0;

    /** constructor de la clase */
    constructor(nombre, apellido, edad) {

        /** el atributo de objeto _idPersona se asigna valor a partir del atributo
         * de clase contadorPersonas */
        this._idPersona = ++Persona.contadorPersonas;

        /** atributos de objeto */
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    /** getter y setter */

    /** idPersona no requiere setter por que su valor se asigna en el 
     * constructor mediante el atributo de clase contadorPersonas */
    get idPersona() { return this._idPersona; }

    get nombre() { return this._nombre; }
    set nombre(nombre) { this._nombre = nombre; }

    get apellido() { return this._apellido; }
    set apellido(apellido) { this._apellido = apellido; }

    get edad() { return this._edad; }
    set edad(edad) { this._edad = edad; }

    /** sobreescribimos el método toString para devolver como string
     * los datos de los atributos del objeto */
    toString() {

        /** damos formato al string de salida mediante las `` */
        return `${this._idPersona} ${this._nombre} ${this._apellido} ${this.edad}`;

    }

}

/** la clase Empleado hereda de la clase Persona, es decir Empleado es la
 * clase hijo y Persona la clase padre */
class Empleado extends Persona {

    /** atributo de clase */
    static contadorEmpleados = 0;

    /** constructor de la clase */
    constructor(nombre, apellido, edad, sueldo) {

        /** llama al constructor de la clase padre, es decir el constructo 
         * de la clase Persona */
        super(nombre, apellido, edad);

        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;


    }

    /** getter y setter */
    get idEmpleado() { return this._idEmpleado; }

    get sueldo() { return this._sueldo; }
    set sueldo(sueldo) { this._sueldo = sueldo; }

    toString() {

        /** llamamos al metodo toString de la clase padre Persona mediante
         * la palabra reservada super */
        return `${super.toString()} ${this._idEmpleado} ${this._sueldo}`;
    }

}

class Cliente extends Persona {

    /** atributo de clase */
    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro) {

        /** llamamos al contructor de la clase padre Persona */
        super(nombre, apellido, edad);

        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente() { return this._idCliente; }

    get fechaRegistro() { return this._fechaRegistro; }
    set fechaRegistro(fechaRegistro) { this._fechaRegistro = fechaRegistro; }

    toString() {
        return `${super.toString()} ${this._idCliente} ${this._fechaRegistro}`;
    }

}

/** prueba clase Persona */
let persona1 = new Persona('Juan', 'Perez', 28);
console.log(persona1.toString());
let persona2 = new Persona('Carlos', 'Ramirez', 35);
console.log(persona2.toString());

/** prueba clase Empleado */
let empleado1 = new Empleado('Karla', 'Gomez', '25', 5000);
console.log(empleado1.toString());
let empleado2 = new Empleado('Laura', 'Quintero', 33, 7000);
console.log(empleado2.toString());

/** prueba de clase Cliente */
let cliente1 = new Cliente('Miguel', 'Cervantes', 30, new Date());
console.log(cliente1.toString());
let cliente2 = new Cliente('Maria', 'Lara', 38, new Date());
console.log(cliente2.toString());
```

## Sistema de ventas

![SistemaVentasUJS.png](data:image/png;base64,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)

```js
class Producto {

    /** atributo de clase */
    static contadorProductos = 0;

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    /** getter y setter */
    get idProducto() { return this._idProducto; }

    get nombre() { return this._nombre; }
    set nombre(nombre) { this._nombre = nombre; }

    get precio() { return this._precio; }
    set precio(precio) { return this._precio = precio; }

    toString() {

        /** el $ extra que tiene la sentencia $${this._precio} se va a imprimir
         * como el símbolo y al lado el valor del atributo this._precio */
        return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}  `;
    }
}


class Orden {
    static contadorOrdenes = 0;

    /** con el método get como static estamos simulando una constante de clase */
    static get MAX_PRODUCTOS() {
        return 5;
    }

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
    }

    /** getter y setter */
    get idOrden() { return this._idOrden; }

    agregarProducto(producto) {

        /** revisame si el array _productos tiene menos de 5 elemenos y mediante
         * push sumamos a la al array un elemenos de tipo productos */
        if (this._productos.length < Orden.MAX_PRODUCTOS) {
            this._productos.push(producto);
        }
        else {

            /** mensaje que se muestra si el array _productos tiene mas de 5 elementos */
            console.log('No se pueden agregar más productos');
        }
    }

    calcularTotal() {
        let totalVenta = 0;

        /** mediante for of recorremos un array elementos por elemento, el elemento
         * se guarda en la variable producto, con of indicamos cual es el array
         * sobre el cual vamos a iterar */
        for (let producto of this._productos) {
            totalVenta += producto.precio;
        }
        return totalVenta;
    }

    mostrarOrden() {
        let productosOrden = '';
        for (let producto of this._productos) {

            /** en productosOrden armamos el string que vamos a mostrar despues 
             * con \n hacemos un salto de línea antes de sumar el string del método 
             * toString */
            productosOrden += '\n{' + producto.toString() + '}';
        }

        /** mostramos los datos de la orden y al final la lista de productos
         * guardada en productosOrden */
        console.log(`Orden: ${this._idOrden} Total: $${this.calcularTotal()}, Productos: ${productosOrden} `);
    }
}

/** creamos objetos de tipo Producto */
let producto1 = new Producto('Pantalón', 200);
let producto2 = new Producto('Camisa', 100);

/** creamos un objeto de tipo Orden  y agregamos los productos creados a 
 * la orden, despues mostramos la orden */
let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.mostrarOrden();

let orden2 = new Orden();
let producto3 = new Producto('Cinturon', 50);
orden2.agregarProducto(producto3);
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.mostrarOrden();
```
