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

1.  Paréntesis: `()`
2.  División y multiplicación: `/ *`
3.  Suma y resta: `+ -`


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


En el ejercicio utilizamos las ``para indicar que, lo que esta entre las tildes, va a formatearse como un`string`respetando los espacios y los saltos de línea. Lo que encontramos entre las tiles se formatea como está escrito. Para poder consultar los valores de los atributos utilizamos`${this.atributo}`, esto indica que, en lugar de mostrar es sentencia, muestre el valor guardado en el atributo al que hace referencia.


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

## Mundo PC


![MundoPC-UJS.png](data:image/png;base64,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/PrUJan9JNtu+zDPb267banLb2vct1Vuan5V8uN8q0JtNO6xjnv6kI9Gf7MVJDAWBKwLmxVG6vys5badLrR6t12fFOVTkNsptjXu2yrXTmY4KTnfhsO1L7laxz0FeV96lPUkARKofWxaiNC6UBI9CYwSgbbGfVvljlLfsS39I2Ad9xTk/etb1pgExpbAME5ZGVuYbPhYE3jypN5pJ1XgQZjwIoFxJGCZbxTk4zgy2GYSIAESIAESIAESIIHOEKAg70xXsCIkQAIkQAIkQAIkQALjSICCfBx7nW0mARIgARIgARIgARLoDAEK8s50BStCAiRAAqNHAAF09u/f77Zt2+amTp06eg1ki0ighwQ4L7vXaRTk3esT1ogESIAERoqA9ZSBkWo0G0MCHSfAedmtDqIg71Z/sDYkQAI5BFKfskLYzRDgg78ZziyFBMoQ4LwsQ2v4aSnIh8+YJZAACSQiwAdIIpANZ8N+axg4iyMBAwHOSwOkBpNQkDcIm0WRAAnUI8AHSD1+bd3NfmuLPMslgTgBzstujQ4K8m71B2tDAiSQQ4APkH4OD/ZbP/uNtR5tApyX3epfCvJu9QdrQwIkkEPgG9/4hnvw4MFTKb797W+7Tz/99Kmfw+f8pz/9KdN3jM/bb7/tdu7c+VS/7Nq1y+F34cX0XxEhn684cDykGQ+xdZMPoXYIUJC3w52lkgAJkAAJkAAJkAAJkIAnQEHOgUACJEACJEACJEACJEACLRKgIG8RPosmARIgARIgARIgARIgAQpyjgESIAESIAESIAESIAESaJEABXmL8Fk0CZAACZAACZAACZAACVCQcwyQAAmQAAmQAAmQAAmQQIsEKMhbhM+iSYAESIAESIAESIAESICCnGOABEiABEiABEiABEiABFokQEHeInwWTQIkQAIkQAIkQAIkQAIU5BwDJEACJEACJEACJEACJNAiAQryFuGzaBIgARIgARIgARIgARKgIOcYIAESIAESIAESIAESIIEWCcMI8YgAAAFVSURBVFCQtwifRZMACZAACZAACZAACZAABTnHAAmQAAmQAAmQAAmQAAm0SICCvEX4LJoESIAESIAESIAESIAEKMg5BkiABEiABEiABEiABEigRQIU5C3CZ9EkQAIkQAIkQAIkQAIkQEHOMUACJEACJEACJEACJEACLRKgIG8RPosmARIgARIgARIgARIgAQpyjgESIAESIAESIAESIAESaJEABXmL8Fk0CZAACZAACZAACZAACVCQcwyQAAmQAAmQAAmQAAmQQIsEKMhbhM+iSYAESIAESIAESIAESICCnGOABEiABEiABEiABEiABFokQEHeInwWTQIkQAIkQAIkQAIkQAIU5BwDJEACJEACJEACJEACJNAiAQryFuGzaBIgARIgARIgARIgARKgIOcYIAESIAESIAESIAESIIEWCVCQtwifRZMACZAACZAACZAACZDA/wdCbu4lFjIbaAAAAABJRU5ErkJggg==)


Las clases Ratón y Teclado tiene una relación de herencia con la clase DispositivoEntrada siendo esta la clase padre y las otras dos clases hijo. Así mimos las clases Ratón, Teclado y Monitor tiene una relación de agregación con la clase Computadora, ya que varios atributos de los objetos tipo Computadora son a su vez objetos de tipo Ratón, Teclado y Monitor.


```js
class DispositivoEntrada {

    constructor(tipoEntrada, marca) {
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }

    /** getter y setter */
    get tipoEntrada() { return this._tipoEntrada; }
    set tipoEntrada(tipoEntrada) { this._tipoEntrada = tipoEntrada; }

    get marca() { return this._marca; }
    set marca(marca) { this._marca = marca; }
}

/** hereda de DispositivoEntrada */
class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {

        /** llamamos al constructor de la clase padre */
        super(tipoEntrada, marca);

        this._idRaton = ++Raton.contadorRatones;
    }

    /** getter y setter */
    get idRaton() { return this._idRaton; }

    toString() {
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}

/** hereda de DispositivoEntrada */
class Teclado extends DispositivoEntrada {
    static contadorTeclado = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclado;
    }

    get idTeclado() { return this._idTeclado; }

    toString() {
        return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }

}

class Monitor {
    static contadorMonitores = 0;

    constructor(marca, medida) {
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;
        this._medida = medida;
    }

    get idMonitor() { return this._idMonitor; }

    toString() {
        return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._medida}]`;
    }
}

class Computadora {
    static contadorComputadoras = 0;

    /** la clase tiene un ralación de agregación con las clases monitor
     * raton y teclado, es decir, que atributos de la misma son objetos de estas */
    constructor(nombre, monitor, raton, teclado) {
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._raton = raton;
        this._teclado = teclado;
    }

    toString() {
        return `Computadora ${this._idComputadora}: ${this._nombre} \n ${this._monitor} \n ${this._raton} \n ${this._teclado}`;
    }
}

/** tiene un relación de agregación con el objetod Computadora, ya que uno 
 * de sus atributos es un array de referencias a objetos de este tipo */
class Orden {
    static contadorOrdenes = 0;

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;

        /** mediante un array vamos guardar la referencia a objetos de tipo 
         * Computadora, es decir, en el array _computadoras guardamos la referencia
         * para acceder a objetos de tipo Computadora */
        this._computadoras = [];
    }

    get idOrden() { return this._idOrden; }

    agregarComputadora(computadora) {

        /** mediante el método push agregamos un elemento al final del array, en 
         * este caso la referencia a un objeto de tipo Computadora */
        this._computadoras.push(computadora);
    }

    mostrarOrden() {

        /** creamos una variable tipo string vacia */
        let computadorasOrden = '';
        for (let computadora of this._computadoras) {

            /** a la variable le sumamos \n para un salto de línea y luego
             * lo que devuelve el método toString() del objeto computadora
             * al que llamamos solo escribiendo ${computadora} */
            computadorasOrden += `\n${computadora}`;
        }

        /** cuando tenemos armada la orden mostramos el número de orden y luego
         * una a una cada computadora de la orden armadas en computadorasOrden */
        console.log(`Orden: ${this._idOrden}, Computadoras: ${computadorasOrden}`);
    }
}

let raton1 = new Raton('USB', 'HP');
console.log(raton1.toString());
let raton2 = new Raton('Bluetooth', 'Dell');
raton2.marca = 'HP';
console.log(raton2.toString());

let teclado1 = new Teclado('Bluetooth', 'MSI');
let teclado2 = new Teclado('USB', 'Acer');
console.log(teclado1.toString());
console.log(teclado2.toString());

let monitor1 = new Monitor('HP', 15);
let monitor2 = new Monitor('Dell', 27);
console.log(monitor1.toString());
console.log(monitor2.toString());

let computadora1 = new Computadora('HP', monitor1, raton1, teclado1);
console.log(`${computadora1}`);
let computadora2 = new Computadora('Armada', monitor2, raton2, teclado2);
console.log(`${computadora2}`);

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.agregarComputadora(computadora2);
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.agregarComputadora(computadora1);
orden2.mostrarOrden();
```

# Modo strict


En JavaScript, si utilizamos una variable sin haberla declarado, el sistema no nos muestra un error. Este forma de trabajar se considera una mala práctica. Para que el sistema requiera la declaración de las variables se utiliza el modo `strict` agregando la cadena `"use strict";` al inicio del programa, lo que va a afectar a todo lo que siga a continuación de esta. Si no utilizamos la sentencia `"use strict";` al comienzo del programa también podemos hacerlo, por ejemplo, al comienzo de una función.


```js
"use strict";

/** estas sentencias daran error */
x = 10;
console.log(x);
miFuncion();

function miFuncion() {
    y = 15;
    console.log(y);
}
```

```js
x = 10;
console.log(x);
miFuncion();

function miFuncion() {
    "use strict";

    /** estas sentencias daran error */
    y = 15;
    console.log(y);
}
```

# Programación orientada a objetos


## Sobreescritura


Los atributos y métodos de la clase padre se heredan a la clase hijo. Muchas veces podemos redefinir o modificar el comportamiento de algunos de los métodos heredados en la clase hijo. Esta redefinición se conoce como sobrescribir el método.


![Sobreescritura.png](data:image/png;base64,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)


```js
/** clase padre */
class Empleado {

    constructor(nombre, sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    obtenerDetalles() {
        return `Empleado: nombre: ${this.nombre}, sueldo: ${this.sueldo}`;
    }
}

/** clase hijo */
class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    obtenerDetalles() {

        /** al sobreescribir el método obtener detalles cambiamos el comportamiento
         * del mismo agregando el depto al string que devuelve. Mediante super
         * accedemos al método de la clase padre para traer el string que genera */
        return `Gerente: ${super.obtenerDetalles()} depto: ${this.departamento}`;
    }
}

let empleado1 = new Empleado('Juan', 3000);
console.log(empleado1.obtenerDetalles());

let gerente1 = new Gerente('Carlos', 5000, 'Sistemas');
console.log(gerente1.obtenerDetalles());
```

![polimorfismo.png](data:image/png;base64,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)


## Polimorfismo


Polimorfismo significa multiples formas. En nuestro caso vamos a llamar de varias formas al mismo método, lo vamos a llamar mediante un objeto de tipo Empleado y luego mediante un objeto de tipo Gerente.


```js
class Empleado {
    constructor(nombre, sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    obtenerDetalles() {
        return `Empleado: nombre: ${this.nombre}, sueldo: ${this.sueldo}`;
    }
}

class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    obtenerDetalles() {
        return `Gerente: ${super.obtenerDetalles()} depto: ${this.departamento}`;
    }
}

/** definimos un método fuera de las clases padre e hijo que recibe un parametro
 * esta función llama al método correspondiente, segun el objeto que le pasamos */
function imprimir(tipo) {
    console.log(tipo.obtenerDetalles());
}

let empleado1 = new Empleado('Juan', 3000);
let gerente1 = new Gerente('Carlos', 5000, 'Sistemas');

/** llamamos al método obtenerDetalles del objeto de tipo Empleado y luego
 * del objeto de tipo Gerente, todo de la forma objeto.metodo() mediante
 * la función imprimir y la referencia del objeto que pasamos por parametro */
imprimir(empleado1);
imprimir(gerente1);
```

## Palabra reservada `instance of`


`instanceof` nos permite conocer el tipo de instancia de una clase con el que estamos trabajando. Recordando que, por ejemplo, las variables con datos numéricos en fin de cuentas son instancias de la clase `Number`, con `instanceof` podemos conocer el tipo o clase al que pertenece cualquier variable u objeto. Si el objeto sobre el que consultamos tiene una clase padre, la sentencia va a devolver la clase padre. `instanceof` devuelve valores sobre la clase misma del objeto o sobre la clase padre, si el mismo la tiene. A la hora de chequear el tipo de objeto con `instanceof` conviene hacerlo desde la menor jerarquía e ir subiendo.


```js
class Empleado {
    constructor(nombre, sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    obtenerDetalles() {
        return `Empleado: nombre: ${this.nombre}, sueldo: ${this.sueldo}`;
    }
}

class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    obtenerDetalles() {
        return `Gerente: ${super.obtenerDetalles()} depto: ${this.departamento}`;
    }
}

function determinarTipo(tipo) {
    console.log(tipo.obtenerDetalles());

    /** devuelve true si tipo es una instancia de la clase Gerente. Preguntamos 
     * primero si es de tipo gerente por que, además de ser de tipo Gerente es
     * de tipo Empleado, por la relación de herencia. Si preguntaramos primero
     * si es tipo Empleado siempre va a devolver true, aunque sea un objeto de 
     * tipo Gerente */
    if (tipo instanceof Gerente) {
        console.log('Es un objeto de tipo Gerente');
        console.log(tipo.departamento);
    }

    /** devuelve true si tipo es una instancia de la clase Empleado */
    else if (tipo instanceof Empleado) {
        console.log('Es un tipo Empleado');
        console.log(tipo.departamento);
    }

    /** devuelve true si tipo es una instancia de la clase Object */
    else if (tipo instanceof Object) {
        console.log('Es un tipo Object');
    }
}

let empleado1 = new Empleado('Juan', 3000);
let gerente1 = new Gerente('Carlos', 5000, 'Sistemas');

determinarTipo(empleado1);
determinarTipo(gerente1);
```

# Manejo de errores


## Bloque `try catch finally`


En la ejecución de un programa pueden aparecer errores de distinta índole. Algunos errores se pueden salvar y otros no. Cuando sucede un error en una sentencia del programa el mismo finaliza su ejecución en ese momento. Para que la ejecución no se finalice el código que puede generar un error lo ejecutamos dentro de un bloque `try`, si sucede un error lo capturamos en el bloque `catch` y trabajamos sobre el mismo. El bloque `finally` es opcional, se ejecuta siempre, al finalizar el bloque `try` o, en caso de error, al finalizar el bloque `catch`.


```js
/** utilizamos strict para visualizar errores si alguna variable no se declara */
'use strict'

/** mediante el bloque try indicamos que tiene que intentarse la ejecución 
 * del código que está entre sus {}, si el mismo da un error ese es capturado
 * por el bloque catch */
try {

    /** si hacemos x = 10 sin el let nos va a dar un error */
    x = 10;
}

/** si la ejecución de lo que esta en el bloque try da un error el mismo se
 * pasa al bloque catch mediante el parametro error. En el ejemplo solo
 * mostramos el error pero, conociendolo, podemos trabajar sobre el mismo */
catch (error) {
    console.log(error);
}

/** este bloque se ejecuta siempre, sin importar si en el bloque try encontramos
 *  un error y pasamos a revisarlo en el bloque catch o no */
finally {
    console.log('termina la revisión de errores');
}

