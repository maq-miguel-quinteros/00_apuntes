# React + TypeScript


## Instalación y estructura de carpetas


Creamos un nuevo proyecto de **React** con **Vite** mediante el comando `npm create vite@latest`. Vamos a trabajar con estructura donde el componente `App.tsx` va a contener cada una de las páginas, que van a hacer componentes, que vamos a declarar en una carpeta llamada _pages_, que creamos dentro de la carpeta _src_. Más adelante vamos a actualizar la estructura de carpetas y van a aparecer carpetas como _components_ o _types_ entre otras.


## useState


Dentro de la carpeta pages creamos el componente `UseStateComponent.tsx` que vamos a utilizar par explicar el uso del **hook useState**. Comenzamos creando un tipo de dato, para los datos de usuario con los que vamos a trabajar, mediante la palabra reservada `type`. Probamos asignado estos datos a una variable común y asignando los mismo a un estado.

```typescriptreact
import { useState } from "react"

// declaramos el tipo de dato llamado User, que es un objeto, con sus atributos y métodos
type User = {
	id: number,
	name: string,
	username: string,
	email: string
	show: boolean
}

export const UseStateComponent = () => {
	// creamos la variable user1, de tipo User, y le asignamos valores a sus atributos
	const user1: User = {
		id: 1,
		name: "Leanne Graham",
		username: "Bret",
		email: "Sincere@april.biz",
		show: true
	}

	// mediante <User> indicamos que el tipo de dato que puede recibir la variable de estado user va a ser de tipo User, luego le asignamos de forma explicita un usuario
	const [user, setUser] = useState<User>({
		id: 2,
		name: "Ervin Howell",
		username: "Antonette",
		email: "Shanna@melissa.tv",
		show: true
	})

	return (
		<div>
			<h2>useState hook</h2>
			{user1.show && <p>Variable user1 name: {user1.name}</p>}
			{user.show && <p>State user name: {user.name}</p>}
		</div>
	)
}
```

Podemos asignar datos a la variable de estado `user` de varias maneras.

```typescriptreact
// creamos una variable de tipo User
const user2 = {
	id: 2,
	name: "Ervin Howell",
	username: "Antonette",
	email: "Shanna@melissa.tv",
	show: true
}

// asignamos el valor de la variable user2 a la variable de estado user cuando llamamos al hook
const [user, setUser] = useState<User>(user2)
```

Podemos llamar al hook e indicar que la variable de estado no va a tener ningún valor hasta que no utilicemos la función `useUser`

```typescriptreact
const user2 = {
	id: 2,
	name: "Ervin Howell",
	username: "Antonette",
	email: "Shanna@melissa.tv",
	show: true
}

const [user, setUser] = useState<User>()

// mas adelante en alguna handleFunction le asignamos un valor a la variable de estado user
setUser(user2)
```

Si queremos que la variable de estado tenga un valor, por ejemplo un objeto vacío `{}` o `undefined`:

* Asignar un objeto vacío: `const [user, setUser] = useState<User>({})`. En este caso TypeScript no puede inferir el tipo de datos que tiene asignada la variable de estado user al momento de crearse. Funciona pero el código dará error.

* Asignar la palabra reservada `undefined`: `const [user, setUser] = useState<User>(undefined)`. En este caso TypeScript sabe que no está definido el tipo de dato que tiene asignada la variable de estado user al momento de crearse. Funciona pero el código dará error.

* Indicar que la variable de estado puede recibir, también, `undefined`: `const [user, setUser] = useState<User | undefined>(undefined)`. En este caso TypeScript sabe que el tipo de datos de la variable user puede ser User o undefined. Es decir, no estar definido.

```typescriptreact
const user2 = {
	id: 2,
	name: "Ervin Howell",
	username: "Antonette",
	email: "Shanna@melissa.tv",
	show: true
}

// mediante | indicamos cuales son los tipos de datos que puede recibir la variable de estado user
const [user, setUser] = useState<User | undefined>(undefined)

// mas adelante en alguna handleFunction le asignamos un valor a la variable de estado user
setUser(user2)
```

Código para probar todo lo visto:

```typescriptreact
import { useState } from "react"

type User = {
    id: number,
    name: string,
    username: string,
    email: string
    show: boolean
}

export const UseStateComponent = () => {

    const user1: User = {
        id: 1,
        name: "Leanne Graham",
        username: "Bret",
        email: "Sincere@april.biz",
        show:true
    }

    const user2: User = {
		id: 2,
		name: "Ervin Howell",
		username: "Antonette",
		email: "Shanna@melissa.tv",
		show: true
	}

    const [user, setUser] = useState<User>({
        id: 1,
        name: "Leanne Graham",
        username: "Bret",
        email: "Sincere@april.biz",
        show:true
    });

    const [userOne, setUserOne] = useState<User>();
    const [userTwo, setUserTwo] = useState<User | undefined>(undefined);

	


    return (
        <div>
            <h2>useState hook</h2>
			<p>Diferencia entre </p>
            {user1.show && <p>Variable user1 name: {user1.name}</p>}
            {user && <p>State user name: {user.name}</p>}

            <p><button onClick={() => setUserOne(user1)}>Test State userOne: <i>{"useState<User>()"}</i></button></p>
            {userOne && <p>State userOne name: {userOne.name}</p>}

            <p><button onClick={() => setUserTwo(user2)}>Test State userTwo: <i>{"useState<User | undefined>(undefined)"}</i></button></p>
            {userTwo!==undefined && <p>State userTwo name: {userTwo.name}</p>}

			
        </div>
    )
}
```

## useEffect


