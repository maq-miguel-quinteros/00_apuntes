# Creando un entorno virtual

En python tenemos dependencias que se instalan con `pipin`. Podemos instalar estas dependencias de forma global, por lo que van a estar disponibles en todos los proyectos que realicemos aunque no las necesitemos para ese proyecto, o podemos instalarlas en un entorno virtual, donde las dependencias se van a instalar puntualmente para ese proyecto. Si los proyectos se realizan en, por ejemplo, distintas versiones de `Django` o de alguna librería, al tenerlos en entornos virtuales evitamos problemas de compatibilidad entre versiones de esas librerías.

Par crear el entorno virtual, en la carpeta donde vamos a trabajar con el proyecto, desde la consola indicamos lo siguiente. `venv` indica que estamos creando un entorno virtual, `envs` es la carpeta, dentro de la carpeta del proyecto, donde vamos a crear el entorno virtual. Lo guardamos en una carpeta por que es posible que, para el mismo proyecto, podamos tener varios entornos. Lo siguiente es el nombre de la carpeta del entorno propiamente dicho.

```shellscript
python -m venv venvs/venvs_basic_example_01
```

Para activar el entorno y poder, por ejemplo, instalar las dependencias del proyecto, tenemos que ejecutar el archivo activate, desde la carpeta del proyecto utilizamos el siguiente comando. Al hacerlo la consola va a mostrar, en el path anterior a la linea donde ingresamos los comandos algo parecido a `(venvs_basic_example_01)->carpeta_proyecto`, indicando que estamos en el entorno virtual.

```shellscript
venvs/venvs_basic_example_01/Scripts/activate
```

# Creando un proyecto Django

## Diferencia entre proyecto y app de Django

No es lo mismo un proyecto de Django a una aplicación o app de Django. El proyecto Django es todo lo que engloba al proyecto que estamos realizando, y dentro de ese proyecto podemos tener apps. Una app de Django es una parte del proyecto que se encarga de algo específico, por ejemplo, una app blog que se encarga de recibir y publicar post en el proyecto de una web que además cuenta con un catálogo para comprar. La epp blog solo se encarga de una parte del proyecto total.

## Instalación

Después de ingresar en nuestro entorno virtual mediante `activate` instalamos Django con el comando `pip3`, que es un comando de pypi. Pypi es un gestor de paquetes de Python. Al usar `pip3` estamos indicando que la versión de python sobre la que va a instalar el paquete es la 3. Este comando instala Django en el entorno virtual.

```shellscript
pip3 install django
```

Para conocer las dependencias que tenemos instaladas en el entorno virtual utilizamos el siguiente comando. Entre las dependencias que nos devuelve va a aparecer Django con su versión.

```shellscript
pip3 freeze
```

## Crear un nuevo proyecto

Para crear un nuevo proyecto de Django utilizamos el siguiente comando. La carpeta del nuevo proyecto se va a crear en la carpeta general del proyecto y va a aparecer junto a la carpeta `envs` de los entornos virtuales. Dentro de la carpeta creada, con el nombre del proyecto, vamos a encontrar un archivo `manage.py`, con comandos que podemos utilizar desde la consola, y otra carpeta con el nombre del proyecto que va a ser la carpeta raíz del mismo, es decir, que todo el código perteneciente al proyecto se va a ordenar en esta carpeta.

```shellscript
django-admin startproject nombre_proyecto .
```

Cuando creamos el nuevo proyecto se crea una carpeta con el nombre del proyecto que creamos, esta carpeta es una app que se crea por defecto. Dentro de la carpeta del proyecto, donde aparece el archivo manage.py van a aparecer las carpetas correspondientes a cada una de las app que creemos mas adelante.

# AdminPanel de Django

Para conocer los comandos que tenemos disponibles con el proyecto Django, dentro de la carpeta del nuevo proyecto, ejecutamos el siguiente comando. Esto nos devuelve un listado de comandos que vamos a utilizar para gestionar el proyecto.

```shellscript
python manage.py help
```

## Iniciar el servidor

El proyecto que creamos en Django requiere de un servidor para poder ejecutarse. Cuando el mismo está listo para pasar a producción deberá ser compilado y subido a un servidor. Para poder hacer pruebas antes de esta etapa podemos utilizar el comando `runserver` que nos permite emular un servidor y probar el funcionamiento del proyecto.

```shellscript
python manage.py runserver
```

Es posible que al ejecutar el comando por primera vez nos devuelva un error, indicando que es necesario hacer las migraciones. Para solucionar el error ejecutamos el siguiente comando. Este comando lo que hace es crear todas las tablas en la base de datos que maneja el proyecto. Con Django no vamos a trabajar directamente con estas tablas, vamos a crear un modelos con clases que, mediante el comando `migrate` Django va a convertirlas en tablas de una base de datos. Django por defecto usa SQLite como base de datos.

```shellscript
python manage.py migrate
```

El comando nos devuelve una IP con un puerto que, si la ejecutamos en el navegador, nos va a devolver la página por defecto del proyecto, que de momento no tiene nada por lo que solo va a ser una página de prueba de Django. A la IP y puerto que nos devuelve `runserver` tenemos que sumarle `/admin` para ingresar al AdminPanel de Django. Dentro de AdminPanel vamos a poder gestionar los usuarios de nuestro proyecto y las diferentes apps que va a tener el mismo.

## Crear un super user