/** si el error no es atendido se finaliza la ejecución del programa y esta
 * linea de código no llega a ejecutarse. Si el error es atendido por un bloque
 * try catch la ejecución continua */
console.log('continuamos...');
```

## Cláusula `throws`


La cláusula `throws` nos permite devolver nuestros propios errores para que sean tomados por el bloque `catch`. El parametro que pasamos a `catch` que llamamos `error`, por ser un objeto, podemos acceder a sus atributos con `name` y `message`.


```js
'use strict'
let resultado = -1;

try {

    /** isNaN devuelve true si la variable no es un número 
     * mediante throw devolvemos la cadena de caracteres escrita a continuación
     * como un error */
    if (isNaN(resultado)) throw 'No es un número';
    else if (resultado === '') throw 'Es cadena vacía';
    else if (resultado >= 0) throw 'Valor positivo';
    else if (resultado < 0) throw 'Valor negativo';
}
catch (error) {
    console.log(error);

    /** name es el tipo de error */
    console.log(error.name);

    /** message es la explicación del motivo del error */
    console.log(error.message);
}
finally {
    console.log('Termina revisión de errores');
}
```

# Funciones flecha


Cuando declaramos funciones flecha el ideal es hacerlo como `const` para que, una vez asignada la función a la variable, no se pueda asignar un nuevo valor a esta.


```js
/** por hoisting podemos llamar a la función antes de definirla */
miFuncion();
miFuncionAnonima();

/** forma común de declara una función */
function miFuncion() {
    console.log('saludos desde mi función');
}

/** forma común de declarar una funcion anónima y asignarla a una variable */
let miFuncionAnonima = function () {
    console.log('saludos desde mi función anónima');
}

/** forma común de definir una función flecha. Es similar a la función anónima
 * pero no se usa la palabra reservada function, los parametros van entre () si
 * son más de uno, se escribe el símbolo de flecha => y se abren las {}, dentro
 * de estás escribimos las sentencias del comportamiento de la función */
const miFuncionFlecha = () => {
    console.log('saludos desde mi función flecha');
}

/** no se utiliza hoisting para las funciones flecha, se tienen que llamar
 * después de definirlas */
miFuncionFlecha();
```

```js
/** si el cuerpo de la función consta de solo una línea de código no es
 * necesario utilizar las {} */
const miFuncionFlecha = () => console.log('saludos desde mi función flecha');

/** podemos retornar valores desde una función flecha igual que de cualquier otra */
const saludar1 = () => { return 'Saludos desde función flecha'; }
console.log(saludar1());

/** tampoco es necesaria la palabra reservada return si es solo una líne de código */
const saludar2 = () => 'Saludos desde función flecha';
console.log(saludar2());

/** para retornar un objeto tenemos que ponerlo entre (). En el ejemplo las {}
 * pertenecen a la definición del objeto y los () encierran al mismo para que
 * no se confundan con las {} de la definición de la función */
const regresaObjeto = () => ({ nombre: 'Juan', apellido: 'Lara' });
console.log(regresaObjeto());

/** definición de una función anónima con parámetros */
const funcionConParametrosClasico = function (mensaje) {
    console.log(mensaje);
}

/** función flecha con solo un parámetro */
const funcionConParametros1 = (mensaje) => console.log(mensaje);
funcionConParametros1('saludos con parametros');

/** si la función flecha tiene solo un parámetro podemos omitir los () que 
 * rodean al mismo */
const funcionConParametros2 = mensaje => console.log(mensaje);
funcionConParametros2('saludos con parametros');

/** si la función tiene varios parámetros, los mismos van entre () */
const funcionConVariosParametros1 = (op1, op2) => {
    let resultado = op1 + op2;
    return `Resultado: ${resultado}`;
};
console.log(funcionConVariosParametros1(3, 5));

/** resumiendo la sintaxis de la función según lo visto hasta ahora */
const funcionConVariosParametros2 = (op1, op2) => op1 + op2;
console.log(funcionConVariosParametros2(3, 5));
```

# Funciones callback `setTimeout` y `setInterval`


## Funciones callback


Una función de tipo callback es una función que se pasa como parámetro a otra función. Dentro del bloque de código de la primera llamamos a la función callback para obtener su retorno.


```js
/** las llamadas a las funciones se hace de forma secuencial. En el ejemplo además,
 *  por hoisting, al ser funciones comunes las llamamos antes de definirlas */
miFuncion2();
miFuncion1();

function miFuncion1() {
    console.log('función 1');
}

function miFuncion2() {
    console.log('función 2');
}

/** definimos una función para pasar como callback, esta definición es igual
 * a la de cualquier otra función, es decir, no requiere de nada en especial 
 * para poder usarse como función callback */
function imprimir1(mensaje) {
    console.log(mensaje);
}

/** al definir la función sumar recibe entre sus parámetros una función */
function sumar(op1, op2, funcionCallback) {
    let res = op1 + op2;
    funcionCallback(`Resultado: ${res}`);
}

/** cuando pasamos los argumentos a la función entre ellos va el nombre de 
 * la función callback */
sumar(5, 3, imprimir1);

/** también podemos asignar la referencia a una función en una variable y pasar
 * la variable como argumento a la función que recibe para hacer el callback */
let imp = function imprimir2(mensaje) {
    console.log(mensaje);
}

sumar(5, 3, imp);
```

## Función `setTimeout`


El objetivo de las funciones callback es que se utilicen en procesos asíncronos, es decir, mientras se está ejecutando una función, llamamos a la función callback que comienza a ejecutarse en paralelo a la función que veníamos ejecutando. La función `setTimeout` recibe como argumentos una función o la referencia a una función y el tiempo que tiene que esperar antes de ejecutarla en milisegundos.


```js
/** definimos una función para usar como callback */
function miFuncionCallback() {
    console.log('saludo asíncrono después de 3 seg');
}

/** pasamos una función indicando que la misma se ejecute después de 3 segundos
 * de ejecutarse está línea de código */
setTimeout(miFuncionCallback, 3000);

/** pasamos una función anónima que tiene que ejecutarse después de 4 segundos */
setTimeout(function () { console.log('saludo asíncrono 2') }, 4000);

/** pasamos una función flecha que tiene que ejecutarse después de 1 segundo */
setTimeout(() => console.log('saludo asíncrono 3'), 1000);
```

## Función `setInterval`


La función `setInterval` recibe como parámetro una función de tipo callback y un valor de tiempo de milisegundos. Esta función llama a la función callback pasado el intervalo de tiempo definido por los milisegundos.


```js
let reloj = () => {

    /** creamos un objeto de tipo fecha */
    let fecha = new Date();

    /** accedermos a los atributos de la fecha mediante los métodos que tiene 
     * definido el objeto de tipo Date */
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}

/** llamamos a la función relojo cada 1 segundo */
setInterval(reloj, 1000);
```

# Promesas


En una promesa utilizamos funciones de tipo callback. Una promesa es código que tiene varios estados. Lo que hacemos es lanzar una petición para procesar un código en caso de que la promesa se haya resuelto correctamente, en caso de tener problemas se llama otro código denominado rejected. Es decir, tenemos dos posibles caminos sobre nuestra petición, uno es que el código se haya ejecutado correctamente y el otro es que haya devuelto un error. Mientras la promesa no haya terminado de ejecutar su código se encuentra en estado pendiente, una vez que termina puede estar en estado resuelto o rechazado. Para procesar el código cuando se haya resuelto una promesa utilizamos la función `then()`, en caso de error utilizamos la función `catch()`.


```js
/** cuando creamos el objeto de tipo Promise recibe como argumento una función flecha
 *  esta funcion tiene como parámetros 2 funciones de tipo callback 
 * la primera se ejecuta en caso que se haya resuelto la promesa correctamente 
 * y la segunda en caso contrario */
let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = true;

    /** definimos ambos caminos que puede tomar la promesa */
    if (expresion)
        resolver('Resolvió correcto');
    else
        rechazar('Se produjo un error');
});

/** then es un método del objeto de tipo Promise. Este método recibe dos argumentos
 * que son 2 funciones de tipo flecha que se corresponden con las funciones 
 * resolver y rechazar que definimos cuando creamos el objeto */
miPromesa.then(

    /** se ejecuta el código de la promesa, si da verdadero if (expresion) se
     * ejecuta la función resolver, que es una función callback, por lo que lo
     * que se ejecuta es la funcion flecha valor => console.log(valor) 
     * #ver notas abajo */
    valor => console.log(valor),

    /** sucede igual que con resolver pero con rechazar */
    error => console.log(error)
);

/** para trabajar con catch y la función rechazar tenemos que llamar al método
 * de la misma forma que llamamos a then. En este caso then solo recibe
 * 1 argumento, el de resolver */
miPromesa.then(valor => console.log(valor)).catch(error => console.log(error));

/** notas */
/**
 * let resolver = valor => console.log(valor);
 * resolver('Resolvió correcto');
 * 
 * let rechazar = error => console.log(error);
 * rechazar('Se produjo un error');
 */
```

## Función `setTimeout` y promesas


```js
/** cuando creamos el objeto de tipo Promise, a la hora de pasar como argumento
 * la función flecha, no es necesario que la misma tenga las 2 funciones callback
 * como parámetro. En el ejemplo no manejamos el error, si lo tiene, de la promesa */
let promesa = new Promise((resolver) => {
    console.log('inicio promesa');

    /** setTimeout recibe como primer argumento una función callback. Esta función
     * va a ser la que recibamos como argumento cuando llamemos al método then del
     * objeto */
    setTimeout(() => resolver('saludos con promesa y timeout'), 3000);
    console.log('fin promesa');
});

/** llamamos al método then del objeto de tipo Promise. Pasamos como argumento
 * la función flecha que va a convertirse en la función resolver de tipo callback
 * que llamamos en la creación del objeto */
promesa.then(valor => console.log(valor));
```

## Palabra reservada `async`


La palabra reservada `async` facilita el uso de promesas. Al escribir la palabra `async`, antes de la definición de una función, indicamos que esa función está obligado a regresar una promesa.


```js
/** creamos una función anteponiendo la palabra reservada async. Esto permite
 * que la función se comporte como un objeto de tipo Promise, es decir, podemos
 * llamar al método then y catch  */
async function miFuncionConPromesa() {
    return 'saludos con promesa y async';
}

/** al ser una función y no un objeto de tipo Promise usamos los () antes de then
 * en el ejemplo llamamos a la función miFuncionConPromesa, lo que devuelve se
 * asigna al parámetro valor de la función flecha dentro de los () del then */
miFuncionConPromesa().then(valor => console.log(valor));
```

## Palabra reservada `await`


La palabra reservada `await` espera el resultado de una promesa. Una vez que este llega continua la ejecución del código que indicamos. `await` solo se puede usar dentro de una función declarada con `async`.


```js
/** definimos una función con async para que devuelva una promesa */
async function funcionConPromesaYAwait() {

    /** definimos un objeto de tipo Promise de la forma en que veníamos trabajando
     * con la función flecha como parámetro y la función resolver de tipo callback */
    let miPromesa = new Promise(resolver => {
        resolver('Promesa con await');
    });

    /** consumimos dentro de la misma función lo que regresa el objeto miPromesa
     * lo hacemos con la palabra resercada await, esto es equivalente a hacer
     * miPromesa.then(valor => return valor);  */
    console.log(await miPromesa);

}

/** llamamos a la función de forma normal para que se ejecute el código de las
 * promesas */
funcionConPromesaYAwait();
```

## Uso de promesas con `async`, `await` y `setTimeout`


Como ejemplo vamos a definir una función con `async` que devuelve una promesa, pero esa promesa se a resolver después de algunos segundos, cuando se ejecute la función `setTimeout`.


```js
/** definimos una función que devuelve una promesa con async */
async function funcionConPromesaAwaitTimeout() {
    console.log('inicio función');

    /** creamos un nuevo objeto de tipo Promise pasando una función flecha
     * que tiene como parámetro la función callback resolver */
    let miPromesa = new Promise(resolver => {

        /** pasamos a la función setTimeout una función flecha sin parámetros
         * que llama a la función callback resolver. Indicamos que lo haga pasados
         * 3 segundos desde la ejecución de la línea de código */
        setTimeout(() => resolver('promesa con await y timeout'), 3000);
    });

    /** con await indicamos que se ejecute esperamos la respuesta del objeto Promise
     * miPromesa. El mismo ejecuta el código miPromesa.then(valor => return valor); */
    console.log(await miPromesa);
    console.log('fin función');

}

