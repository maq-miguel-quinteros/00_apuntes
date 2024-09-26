# useRef

El hook useRef puede ser usado en alguno de los siguientes casos:

* Permite acceder a nodos de DOM directamente mediante componentes funcionales. Referenciamos un nodo, una etiqueta de HTML, como si de un `getElementBy...` se tratara. Después de eso podemos llamar a las funciones o asignar los valores que ese elemento permite en HTML.

* Permite acceder, desde fuera de una función, a variables o funciones declaradas dentro de una función y que solo son válidas para ese contexto.

## Referencia a nodos del DOM

El hook useRef recibe como parámetro un valor inicial y devuelve un objeto. Este objeto tiene un atributo `current` que podemos utilizar para hacer referencia, por ejemplo, a un nodo, es decir, una etiqueta del DOM. Para que esta referencia suceda, en la declaración de la etiqueta utilizamos la prop reservada `ref` y le damos el valor del objeto que useRef nos devuelve. De esta forma podemos hacer referencia a ese nodo o etiqueta en alguna función de nuestro código.

En el ejemplo ponemos en foco la caja de texto cuando el componente se renderiza por primera vez.

```js
import React, { useRef, useEffect } from 'react'

function FocusInput() {
	// llamamos a la función useRef pasando el valor null y el objeto que devuelve queda en inputRef
	const inputRef = useRef(null)
	
	useEffect(() => {
		// llamamos al atributo current, del objeto inputRef, e indicamos que se haga en lo que sea que represente la referencia inputRef
		inputRef.current.focus()
	}, [])

	return (
		<div>
			{/* indicamos que inputRef sea una referencia al input. De esta forma vamos a poder acceder al método focus de este nodo del DOM */}
			<input ref={inputRef} type="text" />
		</div>
	)
}

export default FocusInput
```

## Referencia a variables o funciones locales

Utilizamos como ejemplo un elemento, que muestra una variable de estado, que a cada segundo se actualiza sumando uno al contador. El problema consiste en que la variable que controla este contador se declara dentro del hook useEffect, por ende, no puede ser accedida por elementos fuera de este.

```js
import React, {useState, useEffect} from 'react'

function HookTimer() {
	const [timer, setTimer] = useState(0)
	
	useEffect(() => {
		// guardamos en interval la función setInterval. setInterval indica a setTimer que sume 1 a timer cuando pasen los 1000 milisegundos indicados en su segundo parámetro
		const interval = setInterval(() => {
			setTimer(timer => timer + 1)
		}, 1000)
		
		return () => {
			// al desmontar el component con clearInterval detenemos la ejecución de setInterval que guardamos en interval
			clearInterval(interval)
		}
	}, [])
	
	return (
		<div>
			{/* el hook vuelve a mostrarse cada vez que timer cambia su valor por la ejecución de setTimer */}
			HookTimer - {timer} -
			{/* si queremos detener el intervalo, mediante un botón, tenemos que poder acceder al lugar donde está guardada la función setInterval, que es interval, pero esta es una variable local de useEffect */}
			<button onClick={() => clearInterval(interValRef.current)}>Clear Timer</button>
		</div>
	)
}

export default HookTimer
```

Para solucionarlo declaramos una variable como useRef y en su atributo current guardamos la ejecución de setInterval.

```js
import React, {useState, useEffect, useRef} from 'react'

function HookTimer() {
	const [timer, setTimer] = useState(0)
	const interValRef = useRef()
	
	useEffect(() => {
		// guardamos el llamado a setInterval en el atributo current en la referencia interValRef
		interValRef.current = setInterval(() => {
			setTimer(timer => timer + 1)
		}, 1000)
		
		return () => {
			// con clearInterval detenemos la ejecución de setInterval que guardamos en interValRef
			clearInterval(interValRef.current)
		}
	}, [])
	
	return (
		<div>
			HookTimer - {timer} -
			{/* si queremos detener el intervalo tenemos que poder acceder al lugar donde está guardada la función setInterval, para eso usamos la referencia interValRef */}
			<button onClick={() => clearInterval(interValRef.current)}>Clear Timer</button>
		</div>
	)
}

export default HookTimer
```
