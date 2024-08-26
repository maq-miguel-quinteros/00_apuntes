
# Redux

Redux es un contenedor de estados previsible para apps creadas con JavaScript.

* Redux fue creados para apps creadas con JavaScript: Redux puede ser usado por cualquier framework o librería de JavaScript como React, Angular, Vue o JavaScript Vanilla.

* Redux es un contenedor de estados: Redux guarda el estado de la aplicación. El estado de la aplicación es el estado individual de todos los componentes de la aplicación. Esto incluye los datos y la lógica de la interfaz de usuario. Redux puede almacenar y modificar estos datos. Un ejemplo del estado de una aplicación puede ser el siguiente:

![application_state](./redux01.png)

* Redux es predecible: En Redux, todas las transiciones de estado, es decir, todas las modificaciones que se le hace a un estado son explicitas. Que sean explicitas significa que son conocidas y que es posible y rastrearlas, saber donde se hicieron. Con Redux, los cambios de estado de la aplicación se vuelven predecibles.

## Instalación

En la carpeta de nuestro proyecto, en la consola instalamos redux con el comando `npm install redux`.

## Tres conceptos fundamentales de Redux

En un caso de ejemplo, el de venta de un pastel en una tienda de pasteles, podemos reconocer tres situaciones entidades:
* La tienda
* El empleado
* El cliente

Estas tres entidades se relacionan en la actividad o acción de la venta de un pastel:
* El cliente
    * compra un pastel
* El empleado
    * revisa si hay stock y entrega el pastel
    * genera el recibo para el seguimiento de la venta

Podemos traducir este ejemplo en los tres conceptos fundamentales de redux

Escenario tienda de pasteles | Concepto en Redux | Explicación
--- | --- | ---
La tienda: guarda los pasteles en su deposito | __store__ | Guarda el estado de la aplicación
El cliente: quiere comprar un pastel | __action__ | Indica los cambios que se van a hacer en el estado de la aplicación
El empleado: realiza la venta | __reducer__ | Lleva a cabo el cambio de estado de la aplicación dependiendo de la acción

## Tres principios de Redux

1. Todos los estados de la aplicación se guardan en un árbol de objetos dentro de una única __store__: mantiene el estado de la aplicación en un único objeto, que será manejado por el __Redux store__.
2. La única forma de cambiar un estado es mediante una __action__, que es un objeto que describe que es lo que debe suceder con ese estado: para actualizar el estado de la aplicación necesitamos indicarle a Redux lo que queremos hacer mediante la acción, no podemos actualizar el objeto de estados directamente.
3. Para especificar como modificar el árbol de estados, mediante las acciones, escribimos __reducers__ puros: los __reducers__ son funciones de javascript puras que reciben el estado anterior y una acción, y devuelven el nuevo estado `(previousState, action) => newState`.

(volver a ver el video y sumar una captura de gráfico del final )
https://www.youtube.com/watch?v=_KhGdZEWC4c&list=PLC3y8-rFHvwheJHvseC3I0HuYI2f46oAK&index=4

## Implementamos Redux

### actions

Las _action_ son la única forma en que nuestra aplicación puede interactuar con la _store_. Llevan información desde la aplicación a la _Redux store_. Las acciones son objetos planos de javascript. Tienen una propiedad _type_ que indican el tipo de acción que deben realizar. La propiedad type por lo general se define como una constante de tipo string.
```js
// definimos la constante. Esto no es estrictamente necesario pero por convención se realiza
const BUY_CAKE = 'BUY_CAKE';

// definimos la acción
{
    type: BUY_CAKE,
    info: 'Primera acción'

}
```

Redux requiere que implementemos una función para la acción, a la que llamamos action creator, que simplemente crea la acción. En el código sería una función que devuelve una acción.
```js
const BUY_CAKE = 'BUY_CAKE';

// definimos el action creator, que es una función que devuelve una acción
function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Primera acción'
    
    }
}

```

### Reducers