/** llamamos a la función que regresa una promesa de forma normal */
funcionConPromesaAwaitTimeout();
```

# Manejo del DOM HTML


## DOM HTML


DOM significa Document Object Model. El DOM esta formado por diferentes elementos que se representan mediante etiquetas o tags. El elemento principal del cual cual se ramifican todos los otros elementos se llama document. Cuando trabajamos desde JavaScript cada uno de estos elementos se representa mediante un objeto, que tiene atributos y métodos. En ese caso el objeto principal y padre de todos los otros objetos es el objeto `document`. Mediante este objeto vamos a manipular nuestro documento HTML, es decir, vamos a poder interactuar con cada uno de los elementos o tags que componen el DOM o la página HTML.


![1200px-DOM-model.jpg](data:image/jpeg;base64,/9j/4AAQSkZJRgABAgEAYABgAAD//gASTEVBRFRPT0xTIHYyMC4wAP/bAIQABQUFCAUIDAcHDAwJCQkMDQwMDAwNDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQEFCAgKBwoMBwcMDQwKDA0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0N/8QBogAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoLAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgsQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+hEAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/8AAEQgE2gSwAwERAAIRAQMRAf/aAAwDAQACEQMRAD8A+y6APJ/iD8W9N8D5tEH23USMiBGwseRkGd+dmRyEALsMHCqwatoU3LXZHXSoSq67R7/5HzBf/EPxj46naG1kuAp/5d7BXjVVPZmjzIV9TLIwrqUIx/4J6kaNOn0Xq9f+B9xV/wCFU+LL797NbMS3OZbiHcfrmUsPxwarmSNOeC0X5B/wpzxR/wA+yf8AgRB/8co5kHtI9/wD/hTnij/n2T/wIg/+OUcyD2ke/wCAf8Kc8Uf8+yf+BEH/AMco5kHtI9/wD/hTnij/AJ9k/wDAiD/45RzIPaR7/gH/AApzxR/z7J/4EQf/AByjmQe0j3/AP+FOeKP+fZP/AAIg/wDjlHMg9pHv+Af8Kc8Uf8+yf+BEH/xyjmQe0j3/AAD/AIU54o/59k/8CIP/AI5RzIPaR7/gH/CnPFH/AD7J/wCBEH/xyjmQe0j3/AP+FOeKP+fZP/AiD/45RzIPaR7/AIB/wpzxR/z7J/4EQf8AxyjmQe0j3/AP+FOeKP8An2T/AMCIP/jlHMg9pHv+Af8ACnPFH/Psn/gRB/8AHKOZB7SPf8A/4U54o/59k/8AAiD/AOOUcyD2ke/4B/wpzxR/z7J/4EQf/HKOZB7SPf8AAP8AhTnij/n2T/wIg/8AjlHMg9pHv+Af8Kc8Uf8APsn/AIEQf/HKOZB7SPf8A/4U54o/59k/8CIP/jlHMg9pHv8AgH/CnPFH/Psn/gRB/wDHKOZB7SPf8A/4U54o/wCfZP8AwIg/+OUcyD2ke/4B/wAKc8Uf8+yf+BEH/wAco5kHtI9/wD/hTnij/n2T/wACIP8A45RzIPaR7/gH/CnPFH/Psn/gRB/8co5kHtI9/wAA/wCFOeKP+fZP/AiD/wCOUcyD2ke/4B/wpzxR/wA+yf8AgRB/8co5kHtI9/wD/hTnij/n2T/wIg/+OUcyD2ke/wCAf8Kc8Uf8+yf+BEH/AMco5kHtI9/wA/DHxdpX76C3kUr3guItw+gSUOfwBo5osXPB6P8AFGjpHxW8W+C5xbX7y3Cp963v1cvjpxI+Jl4+6d5TvtYcVDpxltp6GUqFOpqlbzj/AJbH1X4E+JmmeO4sW5NveRrmW1kI3gd2jYYEseTjcACON6pkZ5JQcPTueVUoypb6ro/62PRazOcKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPJ/i38Qf+EH00JaEHUb3ckAOD5aj787A8HZkBAeGcjIKqwranDmeuyOuhS9rLX4Vv/kfMnw8+Hs/jm4fU9TeQWQkJkkJJluZScsqscnGTmSQ5OTtX5slOxvl0R685qC5Y7/kfWumaTaaLAtrYRJbwp0RBgfUnqzHuzEsepJrA4m29WaFAgoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAxtc8PWHiO3NrqMKTxnOCRh0J/ijcfMje6kZ6HIyKadtik3HVHyL4v8Jah8MtTivbGV/J377W5XhlZeTHJj5d4HBBGyVM8Y3ouyakrM7E1VTjJeqPr34deOYvG2lpecJcxny7mMfwygD5lHXZIMOnXGSuSVNcM48jt06HiVafspcvTdeh6GDmszAWgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPgj4h38/jrxjJaQnKi4Wwt+6qsb+WzD/ZMhklJ9G9q9CC5Y/ie/Rj7OmvS7+f/A0PrnSdMg0W0isLVdkNugRR7DqT6sxyzHuxJPWsjlbu7s0KBBQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAHO+LPD0XijTJ9NlAzKhMbH+CVeY3HphsZx1UsvQmmnZ3Li+V3R8x/BjXZdA8QfYJSUjvVaGRTwBLHueMn/aBDxj/roaqqrxv2NMTHmhzLeOvye/8Amfb9tNvArhPELtABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAfn98Kv9P8W200vJLXEpz3byZSD/30c/UV6UtEfRz0hZeR9p1gcAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAHxPej+z/ABw3l8BdXBwPR7kEj6YYj6Vs/gfp+h2S1pP/AAv8j7f0ufcBXnHz50qnIoAdQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAfn98HP+Rotv8AcuP/AERJXpS2Po6nwv5H2nWBwBQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAfE2vceNpP+won/o9a2+y/Rna/wCE/wDC/wAj7O0d+lecfPHaxdKAJKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgD8/vg5/yNFt/uXH/AKIkr0pbH0dT4X8j7TrA4AoAKACgAoAKAPnf4CeOta8af2l/bdx9q+y/ZPJ/dQRbPN+07/8AUxx7t3lp97OMcYyc5xbd7mFOTle/l+p9EVobhQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQB534e+JmmeJdcvPDlrFcpd6d5/mvKkQhb7POlu/lsszucu4K7o1yuSdp+Uynd2M1NNuK3R6JVGgUAFABQAUAfE2vf8jtJ/2FE/8AR61t9h+jO1/wn/hf5H2Vo/avOPnjuIfu0AS0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAF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oAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA/P74Of8jRbf7lx/6Ikr0pbH0dT4X8j7TrA4AoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPibXv+R2k/wCwon/o9a2+w/Rna/4T/wAL/I+ytH7V5x88dxD92gCWgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA/P74O8eKLYf7Fx/6Ikr0pbH0dT4X8j7TrA4AoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPibXufG0mP+gqn/AKPWtvsP0Z2v+E/8L/I+ytH7V5x88dxD92gCWgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA/P3w83/CH+NUin+Rba+mtmJ6BZDJAGP+zhw+fTmvS+KN/I+i+OnddUn+p9qVgcIUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFA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AKACgAoAKACgAoAKAPLfjX/yJupf9c4f/SmGgD84aANnQPEN/wCF7tdR0qU211GGVZAqPgOCrDbIrryDjleO1AHff8Lw8af9BJv/AAHtP/kegA/4Xh40/wCgk3/gPaf/ACPQAf8AC8PGn/QSb/wHtP8A5HoAP+F4eNP+gk3/AID2n/yPQA2w1m78QahBqOoyefdTzxGSQqq7irqo+VFVRhVA4UdPWv1fLv8AkX0/8E//AEqR7FL+GvR/qfofXwp5wUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAHyZ8e/wDkN23/AF4p/wCj56+2yj+BP/r4/wD0mJ6FD4X6/oj33wH/AMgux/69bf8A9FJX5zi/95rf9fan/pbPMn8UvV/mevWn3RXEZlygAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf/Vt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFAHlvxr/5E3Uv+ucP/AKUw0AfnDQAUAFABQAUAFAHoPhf/AFlp/wBdo/8A0aK/V8u/5F9P/BP/ANKkexS/hr0f6n6R18KecFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQB8mfHv/kN23/Xin/o+evtso/gT/6+P/0mJ6FD4X6/oj33wH/yC7H/AK9bf/0UlfnOL/3mt/19qf8ApbPMn8UvV/mevWn3RXEZlygAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf/Vt/un+VAHOUAFABQAUAFABQAUAF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B6Fsetfd1pxyzBuz1hDlj5zl1/8AAnf0uejJ+yh6L8T7P0dORX5GeMehWwwtAFqgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf/Vt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBk67ott4hsZtNvF3Q3CbTjqp6q6nsyMAyn1AyCOK6aFaeGqRr0naUXddn3T8mtGVGTg1Jbo+LLi31n4Sa3uXgrnY+D5N1ASMg+oPG5c7o3AIOQrH9Up1KGbULr5r7VOX9bPaS+aPXTjWj/V0z6e8I/EjSfFiKscgtrsj5raVgHz38snAlX0K/NjlkXpXyWJwNXCttrmh0mlp8/5fnp2bOOVNw9O539eYYhQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBkazr+n+HoTcalPHboOm4/M2OyIMu59lUmt6VGpXfJSi5Py2Xq9l8ylFy0ij5O+IXxJuPG0g07T0eKwDjbHjMtw+flLhc8A/ciGefmYltoT7XB4KGCi61Zrntq9owXWzf4y7abXv3wpqn70t/wR6R8OfBh8PwGa4A+2XAG/v5adRGD655cjgtgchQT8RmuP+u1FTpfwYN8v959ZfpHyu+rRwVqnO7L4V+Pme+6RbbcGvnTmOyiXaKAJaACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/9W3+6f5UAc5QAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBQ1nwvYeK7FrLUohNHuJU9HjbAw8bjlGHqOo4YFSQevD4irhJqrQk4y69muzWzX/DrUuMnB3i7Hyx4o+BGpaY7SaPIt7D1WOQiKcegycRPj+9ujz/cr7vDZ7RmlHFRdOXWSTlD7l7y9LS9T0I4iL0mrP8P8zjl/4TbQv3Kf2rEq8BVM7xjHpt3oPwr1Pa5dX95yoN+bhF/jZm16UusfwQv/AAkfjb/nrqf/AH7l/wDiKOTL+9D/AMDh/mFqX9370H/CSeNv+eup/wDfuX/4ijky/vQ/8Dh/mFqf9370H/CSeNv+eup/9+5f/iKOTL+9D/wOH+YWp/3fvQf8JJ42/wCeup/9+5f/AIijky/vQ/8AA4f5han/AHfvQf8ACSeNv+eup/8AfuX/AOIo5Mv70P8AwOH+YWp/3fvQf8JJ42/566n/AN+5f/iKOTL+9D/wOH+YWp/3fvQf8JJ42/566n/37l/+Io5Mv70P/A4f5han/d+9B/wknjb/AJ66n/37l/8AiKOTL+9D/wADh/mFqf8Ad+9B/wAJJ42/566n/wB+5f8A4ijky/vQ/wDA4f5han/d+9B/wknjb/nrqf8A37l/+Io5Mv70P/A4f5han/d+9B/wknjb/nrqf/fuX/4ijky/vQ/8Dh/mFqf9370Vbjxl4ttCFnur6IkZAcOpI9QGUZo5Mv70P/A4f5han/d+9Ff/AIT3xP8A8/13/wB9H/Cjky/vQ/8AA4f5han/AHfvRbg8W+MLpd8FxqEqg4yiyMM+mVUjPI496OTL+9D/AMDh/mFqf9370T/8JJ42/wCeup/9+5f/AIijky/vQ/8AA4f5han/AHfvQf8ACSeNv+eup/8AfuX/AOIo5Mv70P8AwOH+YWp/3fvQf8JJ42/566n/AN+5f/iKOTL+9D/wOH+YWp/3fvQf8JJ42/566n/37l/+Io5Mv70P/A4f5han/d+9B/wknjb/AJ66n/37l/8AiKOTL+9D/wADh/mFqf8Ad+9B/wAJJ42/566n/wB+5f8A4ijky/vQ/wDA4f5han/d+9B/wknjb/nrqf8A37l/+Io5Mv70P/A4f5han/d+9B/wknjb/nrqf/fuX/4ijky/vQ/8Dh/mFqf9370H/CSeNv8Anrqf/fuX/wCIo5Mv70P/AAOH+YWp/wB370H/AAknjb/nrqf/AH7l/wDiKOTL+9D/AMDh/mFqf9370H/CSeNv+eup/wDfuX/4ijky/vQ/8Dh/mFqf9370H/CSeNv+eup/9+5f/iKOTL+9D/wOH+YWp/3fvQf8JJ42/wCeup/9+5f/AIijky/vQ/8AA4f5han/AHfvQ1ta8bXQ2CTVTnj5VnX9VUEfXNH/AAnQ1bw/zlB/mw/dL+X70JZ/DzxBrkvnXgaLd96W5kLOf+A5eQn03BQfUVz1c3weGXLSfO1tGnHT73aNvS/oS60IaLXyX9WPavCnw9s/DpEqgz3WMGZwBjPURryEB7nJYjILY4r4nG5nWx3uP3KX8kXv/if2vwXlc4KlWVTTZdv8z1nTtNORkV4Zznc2dt5YFAGqBigAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAin/1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGxp4zGf97+goAWe1D0AYNzpQbtQBlPo/tQBD/Y3tQAf2P7UAH9j+1AB/Y/tQAf2P7UAH9j+1AB/Y/tQAf2P7UAH9j+1AB/Y/tQB80fHKT+ytQtE6b7dj/wCRCKAPD/7Z96APqj4KQf2pocs3XF5Kv5RQH+tAHr/9j+1AB/Y/tQAf2P7UAH9j+1AB/Y/tQAf2P7UAH9j+1AB/Y/tQAf2P7UAH9j+1AB/Y/tQAf2P7UAH9j+1AB/Y3tQBIuj+1AGjb6SF7UAb9vZiPtQBpKu2gB1ABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP8A6tv90/yoA5ygAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDZ07/Vn/e/oKAL9ADCgNADDAtADfs60AH2cUAH2cUAH2cUAH2cUAH2cUAH2cUAH2cUAH2cUAH2cUAfD/wC1UfI1fTgvezf/ANHGgD5X+0NQB99fsvr53hWdj/0Epx/5L2tAH0d9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nFAB9nWgBRAooAkEYFAD8YoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAin/ANW3+6f5UAc5QAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBs6d/qz/vf0FAF+gAoAKACgAoAKACgAoAKACgAoAKACgD4W/ax/wCQxp3/AF5v/wCjmoA+UKAP0F/ZZ/5FOf8A7Cc//pPaUAfSdABQAUAIzBAWYgKBkk8AAdST2Ap76INj5/8AGfx2tNKdrTQUW9mXINw5P2dSP7gUhpv94MidCrOK+owuTzqJVMS3CP8AKvj+d9I/c33SPDr5hGD5KC5n3fw/Lv8AgvU8Un8c+MfFLkwXF4y5+7Zq0SL7EwBTj/fYn1Jr6SOCweHVnCHrO0m//Ar/AII8eWJxFXaUv+3dF+H6kH9m+Mn5J1E/WeTP6yZrX/ZFpy0v/AY/5Gf7/vP/AMCf+Yn9l+MfXUP+/wDJ/wDHKL4XtT/8BX+QWr95/wDgT/zD+y/GPrqH/f8Ak/8AjlF8L2p/+Ar/ACC1fvP/AMCf+Yf2X4x9dQ/7/wAn/wAcovhe1P8A8BX+QWr95/8AgT/zD+y/GPrqH/f+T/45RfC9qf8A4Cv8gtX7z/8AAn/mH9l+MfXUP+/8n/xyi+F7U/8AwFf5Bav3n/4E/wDMP7L8Y+uof9/5P/jlF8L2p/8AgK/yC1fvP/wJ/wCYf2X4x9dQ/wC/8n/xyi+F7U//AAFf5Bav3n/4E/8AMP7L8Y+uof8Af+T/AOOUXwvan/4Cv8gtX7z/APAn/mH9l+MfXUP+/wDJ/wDHKL4XtT/8BX+QWr95/wDgT/zD+y/GPrqH/f8Ak/8AjlF8L2p/+Ar/ACC1fvP/AMCf+Yf2X4x9dQ/7/wAn/wAcovhe1P8A8BX+QWr95/8AgT/zD+y/GPrqH/f+T/45RfC9qf8A4Cv8gtX7z/8AAn/mH9l+MfXUP+/8n/xyi+F7U/8AwFf5Bav3n/4E/wDMP7L8Y+uof9/5P/jlF8L2p/8AgK/yC1fvP/wJ/wCYf2X4x9dQ/wC/8n/xyi+F7U//AAFf5Bav3n/4E/8AMP7L8Y+uof8Af+T/AOOUXwvan/4Cv8gtX7z/APAn/mH9l+MfXUP+/wDJ/wDHKL4XtT/8BX+QWr95/wDgT/zD+y/GPrqH/f8Ak/8AjlF8L2p/+Ar/ACC1fvP/AMCf+Yf2X4x9dQ/7/wAn/wAcovhe1P8A8BX+QWr95/8AgT/zD+y/GPrqH/f+T/45RfC9qf8A4Cv8gtX7z/8AAn/mH9l+MfXUP+/8n/xyi+F7U/8AwFf5Bav3n/4E/wDMP7L8Y+uof9/5P/jlF8L2p/8AgK/yC1fvP/wJ/wCYf2X4x9dQ/wC/8n/xyi+F7U//AAFf5Bav3n/4E/8AMP7L8Y+uof8Af+T/AOOUXwvan/4Cv8gtX7z/APAn/mH9l+MfXUP+/wDJ/wDHKL4XtT/8BX+QWr95/wDgT/zD+y/GPrqH/f8Ak/8AjlF8L2p/+Ar/ACC1fvP/AMCf+Yf2Z4yXkHURj0nk/wDjlH+yfy0//AV/kH7/ALz/APAn/mSJ4p8Z+GCJJLjUIlH/AD8b5Yvp+/Ekf5VDwuDr6clN/wCG0X/5LZlqviKWvNNet2vxuj1nwj8fBK623iKJY84H2qAHaPeWL5iB3LRk+0YHI8DE5NZOeElf+5Lf/t2Wn3P7z1KOY392urf3l+q/y+4+j7W7hvYluLd1likUMjoQysp6FWGQQfavkZRcG4TTUlo09Gn6H0CaklKLuns0WKkYUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP8A6tv90/yoA5ygAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDZ07/Vn/e/oKAL9ABQAUAFABQAUAFABQAUAFABQAUAFAHwt+1j/AMhjTv8Arzf/ANHNQB8oUAfoL+yz/wAinP8A9hOf/wBJ7SgD6ToAKACgD5Q+M/xHkvZ38OaW5W3hOy7kQ8yyDrCCP+WaHhx/G+VPyr833GVYFQisXWXvPWCf2V/N6vp2Wu70+Zx2Kcm8PTfurSTXV9vRde7M3wZ8NI0Rb7WV3yMAyWx+6o6gyj+Jv+mf3V6PuJIX0a+Kd3Ci7LrL/L/P7jjpUF8VT7v8/wDI9liiSBBHEqoijCqoCqB6ADAA+leS23q9z0LW0RJSAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAQqGBBGQeCD0IoA8s8W/DW11NGudLVba6AJ8tflil9sdI2PZlwpP3hzuHp0cVKD5amse/Vf5o46lBS1ho+3R/5HLfDHx/ceDL7+ytSLLYSybJEfINtLnBkAP3V3cSr0x84+YYacxwUcXD29FfvYq6t9tdvX+V/LZ6GExLw8vZ1Pgbs7/Zff07/efaEcocZFfnh9cS0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP8A6tv90/yoA5ygAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDZ07/Vn/e/oKAL9ABQAUAFABQAUAFABQAUAFABQAUAFAHwt+1j/AMhjTv8Arzf/ANHNQB8oUAfoL+yz/wAinP8A9hOf/wBJ7SgD6ToAKAOU8c6+fDOiXepJxJFERF/11kIjjOO4DsGI9Aa7sJR+s16dF7N6/wCFav8ABWObEVPY0pVFulp6vRfiz5A+GWhDWdSa+uRvjs8SfNzumcnYTnrjDOf9oLnrX6Ji6nsoKEdHLT0S3/yPkKEOeXM+mvz/AK1PpKvnz1goAKACgAoAKACgAoA85+LN9cab4Xvbmzlkt54/s+2SJ2jkXddQK210IYZUlTg8gkHgmuTEtxpScW09NVo/iR0UUnNJq6139Gc54c8AyavpdnqE2t6+st3a287hNQIQPLEjsFBiYhQWIUFicYySeayhRcoRk6lW7in8fdX7FyqcsnFQho2vh7Mi+Iuhf8I94J1G2+1Xl/vkt5PNvpvPlXN1arsV9qYjGzcFxwzOc88KvD2dCa5pS1TvJ3fxR/AdKXNVi7Jb7Ky2Z6N4I/5F7S/+wdZ/+k8dddL+HD/DH8kc9T45f4n+Zlaj8T/DOlXBtLm/iEqnawRZZQrDghnijdFIPBBYYPBwazliKUXyuSv83+SLVKbV1HT5L8zqP7csTYNqyTJJZRxPO00Z8xfLjUs7DYGLbQpyqgtkFcbuK3548vOn7tr3Wui32MuV35ba3tY5ab4n+Gre2gvJL5Fhuwxh/dzb2VJGiZjEI/NRRIjKGdFUlTgkc1g8RSSUnJWe2j722tfc19lO7SWq329TT1Txvoei2sV9eXkUdvdDdCylpDKvHKLGHdgMjcQuFJAODVyqwglKUlZ7db+liVTlJuKTut/I19H1qy1+2W902ZLi3ckB0z1HVWBAZWHdWAYZGRyK0jKM1zQd0RKLg7SVmUtf8V6T4XRX1W5jtd+ditlnbHUrGgaRgO5CkA4yeamdSFL42l/XbcqMJT+FXIfD/jPRvFO4aTdR3LIMsgDJIB03eXIqPtzxu24yQM5NKFWFT4JJ/g/ueoShKHxKxHc+N9Fs7y5064ukiubCIT3CusirHG3lbW8woI2J86IBUdnJcALkEBOrCLcHKzirvfRadduqGqcmlJLRuy/H/Jj/AA94z0fxUXXSbpLloeXUB0cDON2yRUYrnjcAVyQM8inCrCr/AA3e3y/MUoSh8SseS678WYdN8YQWYvfL0W3jliv1+zltt3H9qQru8gznEggGYSYz1yRvNcM8So1lHm/dpNS0+0ubyvvbbQ6o0b027e87Na9NPO3fc9f0TxbpXiGzk1LT7hZLS3Z1lmdXhSMxosjlvOWMhVR1ZnI2AE/Nwcd8KkKkXOL91bvVWtr1t0OWUJQfLJavZb/kbNlfW+pQrc2csdxA+dskTrJG20lW2uhKnDAqcHggg8g1aakrxaa7rVENOOjVn5lqqEFABQAUAFABQAUAFAHg/wAWtAWF49XhGPNPlTY7uATG/wBSoKk/7K9zXt4KpdOk+mq9Oq/rzPNxELWmuuj/AEPavhH4lbWdEiSZt01oTbOT1IQAxn/v2yAk9WBNfGZnQWHxMuXSM1zr53v/AOTJ/Jo+iwVT2tFX3j7r+W34NHsaNuFeKekPoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/9W3+6f5UAc5QAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBs6d/qz/vf0FAF+gAoAKACgAoAKACgAoAKACgAoAKACgD4W/ax/5DGnf9eb/wDo5qAPlCgD9Bf2Wf8AkU5/+wnP/wCk9pQB9J0AFAHh/wAfp2h8OxIvAlvYlb6CKd//AEJFr6TJo3xLfanJr/wKK/Js8fMXail3mvyk/wBDg/hHAsekyyD70ly+T7LHGAPwJJ/Gvoca/wB4l2ivzZ5GGVoN+f6I9UrzDtCgAoAKACgAoAKACgDy/wCM3/Io3/8A27f+llvXHiv4Mvl/6UjpofxI/P8AJmD4V+HX23R7C5/tjXYfOs7aTyob/ZFHvhRtkSeUdkaZ2ouTtUAZOKyp0OaEX7SorxTspaLTppsXOraUlyQ0b3jrv6lr4m6X/Y3gW7svPuLzyvI/fXcnmzvuv4X+eTau7bu2rwMIqr2zTrx5KEo3btbWTu/iW7FSfNVTslvotF8LE1jUp9J+HEVzakpKNKsUDLwyiVLeJmBHIIR2II5BGRyKJSccMnHfkj+KS/UIpSrWe3NL8Ls5zwNca1pehW9tY+Go7q2nhV3mOo2a/avMG4ySI6FhuBwI3JKLhD93FZUXONNKNFNNb88db9Wrfg/Q0qKLk26lmntyvQZ4b8P6x4d8O+JINTtTYWk1tdT2cHnxThA9vciRA0Tt9xVhXcypv6gZzhU4Tp06ynHli1JxV07XTvt8glKMp03F3aaTdmuq/wCCdF8HdBs5vCMfmxrJ/aP2kT7gCWUTSwhMn+EBMhegZmYDLEnbCwToq6+K9/vaM60mqmnS1vuTMP8AZ+sY59IuLyYeZItw1ohf5vLgVEmMaZztR5LiR3VcBmOWyQKywSTg5Pe/L6KydvvbLxDtJJdr/Pb9C38HFFnqniLTofltrXUMRIPuqDLdx8Dt8sSD6KPSqwuk6sFspaL5yX6IVfWNOXVx/Rf5nLaTqGp3njHWNQt9LGtz2Uptog91Db/ZYkkkjRoxMrAl1j+8gBXLkn96c4xlJ1qklDncXZe8lyq7Wl+9un6mjUVThFy5U1fZu/3ev9WN270nxLq/iXTddTRhpJtpVS7lW+tJvNgd1Vy6oY2JSIyDhXZwVA+4orRxqyqwqKnyWfvPmi7r8Ol+5CcIwlDn5r7aNWYmm6dDqHxR1EzqHFtaRTKrcjeILFFJB4O3zCy56MFYfMoIIxUsVO/SKf4RX6g21Qjbq2vxkW9SiTTvifY/ZgI/t1g7T7RjeRHectjqf9Hi691BqpLlxUbac0Xf7pf5IS1oSv0en4f5sk1//kp+kf8AYOk/9A1Kif8AvVP/AAv8phH+BL/F/wDInt19ZQ6lby2dyu+C4jeKVcld0cilHXcpDDKkjKkEdQQea9FpSTi9mrP0Zxp2aa3WpV0XRbPw9Zx6dp0fkW0O7Ym53273aRvmkZnOXdjyxxnAwABShBU0oQVktl669Ryk5PmlualWSFABQAUAFABQAUAFAHD/ABGgWbQbnPVPLcexEqf0JH412YV2qx+a/BnPXV6b+X5nL/A27aP7bFn5Q0DAe7CUH/0EVw54rOjLraa+7lt+bOnLHpUj/hf383+R9UWcm5RXx59CaFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP/q2/wB0/wAqAOcoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA2dO/1Z/wB7+goAv0AFABQAUAFABQAUAFABQAUAFABQAUAfC37WP/IY07/rzf8A9HNQB8oUAfoL+yz/AMinP/2E5/8A0ntKAPpOgAoA8I/aE/5ANt/1/wAf/pPc19Nkv+8T/wCvT/8ASoHi5l/Cj/jX/pMjkfhP/wAgZv8Ar5k/9Bjr3cZ/F/7dX6nmYf4Pm/0PTa846woAKACgAoAKACgAoA434geHrjxXoVzpNm0cc9x5O1pSyxjy54pW3FEdhlUIGFPOM4GSOetB1abhG13bfbRp+fY1pyUJKT2V9vRo5LStO8e6RZwafCdAaK0higQudQLlIkVFLEBQWIUFiFUZzgAcVhGOIhFRXsrJJfa6aGrdKTcnz6u/2epf17w94h8V+GrvSdTbTo9QuJIvKa2NwtsIo5YJf3hkR5RISko+VSuPL6fMRc4VKtKUJ8vM2rWvayaet7u+j/AUZQhNSjzcq3va97Neh1Fh4cQ6BBoOpBZVWxhtJ9hO1ikKxsUYhW+8u5GKqw4OAa2UP3apT191Rf3W0MnL33OPdtfecFpHhTxf4Ri/s7RbzT7vT0J8kagk6yxKxJ2AwcMASfvNj+6qDCjljTrUlyU5RcenMndfcbudOfvTUk+vLaz+869tG1i+0O+0/U7i3uL6+huYo2jjaGCITQeUkf8AG7Kr7naQgvhsBTtAPRyzlTlCbTlJNKysldWt336mXNFSjKKaSa827Mk+H/h648KaFbaTeNG89v525oizRnzJ5ZV2l0RjhXAOVHOcZGCSjB0qahK11fbbVt+XcVSSnJyWztv6JGN8K/Bt54H0uXT9QeGSWW6ecGBnZNjRQoAS8cZ3ZjYkBSMEc5yBnh6UqMHGVr819PRLql2LrTVSSlG+1tfVh4H8G3nhnVNZ1C6eF4tXuhPAImcuqebdPiUNGgVsTKMIzjIbnABJSpSpzqSdrTldW9ZPXTzCpNTjCKv7qs/uX+RU1rwHf2+sP4j8MXMVneXC7LmC4Rmtp8Y+Y7Msh+VSdqklhuDKS25ToyU/a0WlJ7p7Mcai5fZ1FdLZrdG3ott4se7jm1m406O1j3b4LKKZjLlGVQZJzlArlX+UEtt2ngmtIKtdOo4W7RT1+b27kSdO1oKV+7a0+SM/S/Bt5ZeMb7xNI8JtL21SCNFZ/ODqtoCXUxhAubd8ESMeV45O2I0pRrSrO3K42S6/Z8rdO5TmnTjT1unfy6/5hqng28vfGNj4mjeEWllavBIjM4mLst2AUURlCubhMkyKeG44G4lSk60aytyxjZrr9ryt17gppU5U9bt38un+RD4x8E6hqWr2fiTQ54IdQsI2i2XKuYZI28zgmPLjiWRSAOQwIZSvKq0pSnGtTaUoq2uzWvb1Y4TUYunNPleum/8AWh0llH4il0u5j1B7GLVXWZbWS0Ext0JiAheQXCuxZZtxcBHTYF+VjkHZe0cGpcqnryuN7LTS9/MzfJzLlvy6Xva++u3kX/DNvqlrp0MWuzR3WoLv86WIARtmRzHtAihHyxFFP7teQev3jVNSUUqjTlrdrbfTounkTPlbfIrR6J/0zerUgKACgAoAKACgAoAKAOO8f/8AIBu/9xf/AEYldeG/iw9X+TMK38OX9dTz74LttlvPpb/zmrlzzaj/ANxP/bDfLP8Al5/27/7cfVumtlRXxh9EbtABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP/q2/wB0/wAqAOcoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA2dO/1Z/wB7+goAv0AFABQAUAFABQAUAFABQAUAFABQAUAfC37WP/IY07/rzf8A9HNQB8oUAfoL+yz/AMinP/2E5/8A0ntKAPpOgAoA8I/aE/5ANt/1/wAf/pPc19Nkv+8T/wCvT/8ASoHi5l/Cj/jX/pMjkfhP/wAgZv8Ar5k/9Bjr3cZ/F/7dX6nmYf4Pm/0PTa846woAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA47x/8A8gG7/wBxf/RiV14b+LD1f5Mwrfw5f11PO/g1/rbz6W/85q5c82o/9xP/AGw3yz/l5/27/wC3H1bpf3RXxh9EdAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf8A1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKAPhb9rH/AJDGnf8AXm//AKOagD5QoA7Hw/8AEHxB4VtzZ6PfT2du0hlMcZUKXYKpblTyVRR+AoA3P+Fy+M/+gtdfmn/xFAB/wuXxn/0Frr80/wDiKAJ4PH+v+K2+yaxfTXkEY81UkKkCQfKGGFHIV2H0Y19Nkv8AvE/+vT/9KgeLmX8KP+Nf+kyPp/4T/wDIGb/r5k/9Bjr3cZ/F/wC3V+p5mH+D5v8AQ9NrzjrCgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDjvH/APyAbv8A3F/9GJXXhv4sPV/kzCt/Dl/XU87+DX+tvPpb/wA5q5c82o/9xP8A2w2yz/l5/wBu/wDtx9W6X90V8YfRnQCgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAin/1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKAPhb9rH/kMad/15v/AOjmoA+UKACgAoAKAOk8L/8AHy//AFyP/oSV9Nkv+8T/AOvT/wDSoHi5l/Cj/jX/AKTI+z/hP/yBm/6+ZP8A0GOvdxn8X/t1fqeZh/g+b/Q9NrzjrCgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDjvH/8AyAbv/cX/ANGJXXhv4sPV/kzCt/Dl/XU87+DX+tvPpb/zmrlzzaj/ANxP/bDbLP8Al5/27/7cfVul/dFfGH0Z0AoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/8AVt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAbOnf6s/739BQBfoAKACgAoAKACgAoAKACgAoAKACgAoA+Fv2sf+Qxp3/Xm//o5qAPlCgD7l/Zt8J6Lrnhma41PT7K9mXUZkElxawTOEEFsQgeRGYKCzELnALE4yTQB9A/8ACuvC3/QH0r/wAtf/AI1QAf8ACuvC3/QH0r/wAtf/AI1QB438b/CmjaFo0FxpdhZWMzXqI0ltbQwuUMM7FC0aKxUsqkqTjKg4yBX02S/7xP8A69P/ANKgeLmX8KP+Nf8ApMih8J/+QM3/AF8yf+gx17uM/i/9ur9TzMP8Hzf6HptecdYUAFABQAUAFABQAUAFABQBxvxA8Q3HhTQrnVrNY3nt/J2rKGaM+ZPFE24I6McK5Iww5xnIyDz1pulTc42urb7atLy7mtOKnJRezvt6Nh8P/ENx4r0K21a8WOOe487csQZYx5c8sS7Q7uwyqAnLHnOMDABRm6tNTla7vtto2vPsFSKhJxWytv6JnZV0GQUAFABQAUAFABQAUAFAHjfxa+IeoeAvsX9nR28v2z7Rv+0JI2PK8jbt8uWLGfNbdndnAxjnPn4mvKhy8iTvfe/S3ZruddGmqt+a+ltvO/keyV6ByBQAUAFABQAUAFABQAUAFAHHeP8A/kA3f+4v/oxK68N/Fh6v8mYVv4cv66nnfwa/1t59Lf8AnNXLnm1H/uJ/7YbZZ/y8/wC3f/bj6t0v7or4w+jOgFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP/q2/wB0/wAqAOcoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA2dO/1Z/wB7+goAv0AFABQAUAFABQAUAFABQAUAFABQAUAfC37WP/IY07/rzf8A9HNQB8oUAfoL+yz/AMinP/2E5/8A0ntKAPpOgAoA8I/aE/5ANt/1/wAf/pPc19Nkv+8T/wCvT/8ASoHi5l/Cj/jX/pMjkfhP/wAgZv8Ar5k/9Bjr3cZ/F/7dX6nmYf4Pm/0PTa846woAKACgAoAKACgCrd3sGnxGe6kjgiT7zyuqIPqzEAfiaTairyaS89BpN6I8k1r42aNZSfZdJSbV7onCpbqQhb08xlJb2MUcgPrXBPFwj7sE5vstvv8A8kzqjQk9ZWivM1fBOq+K9avXu9ctI9N00wMIYOPOMpeMqz7i0g2oJAdwiGSP3Z4I0pSqzlzVIqMLaLre6367X7ehNRU4q0HeV9X0t/XqHxm/5FG//wC3b/0st6MV/Bl8v/SkFD+JH5/kzzLwD411K38PWejeGbA6nfwLO9wzsI7e38y6naNXZmQNI6HcF8xPlIILHcF4qNWSpxp0Y80le/RK8nbtr8zoqU487nUlyrS3d6I6LQfizqVtrCaD4tsk0+e4ZVjki3BAznbHuDPKGjdvlEqSFVbgjAYrtDEyU1Srx5W9mvPbq9PNMzlRjy89J3S/ryPcry8h0+B7q5dYoYUZ5HY4CqoySfoP/rV6Taim3olucaV3ZbnhK/FTX/FE0i+DtKFzbQtt+0XJKqx/7+QIhIwQhlZ8EEhc4HmfWKlRv6vC6XV/8Ol+J2+xhBfvZWfZf0/yLOkfFm+0/Uo9H8YWI0yacgRzIT5OWOFLBmkHlk/KZUldVb7wAyy1HEyjJU8RHlb2fT9dPO4nRTjz0ndLp1/rysez6pfrpVnPfOrSLawyTMiDLsIkZyqg4BYhcKCRyRXoSfLFy7Jv7jkS5mo93Y8Yk8a+PNQH2jS9Cjht+oW6f96R67WntmBPp5Z9s9a8/wBrXlrCkkvPf81+R1+zpLSU9fLb8ma/gP4pHxJevomrWx07VIg2Izu2yFBl1CuA6Oq/NsJYFAWDcYq6OI9pL2c1yzXTv/kyKlLkXPF3ieo6lqNvpFrLfXbiKC3RpJGPZVGeB1JPRQOWJAAJIrtlJQTlLRLVnOk5NRW7PBLL4p+KfFc0knhjSY5rKFtu+diGOOcbzNDEHIIJjXzCuRknIJ8xYirVbdGCcV3/AM7pfLU7XRhTVqkrPy/4Znmfxe8XHxPHYQ3Vu9hqFi93HdWsmSULi1Mbq2BujkCsVOOx6rtduPE1PaKKacZR5k0+nw2+TOijDk5mneLtZ/efatfQnkHz/wD8LB8V+Dvk8U6Ybq3XreWeMY/vNt3RZPZW+z/SvL9tVo/xoXX80f6t+R3ezp1P4UrPs/6v+Z6F4d+Jvh/xNhLW6SKZv+WFx+5kyewDHa5/65u9dUK9Op8MrPs9H/XoYSpThutO61O+rqMAoAKACgAoAKACgDjvH/8AyAbv/cX/ANGJXXhv4sPV/kzCt/Dl/XU87+DX+tvPpb/zmrlzzaj/ANxP/bDbLP8Al5/27/7cfVul/dFfGH0Z0AoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/8AVt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAbOnf6s/739BQBfoAKACgAoAKACgAoAKACgAoAKACgAoA+Fv2sf+Qxp3/Xm//o5qAPlCgD9Bf2Wf+RTn/wCwnP8A+k9pQB9J0AFAHhH7Qn/IBtv+v+P/ANJ7mvpsl/3if/Xp/wDpUDxcy/hR/wAa/wDSZHI/Cf8A5Azf9fMn/oMde7jP4v8A26vzZ5mH+D5v9D02vOOsKACgAoAKACgDz74lahrum6T53hqNpbvzlV9kYldISkhZ0jOdzBxGPuvwx+XuOWu6kYXoq8r66X0s+n3G9JRcrVNFb01Pmzw42h+Jbrd451K++2qxHkXIaKBTn7vmguUXHJG21CngZ6nyIezqP/aZy5uz0X36/wDtp6EuaC/cxVu63+7/AIc+sfDmiaNpNuG0OG2jhccSQbW8wepmBZpPqzt9a9yEIQX7tJLuuvz6nmSlJv327+f+R0damZ5f8Zv+RRv/APt2/wDSy3rjxX8GXy/9KR00P4kfn+TKnwRs47XwrbSxgB7mS4kkPdmWeSEE/RIlH4VOESVJNdW2/va/Qdd3qNdrflf9Tzj9opRbz6VdR8S4uhuHXEbWzJz7F2I+prkxujhJb6/hb/M3w2qkvT9TufjzfSWfhry4yQLq6hhfH9wLJNj6Folz+VdOMbVKy6yS/N/oY4dXn6Jv9P1OK8G+P9X8P6Pa2Nl4avriGOIETx+eFmL/ADmYbbJxiQtuGHYYIAYjFc1KtOnCMY0ZNJbq+t+vw9TadOMpNuok+2mnluYPxF1nXfH9rDbnw7qFnLbSmRZfLuJTtZCrx7fskWAx2MTuP3AMc5GdeVSukvZSTT3s38vhX9IulGNJt+0i79NF+p9HWmuR6H4ettT1tmtvKs7drjzFYSLK0SBkKEb/ADDIduzG7dwRmvWU+Smp1NLRV773svxucDjzTcYa6u33nmC/G+fUWY6Jol9qEKnG9SwP4rFBcAH23VxfW3L+HTlJf12TOj2Cj8c0n/Xdo8xv/EV3q3jrS9QudPm0a4kls4mhm375FadojL88MDbWRvK+6R+7I3HoONzcq8JuDg7xVn11tfZdNPkdKio0pRUlJWeq6aXtu/U9f+Pl3JbeGhGhIW4vIYnx3ULLLg+2+JT9QK78Y7UrLrJL83+hy4dXn6J/ov1O1+G9jFp3hrTo4QAHtIpmx3edRK5Pvuc/y7V00Eo0oJfyp/fqY1Xecr92vu0PB/2jLCKK70+8UASzxTxuR1KwtEyZ+nnMM+nHavMxyScJdWmvut/mduGekl2t+P8Awx9X17Z5gUAePePfC3gnY0+ufZ9PmYEiSFhFO3qwijDecfdoZDXBWp0N6lovutH9y3+5nVTnV2hdrz1X39PvPCtC8Qa9YXxs/BFxf6rZIQAlzb7olH907ncRp0+fNsSeNo6nzYTqRly4ZylHs1p/wPXQ7ZRg1eslF+T/AK/U+1q+hPICgAoAKACgAoA47x//AMgG7/3F/wDRiV14b+LD1f5Mwrfw5f11PO/g1/rbz6W/85q5c82o/wDcT/2w3yz/AJef9uf+3H1bpf3RXxh9EdAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf/AFbf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKAPhb9rH/kMad/15v/6OagD5QoA/QX9ln/kU5/8AsJz/APpPaUAfSdABQB438dbFrvw00qjP2S5hmP0O+HP5zCvoMomoYpRf2oSj+Uv/AG08nMI81G6+zJP81+p5b8H71Xsbi0z88U4kx/syIqj9Y2/Ovp8bG04y6NW+5/8ABPFwz91x7O/3/wDDHr1eUdwUAFABQAUAFABQBz+ueFdJ8SJs1S1iueMBmXEij/ZlXbIv/AWFZTpwqaTin+f37lxnKHwtr+ux5Nc/Bu50SQ3XhDU7jTpCc+TKxaFj2BZR90ekkU31rheFcPeoTcX2e39eqZ1KupaVYp+a3/r7jqfBOp+LPtr6Z4ntohGkDSR3sONsjq8ahG2EoGZXZgNkTYQ/IRkjalKtzOFaKta6kuuq+X5GdRU7c1N9dn0/r5h8Zv8AkUb/AP7dv/Sy3p4r+DL5f+lIKH8SPz/Jh8Gf+RRsP+3n/wBLLijC/wAGPz/9KYV/4kvl+SPL/wBpH/mFf9vv/tpXFjvsf9vf+2nRhftfL9T2j4i+FW8YaJNp0RAuAVlgLcDzY+QCewdSyZ7bs9sV6Fen7WDgt916r+rHJSn7OSl02foeReA/ipb+FbRfDvimOaxuLDMSSGJ2BjBO1XVQXBUfKrKrI6BTnPXho4hUl7KsnFx0vbodVSi5vnp2aZ2N/wDHDQI8R6YLjVLl+I4oIZE3N2BMqo3P+yjn/ZNbvF01pC8n0ST/AF/yZkqE/tWivN/5D/jhpV1qnhxvsas5triOeVVBJMSrIjHA5IUurt6KpboKeLi5U/d6NN+mv+dxUGoz16q3zOc8D/F/w3peh2tldu9pPZwJE0QhkcOyDDOjRqyfvTlzvKHcxz6nGjiaUacYy0aVrWevnp3NKlGbk2tU33PNdd1m68QeN9I1K4he1hubiwa0jk4k+yi8KI7j+EySLJIByNrLgsMMeScnOvTm1ZNx5U9+Xm6+ruzojFQpSindpSv62Po/4meF5PFugz2NuM3KFZ4AeN0keTsyeAXQugJIAZgScZr1q9P2tNxW+69V/VjgpT9nJN7bM8r+HXxb07Q9MTRfEJlsrnT8whmikYMik7VZUVnSSMfIVZQMKDuySBxUMTGEfZ1bxcdNn+mzWx01aLlLnp6p67nmXxc8Sy+Lri21OKKSHS8TQWbSDa0zRmNp5QvZCZI0XrnYc4YMq8eJqOq1NJqGqjfra13+KOijH2acb+9o35dkfcFfRnjnz/5XxC8bffaLw5ZP2XIuCp+haYMPQtbZ9K8u2Irdqcfx/wA/yO79zT/vv8P8vzN7Q/gpoenP9p1Iy6tdE7me5Y7C3r5an5s9xK8tawwkI6zvN+f+X+dzOVeT0j7q8v6/Kx61a2kNjGILaNIYk4VI1VEUegVQAPwFdySirJWXZaHM23qyxTEFABQAUAFABQB578Tr1bTQ5YycNcvHGv4OJD/46h/Ou/CRvVT7Jv8AC36nLXdoNd7L9f0OY+DlsUiubjtJJGg/7ZqzH/0YK8vO5pzpU+sYyl/4E0v/AG07ssjaM592l9yb/wDbj6h0v7or5I946AUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAEU/8Aq2/3T/KgDnKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKANnTv9Wf97+goAv0AFABQAUAFABQAUAFABQAUAFABQAUAfC37WP/ACGNO/683/8ARzUAfKFAH6C/ss/8inP/ANhOf/0ntKAPpOgAoAy9b0qLXLGfTp/9XdRPET1K7gQGHupwy+4FbUqjoVI1Y7xaf3dPnsZ1IKpCVN7NNfefC+iXtx8Ptde3vlKiJ2t7lR3TIIdfUD5ZEP8AEhwOGr9Pko4yip03ulKL8+z/ABT7P0Pio3w1Rxn0dn/n+q8j6fgnjuY1mhYPG4DKynIKkZBB9CK+dacXZ6NHrJ31WxLSGFABQAUAFABQAUAFABQBVvbG31KFra8ijuIHxuilRZI22kMu5HBU4YBhkcEAjkCpaUlaSTXZ6oabjqnZ+QWVjb6bCttZxR28EedsUSLHGu4lm2ogCjLEscDkkk8k0JKKtFJLstEDberd35lXUtD0/Wdn9o2tveeVu2faIY5dm7G7b5itt3bV3YxnaM9BSlCM/jinba6T/Mak4/C2vR2NSrJM6/0ix1UBb63gugvQTRJKB9N6tiocYy+JJ+qTKTcfhbXo7DbDRbDSc/Yba3tc8HyYY4s/XYq0RhGHwpL0SX5A5N7tv1Zp1ZJhjwzpCzfahY2gnzu837PD5mfXfs3Z985rP2cL35Y372Vy+aVrXdu12WLrQ9PvbhL25tbea5h2+VNJDG8sexi6bJGUumxyWXaRtYlhgnNNwi2pOKbWzaV18xKTSsm0u19DUqyTHvPD+majKJ7y0tbiUdJJYIpHGOmGdS3H1rNwjJ3lFN92ky1KUdE2l5Njr/QdN1UIt9aW10sAIiE0EUojDbdwQOrBAdq524ztXPQU3CMrc0U7bXSdvQSlKPwtr0djWqyQoAKACgAoAKACgAoAKAEJAGTwBQB8y/EHxJ/wkt+lrZ5kt7cmOPbz5srEBmXHUEgKnqAWH3q+hw9P2EHOpo2ru/RLXX83/wAA8itP2slGGqWi82/60PcvBWjf2LZQ2n8ajdIR3kY7m+oBO0H0Ar87xlf61WnW6N2j/hWi+/d+bZ9fh6XsKcafVK79Xq/8vQ9m01NqiuA6jboAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/8AVt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAbOnf6s/739BQBfoAKACgAoAKACgAoAKACgAoAKACgAoA+Fv2sf+Qxp3/Xm//o5qAPlCgD9Bf2Wf+RTn/wCwnP8A+k9pQB9J0AFABQB4v8VvhoPFsQ1DTwqalAuMHAW4QZIRj0Dr/wAs3PHOxzt2sn0GXY/6o/ZVbulJ/OD7ry7r5rXR+Ti8L7dc9PSov/Jl29ez+T8vnDw94w1LwVM1hdRs0MbESW8uUeNu+wkZQ9ypBVuuATur7SpRp4mKqU2tVpJaprz7/mfOQqToNwknpuno0e0aZ8Q9E1JQfPFu56pOPLI/4Ecxn8HNeTPDVYfZuu61/Df8DvjWhLrb10/4BvDxHpZ5F5a/+BEX/wAXWPsqn8kv/AX/AJGnPH+Zfeg/4SLS/wDn8tf+/wDF/wDF0vZVP5Jf+Av/ACHzx/mX3oP+Ei0v/n8tf+/8X/xdHsqn8kv/AAF/5Bzx/mX3oP8AhItL/wCfy1/7/wAX/wAXR7Kp/JL/AMBf+Qc8f5l96D/hItL/AOfy1/7/AMX/AMXR7Kp/JL/wF/5Bzx/mX3oP+Ei0v/n8tf8Av/F/8XR7Kp/JL/wF/wCQc8f5l96D/hItL/5/LX/v/F/8XR7Kp/JL/wABf+Qc8f5l96D/AISLS/8An8tf+/8AF/8AF0eyqfyS/wDAX/kHPH+Zfeg/4SLS/wDn8tf+/wDF/wDF0eyqfyS/8Bf+Qc8f5l96D/hItL/5/LX/AL/xf/F0eyqfyS/8Bf8AkHPH+Zfeg/4SLS/+fy1/7/xf/F0eyqfyS/8AAX/kHPH+Zfeg/wCEi0v/AJ/LX/v/ABf/ABdHsqn8kv8AwF/5Bzx/mX3oP+Ei0v8A5/LX/v8Axf8AxdHsqn8kv/AX/kHPH+Zfeg/4SLS/+fy1/wC/8X/xdHsqn8kv/AX/AJBzx/mX3oP+Ei0v/n8tf+/8X/xdHsqn8kv/AAF/5Bzx/mX3oP8AhItL/wCfy1/7/wAX/wAXR7Kp/JL/AMBf+Qc8f5l96D/hItL/AOfy1/7/AMX/AMXR7Kp/JL/wF/5Bzx/mX3oP+Ei0v/n8tf8Av/F/8XR7Kp/JL/wF/wCQc8f5l96D/hItL/5/LX/v/F/8XR7Kp/JL/wABf+Qc8f5l96D/AISLS/8An8tf+/8AF/8AF0eyqfyS/wDAX/kHPH+Zfeg/4SLS/wDn8tf+/wDF/wDF0eyqfyS/8Bf+Qc8f5l96D/hItL/5/LX/AL/xf/F0eyqfyS/8Bf8AkHPH+Zfeg/4SLS/+fy1/7/xf/F0eyqfyS/8AAX/kHPH+Zfeg/wCEi0v/AJ/LX/v/ABf/ABdHsqn8kv8AwF/5Bzx/mX3oP+Ei0v8A5/LX/v8Axf8AxdHsqn8kv/AX/kHPH+Zfeg/4SLS/+fy1/wC/8X/xdHsqn8kv/AX/AJBzx/mX3oP+Ei0v/n8tf+/8X/xdHsqn8kv/AAF/5Bzx/mX3oP8AhItLH/L5a/8Af+L/AOLo9lU/kl/4C/8AIXPH+ZfejJv/AB5omnKS11HKR0WE+aT7AplR/wACYD3raOHqy2i166fmQ60I9V8tTxrxV8RbrxCDZWKtbWz/ACkDmWUH+Fiv3VPTYuc9CzA4r1qWGjR9+o02tb7Jef8AwWcFSs6nuwVk/vf9djo/Avgh7Jl1C/XE3/LKI/8ALPP8T/7eOg/g6n5uF+WzLMVWTw2Hfufal/N5L+73fX039vB4N0/31Ze99mPbzfn5dPXb37SrM5BxXyp7p31rHsUUAXaACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf8A1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKAPhb9rH/AJDGnf8AXm//AKOagD5QoA/QX9ln/kU5/wDsJz/+k9pQB9J0AFABQA1lyKAOA8W+BtM8UJ/p0IaRRhZU+SVfo46j/ZYMuedua7sPi62Ed6MrLrF6xfy/VWfmctXD066/eLXo1o18/wBHoeBat8EJIWJsboFeyzJgj6uhwf8Av2tfS087W1alr3g/0f8A8kzx55Z/z7n8pL9V/kcw/wAItWQ4822/76l/+NV1f21Q/kqfdH/5M5/7Nq/zQ++X/wAiR/8ACp9VH/LW2/76l/8AjNP+2sP/ACVfuj/8mH9m1f5offL/AORE/wCFT6r/AM9bb/vqX/4zR/bWH/kq/dH/AOTD+zav80Pvl/8AIh/wqfVf+ett/wB9S/8Axmj+2sP/ACVfuj/8mH9m1f5offL/AORD/hU+q/8APW2/76l/+M0f21h/5Kv3R/8Akw/s2r/ND75f/Ih/wqfVf+ett/31L/8AGaP7aw/8lX7o/wDyYf2bV/mh98v/AJEP+FT6r/z1tv8AvqX/AOM0f21h/wCSr90f/kw/s2r/ADQ++X/yIf8ACp9V/wCett/31L/8Zo/trD/yVfuj/wDJh/ZtX+aH3y/+RD/hU+q/89bb/vqX/wCM0f21h/5Kv3R/+TD+zav80Pvl/wDIh/wqfVf+ett/31L/APGaP7aw/wDJV+6P/wAmH9m1f5offL/5EP8AhU+q/wDPW2/76l/+M0f21h/5Kv3R/wDkw/s2r/ND75f/ACIf8Kn1X/nrbf8AfUv/AMZo/trD/wAlX7o//Jh/ZtX+aH3y/wDkQ/4VPqv/AD1tv++pf/jNH9tYf+Sr90f/AJMP7Nq/zQ++X/yJBc/DHULKNp7ie0iiTlnd5FUZOOSYsDkgUf21h/5Kv3R/+TD+zav80Pvl/wDImN/wiS/9BHTf/Ahv/jdH9tYf+Sr90f8A5MP7Nq/zQ++X/wAiWbTwNJfyCC2vtPmkOSESZ2YgDJwBFngcmj+2sP8AyVfuj/8AJh/ZtX+aH3y/+RNf/hU+q/8APW2/76l/+M0f21h/5Kv3R/8Akw/s2r/ND75f/Ih/wqfVf+ett/31L/8AGaP7aw/8lX7o/wDyYf2bV/mh98v/AJEP+FT6r/z1tv8AvqX/AOM0f21h/wCSr90f/kw/s2r/ADQ++X/yIf8ACp9V/wCett/31L/8Zo/trD/yVfuj/wDJh/ZtX+aH3y/+RD/hU+q/89bb/vqX/wCM0f21h/5Kv3R/+TD+zav80Pvl/wDIh/wqfVf+ett/31L/APGaP7aw/wDJV+6P/wAmH9m1f5offL/5EP8AhU+q/wDPW2/76l/+M0f21h/5Kv3R/wDkw/s2r/ND75f/ACIf8Kn1X/nrbf8AfUv/AMZo/trD/wAlX7o//Jh/ZtX+aH3y/wDkQ/4VPqv/AD1tv++pf/jNH9tYf+Sr90f/AJMP7Nq/zQ++X/yIf8Kn1X/nrbf99S//ABmj+2sP/JV+6P8A8mH9m1f5offL/wCRD/hU+q/89bb/AL6l/wDjNH9tYf8Akq/dH/5MP7Nq/wA0Pvl/8iH/AAqfVf8Anrbf99S//GqP7aw/8lT7o/8AyYf2bV/mh98v/kTRtPhJcE5urhFHcRozE/ixTH12n6VzTzuK/hUm3/eaX4K/5o2jlkvtzS9Ff87fkej6F4GsdEIaCMvL/wA9ZPmf8OAF/wCAqM98187iMdXxelSVofyx0j8+r+bZ69HC0qGsFeX8z1f+S+SR6DY6WcjivMO07SxshGBxQBtqu0UAOoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/wDVt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAbOnf6s/739BQBfoAKACgAoAKACgAoAKACgAoAKACgAoA+Fv2sf8AkMad/wBeb/8Ao5qAPlCgD9Bf2Wf+RTn/AOwnP/6T2lAH0nQAUAFABQAxkDUAUJrMP2oAypNKB7UAVjpA9KAE/scelAB/Y49KAD+xx6UAH9jj0oAP7HHpQAf2OPSgA/scelAB/Y49KAD+xx6UAH9jj0oAP7HHpQB538WLL7D4W1CccbI4z+c8Q/rQB8Hf2wfWgD1j4KXX9oeKbeA87o7g/lC5oA+3f7HHpQAf2OPSgA/scelAB/Y49KAD+xx6UAH9jj0oAP7HHpQAf2OPSgA/scelAB/Y49KAD+xx6UAH9jj0oAUaQB2oAsxaUF7UAasNmI+1AF9UC0APoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf8A1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKAPhb9rH/AJDGnf8AXm//AKOagD5QoA/QX9ln/kU5/wDsJz/+k9pQB9J0AFABQAUAFABQAm0UAJsFABsFABsFABsFABsFABsFABsFABsFABsFABsFABsFABsFAHk3xyUL4J1QjtFF/wClENAH5i7zQB7n+zmS3jW0B/543X/pO9AH6QbBQAbBQAbBQAbBQAbBQAbBQAbBQAbBQAbBQAbBQAbBQAbBQAbBQAu0CgBaACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf8A1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKAPhb9rH/AJDGnf8AXm//AKOagD5QoA/QX9ln/kU5/wDsJz/+k9pQB9J0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAeTfHT/kSNV/65Rf8ApTDQB+YFAHun7OP/ACO1p/1xuv8A0negD9JKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/9W3+6f5UAc5QAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBs6d/qz/AL39BQBfoAKACgAoAKACgAoAKACgAoAKACgAoA+Fv2sf+Qxp3/Xm/wD6OagD5QoA/QX9ln/kU5/+wnP/AOk9pQB9J0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAeTf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oAKACgAoA2dO/wBWf97+goAv0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAHg37SX/ACJdx/18Wv8A6NFAH5wUAfSv7LH/ACNdx/2DJ/8A0otKAP0DoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPnf43/wDHzZf9c5v/AEJK+Pzj4qXpL80enhtpeqOw8K/8gm0/64R/yoofw4f4UEvifqb9dBAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAHmnxS/5BsP/Xyv/ouWvMxvwL/F+jN6W79Bnw4/48V/66P/ADFe/lX+7L/FI48R8fyR7tY/d/CvcOQ0aACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAin/1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDwb9pL/kS7j/r4tf/AEaKAPzgoA+lf2WP+RruP+wZP/6UWlAH6B0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAHzv8b/+Pmy/65zf+hJXx+cfFS9Jfmj08NtL1R2HhX/kE2n/AFwj/lRQ/hw/woJfE/U366CAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPNPil/wAg2H/r5X/0XLXmY34F/i/Rm9Ld+gz4cf8AHiv/AF0f+Yr38q/3Zf4pHHiPj+SPdrH7v4V7hyGjQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAEU/8Aq2/3T/KgDnKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKANnTv9Wf97+goAv0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQ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ANW3+6f5UAc5QAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBs6d/qz/vf0FAF+gAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgD54+N/8Ax8WP/XOb/wBCjr4/OPipekvzR6WG2l8v1Ou8Kf8AIItP+uCfyoofwof4UOfxP1OgroICgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoA8z+KX/IOh/wCvkf8AouSvMxvwR/xfozelu/QT4cf8eK/9dH/mK9/K/wDdl/il+Zx4j4/kj3Wx+6K9w5DRoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgCKf8A1bf7p/lQBzlABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGzp3+rP+9/QUAX6ACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAPnj43/wDHxY/9c5v/AEKOvj84+Kl6S/NHpYbaXy/U67wp/wAgi0/64J/Kih/Ch/hQ5/E/U6CuggKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDzP4pf8g6H/AK+R/wCi5K8zG/BH/F+jN6W79BPhx/x4r/10f+Yr38r/AN2X+KX5nHiPj+SPdbH7or3DkNGgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAIp/wDVt/un+VAHOUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAbOnf6s/739BQBfoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAK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mhpa59M+FdYudf0yHUL20l0yebzN9rNu8yLZK8a7t8cTfOqiQZjX5XGMjDHzpxUJOMXzJdV6fM3TurtWOhrMoKACgAoA8W+KWoq80FihyYlaV/YvgIPYgKx+jA14uNndxprpq/nsdVJbs67wRaG0sYIzwSu8/VyW/QHH4V9jgafssPTg97cz/wC3m5frY8uq+acn52+7Q9ksRhRXomJoUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP8A6tv90/yoA5ygAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgDZ07/Vn/e/oKAL9ABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAGXrelRa3ZTWE/3J0Kk91PVWHujAMPcCsK1KNenKjPaSt6dn8nqXGTg1JdD5P0y8uvAWrPBdKcKfLnQdHTOVkTOAeMOh4yCV43HH56ufBVXCotnaS7ro1+aPZ0qxTj8j6Cs72HUIVuLZxJFIMqw/ke4I6EHBB4IzXvRkppSi7pnI1bRlmrEFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAYev6/b+HrczzkFzkRxg/NI3oPQD+Juij1JAOFWrGjHmlv0XdlRi5OyPAtOt5/E+otc3PzBn8yY9sfwoPYgBQOyg+leZhKEsbX5p/AnzTfS3SPz29L9jepNUoWW+y/wAz6B0eHGOK/Qjxj0a0XaooAt0AFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQBFP/q2/3T/KgDnKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKANnTv8AVn/e/oKAL9ABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQB59448E2/imEP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)


## Crear un documento HTML


Las sentencias de JavaScript con las que vamos a trabajar tenemos que escribirlas dentro del elemento `<script>`, el mismo tiene que estar al final del elemento `<body>`, justo antes del cierre del mismo para que pueda acceder a los objetos de los elementos como el `head`, `body`, `h1`, etc.


```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    </meta>
    <title>Ejemplo DOM con JavaScript</title>
