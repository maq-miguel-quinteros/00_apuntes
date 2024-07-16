# TypeScript

¿que es typeScript?

Los archivos typescript tiene extensión ts.

## Variables

### Definir el tipo de dato

Para trabajar con variables en TypeScript tenemos que definir de forma estricta su tipo de variable y después utilizar datos de ese tipo, en esa variable, en todo el código.

El tipo de variable se define de forma implícita, es decir, se infiere en base al tipo de dato que le asignamos cuando la creamos.

```ts
let user = "Miguel"
user = 10 // dará error
user = {} // dará error
user = "Quinteros" // no dará error

let age = 38
age = "eighteen" // dará error
age = false // dará error
```

También podemos definir el tipo de dato de forma explicita mediante los dos puntos `:` cuando creamos la variable. En el momento de crearla también podemos asignarle un valor.

```ts
let ageWidthType: number // el tipo de datos es number
age = 38
age = "eighteen" // dará error
let ageWidthType2: number = 38 // indicamos el tipo de datos y le asignamos un valor
```

### Tipos de datos básicos

Tenemos 3 tipos de datos básicos que podemos usar:
* Number
* String
* Boolean

```ts
let testNumber: number
testNumber = 38

let testString: string
testString = "hello"

let testBoolean: boolean
testBoolean = false
```

Podemos indicar que una variable sea capaz de recibir más de un tipo de datos mediante la definición explicita, utilizando un `|`. Esto se denomina __union types__.

```ts
let testStringOrNumber: string | number; // la variable puede recibir string o number
testStringOrNumber = 10
testStringOrNumber = "10"
```

### Estructuras de datos

Los `array` también pueden definirse de forma implícita. Donde, el tipo de datos que contenga el array va a ser el tipo de datos que luego pueda recibir.

```ts
let names = ["john", "jane", "tom"] // definimos un array de elementos de tipo string
names.push(3) // dará error
names.push("mike")

let numbers = [11, 22, 35] // definimos un array de elementos de tipo number
numbers.push(true) // dará error
numbers.push(92)

let testStringArray: string[];

```

Cuando definimos una variable como array, de forma explicita, indicamos el tipo del array y, mediante `[]` justo al lado, que la variable es un array de ese tipo.

```ts
let testStringArray: string[] // array de elementos de tipo string
testStringArray = [1,2,3] // dará error
testStringArray = ["one", "two", "three"]

let testNumberArray: number[] // array de elementos de tipo number
testNumberArray = [true, "hi", 23] // dará error
testNumberArray = [12, 55, 23]
```

Podemos indicar que una variable de tipo array sea capaz de recibir más de un tipo de datos en sus elementos mediante la definición explicita, utilizando un `|` y poniendo entre paréntesis los tipos de elementos que puede recibir. Esto se denomina __union types__.

```ts

let testStringOrNumberArray: (string | number)[] // array de elementos de tipo string o number
testStringOrNumberArray = [1, "two", 3]
```

En el caso de las variables de tipo `object` también pueden definirse de forma implícita. El tipo de datos que contenga cada uno de los atributos del objeto, va a ser el tipo de datos que los mismos puedan recibir si los cambiamos.

```ts
let user = {
	username: "john",
	age: 22,
	isAdmin: false,
}
user.username = "jane"
user.age = "eighteen" // dará error
user.age = 29
user.isAdmin = "no" // dará errpr
user.isAdmin = true

  
```

No podemos agregar atributos, a un objeto, que no existan en la definición del objeto.

```ts
let user = {
	username: "john",
	age: 22,
	isAdmin: false,
}
user.phone = "+12345678" // dará error
```

Cuando definimos la variable como objeto, de forma explicita, indicamos el tipo de dato de cada uno de los atributos.

```ts
let userObj: {
	username: string
	age: number
	isAdmin: boolean
}
```

Cuando damos valores a un objeto definido no podemos dejar alguno de sus atributos sin ningún valor válido para ese atributo.

```ts
let userObj: {
	username: string
	age: number
	isAdmin: boolean
}
userObj = { // dará un error indicando que falta definir el valor del atributo isAdmin
	username: "john",
	age: 23,
	phone:"+1234567" // dará error
}
```

