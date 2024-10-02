# Instalación

Para conocer la versión de python que tenemos instalada. En una terminal o consola de comandos ejecutamos el comando `python3 --version`.

# Ejecutar un fichero de python

La extensión de los archivos de python es `py`. Mediante la función `print()` podemos imprimir un mensaje en la consola. Para ejecutar un archivo de python desde la consola usamos el comando `python3 rutaArchivo\nombreArchivo`.

Cuando creamos un nuevo proyecto de python desde un IDE como PyCharm o Visual Studio Code, en la carpeta del proyecto, se crea un archivo `main.py`, que es desde donde vamos a iniciar la ejecución de nuestro proyecto.

# Comentarios

```py3
# Comentarios de una línea
""""
Comentarios que
ocupan varias
líneas
"""
```

# Variables

## Declaración de variables

Las variables se declaran indicando el nombre de la variables y el valor de la misma. No es necesario indicar el tipo de la variable en la declaración.

```py3
name = 'Miguel'

"""
Características de la variable
id      -> name
type    -> String
value   -> Miguel
"""
```

Para mostrar el valor de una variable por consola utilizamos la función `print()`.

```py3
print(name)
```

Los nombres (id) de las variables comienzan siempre con una letra o un guión bajo (_). Los nombres de las variables no pueden empezar con un número. Por convención a los nombres de variables compuestos de varias palabras los separamos por guión bajo. Ej. `last_name`. Las variables en python son `key sensitive`, es decir, se diferencia mayúsculas de minúsculas. Ej. no es lo mismo `name` que `Name` o que `nAme`. 

## Números

Las variables numéricas son las que contienen valores numéricos, tanto enteros como decimales. Sobre estas variables podemos realizar las operaciones aritméticas de `suma (+)`, `resta (-)`, `multiplicación (*)`, `división (/)`, `resto (%)`, `potencia (**)`, `un resultado entero (//)`. Las operaciones se realizan como en los calculos matemáticos, de izquierda a derecha, realizando primero lo que esté entre paréntesis `()`, después potencia y enteros, después multiplicaciones u divisiones, y finalmente suma y resta.

```py3
num1 = 15
num2 = 3
result = num1 + num2
print(result)
```

## Cadenas

Las variables que guardan cadenas de caracteres, para el asignación de valor utilizamos comillas dobles ("") o simples (''). Si queremos que dentro de la cadena haya comillas, para no generar un error, utilizamos el otro tipo de comillas que no estamos utilizando para la asignación.

```py3
name1 = "Miguel "Ángel" Quinteros" # error de sintaxis
name2 = 'Miguel "Ángel" Quinteros'
print(name2)
```

Para combinar 2 variables de tipo String utilizamos el operador +

```py3
name = 'Miguel'
last_name = 'Quinteros'
full_name = name + ' ' + last_name
print('Me llamo: ' + full_name)
```

Para trabajar con cadenas de texto, sin la necesidad de utilizar el operador + para concatenar las variables, utilizamos una f antes de las comillas y a las variables las encerramos entre llaves. Dentro de las llaves podemos podemos agregar también operaciones aritméticas como `{edad + 3}`, la función `print()` en este caso va a devolver el resultado de la operación cuando muestre el String.

```py3
name = 'Miguel'
last_name = 'Quinteros'
age = 39
print(f'Me llamo {name} {last_name} y tengo {age} años.')
```

Si necesitamos mostrar en más de una ocasión el mismo String mediante `print()`, utilizamos el operador de multiplicación (*).

```py3
name = 'Miguel'
print(name * 5)
```

## Listas o colecciones

Una lista es un array. Dentro de la lista podemos tener variables de distintos tipos como números, cadenas, booleanos, otras listas u otros tipos avanzados. Para acceder a un elemento de la lista lo hacemos mediante el nombre de la lista y entre corchetes `[]` el número de indice del elemento que buscamos comenzando desde 0. Así el primer elemento de la lista es el de indice 0, el segundo elemento de la lista es indice 1, etc.

```py3
list = ['Python', 'Django', 'React', 'Vue']
print(list[0])
```

Para acceder al último elemento de la lista, cuando no sabemos el valor del indice del mismo, utilizamos -1. Mediante esta notación de valores negativos podemos acceder al ante último elemento de la lista con el valor de indice -2 y así contando desde atrás hacia adelante.

```py3
list = ['Python', 'Django', 'React', 'Vue']
print(list[-1])
print(list[-3])
```

Para modificar un elemento de la lista simplemente le asignamos un nuevo valor al elemento con indicando su índice.

```py3
list = ['Python', 'Django', 'React', 'Vue']
print(list)

list[1] = 'Flutter'
print(list)
```

Para agregar un elemento a la lista utilizamos el método `append()`. El elemento se va a agregar al final de la lista.

```py3
list = ['Python', 'Django', 'React', 'Vue']
print(list)

list.append('Angular')
print(list)
```

Para agregar un elemento en medio de otros elementos de la lista utilizamos el método `insert()`. El método recibe 2 parámetros, el primero indica que número de índice va a temer el elemento que agregamos, el segundo parámetro es el elemento que vamos a agregar en la lista.

```py3
list = ['Python', 'Django', 'React', 'Vue']
print(list)

list.insert(2, 'Angular')
print(list)
```

## Tuplas

Una tupla es un array