</head>

<body>
    <h1>Ejemplo DOM con JavaScript</h1>
    <p>Saludos!</p>

    <script>
        // aquí van las sentencias de Javascript
    </script>

</body>

</html>
```

## Acceder a elementos del DOM


Para acceder a los elementos del DOM, como objetos, por lo general les damos un `id` con la sentencia `id='nombreId'`. Después, el el código JavaScript, buscamos este elemento por su `id`.


```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Ejemplo DOM con JavaScript</title>
</head>

<body>
    <h1 id='ejemplo1_h1'>Ejemplo DOM con JavaScript</h1>
    <p id='ejemplo1_p'>Saludos!</p>
</body>

</html>
```

```js
/** para acceder al elemento usamos, del objeto document, el método getElementById
 * pasando como argumento el id que le dimos al elemento. Esta sentencia nos
 * devuelve un objeto cuya referencia se guarda en la variable cabecero
 * podemos decir que nos regresa todo el elemento h1 */
let cabecero = document.getElementById('ejemplo1_h1');

/** para acceder al texto que muestra el elemento h1 con id cabecero utilizamos 
 * el metodo get innerHTML que nos devuelve el String */
console.log('valor cabecero:' + cabecero.innerHTML);

/** podemos llegar al mismo resultado sin guardar la referencia en la variable */
console.log('valor cabecero:' + document.getElementById('ejemplo1_h1').innerHTML);

