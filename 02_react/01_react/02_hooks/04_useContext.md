# useContext

El hook useContext permite pasar datos, como variables, desde un componente padre de un nivel superior, a componentes hijos de hijos, es decir, a componentes que están varios niveles inferiores en el árbol de componentes. En lugar de pasar los datos como props a un hijo y que ese hijo lo pase como props al siguiente, y así sucesivamente, hasta llegar al componente que requiere esa información, utilizamos el hook useContext.

## ReactContext

Revisamos primero como funciona reactContext. Para el ejemplo utilizamos App.jsx y tres archivos de componentes anidados. Donde App es padre de ComponentC, ComponentC es padre de ComponentD y ComponentD es padre de ComponentE

Archivo `App.jsx`:

```javascriptreact
import React from 'react'
import ComponentC from './components/ComponentC'

// creamos dos componentes como componentes de contexto, que permiten pasar datos a traves del árbol de componentes
export const NameContext = React.createContext()
export const LastNameContext = React.createContext()

function App() {
	return (
		<div className="App">
			{/* encerramos a ComponentC como hijo de UserContext y pasamos la información como prop */}
			<NameContext.Provider value={'Miguel'}>
				{/* si necesitamos pasar mas de un dato anidamos los contextos */}
				<LastNameContext.Provider value={'Quinteros'}>
					<ComponentC />
				</LastNameContext.Provider>
			</NameContext.Provider>
		</div>
	)
}

export default App
```

Archivo `ComponentC.jsx`:

```javascriptreact
import React from 'react'
import ComponentE from './ComponentE'

function ComponentC() {
	return <ComponentE />
}
export default ComponentC
```

Archivo `ComponentE.jsx`:

```javascriptreact
import React from 'react'
import ComponentF from './ComponentF'

function ComponentE() {
	return <ComponentF />
}
export default ComponentE
```

Pasamos por varios componentes que llaman a otros componentes, hasta que llegamos al ComponentF, que va a utilizar los datos del contexto que declaramos en App.

Archivo `ComponentF.jsx`:

```javascriptreact
import React from 'react'
import { NameContext, LastNameContext } from '../App'

function ComponentF() {
	return (
		<div>
			{/* encerramos en el component NameContext el código que va a utilizar los datos que vienen desde App */}
			<NameContext.Consumer>
				{/* denominamos name al valor que tiene value en NameContext en App. Para poder utilizar el valor usamos una función flecha */}
				{name => {
					{/* al tener contextos anidados en App tenemos que hacer un return y dentro utilizar el componente del siguiente contexto */}
					return (
						<LastNameContext.Consumer>
							{lastname => {
								return <div>User name value {name}, lastname context value {lastname}</div>
							}}
						</LastNameContext.Consumer>
					)
				}}
			</NameContext.Consumer>
		</div>
	)
}

export default ComponentF
```

## Consumir los valores de elementos de contexto mediante el hook useContext

La declaración de los componentes de contexto es la misma que realizamos en el archivo App. De igual forma encerramos a los componentes que van a poder consumir esos contextos dentro de los componentes de contexto y asignamos en value los datos que queremos que puedan ser consultados.

Archivo `ComponentF.jsx`:

```javascriptreact
import React, { useContext } from 'react'
import { NameContext, LastNameContext } from '../App'

function ComponentF() {
	// asignamos a las variables lo que el contexto devuelve de su prop value	
	const name = useContext(NameContext)
	const lastname = useContext(LastNameContext)

	return ( 
		<div>
			Name is {name} and lastname is {lastname}
		</div>
	)
}

export default ComponentF
```
