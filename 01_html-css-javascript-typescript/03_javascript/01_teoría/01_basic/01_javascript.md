# JavaScript


# Tipos de datos


El tipo de dato `string` (cadena de caracteres)


```js
var nombre = "Carlos";
console.log(nombre);
```

El tipo de dato `number` (numérico)


```js
var numero = 1000;
console.log(numero);
```

El tipo de dato `object` (objeto)


```js
var objeto = {
    nombre: "Juan",
    apellido: "Perez",
    telefono: "55443322"
}
console.log(objeto);
```

Las variables son dinámicas, con asignarle el valor indicamos el tipo de datos que almacena, a su vez si cambiamos su valor por otro, de otro tipo de datos, la misma cambia para adaptarse a al mismo.

El tipo de dato `typeof` devuelve el tipo de datos que está almacenado en la variable al momento de usarlo.


```js
var nombre = "Carlos";
console.log(typeof nombre);

var nombre = 5;
console.log(typeof nombre);

var objeto = {
    nombre: "Juan",
    apellido: "Perez",
    telefono: "55443322"
}
console.log(typeof objeto);
```

El tipo de dato `boolean` puede tomar los valores de `true` o `false` (verdadero o falso). Este tipo de variable se conoce como bandera.


```js
var bandera = false;
console.log(typeof bandera);
```

El tipo de dato `function` (función) permite realizar una tarea. Lleva adelante una serie de lineas de código y, si necesitamos volver a realizar esa tarea, podemos volver a llamar a la función.


```js
function miFuncion() { }
console.log(typeof miFuncion);
```

El tipo de dato `Symbol` se utiliza para crear un valor único de una variable. Si necesitamos crear una variable de este tipo llamamos a la función `Symbol()` y entre los paréntesis pasamos una cadena de caracteres.


```js
var simbolo = Symbol("mi simbolo");
console.log(typeof simbolo);
```

El tipo de dato `class` (clase) es un tipo `function`. Por lo general se define la clase con su nombre en singular y empezando en mayúsculas. Para poder definir objetos de esta clase necesitamos un método o función, propio de la clase, llamado constructor. Con la palabra reservada `this` seguida de `.atributo` indicamos que al atributo, propio de la clase, le asignamos un `valor`, que viene por parámetros en el constructor, de la forma `this.atributo = valor`.


```js
class Persona {

	/** método constructor de la clase recibe por parametros nombreNuevo, apellidoNuevo */
	constructor(nombreNuevo, apellidoNuevo) {

		/** asignamos a los atributos nombre y apellido, propios de la clase, lo que llega por parametro */
		this.nombre = nombreNuevo;
		this.apellido = apellidoNuevo;
	}
}
console.log(typeof Persona);
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