let parrafo = document.getElementById('ejemplo1_p');

/** tambien podemos utilizar template literal a la hora de dar formato al texto
 * de una salida o acceder a los valores de los atributos de un elemento */
console.log(`valor parrafo: ${parrafo.innerHTML}`);
```

## Modificar elementos del DOM


Podemos modificar el el texto que muestra un elemento HTML, modificando el valor del atributo innerHTML que corresponde a ese elemento.


```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Ejemplo DOM con JavaScript</title>
</head>

<body>
    <h1 id='ejemplo2_h1'>Ejemplo DOM con JavaScript</h1>
    <p id='ejemplo2_p'>Saludos!</p>
</body>

</html>
```

```js
/** asignamos a la variable parrafo la referencia al objeto del elemento con
 * id parrafo */
let parrafo = document.getElementById('ejemplo2_p');

/** mediante el método set del atributo innerHTML modificamos el valor del texto
 * del elemento cuya referencia guardamos en la variable parrafo */
parrafo.innerHTML = 'Nuevo valor para el párrafo';
```

## Método getElementByTagName


En HTML los `id` no pueden repetirse. Si necesitamos identificar varios elementos del mismo tipo o con la misma etiqueta o tag podemos utilizar el método `getElementByTagName()`.


```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Ejemplo DOM con JavaScript</title>
</head>