Los reducers especifican como van a cambiar los estados de la aplicación en respuesta a las acciones enviados a la store. Las acciones solo describen que va a pasar, pero no describen como cambian los estados de la aplicación.

Un reducer es una función que acepta un estado y una acción como argumento, y devuelve un nuevo estado para la aplicación. `(previousState, action) => newState`.

De acuerdo con la definición de Redux el estado de la aplicación esta representado por único objeto.
```js
// ACTION
const BUY_CAKE = 'BUY_CAKE';
function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Reduce el número de cakes en 1'    
    }
}

// STATE
// estado de la aplicación
const initialState = {
    numOfCakes: 10,
    other: 50
}

// REDUCER FUNCTION
const reducer = (state = initialState, action) => {
    switch (action.type){
        case BUY_CAKE:
            // copiamos el contenido de state y de este modificamos numOfCakes. Devolvemos un nuevo objeto
            return {...state, numOfCakes: state.numOfCakes - 1}
        default:
            return state;
    }
}

```

### Redux Store (state)

Para toda nuestra aplicación solo tenemos una Redux store. Las funciones que cumple la store son:
* Guarda el estado de la aplicación.
* Permite acceder al estado de la aplicación mediante métodos `getState()`.
* Permite modificar el estado de la aplicación mediante un método llamado __dispatch__ que recibe como parámetro una __action__ de la forma `dispatch(action)`.
* Permite a la aplicación registrar __listeners__ mediante un método llamado __suscribe__ de la forma `suscribe(listener)`. El método suscribe recibe como parámetro una función, está función se va a ejecutar cada vez que cambie el valor del estado de la aplicación.
* Permite a la aplicación desregistrar __listeners__, es decir, dejar de ejecutar cierta función cada vez que se actualiza el estado de la aplicación. Esto se hace mediante la función que devuelve el método __suscribe__.
```js
// en caso de tratarse de una aplicación de javascript simple utilizamos
// const redux = require('redux')

// importamos la librería
import redux from 'redux'
// importamos el método createStore de redux
const createStore = redux.createStore

// ACTION
const BUY_CAKE = 'BUY_CAKE';
function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Reduce el número de cakes en 1'    
    }
}
// STATE
const initialState = {
    numOfCakes: 10,
    other: 50
}
// REDUCER FUNCTION
const reducer = (state = initialState, action) => {
    switch (action.type){
        case BUY_CAKE:
            return {...state, numOfCakes: state.numOfCakes - 1}
        default:
            return state;
    }
}

// * Guarda el estado de la aplicación
// el método createStore de redux recibe como parámetro un método reducer, este método reducer tiene a su vez como parámetro el objeto state que, al momento de declararlo en el método reducer, lo hacemos igual al objeto initialState. De esta forma, mediante los parámetros del método reducer, pasamos a createStore el estado inicial de la aplicación, es decir, el estado de la aplicación
const store = createStore(reducer)

// * Permite acceder al estado de la aplicación mediante métodos `getState()`
// el método getState es parte del paquete de redux. Para consultar el estado actual de la aplicación podemos hacer console.log
console.log('estado inicial: ' + store.getState())

// * Permite a la aplicación registrar listeners mediante un método llamado suscribe de la forma `subscribe(listener)`
// la función que va a recibir subscribe en el ejemplo es un console.log. Está función se va a ejecutar cada vez que se actualize el estado de la aplicación. La ejecución de store.suscribe devuelve una función que usaremos para cancelar suscripción
const unsubscribe = store.subscribe(()=>{
    console.log('nuevo estado: ' + store.getState())
})

// * Permite modificar el estado de la aplicación mediante un método llamado __dispatch__ que recibe como parámetro una __action__ de la forma `dispatch(action)`
// puedo ejecutar la acción todas las veces que quiera mediante el dispatch. Cada vez que lo ejecute además se va a ejecutar el console.log indicando en store.suscribe()
store.dispatch(buyCake)
store.dispatch(buyCake)
store.dispatch(buyCake)

// * Permite a la aplicación desregistrar __listeners__, es decir, dejar de ejecutar cierta función cada vez que se actualiza el estado de la aplicación
// llamamos a la función unsubscribe para dejar de ejecutar el código de subscribe cada vez que se actualiza el estado de la aplicación
unsubscribe()
store.dispatch(buyCake) // esta ejecución no llamará al console.log de store.subscribe
```