Una vez que ingresamos al AdminPanel de Django vemos que nos pide un usuario y contraseña. Para crear un usuario y contraseña que tenga todos los permisos de administración del proyecto, es decir, un super usuario utilizamos el siguiente comando. A continuación nos va a solicitar un nombre de usuario, un mail y una contraseña.

```shellscript
python manage.py createsuperuser
```

# Leer SQLite

Para trabajar con la base de datos SQLite, que Django crea por defecto, utilizamos el software [DB Browser for SQLite](https://sqlitebrowser.org/).

# Partes del proyecto Django

## Aplicaciones

Creamos una app que vamos a utilizar para gestionar los post dentro del blog. Creamos la nueva aplicación o app con el siguiente comando donde posts es el nombre de la aplicación que estamos creando. Se genera una nueva carpeta en la raíz del proyecto con el nombre de la app que creamos.

```shellscript
python manage.py startapp posts
```

Una vez creada la nueva app tenemos que indicar en el proyecto que esta app existe. Para hacerlo, en la carpeta de la app por defecto, que se crea cuando creamos el proyecto, en este caso es my_blog, editamos el archivo `settings.py` y agregamos a la lista `INSTALLED_APPS` el nombre de la nueva app que creamos.

```py3
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts'
]
```

## Vistas

Django esta creado para crear una web completa, tango backend como frontend. Por este motivo permite configurar vistas, acorde con el paradigma modelo-vista-controlador. Para crear una vista, para la aplicación posts, dentro de la carpeta de esta app, editamos el archivo `views.py`. A modo de ejemplo importamos las vistas genéricas que nos facilita Django.

```py3
# Se utiliza para crear una respuesta http a pedido get, post, put etc
from django.http import HttpResponse

# Lo utilizamos para poder generar una vista con los métodos que ofrece como el método get
from django.views.generic.base import View

class HelloWord(View):
    # Redefinimos el método get de View para generar una respuesta
    def get(self, request):
        # La respuesta a una llamada get desde el navegador va a ser una vista (página) de momento con solo el texto Hola mundo
        return HttpResponse(content='Hola Mundo')
```

Para que esta vista sea la respuesta a, en el ejemplo una petición `GET`, tenemos que configurar la ruta de esa vista. Para configurar la ruta editamos el archivo `url.py`, en la carpeta de la app principal del proyecto llamada `my_blog`.

```py3
from django.contrib import admin
from django.urls import path

# Importamos la vista que creamos en la app posts
from posts.views import HelloWord

urlpatterns = [
    path('admin/', admin.site.urls),

    # Configuramos un nuevo path, en este caso cuando está vacío y le indicamos que renderice la clase HelloWord como una vista con as_view()
    path('', HelloWord.as_view()),

    # También podemos indicar una ruta específica para esa app
    path('posts/', HelloWord.as_view()),
]
```

### Templates

Para crear un template, es decir, una plantilla que va a utilizar la vista que creamos, dentro de la carpeta de la app donde se encuentra la vista, que en el ejemplo es la carpeta posts, creamos una nueva carpeta llamada `template`. Dentro de esta carpeta creamos un archivo `.html` que será uno de nuestros templates. Modificamos el archivos `views.py` y, mediante el método `render` indicamos que renderice el template cuando se haga una llamada al path que configuramos previamente para la petición http get.

```py3
from django.http import HttpResponse

# Mediante render convertimos el template en la respuesta a la petición http get
from django.shortcuts import render

from django.views.generic.base import View

class HelloWord(View):
    def get(self, request):
        # El método render va a buscar, de forma automática, el template que indicamos en el segundo parámetro en la carpeta con nombre templates, es decir, si guardamos los templates en una carpeta con ese nombre no es necesario indicar la ruta exacta en el segundo parámetro
        return render(request, 'hello_word.html')
```

### Pasar variables con datos desde la vista al template

Lo que pasamos, mediante el método `render` a un template para generar una vista se llama contexto. A la variable que utilizamos para ese contexto podemos llamarla `data` o `context` o de cualquier forma, en el ejemplo la vamos a llamar `context`.

```py3
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWord(View):
    def get(self, request):
        
        # Creamos un diccionario con datos, pero el mismo puede venir de una clase de python en otro archivo etc.
        context = {
            'name': 'Miguel Ángel Quinteros',
            'age': 39,
            'languages': ['Python', 'Django', 'React']
        }

        # Pasamos los datos que queremos que se utilicen en el template como un tercer parámetro de un atributo del método render llamado context
        return render(request, 'hello_word.html', context=context)
```

Para que los datos que pasamos mediante el parámetro `context` del método `render` sean renderizados en el template y aparezcan cuando hacemos una petición http get a ese path tenemos que modificar el html del template de la siguiente forma.

```html
<body>
    <h1>Hola Mundo</h1>

    <!-- Utilizamos {{ name }} para indicar que en ese espacio tiene que mostrar el contenido de la variable name que viene en el context -->
    <p>Mi nombre es {{ name }}</p>
    <p>Tengo {{ age }}</p>
    <h3>Lenguajes</h3>

    <!-- Mediante {% code %} indicamos que lo contenido en ese espacio es código de python que utilizamos para renderizar varios componentes o para discriminarlos mediante un if -->
    {% for language in languages %}
        <li>{{ language }}</li>

    <!-- indicamos con endfor que termina la ejecución del for que va a mostrar la lista de lenguajes -->
    {% endfor %}
</body>
```

## Modelos