<body>
    <h1 id='cabecero'>Ejemplo DOM con JavaScript</h1>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento N</li>
    </ul>
</body>

</html>
```

```js
/** si existe más de 1 elemento con el mismo tag el método getElementsByTagName
 * devuelve un array de objetos correspondientes a ese elemento */
let elementos = document.getElementsByTagName('li');

/** mostramos el número de elementos que son de tipo párrafo */
console.log(`No. elementos de la lista: ${elementos.length}`);

/** recorremos el array de párrafos para poder trabajar con los atributos de 
 * cada uno */
for (let i = 0; i < elementos.length; i++) {
    console.log(`${i} - ${elementos[i].innerHTML}`);
}
```

## Método `getElementByClassName`


Podemos utilizar el método `getElementByClassName()` para recuperar todos los elementos que tengan el mismo nombre de clase de css.


```html
< !DOCTYPE html >
	<html>
		<head>
			<meta charset="UTF-8">
				<title>Ejemplo DOM con JavaScript</title>
				<style>
					.azul{
						color: blue;
        }
				</style>
		</head>
		<body>
			<h1 class='azul'>Ejemplo DOM con JavaScript</h1>
			<p class='azul'>Saludos!</p>
			<p class='azul'>Otro parrafo</p>
		</body>
	</html>