Para trabar con Redux creamos un objeto __initialState__ con atributos que pueden ser modificados, una función __action creator__ que devuelve un objeto __action__ que indica cual es la acción que vamos a realizar y una función __reducer__, que recibe como parámetro el el objeto _initialState_ y una variable _action_, y que modifica devuelve un nuevo objeto _state_ modificado según lo indicando por la variable _action_. En reducer es donde indicamos como se va a modificar el estado en base al tipo de acción.

Teniendo esto creado podemos armar el circuito de Redux. Primero creamos una store mediante la función redux.createStore(reducer). El método createS recibe como parámetro la función reducer, y por ende, el valor inicial del estado de la aplicación. Tenemos disponible el método store.getState() para saber el valor del estado al momento de llamar al método. Creamos un listener, una función que se va a ejecutar cada vez que se actualice el estado de la aplicación, para hacerlo utilizamos store.subscribe(listener). subscribe nos devuelve una función a la que podemos llamar unsubscribe, que vamos a utilizar para cancelar el listener. Podemos modificar el estado de la aplicación mediante store.dispatch(action), método al que le pasamos la action, lo que queremos que haga el reducer que pasamos cuando creamos la store. Cuando no queremos que se siga ejecutando subscribe utilizamos el método unsubscribe.

## Multiples reducers

En el caso de tener estados de la aplicación que tienen multiples atributos, mediante acciones diferentes, podemos utilizar una única función reducer para modificar ese estado.

```js
import redux from 'redux'
const createStore = redux.createStore

// ACTION
const BUY_CAKE = 'BUY_CAKE';

// creamos una nueva acción
const BUY_ICECREAM = 'BUY_ICECREAM';

function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Reduce el número de cakes en 1'    
    }
}

// creamos un nuevo action creator
function buyIceCream() {
    return {
        type: BUY_ICECREAM
    }
}

// STATE
const initialState = {
    numOfCakes: 10,
	// agregamos un atributo al estado de la aplicación
	numOfIceCreams: 20,
    other: 50
}

// REDUCER FUNCTION
// agregamos cases al switch para las diferentes acciones que modifican los diferentes atributos del estado de la aplicación
const reducer = (state = initialState, action) => {
    switch (action.type){
        case BUY_CAKE:
            return {...state, numOfCakes: state.numOfCakes - 1}
		// agregamos un case para la acción BUY_ICECREAM
		case BUY_ICECREAM:
				return {...state, numOfIceCreams: state.numOfIceCreams - 1}
        default:
            return state;
    }
}

// STORE
const store = createStore(reducer)

// GET METHOD
console.log('estado inicial: ' + store.getState())

// LISTENER
const unsubscribe = store.subscribe(()=>{
    console.log('nuevo estado: ' + store.getState())
})

// DISPATCH
store.dispatch(buyCake)
store.dispatch(buyIceCream)
store.dispatch(buyCake)

// UNSUBSCRIBE LISTENER
unsubscribe()
store.dispatch(buyIceCream)
```

La otra forma de resolves esto es trabajar con multiples reducers. Para ello vamos a dividir el estado y las funciones reducer. De esta forma tenemos un reducer y su lógica trabajando sobre un estado y otro diferente trabajando sobre el otro estado.

