# useReducer

useReducer es un hook que utilizamos para manipular variables de estado. En react contamos con useState para el manejo de esas variables de estado. useReducer es una alternativa a useState. ¿Cual es la diferencia entre uno y otro? useState está construido en base a useReducer, por ende, useReducer es un hook mas primitivo si lo comparamos con useState.

## Método reduce en javascript

`reduce`, junto con `foreach` y `map` son métodos de las variables de tipo array en javascript. El método `reduce()` ejecuta una función _'reducer'_, una función que nosotros declaramos y le pasamos como parámetro, en cada elemento del array donde se llama. Además podemos pasar un segundo parámetro, con un valor inicial, para que ejecute la función '_reducer_' sobre este antes antes de hacerlo sobre los elementos del array.

```js
const array1 = [1, 2, 3, 4];
const initialValue = 5;

// declaramos una función 'reducer' a la que llamamos callbackFn, donde accumulator puede contener un valor que queramos se mantenga en cada paso de elemento del array y currentValue es el elemento actual que se está evaluando mientras que currentIndex es el indice del elemento en el array del elemento actual que se está evaluando
const callbackFn = (accumulator, currentValue, currentIndex) => {
	console.log('número de elemento del array: ' + currentIndex)
	return accumulator + currentValue
}

// llamaos al método reduce de array1 indicando con callbackFn que debe hacer sobre cada elemento del array
array1.reduce(callbackFn) // devuelve 10

// llamaos al método reduce de array1 indicando con callbackFn que debe hacer sobre cada elemento del array pero además indicamos que debe empezar con el valor indicado en initialValue
array1.reduce(callbackFn, initialValue) // devuelve 15
```

Si comparamos el método `reduce`, de las variables de tipo array, con el hook useReducer:

* Ambos reciben como primer parámetros una función _reducer_ pero, mientras el método reduce recibe como segundo parámetro en _initialValue_ cualquier valor, el hook useReducer recibe como segundo parámetro una variable de estado.

* La función _reducer_, que pasamos como primer parámetro. En el caso del método reduce, la función reducer recibe como parámetros _accumulator_, que mantiene un valor por cada elemento del array recorrido y _currentValue_ que es el elemento actual. En el caso del hook useReducer la función reducer recibe como parámetros _currentState_, que es el valor actual de la variable de estado y _action_ que es lo que debe realizarse sobre esa variable de estado.

* La función reducer del método reduce devuelve un único valor, mientras que la función reducer del hook useReducer devuelve un nuevo estado.

* El método reduce devuelve un valor único, mientras que el hook useReducer devuelve un nuevo estado indicado como __newState__ y una función indicada como __dispatch__

reduce en javascript | useReducer en React
--- | ---
array.reduce(_reducer_, __initialValue__) | useReducer(_reducer_, __initialState__)
__singleValue__ = reducer(__accumulator__, __itemValue__) | __newState__ = reducer(__currentState__, __action__)
reduce method return a __single value__ | useReduce hook returns a __pair of values__: __[newState, dispatch]__

## useReducer con variables de estado y acción simples

```javascriptreact
import React, { useReducer } from 'react'

const initialState = 0

// declaramos la función reducer. state va a ser el valor de initialState de useReducer cuando declaramos el hook y en adelante va a ser el valor que vaya tomando la variable de estado count. action va a ser el valor del parámetro que pasamos a dispatch, que es la función de devuelve useReducer
const reducer = (state, action) => {
	switch (action) {
		case 'increment':
			return state + 1
		case 'decrement':
			return state - 1
		// si tocamos el botón reset devuelve el valor de initialState que se guarda en la variable de estado count
		case 'reset':
			return initialState
		default:
			return state
	}
}

function CounterOne() {
	// al llamar a useReducer creamos una variable de estado count y una función dispatch que modifica esa variable de estado en base a un parámetro que le pasamos
	const [count, dispatch] = useReducer(reducer, initialState)
	return (
		<div>
			<div>Count = {count}</div>
			{/* según el parámetro que pasamos a dispatch es el camino del switch que va a tomar en la función reducer del useReducer */}
			<button onClick={() => dispatch('increment')}>Increment</button>
			<button onClick={() => dispatch('decrement')}>Decrement</button>
			<button onClick={() => dispatch('reset')}>Reset</button>
		</div>
	)
}

export default CounterOne
```

## useReducer con un objeto como variable de estado y un objeto como acción

