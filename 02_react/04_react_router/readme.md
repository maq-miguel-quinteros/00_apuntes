# Instalación React Router v6.4

Hacemos la instalación mediante el comando.

```shellscript
npm install react-router-dom
```

En caso de existir una versión 7 de react-router instalamos la versión 6.4 mediante el comando.

```shellscript
npm install react-router-dom@6.4
```

# Agregamos el enrutador _router_

## Carpeta `pages` (páginas)

Vamos a guardar las páginas de nuestro proyecto en una carpeta dentro de la carpeta `src`. Nombramos a esta carpeta `pages`. Dentro de esta carpeta vamos a tener componentes de react para cada una de las páginas con nombres como `Home.jsx`, `About.jsx` o `Blog.jsx`. 

## Carpeta `routers` (enrutadores)

Vamos a guardar el enrutador en una carpeta dentro de la carpeta `src`. Vamos a nombrar a esta carpeta `routers`. Dentro de la carpeta `routers` creamos un nuevo archivo llamado `index.jsx`. Llamamos al archivo `index.jsx` para que, cuando traigamos su contenido desde otro archivo, no tengamos la necesidad de indicar el nombre del mismo.

Dentro del archivo `index.jsx` vamos a exportar una constante a la cual le asignamos el método `createBrowserRouter()` de `react-router-dom`. Este método recibe un array de objetos donde cada objeto va a representar una ruta de nuestro proyecto.

```javascriptreact
// importamos las funciones y hooks de react-router-dom
import { createBrowserRouter } from 'react-router-dom'

// importamos los componentes que utilizamos en las rutas
import Home from '../pages/Home'
import About from '../pages/About'
import Blog from '../pages/Blog'

export const router = createBrowserRouter([
    {
        // la ruta por defecto se configura mediante /
        path: '/',
        // cuando vayamos al path / va a devolver el elemento de react que configura la página Home
        element: <Home />
    },
    {
        path: '/about',
        element: <About />
    },
    {
        path: '/blog',
        element: <Blog />
    }
])
```

## Configuración de `main.jsx`

Editamos el archivo `main.jsx` dentro de la carpeta `src`. Configuramos el enrutador que creamos indicando que nuestra app se va a configurar en base a este archivo. Para hacer esto vamos a envolver nuestra app mediante un proveedor (`provider`). Descartamos de esta manera el uso del archivo `App.jsx` que podemos borrar.

```javascriptreact
// otras importaciones

// importamos el proveedor que permite envolver la app y de esta manera trabajar mediante el enrutador
import { RouterProvider } from 'react-router-dom'

// importamos el enrutador. No necesitamos indicar que tiene que buscar en index.jsx por llamarse index este archivo
import { router } from './routers'

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>,
)
```

# Hook `useRouterError`

Cuando tratamos de ingresar en una ruta que no está configurada o que no existe, al trabajar con `createBrowserRouter` nos va a devolver una página de error por defecto de esta nueva API. Podemos controlar la página que se muestra cuando existe un error en la ruta a la que se accede, así como también los datos que se devuelven del error. para hacerlo utilizamos el hook `useRouterError`.

Dentro de la carpeta `pages` creamos un nuevo componente de react al que llamamos `NotFound.jsx`.

```javascriptreact
import { useRouteError } from 'react-router-dom'

export default NotFound = () => {

    const error = useRouteError()

    return 'Página no encontrada'
}
```

`index.jsx` dentro de `routers`

```javascriptreact
// otras importaciones
import Blog from '../pages/Blog'

import NotFound from '../pages/NotFound'

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Home />,
        // mediante el atributo errorElement indicamos la página que se va a mostrar en caso de error al ingresar en la ruta /
        errorElement: <NotFound />
    },
    {
        path: '/about',
        element: <About />,
        errorElement: <NotFound />
    },
    {
        path: '/blog',
        element: <Blog />,
        errorElement: <NotFound />
    }
])
```