Cuando necesitamos indicar que alguno de los atributos de un objeto puede no estar definido, en la definición del objeto indicamos el nombre del atributo con un `?`.

```ts
let userObj2: {
	username: string
	age: number
	isAdmin: boolean
	phone?: string
}
userObj2 = {
	username: "jane",
	age: 43,
	isAdmin: false,
}
```

### Tipo de dato ANY

Podemos definir una variable sin indicar un tipo de datos, en ese caso el tipo de datos de datos de la variable será `any`. Esto no es una forma recomendable de trabajar. La variable puede ser definida de forma implícita.

```ts
let testAny
testAny = 12
testAny = "Hello"
testAny = true
testAny = [true]
testAny = {}
```

También podemos definir la variable como any de forma explicita.

```ts
let testAny: any
testAny = 12
testAny = "Hello"
testAny = true
testAny = [true] // array con elementos de tipo boolean
testAny = {}

let testAnyArray: any[]
testAnyArray = [1, "two", false, []]
```

## Funciones

Las funciones son un tipo de variable especia, pero que responden a la misma lógica de los otros tipos de variables en typescript. En este caso el tipo de dato de una variable que guarda una función es `function`.

```ts
let sayHi = () => {
	console.log("Hi, welcome");
};
sayHi = "hi" // dará error
```

Las funciones pueden o no retornar un valor, en ese caso tenemos que tener en cuenta el tipo de dato del valor que retorna la función.

```ts
let sayHi = () => { // el tipo de return de la función es void
	console.log("Hi, welcome");
}

let sayHi = (): void => { // indicamos el retorno de forma explicita
	console.log("Hi, welcome");
}

let funcReturnString = (): string => { // dará un error
	console.log("hi")
	return 20
}

let funcReturnString = (): string => {
	console.log("hi")
	return "lama dev"
}
```

Las funciones pueden o no recibir datos como parámetro, en ese caso tenemos que indicar el tipo de datos que recibe.

```ts
// indicamos que recibe como parámetro una variable de tipo number, reconoce de forma implícita el tipo de dato que devuelve
let multiple = (num: number) => {
	return num * 2;
}

// indicamos que recibe como parámetro una variable de tipo number y devuelve un dato del tipo number
let multiple2 = (num: number): number => { // 
	return num * 2;
}

// no devuelve ningún dato
let multiple3 = (num: number): void => {
	num = num * 2;
}

// puede recibir o no un tercer parámetro de tipo number
let sum = (num1: number, num2: number, another?: number): number => {
	return num1 + num2;
}
sum(2, 3)



```

## Tipos de datos personalizados (type aliases)

Para evitar tener que pasar, por ejemplo a una función, un objeto completo, indicando cada uno de los tipos de datos de sus atributos, como se ve en el código:

```ts
let func = (user: { username: string; age: number; phone?: string }): void => {
	console.log(user.username);
}
```

Podemos utilizar la palabra reservada `type` y crear un tipo de dato personalizado.

```ts
type UserType = {
	username: string
	age: number
	phone?: string
}
let betterFunc = (user: UserType): void => {
	console.log(user.username)
}
```

De esta forma definimos un prototipo para el tipo de datos, que permite indicar puntualmente cuales son los atributos que va a tener una variable de ese tipo y hasta cuales son los valores que pueden tomar esos atributos.

```ts
type UserType2 = {
	username: string
	age: number
	phone?: string
	// una variable de tipo UserType2, en su atributo theme, solo puede tomar uno de los dos valores indicados
	theme: "dark" | "light" 
}

const userWithTheme: UserType2 = {
	username: "john",
	age: 43,
	theme:"pink" // dará error
}

const userWithTheme: UserType2 = {
	username: "john",
	age: 43,
	theme: "dark"
}
```

Mediante `type` también podemos definir la firma de una función (function signature), es decir, un prototipo que sirva para definir nuevas funciones luego, que van a tener que cumplir con los requisitos del prototipo.