```js
import redux from 'redux'
const createStore = redux.createStore

// ACTION
const BUY_CAKE = 'BUY_CAKE';
const BUY_ICECREAM = 'BUY_ICECREAM';
function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Reduce el número de cakes en 1'    
    }
}
function buyIceCream() {
    return {
        type: BUY_ICECREAM
    }
}

// STATE
// dividimos en dos el estado de la aplicación
const initialCakeState = {
    numOfCakes: 10
}
const initialIceCreamState = {
	numOfIceCreams: 20
}

// REDUCER FUNCTION
// dividimos en dos la función reducer
const cakeReducer = (state = initialCakeState, action) => {
    switch (action.type){
        case BUY_CAKE:
            return {...state, numOfCakes: state.numOfCakes - 1}
        default:
            return state;
    }
}
const iceCreamReducer = (state = initialIceCreamState, action) => {
    switch (action.type){
		case BUY_ICECREAM:
				return {...state, numOfIceCreams: state.numOfIceCreams - 1}
        default:
            return state;
    }
}

// STORE
const store = createStore(reducer)

// GET METHOD
console.log('estado inicial: ' + store.getState())

// LISTENER
const unsubscribe = store.subscribe(()=>{
    console.log('nuevo estado: ' + store.getState())
})

// DISPATCH
store.dispatch(buyCake)
store.dispatch(buyIceCream)
store.dispatch(buyCake)

// UNSUBSCRIBE LISTENER
unsubscribe()
store.dispatch(buyIceCream)
```

### Combinar reducers en Redux

En redux podemos tener solo una store, por ende, para trabajar con mas de un objeto de estado y más de un reducer tenemos que combinar estos mediante un método de redux. De esta forma podemos tener objetos de estado separados cada uno con sus tipos de acciones y reducer.

```js
import redux from 'redux'
const createStore = redux.createStore

// traemos el método de redux combineReducers
const combineReducers = redux.combineReducers

// ACTION
const BUY_CAKE = 'BUY_CAKE';
const BUY_ICECREAM = 'BUY_ICECREAM';
function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Reduce el número de cakes en 1'    
    }
}
function buyIceCream() {
    return {
        type: BUY_ICECREAM
    }
}
// STATE
const initialCakeState = {
    numOfCakes: 10,
	other: 20
}
const initialIceCreamState = {
	numOfIceCreams: 20
}
// REDUCER FUNCTION
const cakeReducer = (state = initialCakeState, action) => {
    switch (action.type){
        case BUY_CAKE:
            return {...state, numOfCakes: state.numOfCakes - 1}
        default:
            return state;
    }
}
const iceCreamReducer = (state = initialIceCreamState, action) => {
    switch (action.type){
		case BUY_ICECREAM:
				return {...state, numOfIceCreams: state.numOfIceCreams - 1}
        default:
            return state;
    }
}

// COMBINE REDUCERS
// el método combineReducers recibe como parámetro un objeto, este tiene como atributos los métodos reducer. A la hora de consultar el estado vamos a ver que cake se convierte en un objeto que como atributos los numOfCakes: 10 y other: 20. A su vez iceCream se convierte en un objeto que tiene como atributos numOfIceCreams: 20
const rootReducer = combineReducers({
	cake: cakeReducer,
	iceCream: iceCreamReducer
})

// STORE
// creamos la store pasando como parámetro el objeto con los reducer como atributos
const store = createStore(rootReducer)

// GET METHOD
console.log('estado inicial: ' + store.getState())
// LISTENER
const unsubscribe = store.subscribe(()=>{
    console.log('nuevo estado: ' + store.getState())
})
// DISPATCH
store.dispatch(buyCake)
store.dispatch(buyIceCream)
store.dispatch(buyCake)
// UNSUBSCRIBE LISTENER
unsubscribe()
store.dispatch(buyIceCream)
```

## Middleware

Middleware es la forma sugerida para extender Redux utilizando funcionalidades externas. Provee un espacio de extensión para funciones de terceros entre el envío de una acción y el momento que llega al reducer. Usamos middleware para logging, reporte de errores, realizar tareas asincrónicas, etc. Para utilizar estas funciones de terceros utilizamos un método de redux llamado applyMiddleware y le pasamos la función que queremos ejecutar como parámetro. Esta función applyMiddleware irá como segundo parámetro de createStore cuando creamos la store

### Redux logger