```javascriptreact
import React, { useReducer } from 'react'

// pasamos como estado inicial un objeto con dos atributos
const initialState = {
	firstCounter: 0,
	secondCounter: 10
}
// tanto state como action son ahora objetos 
const reducer = (state, action) => {
	// el atributo type del objeto action indica cual es la acción que queremos realizar
	switch (action.type) {
		case 'increment':
			// al atributo firstCounter del objeto state le asignamos el valor que este mismo tenía mas el valor indicado en el atributo value del objeto action. Al ser objetos tenemos que utilizar propagación mediante el operador spread ...state, para reemplazar el valor de firstCounter en state
			return { ...state, firstCounter: state.firstCounter + action.value }
		case 'decrement':
			return { ...state, firstCounter: state.firstCounter - action.value }
		case 'increment2':
			return { ...state, secondCounter: state.secondCounter + action.value }
		case 'decrement2':
			return { ...state, secondCounter: state.secondCounter - action.value }
		case 'reset':
			return initialState
		default:
			return state
	}
}

function CounterTwo() {
	const [count, dispatch] = useReducer(reducer, initialState)
	return (
		<div>
			<div>Count = {count.firstCounter}</div>
			{/* pasamos como parámetro a dispatch un objeto con los atributos type u value */}
			<button onClick={() => dispatch({ type: 'increment', value: 1 })}>
				Increment
			</button>
			<button onClick={() => dispatch({ type: 'decrement', value: 1 })}>
				Decrement
			</button>
			<button onClick={() => dispatch({ type: 'increment', value: 5 })}>
				Increment 5
			</button>
			<button onClick={() => dispatch({ type: 'decrement', value: 5 })}>
				Decrement 5
			</button>
			<button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
			{/* muestra el valor del segundo contador, controlado por los botones que aparecen abajo de este */}
			<div>Secound Counter = {count.secondCounter}</div>
			<div>
				<button onClick={() => dispatch({ type: 'increment2', value: 1 })}>
					Increment
				</button>
				<button onClick={() => dispatch({ type: 'decrement2', value: 1 })}>
					Decrement
				</button>
			</div>
		</div>
	)
}

export default CounterTwo
```

## Usar varios useReducer

```javascriptreact
import React, { useReducer } from 'react'

const initialState = 0
const reducer = (state, action) => {
	switch (action) {
		case 'increment':
			return state + 1
		case 'decrement':
			return state - 1
		case 'reset':
			return initialState
		default:
			return state
	}
}

function CounterThree() {
	// para mantener mas simple el código, si vamos a hacer la misma funcionalidad, en vez de pasar objetos como parámetros de la función reducer, podemos crear más de un useReducer
	const [count, dispatch] = useReducer(reducer, initialState)
	const [countTwo, dispatchTwo] = useReducer(reducer, initialState)

	return (
		<div>
			<div>Count = {count}</div>
			<button onClick={() => dispatch('increment')}>Increment</button>
			<button onClick={() => dispatch('decrement')}>Decrement</button>
			<button onClick={() => dispatch('reset')}>Reset</button>

			<div>Count = {countTwo}</div>
			<button onClick={() => dispatchTwo('increment')}>Increment</button>
			<button onClick={() => dispatchTwo('decrement')}>Decrement</button>
			<button onClick={() => dispatchTwo('reset')}>Reset</button>
		</div>
	)
}

export default CounterThree
```

## useReducer con useContext

Hasta ahora utilizamos useReducer con variables de estado locales, es decir, variables de estado a nivel del componente donde se declaran. Si queremos compartir variables de estado entre componentes, es decir, variables de estado globales, podemos combinar useReducer con useContext.

Podemos enviar variables de estado de un componente a su hijo mediante props, pero esto se vuelve engorroso cuando el componente al que queremos llegar es un hijo que se encuentra varios componentes mas abajo del árbol de componentes, es decir, que es el hijo. del hijo. del hijo, etc., del componente donde se origina la variable de estado.

El componente App va a ser el padre, y vamos a pasar la variable de estado y dispatch de un useReducer de este componente a tres componentes hijos en distintos niveles abajo del árbol de componentes. A ComponentA que es hijo de App, a ComponentD que es hijo de ComponentB que es hijo de App y a ComponentF que es hijo de ComponentE que es hijo de ComponentC que es hijo de APP.

