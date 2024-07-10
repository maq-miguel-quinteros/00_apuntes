# useEffect

El _hook_ `useEffect` nos permite realizar efectos secundarios en componentes de función. Este proceso se realiza en tres momentos diferentes, correspondientes al ciclo de vida de un componente.
1. Cuando el componente es creado: _componentDidMount_.
2. Cuando se actualiza el estado del componente: _componentDidUpdate_.
3. Cuando el componente es destruido: _componentWillUnmount_.

El _hook_ debe desplegarse dentro del componente de función, de esta forma tiene acceso a las variables de estado de la función y se ejecuta cada vez que el componente es renderizado.

El _hook_ recibe como parámetros una función, que en general declaramos dentro del _hook_, como una función flecha, y un array de variables de estado que, al modificarse y volver a renderizar el componente, indican al _hook_ que debe volver a ejecutarse.

```javascriptreact
useEffect (()=>{ // función o función flecha como primer argumento
	console.log("hola") // lo que se realiza cuando se ejecuta el hook
	return () => { // lo que se realiza cuando el componente se desmonta, cierra o borra
		console.log("adios")
	}
}, [var1, var2]) // variables de estado que, al modificarse, hacen que se ejecute el hook
```

## useEffect después de renderizar

Llamamos al _hook_ `useEffect` y le pasamos como argumento una función flecha con la que indicamos lo que debe realizar. En el ejemplo vamos a cambiar lo que está escrito en el título de la página:

```javascriptreact
useEffect( () => { 
    document.title = 'Nuevo título';
})
```

Con esta sintaxis estamos indicando que `useEffect` se ejecute cada vez que se renderiza el componente donde se encuentra. Es decir, se ejecuta cuando el componente es creado y cuando se actualiza su estado. En el siguiente ejemplo tenemos un atributo de estado llamado `count` que actualiza su valor al hacer clic en un botón. Cuando el componente se crea, con el atributo de estado `count` con valor 0, y cada vez que el valor de este atributo se actualiza, el _hook_ `useEffect` se ejecuta cambiando el valor del texto en el título de la ventana.

```javascriptreact
import React, { useState, useEffect } from 'react'

export const HookCounterOne = () => {

	const [count, setCount] = useState(0)
    
	useEffect(() => {
		// cada vez que se renderiza el componente se ejecuta el useEffect hook cambiando document.title
		document.title = `You clicked ${count} times`
    })
    
	return (
		<div>
			{/* al modificar la variable de estado con setCount el componente vuelve a renderizarse */}
			<button onClick={() => setCount(prevCount => prevCount + 1)}>
				Click {count} times
			</button>
		</div>
	)
}
```

## useEffect con ejecución condicional

Para evitar problemas de performance, y cuando no necesitamos que useEffect se ejecute cada vez que se renderiza el componente donde lo utilizamos, es que podemos condicionar su ejecución. Para condicionar la ejecución del hook utilizamos el segundo parámetro que pasamos al mismo, que es un _array_ de variables de estado que, al modificarse, y generar un nuevo renderizado del componente, pueden también indicar que se realice una nueva ejecución del hook.

```javascriptreact
import React, { useState, useEffect } from 'react'

function HookCounterOne() {
	const [count, setCount] = useState(0)
	const [name, setName] = useState('')

	useEffect(() => {
		// el useEffect hook solo se ejecuta cuando se modifica la variable de estado count
		console.log('useEffect - Updating document title ')
		document.title = `You clicked ${count} times`
	}, [count]) // array de variables de estado que indican al hook cuando debe ejecutarse

	return (
		<div>
			{/* al modificar la variable de estado con setName hacemos que el componente vuelva a renderizarse */}
			<input type="text" value={name} onChange={e => setName(e.target.value)} />
			
			{/* al modificar la variable de estado con setCount el componente vuelve a renderizarse */}
			<button onClick={() => setCount(count + 1)}>
				useEffect - Click {count} times
			</button>
		</div>
	)
}

export default HookCounterOne
```

## useEffect que se ejecuta solo una vez

