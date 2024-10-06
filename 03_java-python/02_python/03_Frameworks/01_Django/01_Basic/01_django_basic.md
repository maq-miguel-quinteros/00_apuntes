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