* __App__: _declara el useReducer_ -> __ComponentA__: _consume la variable de estado y la función dispatch_
* __App__: _declara el useReducer_ -> ComponentB -> __ComponentD__: _consume la variable de estado y la función dispatch_
* __App__: declara el useReducer -> ComponentC -> ComponentE -> __ComponentF__: _consume la variable de estado y la función dispatch_

El archivo `App.jsx`

```javascriptreact
import React, { useReducer } from 'react'
import ComponentA from './components/ComponentA'
import ComponentB from './components/ComponentB'
import ComponentC from './components/ComponentC'

const initialState = 0
const reducer = (state, action) => {
	switch (action) {
		case 'increment':
			return state + 1
		case 'decrement':
			return state - 1
		case 'reset':
			return initialState
		default:
			return state
	}
}

// creamos el componente de contexto de React
export const CountContext = React.createContext()

function App() {
	const [count, dispatch] = useReducer(reducer, initialState)
	return (
		<>
		{/* pasamos como la prop value de CountContext.Provider un objeto con la variable de estado count y la función dispatch que nos devuelve useReducer */}
			<CountContext.Provider value={{ countState: count, countDispatch: dispatch }}>
				<div>
					<ComponentA />
					<ComponentB />
					<ComponentC />
				</div>
			</CountContext.Provider>
		</>
	)
}

export default App
```

Archivo `ComponentA.jsx`

```javascriptreact
import React, {useContext} from 'react'
import { CountContext } from '../App';

function ComponentA() {
	// recuperamos el objeto que pasamos por la prop value de CountContext.Provider mediante el hook useContext
	const countContext = useContext(CountContext)
	return (
		<div>
			{/* utilizamos la variable de estado que pasamos en el atributo countState que recuperamos en la variable countContext mediante el useContext */}
			Component A {countContext.countState}
			{/* recuperamos la función dispatch que pasamos en el atributo countDispatch que recuperamos en la variable countContext mediante el useContext */}
			<button onClick={() => countContext.countDispatch('increment')}>Increment</button>
			<button onClick={() => countContext.countDispatch('decrement')}>Decrement</button>
			<button onClick={() => countContext.countDispatch('reset')}>Reset</button>
		</div>
	)
}

export default ComponentA
```

Archivo `ComponentB.jsx`:

```javascriptreact
import React from 'react'
import ComponentD from './ComponentD'

function ComponentB() {
	return (
		<div>
			Component B<ComponentD />
		</div>
	)
}

export default ComponentB
```

Archivo `ComponentD.jsx`:

```javascriptreact
import React, {useContext} from 'react'
import { CountContext } from '../App';

function ComponentD() {
	const countContext = useContext(CountContext)
	return (
		<div>
			Component D {countContext.countState}
			<button onClick={() => countContext.countDispatch('increment')}>Increment</button>
			<button onClick={() => countContext.countDispatch('decrement')}>Decrement</button>
			<button onClick={() => countContext.countDispatch('reset')}>Reset</button>
		</div>
	)
}

export default ComponentD
```

Archivo `ComponentC.jsx`:

```javascriptreact
import React from 'react'
import ComponentE from './ComponentE'

function ComponentC() {
	return (
		<div>
			Component C<ComponentE />
		</div>
	)
}

export default ComponentC
```

Archivo `ComponentE.jsx`:

```javascriptreact
import React from 'react'
import ComponentF from './ComponentF'

function ComponentE() {
	return (
		<div>
			Component E<ComponentF />
		</div>
	)
}

export default ComponentE
```

Archivo `ComponentF.jsx`:

```javascriptreact
import React, {useContext} from 'react'
import { CountContext } from '../App';

function ComponentF() {
	const countContext = useContext(CountContext)
	return (
		<div>
			Component F {countContext.countState}
			<button onClick={() => countContext.countDispatch('increment')}>Increment</button>
			<button onClick={() => countContext.countDispatch('decrement')}>Decrement</button>
			<button onClick={() => countContext.countDispatch('reset')}>Reset</button>
		</div>
	)
}

export default ComponentF
```

## fetch de datos con useReducer

Anteriormente realizábamos el fetch de datos mediante hooks useState, generando un estado para cada momento del fetch, es decir, para el loading, success y error. El fetch quedaba de la siguiente manera:

