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
// importamos los
import { useRouteError, Link } from 'react-router-dom'

export default NotFound = () => {

    // hacemos a la variable error igual a lo que devuelve el hook useRouteError
    const error = useRouteError()

    // la página que vamos a devolver en caso de error
    return (
        <div>
            <h2>404</h2>
            <p>Page not found</p>
            <p>{ error.statusText || error.message }</p>

            {/* Mediante Link podemos indicar un link con una ruta a la cual volver */ }
            <Link to='/'>Volver a Home</Link>
        </div>
    )
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

# Rutas anidadas

Podemos tener una página _layout_, es decir, una página que sea el template base de todas las otras páginas, y de todas las rutas, podemos utilizar rutas anidadas para que cada una de las páginas, y sus rutas, se carguen en base a ese _layout_.

Creamos una nueva carpeta en la carpeta `src`. Llamamos a esa carpeta `layouts`. Creamos un nuevo componente dentro de la carpeta que vamos a llamar, como ejemplo, `LayoutPublic.jsx`.

```javascriptreact
import { Outlet } from 'react-router-dom'

const LayoutPublic = () => {
    return (
        <>
            <nav>Navbar</nav>

            {/* Mediante el componente Outlet indicamos que todo lo que figure en children, en el archivo de rutas, se va a renderizar en ese componente y a mostrarse en el espacio que ocupa ese elemento en la página que devuelve el componente LayoutPublic */}
            <Outlet />
            <footer>Footer</footer>
        </>
    )
}
export default LayoutPublic
```

`index.jsx` dentro de `routers`

```javascriptreact
// otras importaciones
import NotFound from '../pages/NotFound'

import LayoutPublic  from './layouts/LayoutPublic'

export const router = createBrowserRouter([
    {
        path: '/',
        element: <LayoutPublic />,
        // todos los elementos del array children van a compartir el errorElement
        errorElement: <NotFound />,

        // cuando accedamos a alguno de los path de los children, su element se va a renderizar en el componente Outlet dentro del elemento LayoutPublic
        children: [
            {
                // path: '/',
                // mediante index: true indicamos que el elemento home se corresponde con el path: '/' del objeto con ese path y con LayoutPublic como element
                index: true,
                element: <Home />,
            },
            {
                path: '/about',
                element: <About />,
            },
            {
                path: '/blog',
                element: <Blog />,
            }
        ]
    },
    
])
```

# NavBar con `NavLink`

Creamos una carpeta para los componentes de las páginas en la carpeta `src`. Nombramos a la carpeta `components`. Dentro de `components` creamos un nuevo componente para manejar la navbar que llamamos `NavBar.jsx`. Mediante el componente `NavLink`, que importamos de `react-router-dom`, configuramos el navbar de la página. `NavLink` tiene la ventaja de detectar cual es la ruta activa cuando estamos en alguna de ellas y le coloca la clase active a los estilos del link. Si la clase active no está creada en los estilos del proyecto no va a tener efecto. Si queremos tener clases personalizadas tenemos el atributo `isActive` del componente `NavLink` que podemos configurar para eso.

```javascriptreact
import { NavLink } from 'react-router-dom'

export default function NavBar() {

    return(
        <nav>
            <NavLink to='/'>Home</NavLink>
            <NavLink to='/blog'>Blog</NavLink>
            <NavLink to='/about'>About</NavLink>
        </nav>
    )
}
```

`LayoutPublic.jsx` dentro de `layouts`

```javascriptreact
import { Outlet } from 'react-router-dom'

// traemos el navbar al layout para que aparezca en todas las páginas de las rutas configuradas 
import NavBar from '../components/NavBar'

const LayoutPublic = () => {
    return (
        <>
            <NavBar />
            <Outlet />
            <footer>Footer</footer>
        </>
    )
}
export default LayoutPublic
```

# _Fetching_ con `Loader` y `useLoaderData`

Para hacer el fetching mediante `Loader` y `useLoaderData` primero tenemos que generar y exportar una función que sea la encargada de hacer el fetching. Por convención llamamos a esta función `loaderElement`. La función la declaramos en el elemento que devuelve la página sobre la que vamos a cargar los datos. En el ejemplo lo hacemos sobre el elemento `Blog`.

```javascriptreact
const Blog = () => {
    return 'Blog'
}
export default Blog

export const loaderBlog = async () => {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts')
    const posts = await res.json()
    
    // retornamos en un objeto los posts. Al retornar {posts} es lo mismo que retornar {posts: posts}
    return {posts}
}
```

`index.jsx` dentro de `routers`

```javascriptreact
// otras importaciones
import LayoutPublic  from './layouts/LayoutPublic'

import Blog, { loaderBlog } from '../pages/Blog'

export const router = createBrowserRouter([
    {
        path: '/',
        element: <LayoutPublic />,
        errorElement: <NotFound />,
        children: [
            {
                index: true,
                element: <Home />,
            },
            {
                path: '/about',
                element: <About />,
            },
            {
                path: '/blog',
                element: <Blog />,
                // configuramos el atributo loader para el path /blog y el elemento Blog
                loader: loaderBlog
            }
        ]
    },
    
])
```

`Blog.jsx` dentro de `pages`

```javascriptreact
// mediante el hook useLoaderData vamos a recuperar lo que devuelve la función que pasamos al atributo loader de la configuración del path
import { useLoaderData } from 'react-router-dom'

const Blog = () => {

    // desestructuramos para recuperar los elementos del atributo posts que los pasamos como posts
    const { posts } = useLoaderData()

    return (
        
    )
}
export default Blog

export const loaderBlog = async () => {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts')
    const posts = await res.json()
    return {posts}
}
```