```

```js
/** asignamos a la variable elementos un array de referencias a objetos que 
 * con la clase css azul, es decir class='azul'. Estos elementos pueden ser
 * de distinto tipo cono h1 p o a */
let elementos = document.getElementsByClassName('azul');
console.log(`No. elementos: ${elementos.length}`);

for (let elemento of elementos) {
	console.log(`${elemento.innerHTML}`);
}
```

## Método `querySelectorAll`


Utilizando el método `querySelectorAll()` además de indicar la clase de los elementos que vamos a seleccionar podemos indicar el tipo de elemento. Para hacerlo utilizamos la notación de css de `elemento.clase`.

```html
<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<title>Ejemplo DOM con JavaScript</title>
	<style>
		.verde {
			color: green;
		}
	</style>
</head>

<body>
	<h1 class='verde'>Ejemplo DOM con JavaScript</h1>
	<p class='verde'>Saludos!</p>
	<p class='verde'>Otro parrafo</p>
	<script>

	</script>

</body>

</html>
```

```js
/** en el ejemplo recuperamos la referencia a los elementos de tipo parrafo p
 * que tienen la clase azul */
let elementos = document.querySelectorAll('p.verde');

console.log(`No. elementos: ${elementos.length}`);
for (let elemento of elementos) {
	console.log(`${elemento.innerHTML}`);
}
```

## Manejo de formularios

Al formulario le damos un id para poder referenciar e iterar sobre sus elementos luego. Utilizamos el evento `onclick()` para indicar que, al hacer click sobre el botón donde esta definido el evento, se llame a una función.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ejemplo Formulario con JavaScript</title>
</head>
<body>
    <form id='ejemplo3_form'>
        Nombre: <input type="text" name='nombre' value='Juan'/>
        <br/>
        Apellido: <input type='text' name='apellido' value='Perez'/>
        <br/>
    </form>

    <!-- mediante el evento onclick, al hacer click sobre el botón, se llama a la función mostrarValores -->
    <button onclick='mostrarValores()'>Mostrar</button>

    <div id='ejemplo3_div'></div>

    <script>
        function mostrarValores() {

        /** document.forms es un array con todos los formularios del documento
        * para acceder al formulario específico sobre el que vamos a trabajar
        * utilizamos la id que le asignamos en el HTML */
        let formulario = document.forms['ejemplo3_form'];            
        let texto = '';            
        for (let elemento of formulario) {

            /** el valor asignado al atributo value de cada elemento del formulario
            * lo vamos concatenando al texto en la variable texto, luego hacemos un
            * salto de línea con <br/> */          
            texto += elemento.value + '<br/>';                
        }

        /** el texto en el elemento tipo div con id valores, que empieza vacío
        * se modifica con el valor de la variable texto, que recuperó todos los
        * valores de los atributos value de los elementos del formulario */
        document.getElementById('ejemplo3_div').innerHTML = texto;            
    }    
    </script>

</body>
</html>
```

## Manejo individual de elementos del formulario

Para acceder a un elemento en particular de un formulario podemos utilizar su atributo `name`.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ejemplo Formulario con JavaScript</title>
</head>
<body>
    <form id='ejemplo4_form'>
        Nombre: <input type="text" name='nombre' value='Juan'/>
        <br/>
        Apellido: <input type='text' name='apellido' value='Perez'/>
        <br/>
    </form>
    <button onclick='mostrarValores()'>Mostrar</button>
    <div id='ejemplo4_div'></div>
    
    <script>
        function mostrarValores(){
            let formulario = document.forms['ejemplo4_form'];            
            let texto = '';

            /** en la variable formulario tenemos la referencia al array de elementos del
            * formulario que capturamos mediante su id. Podemos acceder a un elemento en
            * particular desde su atributo name. En el ejemplo accedemos a input con 
            * atributo name='nombre' */
            let nombre = formulario['nombre'];
            
            let apellido = formulario['apellido'];

            /** con al referencia del elemento del formulario en la variable nombre y
            * apellido podemos acceder a sus atributos value */
            texto = nombre.value + '<br/>' + apellido.value;
            
            document.getElementById('ejemplo4_div').innerHTML = texto;            
        }        
    </script>
</body>
</html>
```

## Método `write`

Mediante el método `write`, cuya sintaxis es `document.write()`, podemos imprimir texto directamente en el flujo de información que muestra el documentos HTML. Esto sobrescribe por completo la información que se estaba mostrando hasta antes de ejecutar el método.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1>Manejo DOM con JavaScript</h1>
    <button onclick="mostrar()">Mostrar</button>
    <br/>
    <script>
    
        /** al cargar por primera vez la página se muestra este mensaje */
        _document.write('Saludos desde JavaScript'); // no ejecutar, borra los markdown de la notebook

        /** al tocar el el botón mostrar se sobreescribe todo lo que había en el
        * el documento y se reemplaza con lo que pasamos como argumento al método */
        function mostrar() {
        _document.write('Adios'); // no ejecutar, borra los markdown de la notebook
        }        
    </script>
</body>
</html>
```

## Cambio de estilo CSS en el DOM

En el caso de los estilos de css cada elemento HTML tiene como atributo un objeto style, que a su vez tiene como atributo los distintos modificadores de estilo disponibles, es decir que asignado un nuevo valor a, por ejemplo, `document.elementBy...().style.color = 'red'` modificamos el color de fuente de ese elemento.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id='ejemplo5_h1'>Manejo DOM con JavaScript</h1>
    <button onclick="mostrar()">Mostrar</button>
    <br/>
    <script>
    
        /** al tocar en el boton mostrar el color del elemento con id titulo cambia a
        * rojo por el modificador de estilos css color = 'red' */
        function mostrar() {
            document.getElementById('ejemplo5_h1').style.color = 'red';           
        }        
    </script>
</body>
</html>
```

# Manejo de eventos en el DOM

Los eventos de JavaScript se indican en el elemento HTML. siempre empieza con on y luego el evento que sucede, por ejemplo, `onclick`. Cada elemento HTML se corresponde con un objeto del tipo del elemento, por ejemplo, un elemento HTML h1 se corresponde con un objeto en JavaScript del tipo de h1 que es un título. Al ser objetos tienen atributos y métodos. Cuando trabajamos dentro de los métodos del objeto, con atributos del propio objeto, utilizamos la palabra reservada `this` para indicar que es sobre un atributo o método del mismo. En el caso de los elementos HTML, por ser objetos, sucede lo mismo, si trabajamos sobre atributos o métodos del objeto dentro del mismo objeto utilizamos `this` para indicarlo.

```html
<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<title>Manejo DOM con JavaScript</title>
</head>

<body>

	<!-- en el evento onclick indicamos que el texto del elemento donde estamos ubicado se modifique
    por Nuevo título. this está apuntando al elemento h2 donde se encuentra, es decir que con this 
    podemos trabajar sobre los atributos y métodos de ese elemento h2 -->
	<h2 onclick="this.innerHTML='Nuevo título'" id='titulo'>Manejo DOM con JavaScript 1</h2>

	<!-- paramos el elemento h2 como argumento de la función cambiarTexto mediante this  -->
	<h2 onclick="cambiarTexto(this)">Manejo DOM con JavaScript 2</h2>
	<br />
	<script>
		function cambiarTexto(titulo) {
			console.log(titulo);
			console.log(titulo.innerHTML);
			titulo.innerHTML = 'Cambiamos el título';
			console.log(titulo.innerHTML);
		}          
	</script>
</body>

</html>
```

## Asociar eventos a elementos

Podemos asociar un evento a un elemento desde el documento HTML. También podemos asociar un evento a un elemento desde el código JavaScript.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id='ejemplo6_h1'>Manejo DOM con JavaScript</h1>
    <br/>
    <div id='ejemplo6_div'></div>
    <script>
    
        /** recuperamos la referencia al objeto del elemento mediante su id. Luego
        * asignamos al evento onclick el valor cambiarTexto, que es el nombre de la
        * función de tipo callback que tiene que ejecutarse cuando se cumpla ese evento */
        document.getElementById('ejemplo6_h1').onclick = cambiarTexto;

        function cambiarTexto() {          
        document.getElementById('ejemplo6_div').innerHTML = 'Nuevo contenido';            
        }        
    </script>
</body>
</html>
```