```javascriptreact
import React, {useState, useEffect} from 'react'
import axios from 'axios';

function DataFetchingOne() {
	const [loading, setLoading] = useState(true)
	const [error, setError] = useState('')
	const [post, setPost] = useState({})

	useEffect(() => {
		axios
			.get(`https://jsonplaceholder.typicode.com/posts/1`)
			.then(response => {
				setLoading(false)
				setPost(response.data)
				setError('')
			})
			.catch(error => {
				setLoading(false)
				setPost({})
				setError('Something went wrong!, error: '+ error)
			})
	}, [])

	return (
		<div>
			{loading ? 'Loading' : post.title}
			{error ? error : null}
		</div>
	)
}

export default DataFetchingOne
```

Generamos el mismo fetch pero esta vez utilizando useReducer:

```javascriptreact
import React, { useReducer, useEffect } from 'react'
import axios from 'axios'

// los tres estados, correspondientes a los tres momentos del fetch los guardamos en el mismo objeto
const initialState = {
	loading: true,
	error: '',
	post: {}
}

const reducer = (state, action) => {
	// tanto state como action son objetos
	switch (action.type) {
		// cuando el fetch es exitoso, es decir, vamos por el camino del then
		case 'FETCH_SUCCESS':
			return {
				// deja de mostrarse Loading en la pantalla
				loading: false,
				// guarda en post los datos que vienen desde la API
				post: action.payload,
				// limpiar el atributo error de posibles valores que hayan quedado de otra ejecución anterior
				error: ''
			}
		// cuando el fetch da error, es decir, vamos por el camino de catch
		case 'FETCH_ERROR':
			return {
				loading: false,
				// limpia el atributo post de posibles valores que hayan quedado de otra ejecución anterior
				post: {},
				// informa que hay un error
				error: 'Something went wrong!'
			}
		default:
			return state
	}
}

function DataFetchingTwo() {
	// state es mi variable de estado, que es un objeto con los atributos loading, error y post. Con la función dispatch voy a modificar estos atributos
	const [state, dispatch] = useReducer(reducer, initialState)

	useEffect(() => {
		axios
			.get(`https://jsonplaceholder.typicode.com/posts/1`)
			.then(response => {
				// indico que en el switch, de la función reducer, tome el camino de FETCH_SUCCESS. Al atributo payload, del objeto que paso a dispatch, que se convierte en action, le paso la respuesta del fetch
				dispatch({ type: 'FETCH_SUCCESS', payload: response.data })
			})
			.catch(error => {
				dispatch({ type: 'FETCH_ERROR' })
			})
	}, [])
	return (
		<div>
			{/* mientras se traen los datos va a mostrar el mensaje loading, al ejecutarse el then en el useEffect va a mostrar el valor del atributo title dentro del objeto post dentro de la variable de estado, que también es un objeto, state */}
			{state.loading ? 'Loading' : state.post.title}
			{state.error ? state.error : null}
		</div>
	)
}

export default DataFetchingTwo
```

## Cuando utilizar useState y cuando useReducer

Analizamos cuando utilizar useState o useReducer según distintos escenarios:

* Según el tipo de estado: para variables de estado de tipo number, string o boolean usamos useState. Para variables de estado de tipo object o array usamos useReducer.

* Según la cantidad de variables de estado: si tenemos uno o dos estados podemos manejar cada uno con su useState. Si tenemos tres o mas estados puede ser mejor repensar la lógica para trabajar con una variable object y un useReducer que se encargue, mediante su función reducer, de actualizar los atributos de ese objeto como variable de estado.

* Según la relación de las variables de estado: si tenemos variables de estado que funcionan de forma independiente una de otra las trabajamos con useState. Si el cambio en una variable de estado conlleva a tener que modificar otras es preferible trabajarlas como atributos de un objeto, como variable de estado, en un useReducer.

* Según la lógica de negocio: si la variable de estado no responde a una lógica de negocio particular utilizamos useState. Si existe una lógica de negocio useReducer permite tener toda está lógica concentrada en la variable initialState y en la función reducer, que se declaran fuera del componente y solo se utilizan cuando llamamos al hook.

* Según si la variable de estado sea local o global: para variables de estado locales, es decir, variables de estado a nivel de componente, utilizamos useState. Para variables de estado globales, es decir, a nivel de contexto, utilizamos useReducer en combinación con useContext.

Escenario | useState | useReducer
--- | --- | ---
Tipos de estado | number, string y boolean | object o array
Cantidad de variables de estado | una o dos variables de estado | un objeto que contenga como atributos las variables de estado
Variables de estado relacionadas | No | Si
La lógica de negocio | sin lógica de negocio | con lógica de negocio
Variables de estado locales y globales | local | global
