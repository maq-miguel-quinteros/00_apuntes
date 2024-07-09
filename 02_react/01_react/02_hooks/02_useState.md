# useState

* El _hook_ `useState` es una función que permite añadir un estado a un componente de función.
* Los estados son atributos que pueden almacenar un valor de tipo  _number_, _string_, _boolean_, _object_ o _array_.
* El _hook_ `useState` devuelve dos elementos:
    1. el primer elemento es un estado con su valor por defecto. Ej. `name`.
    2. el segundo elemento es un método con el que podemos cambiar el valor del estado. Por convención a este método lo nombramos como `set` y el nombre del estado en mayúsculas. Ej. `setName`.
* Cuando llamamos al método _setter_ del estado, cambiando el valor del mismo, hacemos que el componente vuelva a renderizarse.

## Sintaxis y uso básico

Mediante el _hook_ `useState` generamos un atributo de estado que podemos utilizar en un componente de función. Solo podemos utilizar el _hook_ en un componente de función. Los _hooks_ no funcionan en componentes de clases. El atributo de estado, o simplemente estado, es un atributo que guarda un valor que podemos consultar y modificar durante el ciclo de vida del componente. Primero necesitamos importar la función o _hook_:

```javascriptreact
import { useState } from react;
```

Para crear un estado utilizamos el _hook_ `useState` inmediatamente después de la declaración del componente de función, antes de la declaración de otras funciones o del `return`, de la siguiente forma:

```javascriptreact
const [count, setCount] = useState(0);
```

En el ejemplo, mediante desestructuración, con la palabra reservada `const` creamos un atributo llamado `count`, que vamos a usar de contador, y un método llamado `setCount` para modificar este atributo. Como buena práctica utilizamos la forma _atributo_, _setAtributo_ a la hora de nombrar al atributo de estado y al método que lo modifica. El atributo `count` solo podrá ser modificado mediante el método `setCount`. Para crear estos asignamos al atributo y método el hook `useState` utilizando el `= useState(0)` y entre los `()` ingresamos el valor inicial del atributo `count` que en ejemplo es `0`. Un componente que muestra un botón con un contador reactivo se declara de la siguiente forma:

```javascriptreact
// importamos el hook
import { useState } from react;

export const HookCounter = () => {

    // creamos el atributo de estado, con valor inicial 0, y el método que lo modifica mediante el hook
    const [count, setCount] = useState(0);

    return (
        <>
            {/** al elemento de HTML button le asignamos un evento onClick. Cuando hacemos clic en el botón el evento llama a una función flecha que a su vez llama al método setCount. setCount suma 1 el valor que viene guardando el atributo de estado count */}
            <button onClick={() => setCount(count + 1)}>Count {count}</button>
        </>
    )
}
```

## Establecer estado basado en el estado anterior

Vamos a establecer el nuevo estado del atributo de estado, es decir, a cambiar el valor de este atributo, tomando como base el estado o valor que el atributo tenía previamente. Para hacer el cambio de valor de un atributo de estado, tomando como base el valor anterior, utilizamos el método que declaramos cuando llamamos al _hook_ `useState`, que en el ejemplo se hace de la siguiente forma:

```javascriptreact
setCount(count + 1);
```

Esta forma de actualizar el estado, en base a su valor anterior, no es una forma de trabajo segura. Para actualizar correctamente un atributo de estado en base a su valor anterior utilizamos la segunda forma de uso del método `set` que creamos al llamar al _hook_ `useState`, en nuestro ejemplo el método `setCount`, esta forma es pasando al método una función flecha que contemple el estado anterior y la actualización que hacemos sobre el mismo:

```javascriptreact
setCount((prevCount) => prevCount + 1);
```

La función flecha que pasamos tiene como parámetro la variable `prevCount` esta variable contiene el valor del atributo de estado `count` al momento de llamar a la función `setCount`. El `return` de la función flecha va a ser el valor actualizado del estado que finalmente `setCount` se encargará de guardar en `count`. Tenemos que realizar la actualización del estado de esta forma siempre que utilicemos en la actualización el valor anterior del mismo estado.

