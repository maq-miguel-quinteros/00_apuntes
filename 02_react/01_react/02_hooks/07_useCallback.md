# useCallback

Los componentes vuelven a renderizarse cuando sus variables de estado o sus props se modifican.

En ocasiones tenemos un componente padre, con distintas variables de estado y funciones. Pasamos estas variables de estado y funciones a distintos componentes hijos como props. En principio, cuando una variable de estado se modifica, esto genera que el componentes padre vuelva a renderizarse como así también el componente hijo que recibe esa variable de estado como prop. A su vez, si pasamos una función a un componente hijo, y desde este componente modificamos la variable de estado, esto genera que el componente hijo, que recibe la función vuelva a renderizarse junto con el componente padre y el componente hijo que recibe la variable de estado como prop. Si tenemos varias funciones distintas, que pasamos a distintos componentes hijos, cada vez que el componente padre vuelve a renderizarse, vuelve a crear las funciones que pasa a los componentes hijos, por lo que, en cada renderizado del padre, todos los componentes hijos que reciben funciones también vuelven a renderizarse. Este renderizado de componentes que no se modificaron ni interactuaron genera una baja en la performance de la app.

* Un componente padre tiene varias funciones distintas, que pasa como props a varios hijos distintos.

* El componente padre vuelve a renderizarse, a raíz de un cambio en una variable de estado o en una prop que recibe.

* Cuando el padre vuelve a renderizarse vuelve a crear las funciones que pasa a los componentes hijos mediante las prop.

* Los componentes hijos vuelven a recibir la función creada por el padre y, por ende, al tener un cambio en sus props, vuelven a renderizarse. No importa que la función que reciben sea la misma que recibieron en el primer renderizado, esta es una función que volvió a crear el componente padre, por ende es una función nueva.

Definimos el componente padre en el archivo `ParentComponent.jsx`:

```javascriptreact
import React, { useState } from 'react'
import Count from './Count'
import Button from './Button'
import Title from './Title'

function ParentComponent() {
	const [age, setAge] = useState(25)
	const [salary, setSalary] = useState(50000)

	// utiliza la variable de estado age
	const incrementAge = () => {
		setAge(age + 1)
	}

	// utiliza la variable de estado salary
	const incrementSalary = () => {
		setSalary(salary + 1000)
	}

	return (
		<div>
			<Title />
			<Count text="Age" count={age} />
			<Button handleClick={incrementAge}>Increment Age</Button>
			<Count text="Salary" count={salary} />
			<Button handleClick={incrementSalary}>Increment Salary</Button>
		</div>
	)
}

export default ParentComponent
```

Si ejecutamos el código y visualizamos la consola vemos que, en el primer renderizado nos muestra 5 console.log, el del renderizado del título, el del contador de age, el del botón para incrementar age, el del contador de salary y el del botón para incrementar salary. Al hacer clic, por ejemplo en el primer botón, solo deberían volver a renderizarse el contador de age y el botón para incrementar age, pero en su lugar vemos que vuelven a renderizarse los 5 componentes. Lo mismo sucede si tocamos el botón para incrementar salary.

Archivo `Title.jsx`:

```javascriptreact
import React from 'react'

function Title() {
	console.log('Rendering Title')
	return (
		<h2>
			useCallback Hook
		</h2>
	)
}

export default Title
```

Archvo `Count.jsx`:

```javascriptreact
import React from 'react'

function Count({ text, count }) {
	console.log(`Rendering ${text}`)
	return <div>{text} - {count}</div>
}

export default Count
```

Archivo `Button.jsx`:

```javascriptreact
import React from 'react'

function Button({ handleClick, children }) {
	console.log('Rendering button - ', children)
	return (
		<button onClick={handleClick}>
			{children}
		</button>
	)
}

export default Button
```

## React.memo(Component)

Si queremos evitar que un componente vuelva a renderizarse cuando no tuvo ningún cambio en sus variables de estado o en las props que recibe, en la declaración del componente utilizamos la función de alto nivel React.memo(Component) de la forma `export React.memo(Button)` por ejemplo.

## Indicamos cuando debe volver a renderizarse un elemento

el hook useCallback devuelve una versión en memoria de una función callback que solo cambia si alguna de las variables que le pasamos como dependencias cambia. Es decir, el componente que recibe una función, como prop, mediante el hook useCallback, solo va a volver a renderizarse si la variable que indicamos al hook como dependencia cambia.

El hook useCallback recibe dos parámetro, una función indicando qué es lo que debe hacer y un array de dependencias indicando cuando lo debe hacer, es decir, indicando ejecutar la función cuando alguna de las variables del array se modifique.

Utilizamos useCallback, generalmente, en funciones que pasamos a componentes hijos que pueden modificar estados.

Modificamos el archivo `ParentComponent.jsx`:

```javascriptreact
import React, { useState, useCallback } from 'react'
import Count from './Count'
import Button from './Button'
import Title from './Title'

function ParentComponent() {
	const [age, setAge] = useState(25)
	const [salary, setSalary] = useState(50000)

	// incrementAge se va a ejecutar solo cuando age se modifique. Al ejecutarse va a generar que el elemento que recibe esta función como prop vuelva a renderizarse
	const incrementAge = useCallback(() => {
		setAge(age + 1)
	}, [age])

	const incrementSalary = useCallback(() => {
		setSalary(salary + 1000)
	}, [salary])

	return (
		<div>
			<Title />
			<Count text="Age" count={age} />
			<Button handleClick={incrementAge}>Increment Age</Button>
			<Count text="Salary" count={salary} />
			<Button handleClick={incrementSalary}>Increment Salary</Button>
		</div>
	)
}

export default ParentComponent
```