## Manejo de evento `onload`

Un evento `onload` se ejecuta cuando se carga el documento HTML.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body onload="entrar()">
    <h1 id='ejemplo7_h1'>Manejo DOM con JavaScript</h1>
    <br/>
    <div id='ejemplo7_div'></div>
    <script>
        function entrar() {

            /** mediante alert desplegamos una ventana emergente mostrando un mensaje */
            alert('Entrando a la página web');

            let texto = '';

            /** navegator es un objeto de JavaScript que tiene atributos y métodos
            * relacionados con el navegador web que estamos utilizando para visualizar
            * el documento HTML */      
            if (navigator.cookieEnabled) {              
                texto = 'Cookies están habilitadas';                
            }            
            else {              
                texto = 'Cookies están inhabilitadas';                
            }            
            document.getElementById('ejemplo7_div').innerHTML = texto;            
        }        
    </script>
</body>
</html>
```

## Manejo de evento `onchange`

Por lo general utilizamos el evento `onchange` cuando modificamos los valores de un campo de texto o los elementos de un formulario.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id=''>Manejo DOM con JavaScript</h1>
    <br/>

    <!-- cuando hagamos una modificación sobre el input de texto el evento onchange 
    llama a la función convertir enviando como argumento el mismo elemento -->
    Nombre: <input type="text" onchange="convertir(this)"/>
    
    <script>
        function convertir(nombreInput) {

            /** convertims en mayúsculas el contenido de la caja de texto que se encuentra
            * en el atributo value */
            nombreInput.value = nombreInput.value.toUpperCase();            
        }        
    </script>
</body>
</html>
```

## Eventos `onmouseover` y `onmouseout`

Los eventos `onmouseover` y `onmouseout` responden a las acciones colocar el mouse sobre un elemento y sacar el mouse de ese elemento.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id='' onmouseover="rojo(this)" onmouseout="azul(this)">
        Manejo DOM con JavaScript
    </h1>
    <br/>
    <script>
        function rojo(titulo) {
            titulo.style.color = 'red';            
        }
        
        function azul(titulo) {          
            titulo.style.color = 'blue';            
        }        
    </script>
</body>
</html>
```

## Eventos `onmousedown` y `onmouseup`

Los eventos `onmousedown` y `onmouseup` se ejecutan al hacer click sobre un elemento y al soltar el click respectivamente.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id='' onmousedown="rojo(this)" onmouseup="azul(this)"
    onclick="verde(this)">
        Manejo DOM con JavaScript
    </h1>
    <br/>
    <script>
        function rojo(titulo){
            console.log('onmousedown cambio a rojo');            
            titulo.style.color = 'red';            
        }
        
        function azul(titulo) {          
            console.log('onmouseup cambio a azul');            
            titulo.style.color = 'blue';            
        }
        
        function verde(titulo) {          
            console.log('click cambio a verde');            
            titulo.style.color = 'green';            
        }        
    </script>
</body>
</html>
```

## Eventos `onfocus` y `onblur`

El evento `onfocus` se ejecuta cuando damos click sobre una caja de texto, es decir, ponemos en foco la caja de texto. El evento `onblur` se activa cuando quitamos el foco de una caja de texto.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id=''>Manejo DOM con JavaScript</h1>
    <br/>
    Nombre: <input type="text" onfocus="cambiar(this)" onblur="regresar(this)"/>
    <br/><br/>
    Apellido: <input type="text" onfocus="cambiar(this)" onblur="regresar(this)"/>
    <script>
        function cambiar(elementoInput){
            elementoInput.style.background = 'yellow';            
        }
        
        function regresar(elementoInput) {          
            elementoInput.style.background = 'red';            
        }        
    </script>
</body>
</html>
```

## Método `addEventListener`

Mediante el método `addEventListener` agregamos eventos a elementos del documentos HTML. Los eventos que pasamos como argumentos del método se pasan entre '' sin el `on` de la forma `addEventListener('event', function)`.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id=''>Manejo DOM con JavaScript</h1>
    <br/>
    Nombre: <input type="text" id='ejemplo8_input1'/>
    <br/><br/>
    Apellido: <input type="text" id='ejemplo8_input2'/>
    <script>
    
        /** capturamos la referencia al elemento con id nombre. Mediante el método 
        * addEventListener agregamos al elemento el evento que pasamos como argumento
        * del metodo y la función o acción que va a realizar. El elemento quedaría como 
        * <input type="text" id='nombre' onfocus='cambiar(this)' /> */
        document.getElementById('ejemplo8_input1').addEventListener('focus', cambiar);
        document.getElementById('ejemplo8_input1').addEventListener('blur', regresar);       

        /** la función que pasamos, en el ejemplo cambiar, es una función callback */
        document.getElementById('ejemplo8_input2').addEventListener('focus', cambiar);        
        document.getElementById('ejemplo8_input2').addEventListener('blur', regresar);

        /** si indicamos que la función recibe un argumento este es el evento que la 
        * llama. Teniendo el evento como argumento podemos saber cual elemento mandó
        * a llamar la función mediante el atributo target de la forma event.target */
        function cambiar(evento) {          
            let componente = evento.target;            
            componente.style.background = 'yellow';            
        }
        
        function regresar(evento) {          
            evento.target.style.background = 'white';
        }     
    </script>
</body>
</html>
```

## Funciones flecha con eventos

En lugar de definir funciones por separado y llamarlas desde el `addEventListener` podemos hacerlo mediante funciones flecha. La desventaja de esta opción es que no podemos reutilizar el código.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id=''>Manejo DOM con JavaScript</h1>
    <br/>
    Nombre: <input type="text" id='ejemplo9_input1'/>
    <br/><br/>
    Apellido: <input type="text" id='ejemplo9_input2'/>
    <script>
    
        /** agregamos la función flecha como segundo parametro del método addEventListener */
        document.getElementById('ejemplo9_input1').addEventListener('focus', (evento) => {
            evento.target.style.background = 'pink';            
        });
        
        document.getElementById('ejemplo9_input1').addEventListener('blur', (evento) => {          
            evento.target.style.background = '';            
        });        

        /** ejemplo sin función flecha */
        document.getElementById('ejemplo9_input2').addEventListener('focus', cambiar);        
        document.getElementById('ejemplo9_input2').addEventListener('blur', regresar);

        function cambiar(evento) {          
            let componente = evento.target;            
            componente.style.background = 'yellow';            
        }
        
        function regresar(evento) {          
            evento.target.style.background = 'white';            
        }        
    </script>
</body>
</html>
```

## Delegación de eventos o `useCapture`

Podemos aplicar eventos a varios elementos de un mismo formulario. Es decir, propagar la configuración que hicimos para un elemento mas externo o padre hacia elementos mas internos o hijos.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Manejo DOM con JavaScript</title>
</head>
<body>
    <h1 id=''>Manejo DOM con JavaScript</h1>
    <br/>
    <form id='ejemplo10_form'>
        Nombre: <input type="text" id='nombre'/>
        <br/><br/>
        Apellido: <input type="text" id='apellido'/>
    </form>    
    <script>
    
        /** recuperamos la referencia al formulario con id forma */
        const forma = document.getElementById('ejemplo10_form');

        /** el addEventListener agrega el evento a todos los elementos del formulario 
        * si el tercer argumento que pasamos es true */
        forma.addEventListener('focus', (evento) => {          
            evento.target.style.background = 'yellow';            
        }, true);
        
        forma.addEventListener('blur', (evento) => {          
            evento.target.style.background = '';            
        }, true);               
    </script>
</body>
</html>
```



# Ejemplos

Para poder probar el ejemplo tenemos que guardar lo siguiente como un documento HTML llamado `index.html` y en la misma carpeta de este documento crear una nueva carpeta llamada `js` y dentro un nuevo archivo `app.js` quedando de la forma `js/app.js`. Dentro del archivo app.js va nuestro código de JavaScript.

```html
<!doctype html>
<html>

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Aplicación Calculadora</title>
</head>

<body>
	<div class=''>
		<h1>Aplicación Calculadora</h1>

		<!-- creamos un formulario con 2 elementos input de tipo number y usamos clases de bootstrap para modificar lo que se ve -->
		<form id='ejemplo11_form'>
			<div class=''>
				<label for='operandoA'>Operando A</label>
				<input type="number" class='' placeholder="Escribe operando A" id='operandoA' />
			</div>
			<div class=''>
				<label for='operandoB'>Operando B</label>
				<input type="number" class="" placeholder="Escribe operando B" id='operandoB' />
			</div>
		</form>

		<!-- el botón lo dejamos fuera del formulario ya que su acción no va a ser enviar información por GET o POST, 
		en ese caso, si tocamos el botón no se actualiza la página -->
		<button onclick='sumar()'>Sumar</button>

		<div id='ejemplo11_div'></div>
	</div>

	<script>
		console.log('Aplicación Calculadora');

		function sumar() {
			const forma = document.getElementById('ejemplo11_form');

			/** accedemos a cada uno de los elementos del array del formulario con id forma
			* para hacerlo usamos el id de cada uno de estos elementos */
			let operandoA = forma['operandoA'];
			let operandoB = forma['operandoB'];

			/** utilizamos parseInt pasar el valor del atributo value de los elementos a 
			* números. Cuando estos se recuperan lo hacen como string aunque se escriban
			* como números en el formulario */
			let resultado = parseInt(operandoA.value) + parseInt(operandoB.value);

			/** la función isNaN devuelve true si la variable que pasamos como argumento 
			* no es un número */
			if (isNaN(resultado)) resultado = 'La operación no incluye números';
			document.getElementById('ejemplo11_div').innerHTML = `Resultado: ${resultado}`;
			console.log(`Resultado: ${resultado}`);
		}
	</script>
</body>

</html>
```

## Aplicación listado de personas

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado de Personas</title>
</head>
<body >
    <div class='' id=''>
        <h1>Listado de Personas</h1>
    </div>   

    <div class=''>
        <button onclick='mostrarPersonas()'
        >Mostrar listado</button>
        <div class=''>
            <ul id='ejemplo12_ul'>
                <!--<li>Juan Perez</li>-->
            </ul>
        </div>
    </div>

    <div class="">

        <button style='cursor: pointer' onclick="agregarPersona()">agregar</button>

        <form id='ejemplo12_form'>
            <input type="text" id='ejemplo12_input1' placeholder="Nombre"/>
            <input type='text' id='ejemplo12_input1' placeholder="Apellido"/>
        </form>
    </div>

    <script>

        /** Creamos la clase persona mediante la cual vamos a crear los elementos del listado */
        class Persona{
            constructor(nombre, apellido){
                this._nombre = nombre;
                this._apellido = apellido;
            }
            get nombre(){
                return this._nombre;
            }
            set nombre(nombre){
                this._nombre = nombre;
            }
            get apellido(){
                return this._apellido;
            }
            set apellido(apellido){
                return this._apellido = apellido;
            }    
        }
        
        /** arreglo de objetos de tipo persona */
        const personas = [
            new Persona('Juan', 'Perez'),
            new Persona('Karla', 'Lara')
        ];
        
        /** función que se llama al tocar en el botón de mostrar listado con el evento onclic */
        function mostrarPersonas(){
            console.log('Mostrar personas...');
            let texto = '';
            for(let persona of personas){
                console.log(persona);

                /** mediante literales creamos escribimos la sintaxis de un elemento HTML
                 * de la forma <li>Juan Perez</li> */
                texto += `<li>${persona.nombre} ${persona.apellido}</li>`;
            }

            /** el elemento que creamos con literales lo pegamos en el contenido del bloque 
             * <ul> convirtiéndose en un elemento de la lista */
            document.getElementById('ejemplo12_ul').innerHTML = texto;
        }

        function agregarPersona(){
            const forma = document.forms['ejemplo12_form'];
            const nombre = forma['ejemplo12_input1'];
            const apellido = forma['ejemplo12_input2'];
            if(nombre.value != '' && apellido.value != ''){
                const persona = new Persona(nombre.value, apellido.value);
                console.log(persona);
                personas.push(persona);
                mostrarPersonas();
            }
            else{
                console.log('No hay información que agregar');
            }
        }
    </script> 
</body>
</html>
```

## Aplicación reloj digital

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>        
        #ejemplo13_div1{
            font-family: sans-serif;
            font-size: 60px;
            text-shadow: 0px 0px 1px #333;
            color:#fff;
        }
        .reloj-contenedor{
            background-color: rgb(12, 119, 206);
            padding: 25px;
            max-width: 350px;
            text-align: center;
            border-radius: 5px;
            margin: 0 auto;
            margin-top: 10%;
        }
        #ejemplo13_div4{
            letter-spacing: 10px;
            font-size: 15px;
        }
        .animar{
            border: rgb(255, 68, 68) 2px solid;
        }
    </style>

    <title>Reloj Digital</title>
    
</head>
<body>
    <div id='ejemplo13_div1'>
        <div class='reloj-contenedor' id='ejemplo13_div2'>
            <div id='ejemplo13_div3'>Reloj digital</div>
            <div id='ejemplo13_div4'>con JavaScript</div>
        </div>
    </div>

    <script>
        const mostrarReloj = ()=>{
            let fecha = new Date();
            let hr = formatoHora(fecha.getHours());
            let min = formatoHora(fecha.getMinutes());
            let seg = formatoHora(fecha.getSeconds());
            document.getElementById('ejemplo13_div3').innerHTML = `${hr}:${min}:${seg}`;

            const meses = ['Ene', 'Feb', 'Mar','Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
            const dias = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'];
            let diaSemana = dias[fecha.getDay()];
            let dia = fecha.getDate();
            let mes = meses[fecha.getMonth()];
            let fechaTexto = `${diaSemana}, ${dia} ${mes}`;
            document.getElementById('ejemplo13_div4').innerHTML = fechaTexto;
            
            /** mediante el método classList obtenemos una lista de todas las 
             * clases que se están aplicando al elemeto y mediante toggle indicamos
             * aplique la clase css animar al objeto en la primera iteración de setInterval
             * y que quite la clase animar en la siguiente iteración */
            document.getElementById('ejemplo13_div2').classList.toggle('animar');
        };

        const formatoHora = (hora)=>{
            if(hora < 10)
                hora = '0' + hora;
                return hora;    
        };
        setInterval(mostrarReloj, 1000);
    </script>
</body>
</html>
```
