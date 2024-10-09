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
```
function nombreFuncion(argumento1, argumento2, ... argumentoN){
  cuerpo de la función
}

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
 *  después definimos atributos y valores a esos atributos */
const persona = {
    nombre: 'Juan',
    apellido: 'Perez'
}
console.log(persona);

/** p1 = persona, es decir que p1 es igual a la referencia del objeto
 *  a la que es igual persona, si modificamos los atributos de p1
 *  se modifican los de persona */
function cambiarValorObjeto(p1) {

    /** mediante punto+atributo indicamos que queremos acceder a algun
     *  atributo del objeto que pasamos por referencia */
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
function Persona(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    
    /** creamos la función */
    this.nombreCompleto = function(){
        return this.nombre + ' ' + this.apellido;
    }
}

let padre = new Persona('Juan', 'Perez', 'jperez@mail.com');

/** llamamos a la función después de crear el objeto */
console.log( padre.nombreCompleto() );

let madre = new Persona('Laura', 'Quintero', 'lquintero@mail.com');
console.log( madre.nombreCompleto() );

padre.nombre = 'Carlos';

console.log( padre );
console.log( madre );
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
let miFuncion2 = function(){};
```

### Uso de `prototype`

Si agregamos un atributo o método a un objeto ya creado, en el ejemplo el atributo `tel` al objeto `padre` de la forma `padre.tel = '11223344';`, ese atributo está disponible solo para ese objeto. Si queremos agregar un atributo o método para todos los objetos, pero no hacerlo en la definición del constructor, utilizamos `prototype`.

```js
function Persona(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + ' ' + this.apellido;
    }
}

let padre = new Persona('Juan', 'Perez', 'jperez@mail.com');

/** creamos el atributo tel en el objeto padre */
padre.tel = '11223344';
console.log( padre.tel );

let madre = new Persona('Laura', 'Quintero', 'lquintero@mail.com');

/** la propiedad tel no esta definida para el objeto madre */
console.log(madre.tel);

/** agregamos el atributo tel a todos los objetos que creamos
 * utilizando el constructor Persona */
Persona.prototype.tel = '44332211';

let padre2 = new Persona('Juan', 'Perez', 'jperez@mail.com');
console.log( padre2.tel );

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
    nombreCompleto: function(){
        return this.nombre + ' ' + this.apellido;
    }
}

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

/** llamamos al método nombreCompleto que pertenece a persona1 */
console.log( persona1.nombreCompleto() );

/** llamamos al método nombreCompleto de persona1 y después al metodo call
 * call recibe como parametro el objeto sobre el cual queremos llamar
 * al método nombreCompleto */
console.log( persona1.nombreCompleto.call( persona2 ) );
```

## Paso de argumentos al método `call`

Los argumentos del método, perteneciente a otro objeto, los pasamos después del objeto sobre el que llamamos al método, seguidos de coma.

```js
let persona1 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto: function(titulo, tel){
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ', ' + tel;
    }
}

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

/** llamamos al método nombreCompleto de persona1 con sus parámetros */
console.log( persona1.nombreCompleto('Lic.', '44332288') );

/** cuando llamamos al método call, además de pasar el objeto como parámetro
 * pasamos los dos parámetros que requiere la función original nombreCompleto */
console.log( persona1.nombreCompleto.call( persona2, 'Ing', '5544332211' ) );
```

### Uso del método `apply`

El método `apply`, como el método `call`, nos permite utilizar un método que pertenece a un objeto en otro objeto. La diferencia está en que, a la hora de pasar argumentos al método del otro objeto, con `call` los pasamos seguidos de comas mientras que con `apply` lo hacemos mediante un `Array`.

```js
let persona1 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto: function(titulo, tel){
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ', ' + tel;
    }
}

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log( persona1.nombreCompleto('Lic', '66887711') );

/** pasamos los argumentos del método nombreCompleto de persona1 
 * mediante un array utilizando el método apply */
let arreglo = ['Ing','55443322'];

console.log(persona1.nombreCompleto.apply(persona2, arreglo));
console.log(persona1.nombreCompleto.apply(persona2, ['Lic', '55448822']) );
```

# Clases
