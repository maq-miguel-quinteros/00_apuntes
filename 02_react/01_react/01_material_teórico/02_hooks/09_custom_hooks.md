# Custom Hooks


¿Que es un custom hook?

- Un custom hook es una función de JavaScript que empieza con el nombre **use**.

- Un custom hook puede llamar a otros hooks si lo necesita.

¿Para qué utilizamos custom hooks?

- Para utilizar la lógica de estos hooks en diferentes componentes.


## useDocumentTitle


Para almacenar los custom hooks que creamos utilizamos una carpeta dentro de la carpeta **src** llamada **hooks**.

En esta carpeta creamos un nuevo archivo llamado `useDocumentoTitle.js` donde vamos a crear la lógica de ese custom hook. Al ser una función de JavaScript, y no devolver jsx, no necesitamos llamar al archivo con extensión jsx. Este hook recibe una variable como parámetro y actualiza el título de la página con el valor de esa variable.

`useDocumentTitle.js`


```js
import { useEffect } from 'react'

function useDocumentTitle(count) {
	useEffect(() => {
		document.title = `Count ${count}`
	}, [count])
}

export default useDocumentTitle
```

Utilizamos el custom hook en nuestro componente. Cuando el componente se renderize por primera vez, y cuando vuelva a renderizarse, llamamos al hook.

`DocTitleOne.jsx`:


```js
import React, { useState } from 'react'

// importamos el custom hook
import useDocumentTitle from '../hooks/useDocumentTitle';

function DocTitleOne() {
	const [count, setCount] = useState(0)

	// llamamos al hook cuando se actualiza el valor de count
	useDocumentTitle(count)

	return (
		<div>
			{/* actualizamos el valor de count */}
			<button onClick={() => setCount(count + 1)}>Count - {count}</button>
		</div>
	)
}

export default DocTitleOne
```

## useCounter


Creamos un custom hook llamado useCounter. Este recibe como parámetros un initialCount, que si no está presente es igual a 0, y un valor para hacer el incremento. El hook devuelve el valor de la variable de estado `count` y tres funciones: `increment`, `decrement` y `reset` que utilizamos para manipular `count`.

`useCounter.js`:


```js
import { useState } from 'react'

function useCounter(initialCount = 0, value) {
	const [count, setCount] = useState(initialCount)

	const increment = () => {
		setCount(prevCount => prevCount + value)
	}

	const decrement = () => {
		setCount(prevCount => prevCount - value)
	}

	const reset = () => {
		setCount(initialCount)
	}

	return [count, increment, decrement, reset]
}

export default useCounter
```

Mediante el custom hook creamos botones para incrementar un contador utilizando la variable de estado y las funciones que devuelve el custom hook.

`CounterOne.jsx`:


```js
import React from 'react'
import useCounter from '../hooks/useCounter'

function CounterOne() {

	// llamamos a useCounter y le pasamos 0 a initialCount y 1 a value como parámetro
	const [count, increment, decrement, reset] = useCounter(0, 1)

	return (
		<div>
			{/* utilizamos la variable de estado count que devuelve el custom hook useCounter */}
			<h2>Count = {count}</h2>
			{/* utilizamos los métodos que devuelve el custom hook useCounter */}
			<button onClick={increment}>Increment</button>
			<button onClick={decrement}>Decrement</button>
			<button onClick={reset}>Reset</button>
		</div>
	)
}

export default CounterOne
```

## useInput


El custom hook useInput recibe como parámetro un valor y devuelve una variable de estado, un objeto (con un atributo y un método) y una función que afecta a la variable de estado.

`useInput.js`:


```js
import { useState } from 'react'

function useInput(initialValue) {
	const [value, setValue] = useState(initialValue)

	const reset = () => {
		setValue('')
	}

	// creamos un objeto llamado bind
	const bind = {
		value, // esto es lo mismo que decir value: value,
		onChange: e => { // onChange es una función que recibe e (un evento) como parámetro
			setValue(e.target.value)
		}
	}

	// devolvemos la variable de estado value, el objeto bind y la función reset
	return [value, bind, reset]
}

export default useInput
```

Utilizamos useInput para manejar los input que ingresamos desde el código HTML.

`UserForm.jsx`:

```js
import React, { useState } from 'react'
import useInput from '../hooks/useInput';

function UserForm() {
	// con el custom hook useInput reemplazamos esta línea const [firstName, setFirstName] = useState('')

	// mediante el custom hook useInput creamos la variable de estado value que llamamos firstName, el objeto bind que llamamos bindFirstName y la función reset que llamamos resetFirstName
	const [firstName, bindFirstName, resetFirstName] = useInput('')
	const [lastName, bindLastName, resetLastName] = useInput('')

	const submitHandler = e => {
		e.preventDefault()
		alert(`Hello ${firstName} ${lastName}`)

		// limpiamos el contenido de la caja de texto input en la pantalla
		resetFirstName()
		resetLastName()
	}
	return (
		<div>
			<form onSubmit={submitHandler}>
				<div>
					<label>First Name</label>
					<input
						type="text"
						{/* el objeto bindFirstName contiene "value:value, onChange:e=>setValue(e.target.value)", esto es lo mismo que indicar en el HTML value={value} y onChange={e=>setValue(e.target.value)}. Utilizamos el spread operador para indicar que tiene que desestructurarse el valor del objeto bindFirstName en los atributos HTML del tag input */}
						{...bindFirstName}
					/>
				</div>
				<div>
					<label>Last Name</label>
					<input
						type="text"
						{...bindLastName}
					/>
				</div>
				<button>Submit</button>
			</form>
		</div>
	)
}

export default UserForm
```