Esta extensión genera un console.log de toda la información relacionada con Redux dentro de nuestra aplicación. Instalamos el paquete de extensión mediante el comando `npm install redux-logger`.

```js
import redux from 'redux'

// importamos el paquete
import reduxLogger from 'redux-logger'

const createStore = redux.createStore
const combineReducers = redux.combineReducers

// creamos la función que permite aplicar middleware
const applyMiddleware = redux.applyMiddleware

// creamos la función logger
const logger = reduxLogger.createLogger()

// ACTION
const BUY_CAKE = 'BUY_CAKE';
const BUY_ICECREAM = 'BUY_ICECREAM';
function buyCake() {
    return {
        type: BUY_CAKE,
        info: 'Reduce el número de cakes en 1'    
    }
}
function buyIceCream() {
    return {
        type: BUY_ICECREAM
    }
}
// STATE
const initialCakeState = {
    numOfCakes: 10,
	other: 20
}
const initialIceCreamState = {
	numOfIceCreams: 20
}
// REDUCER FUNCTION
const cakeReducer = (state = initialCakeState, action) => {
    switch (action.type){
        case BUY_CAKE:
            return {...state, numOfCakes: state.numOfCakes - 1}
        default:
            return state;
    }
}
const iceCreamReducer = (state = initialIceCreamState, action) => {
    switch (action.type){
		case BUY_ICECREAM:
				return {...state, numOfIceCreams: state.numOfIceCreams - 1}
        default:
            return state;
    }
}
// COMBINE REDUCERS
const rootReducer = combineReducers({
	cake: cakeReducer,
	iceCream: iceCreamReducer
})
// STORE
// pasamos como segundo parámetro la función de terceros que queremos que ejecute el reducer cuando creamos la store, utilizamos la función de redux applyMiddleware pasando como parámetro de esta la función de tercero logger
const store = createStore(rootReducer, applyMiddleware(logger))
// GET METHOD
console.log('estado inicial: ' + store.getState())
// LISTENER
const unsubscribe = store.subscribe(()=>{
	// quitamos el console.log ya que, en adelante, la función de terceros logger va a hacer un log de los cambios en los estados de la store
    // console.log('nuevo estado: ' + store.getState())
})
// DISPATCH
store.dispatch(buyCake)
store.dispatch(buyIceCream)
store.dispatch(buyCake)
// UNSUBSCRIBE LISTENER
unsubscribe()
store.dispatch(buyIceCream)
```

### Asynchronous actions

Las acciones sincrónicas son acciones que al ser enviadas (dispatch) actualizan inmediatamente el estado de la aplicación. Las acciones asincrónicas demoran en modificar el estado de la aplicación, por ejemplo, cuando hacemos el llamado a una API solicitando un dato que tenemos que usar para mostrar en la aplicación. Este llamado tiene una demora. A la hora de manejar esto con redux vamos a tener los siguiente componentes:

* STATE:

```js
const state = {
	// esta bandera nos indica que los datos se están trayendo. Se utiliza para notificar eso mismo mediante un mensaje
	loading: true, 
	// los datos de usuario que solicitamos en un array de objetos. Mientras loading es true este atributo va a estar vacío
	data: [],
	// si el llamado devuelve un error lo vamos a guardar en este atributo. Lo usamos para mostrar el error al usuario
	error: ''
}
```

* ACTIONS
	* FETCH_USERS_REQUEST: realiza el llamado a la API para traer un listado de usuarios
	* FETCH_USERS_SUCCESS: si el llamado anterior fue correcto ejecutamos esta segunda acción
	* FETCH_USERS_FAILURE: si el llamado fue incorrecto o dio un error

* REDUCERS

```js
// para la action FETCH_USERS_REQUEST
state = {
	loading: true
}

// para la action FETCH_USERS_SUCCESS
state = {
	loading: false,
	data: dataFromAPI
}

// para la action FETCH_USERS_FAILURE
state = {
	loading: false,
	error: errorFromAPI
}
```

El código quedaría de la siguiente manera:

```js
// STATE
```