```javascriptreact
export const HookCounterTwo = () => {

    // utilizamos la variable initialCount para establecer el valor por defecto del atributo de estado count, y para volver a este cuando tocamos en el botón reset
    const initialCount = 0;
    const [count, setCount] = useState(initialCount);

    const incrementFiveNotWork = () => {
        for (let i = 0; i < 5; i++) {

            // utilizamos la forma poco segura para actualizar al valor del estado. En este ejemplo no se van a sumar 5 al valor del estado
            setCount(count + 1);
        }
    };

    const incrementFive = () => {
        for (let i = 0; i < 5; i++) {

            // el método setCount puede recibir una función flecha. El parámetro prevCount es el valor que tiene count en el momento de llamar a la función setCount
            setCount((prevCount) => prevCount + 1);
        }
    };

    return (
        <>
            Count: {count}

            {/** no utilizamos el valor anterior del estado en este caso, por ende no necesitamos pasar la función flecha al */}
            <button onClick={() => setCount(initialCount)}>Reset</button>

            {/** corregimos las funciones que pasamos en los eventos para realizar de forma correcta la actualización del estado */}
            <button onClick={() => setCount((prevCount) => prevCount + 1)}>Increment</button>
            <button onClick={() => setCount((prevCount) => prevCount - 1)}>Decrement</button>
            
            <button onClick={incrementFiveNotWork}>Not working increment 5</button>
            <button onClick={incrementFive}>Increment 5</button>
        </>
    );
};
```

## useState con objetos

A un atributo de estado podemos asignarle un valor de tipo _int_, _string_, _boolean_, _array_ u _object_ según se requiera. 

En el ejemplo asignamos al atributo de estado `name` un objeto con dos atributos `{firstName: '', lastName: ''}` ambos con su valor inicial como un _string_ vacío. Si queremos actualizar los valores de los atributos de este objeto de a uno a la vez de la forma:

```javascriptreact
setName({ firstName: 'Miguel' })
setName({ lastName: 'Quinteros' })
```

Vamos a notar que cuando actualizamos `firstName` el método `setName` en realidad lo que hace es borrar los atributos del objeto y asignar un nuevo objeto solo con el atributo `firstName` y el nuevo valor. En la siguiente línea `setName` borra el objeto y asigna un nuevo objeto solo con el atributo `lastName` y el nuevo valor. Esto sucede por que `setName` no fusiona y actualiza de forma automática el valor del atributo `name`. Para solucionar esto pasamos como argumentos al método `setName` el valor del atributo que queremos modificar utilizando el operador _spread_ `...` de la siguiente forma:

```javascriptreact
setName({ ...name, firstName: 'Miguel' })
setName({ ...name, lastName: 'Quinteros' })
```

Mediante el operador _spread_ indicamos al método `setName` que 'copie el valor de del atributo de estado name' y sobre este 'actualice el valor del atributo `firstName` o `lastName` del objeto según corresponda'. En el componente siguiente el método `setName` del `input` que actualiza el valor del nombre tiene la sintaxis correcta con el operador _spread_ mientras que el `setName` del `input` que actualiza el apellido tiene la sintaxis incorrecta:

```javascriptreact
import React, { useState } from 'react'

export const HookCounterThree = () => {

	// el valor por defecto del atributo name es un objeto con dos atributos inicialmente en blanco
	const [name, setName] = useState({ firstName: '', lastName: '' })

	return (
		<form>
			<input
				type="text"
				value={name.firstName}

				// mediante el parámetro e, de la función flecha, capturamos lo que se escribe en el input que tiene asociando el evento onChange. Indicamos al método setName que asigne al atributo firstName el valor del atributo e.target.value, que es lo que se escribió en la caja de texto del input
				onChange={e => setName({ ...name, firstName: e.target.value })}
			/>
			<input
				type="text"
				value={name.lastName}
				onChange={e => setName({ lastName: e.target.value })}
			/>
			<h2>Your first name is - {name.firstName}</h2>
			<h2>Your last name is - {name.lastName}</h2>

			{/** mediante JSON.stringify(name) podemos ver como se modifica el valor del atributo de estado name en la medida en que modificamos los valores de los atributos de su objeto */}
			<h2>{JSON.stringify(name)}</h2>
		</form>
	)
}
```

## useState con arreglos

De la misma forma en que trabajamos con los objetos vamos a utilizar el operador _spread_ para sumar elemento a un _array_. El _array_ puede ser estar compuesto de _number_, _string_, _boolean_, _object_ u otros _array_. En el código siguiente el botón 'Add a number' suma al _array_ un objeto con los atributos `id` y `value`. Mediante el operador _spread_ indicamos al método `setName` que 'copie el valor del atributo de estado `...items`' y le 'agregue' el objeto con los atributos mencionados antes.

```javascriptreact
import React, { useState } from 'react'

export const HookCounterFour = () => {
    
	// el valor por defecto de items va a ser un array vacío
	const [items, setItems] = useState([])

	const handlerAddItem = () => {

		// pasamos a setItems un array con ...items, que sería lo mismo a pasar todos los elementos que ya tiene el array contenido en el atributo de estado items, y luego el objeto que queremos agregar a este array
		setItems([
			...items,
			{
				id: items.length,
				value: Math.floor(Math.random() * 10) + 1
			}
		])
	}

	return (
		<div>
			<button onClick={handlerAddItem}>Add a number</button>
			<ul>
				{items.map(item => (
					<li key={item.id}>{item.value}</li>
				))}
			</ul>
		</div>
	)
}
```