```ts
// declaramos el prototipo myFunc, que es una función que recibe un atributo de tipo number y uno de tipo string y no devuelve nada
type myFunc = (a: number, b: string) => void;

// la variable write, de tipo myFunc, tiene que recibir como parámetros un number y un string y no devolver nada
let write: myFunc = (num, str) => {
	// definimos lo que hace la variable write de tipo myFunc que es una función
	console.log(num + " times " + str);
}
```

## Interfaces

Definimos las interfaces con la palabra reservada `interface`. Su utilidad es similar a los objetos y funciones que creamos con la palabra reservada `type`. Las interfaces permiten hacer herencia de atributos y métodos de una variable de tipo objeto a otra.

```ts
// definimos la interface IUser, por convención con una I adelante del nombre
interface IUser {
	username: string;
	email: string;
	age: number;
}

// IEmployee hereda o extiende de IUser, es decir, tiene acceso a sus atributos y métodos
interface IEmployee extends IUser {
	employeeId: number;
}

// dará un error indicando que falta el atributo employeeId
const emp: IEmployee = {
	username: "tom",
	email: "tom@gmail.com",
	age: 43,
}
const emp: IEmployee = {
	username: "tom",
	email: "tom@gmail.com",
	age: 43,
	employeeId: 1,
};

// dará un error indicando que el atributo employeeId no está definido en el prototipo
const client: IUser = {
	username: "tom",
	email: "tom@gmail.com",
	age: 43,
	employeeId: 1
}

const client: IUser = {
	username: "tom",
	email: "tom@gmail.com",
	age: 43,
}
```

En general usamos `type` si el tipo de dato o prototipo no requiere herencia y usamos `interface` si necesitamos hacer la herencia.

## Atributos genéricos

En algunas ocasiones podemos necesitar definir tipos de datos complejos dentro de atributos de un `type` o un `interface`. Además estos tipos de datos complejos pueden llegar a modificarse con el pasar del tiempo, necesitando modificar la definición del prototipo para que pueda recibir la nueva entrada.

```ts
// definimos como type aunque podría ser una interface también
type Author = {
	id: number;
	username: string;
}

interface ICategory {
	id: number;
	title: string;
}

interface IPost {
	id: number;
	title: string;
	desc: string;
	// el atributo extra solo puede contener array de datos de type Author o array de datos de la Interface ICategory
	extra: Author[] | ICategory[];
}
```

Para dejar abierta la posibilidad de cargar otros tipos de datos, no indicados en la definición de la interface IPost, indicamos en la definición que el tipo de datos puede recibir datos genéricos. Para indicar esto, por convención utilizamos `<T>`, pero dentro de las `< >` podemos indicar cualquier palabra o letra.

```ts
// mediante <T> indicamos que el atributo extra va a contener variables del tipo que pasemos entre < >
interface IPostBetter<T> {
	id: number;
	title: string;
	desc: string;
	// indicamos que, además de ser variables del tipo que pasemos entre < >, el contenido del atributo extra va a ser un array
	extra: T[];
}

// indicamos que el tipo de valores que va a tener extra es string
const testMe: IPostBetter<string> = {
	id: 1,
	title: "post title",
	desc: "post desc",
	// asignamos un array de string a extra
	extra: ["str", "str2"],
};
```

El tipo de dato genérico que indicamos con `<T>` no tiene que ser un tipo de dato básico.

```ts
// mediante T extends object indicamos que T va a ser un objeto (con atributos y métodos)
interface IPostEvenBetter<T extends object> {
	id: number;
	title: string;
	desc: string;
	extra: T[];
}

const testMe2: IPostEvenBetter<{ id:number, username:string }> = {
	id: 1,
	title: "post title",
	desc: "post desc",
	extra: [{ id: 1, username: "John" }],
};

// definimos dos tipos de datos más
type Author = {
	id: number;
	username: string;
}
interface ICategory {
	id: number;
	title: string;
}

const testMe3: IPostEvenBetter<Author> = {
	id: 1,
	title: "post title",
	desc: "post desc",
	extra: [{ id: 1, username: "john" }],
};

const testMe4: IPostEvenBetter<ICategory> = {
	id: 1,
	title: "post title",
	desc: "post desc",
	extra: [{ id: 1, title: "cat" }],
};
```
