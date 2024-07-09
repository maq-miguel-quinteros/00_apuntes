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