Para indicar que un hook useEffect se ejecute solo la primera vez que se renderiza el componente, y no en los subsiguientes renderizados, indicamos como segundo parámetro un array vacío `[]`. El componente se renderiza por primera vez cuando ingresamos en la página o cuando actualizamos el navegador con F5. Al ser componentes reactivos, si cambian sus variables de estado, el componente vuelve a renderizarse con el nuevo estado, pero solo el componente, no la página en su totalidad, por ende este no cuenta como un nuevo renderizado que pueda hacer que el useEffect vuelva a ejecutarse, si se declaro como un hook que se ejecuta solo una vez.

```javascriptreact
import React, { useState, useEffect } from 'react'

function HookMouse() {
	const [x, setX] = useState(0)
	const [y, setY] = useState(0)

	// logMousePosition recibe un evento y actualiza las variables de estado x e y con la ubicación del mouse
	const logMousePosition = e => {
		console.log('Mouse event')
		setX(e.clientX)
		setY(e.clientY)
	}

	useEffect(() => {
		console.log('useFffect called')
		// mediante addEventListener indicamos que, para el evento mousemove se llame a la función logMousePosition
		window.addEventListener('mousemove', logMousePosition)

	// el array vacío [] indica que el useEffect solo debe ejecutarse la primera vez que se renderiza el componente
	}, []) 

	return (
		<div>
			Hooks - X - {x} Y - {y}
		</div>
	)
}

export default HookMouse
```

## Ejecutar un código al desmontar un componente con useEffect

Cuando desmontamos un componente, es decir, lo quitamos de dom, si teníamos código ejecutándose, como por ejemplo un `addEventListener`, el mismo fue llamado por un componente que ya no existe, lo que genera errores. Para solucionar esto, mediante el `return` del hook useEffect, podemos indicar, por ejemplo con una función flecha, que un código final se ejecute antes de borrar el componente del DOM, mediante este código final podemos terminar con la ejecución `addEventListener`.

```javascriptreact
import React, { useState, useEffect } from 'react'

function HookMouse() {
	const [x, setX] = useState(0)
	const [y, setY] = useState(0)

	const logMousePosition = e => {
		console.log('Mouse event')
		setX(e.clientX)
		setY(e.clientY)
	}

	useEffect(() => {
		console.log('useFffect called')
		window.addEventListener('mousemove', logMousePosition)

		// indicamos al useEffect que hacer cuando el componente sea desmontado, es decir borrado del DOM
		return () => {
			console.log('Component unmounting code')
			// mediante removeEventListener indicamos que, para el evento mousemove, ya no se llame a la función, es decir, removemos el EventListener
			window.removeEventListener('mousemove', logMousePosition)
		}
	}, [])

	return (
		<div>
			Hooks - X - {x} Y - {y}
		</div>
	)
}

function MouseContainer() {

	const [display, setDisplay] = useState(true)

	return (
		<div>
			{/* al modificar la variable de estado con setDisplay conseguimos que el componente HookMouse se desmonte, es decir, se borra o quita de la pantalla, dejamos de verlo */}
			<button onClick={() => setDisplay(!display)}>Toggle display</button>

			{/* si display es true muestra el componente HookMouse */}
			{display && <HookMouse />}
		</div>
	)
}

export default MouseContainer
```

## useEffect con dependencias incorrectas

Cuando utilizamos funciones declaradas afuera del hook useEffect puede pasar que algunas de las dependencias de esa función no estén consideradas dentro del hook por lo cual el mismo no funcione correctamente. 

```javascriptreact
import React, {useState, useEffect} from 'react'

function IntervalHookCounter() {
	const [count, setCount] = useState(0)

	// la función tick utiliza la variable de estado count y la modifica, es necesario indicar al hook useEffect que considere ese cambio en count para volver a ejecutarse
	const tick = () => {
		setCount(count + 1)
	}
	
	useEffect(() => {
		// mediante setInterval indicamos que se ejecute la función tick cada 1000 milisegundos
		const interval = setInterval(tick, 1000)
		return () => {
			// mediante clearInterval indicamos que deje de ejecutarse setInterval en interval
			clearInterval(interval)
		}
	}, [count]) //cuando cambia count, dentro de la función tick, vuelve a ejecutarse el hook
	
	return (
		<div>
			{count}
		</div>
	)
}

export default IntervalHookCounter
```

## fetch datos de una API con useEffect


Vamos a realizar el fetch de datos mediante `axios`. Primero instalamos `axios` mediante el comando `npm install axios`. Después de instalarlo `axios` debería aparecer entre las dependencias dentro del archivo `package.json`.

