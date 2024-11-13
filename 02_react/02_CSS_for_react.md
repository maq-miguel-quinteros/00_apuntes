# Cómo instalar Tailwind Css en un proyecto de Vite Js con React | Pedro Lara


Video: [Instalar](https://www.youtube.com/watch?v=tuBirltzAAk)


## Instalación


```shellscript
npm init vite@latest
npm install -D tailwindcss postcss autoprefixer
## crea los archivos de configuración
npx tailwindcss init -p
```

## Configuración


En el archivo `tailwind.config.js` configuramos las rutas donde vamos a utilizar tailwindcss

```js
/** @type {import('tailwindcss').Config} */
export default {
	// indicamos que los estilos de taildwindcss se van a utilizar en index.html u em todos los componentes que creemos dentro del src 
	content: [
		"./index.html",
		"./src/**/*.{js,ts,jsx,tsx}",
	],
	theme: {
		extend: {},
	},
	plugins: [],
}
```

En `index.css` dentro de la carpeta `src` agregamos las directivas de taildwindcss

```tailwindcss
/* configuramos las directivas */
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
	font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
	line-height: 1.5;
	font-weight: 400;
	/* otros estilos */
}

/* otras reglas de estilo */
```

# React y TailwindCSS - Dark Theme, cambio de tema

Video: [react y tailwind](https://www.youtube.com/watch?v=_8FTL-xNz9Q)

Podemos indicar que la web que creamos con los estilos de taildwindcss mantenga el modo dark o light los estilos del sistema donde estamos (Windows, android) y también podemos crear un botón para el cambio del estilo de la página.

Agregamos el darkMode a la configuración de tailwindcss, en el archivo `tailwind.config.js` y le indicamos que lo vamos a manejar mediante clases.

```js
/** @type {import('tailwindcss').Config} */
export default {
	content: [
		"./index.html",
		"./src/**/*.{js,ts,jsx,tsx}",
	],
	/* agregamos el modo oscuro a la configuración del proyecto */
	darkMode: 'class',
	theme: {
	extend: {},
	},
	plugins: [],
}
```

En el componente principal de nuestra app, en general el componente `App.jsx`, o en el botón que va a controlar el cambio de modo, configuramos el modo oscuro.

```javascriptreact
import { useEffect, useState } from "react";

export default function Header() {

    const [theme, setTheme] = useState(() =>{
		// window.matchMedia('(prefers-color-scheme: dark)').matches devuelve true si el esquema de colore del SO es dark
        if (window.matchMedia('(prefers-color-scheme: dark)').matches){
            return 'dark'
		} else return 'light'
    })

	// al cambiar el valor de la variable theme agrega o quita la clase dark de body según corresponda
    useEffect(()=> {
        if(theme === 'dark'){
            document.querySelector('body').classList.add('dark')
        }else{
            document.querySelector('body').classList.remove('dark')
        }
    }, [theme])

	// al hacer click en el botón cambia la variable theme a light o dark
    const handleChangeTheme = () => {
        setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light')
    }

    return(
		<>
			{/* al agregarse la clase dark al body los estilos indicados como dark:style se van a aplicar */}	
			<div className="h-screen flex justify-center items-center text-4xl				
							dark:bg-neutral-900">
			
				<button className="rounded px-4 py-2
								bg-slate-200 hover:bg-slate-400
								dark:bg-slate-950 dark:hover:bg-slate900 dark:text-white"
                onClick={handleChangeTheme}>Change Theme
				</button>
			
			</div>
		</>
	)
}
```
