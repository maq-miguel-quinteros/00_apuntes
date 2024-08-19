
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
const store = createStore()




```