Hacemos un llamado a una API mediante el método `get` de `axios`. El método `get` devuelve una promesa que resolvemos con `then` si el llamado es exitoso. Si el llamada devuelve un error lo capturamos con el método `catch`.

Vamos a utilizar la API de prueba [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com).

Si utilizamos el método `get` para el link [jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts), nos va a devolver un array de 100 objetos. Podemos guardar este array en un estado y después, mediante `map`, recorrerlo.

```javascriptreact
import React, { useState, useEffect } from 'react'
// importamos axios
import axios from 'axios'

function DataFetching() {
	// inicializamos posts como un array vacío ya que luego va a recibir un array
	const [posts, setPosts] = useState([])

	useEffect(() => {
		axios
			// llamamos a la api para traer el array con 100 posts
			.get('https://jsonplaceholder.typicode.com/posts')
			// si el llamado es exitoso
			.then(res => {
				console.log(res)
				// guardamos los datos en la variable de estado post
				setPosts(res.data)
			})
			// si el llamado no es exitoso capturamos el error
			.catch(err => {
				console.log(err)
			})
	}, [])

	return (
		<div>
			<ul>
				{/* mediante map recorremos el array de 100 posts y mostramos su título */}
				{posts && posts.map(post => (
					// un map siempre tiene que contar con la prop id con un valor único para ese componente
					<li key={post.id}>{post.title}</li>
				))}
			</ul>
		</div>
	)
}

export default DataFetching
```

También podemos llamar a la API solicitando el valor de solo 1 post mediante su id.

```javascriptreact
import React, { useState, useEffect } from 'react'
import axios from 'axios'

function DataFetching() {
	// inicializamos post como un objeto vacío ya que luego va a recibir un objeto
	const [post, setPost] = useState({})
	const [id, setId] = useState(1)
	const [idFromButtonClick, setIdFromButtonClick] = useState(1)

	useEffect(() => {
		axios
			// llamamos a la API y, de todos los post, traemos el post con id el valor de la variable de estado id
			.get(`https://jsonplaceholder.typicode.com/posts/${id}`)
			.then(res => {
				console.log(res)
				setPost(res.data)
			})
			.catch(err => {
				console.log(err)
			})
	}, [idFromButtonClick]) // indicamos ejecutar el useEffect cuando se modifique la variable de estado idFromButtonClick

	const handleClick = () => {
		setIdFromButtonClick(id)
	}

	return (
		<div>
			{/* guarda lo que ingresamos en la caja de texto en la variable de estado id */}
			<input type="text" value={id} onChange={e => setId(e.target.value)} />
			
			{/* llama a la función handleClick cuando se hace clic en el botón */}
			<button type="button" onClick={handleClick}>Fetch Post</button>
			<div>{post.title}</div>
		</div>
	)
}

export default DataFetching
```

## fetch de datos de una API con useEffect y useState para mostrar loading y error

```javascriptreact
import React, {useState, useEffect} from 'react'
import axios from 'axios';

function DataFetchingOne() {
	// declaramos las variables de estado que van a manejar los tres momentos, loading, success y error
	const [loading, setLoading] = useState(true)
	const [error, setError] = useState('')
	const [post, setPost] = useState({})

	useEffect(() => {
		axios
			.get(`https://jsonplaceholder.typicode.com/posts/1`)
			.then(response => {
				// cambiamos el valor de la variable de estado loading a false para que deje de mostrarse el mensaje Loading en la pantalla
				setLoading(false)
				setPost(response.data)
				// limpiamos la variable de estado error por si quedó con algún valor de una carga anterior
				setError('')
			})
			.catch(error => {
				setLoading(false)
				// limpiamos la variable de estado post por si quedo con algún valor de una carga anterior
				setPost({})
				setError('Something went wrong!, error: '+ error)
			})
	}, [])

	return (
		<div>
			{/* mientras se traen los datos va a mostrar el mensaje loading, al ejecutarse el then en el useEffect va a mostrar el valor del atributo title de la variable de estado post */}
			{loading ? 'Loading' : post.title}
			{/* si hay un error al traer los datos en catch indicamos guardar el log del error en la variable de estado error que se muestra solo si su valor no es '' */}
			{error ? error : null}
		</div>
	)
}

export default DataFetchingOne
```
