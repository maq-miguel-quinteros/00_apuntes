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

Una tupla es un array. Una tupla es inmutable, es decir, los datos que definimos en una tupla no se pueden modificar. Los elementos de las tuplas los definimos entre paréntesis en lugar de corchetes.

```py3
tupla = ('Python', 'Django', 'React', 'Vue')
print(tupla)
```

Si una tupla cuenta con un solo elemento, debe finalizar con coma y luego el cierre del paréntesis.

```py3
tupla = ('Python', )
print(tupla)
```

Para acceder a un elemento de una tupla utilizamos los corchetes `[]` indicando su índice. El uso de valores negativos es igual al de las listas. Al ser inmutables tratar de asignar un nuevo valor a un elemento de una tupla mediante su índice dará un error.

```py3
tupla = ('Python', 'Django', 'React', 'Vue')
print(tupla[1])
print(tupla[-2])

tupa[1] = 'Java' # dará un error
```

## Diccionarios

Son similares a los objetos. Sus elementos cuentas con dos partes una clave y un valor, o `key` y `value`, donde la clave va entre comillas y el valor respeta la forma de escribir el tipo de dato que sea.

```py3
dictionary = {
    'name': 'Miguel',
    'last_name': 'Quinteros',
    'age': 39
}
print(dictionary)
```

Para acceder a un elemento en particular del diccionario utilizamos los corchetes `[]` indicando dentro la clave que queremos consultar.

```py3
dictionary = {
    'name': 'Miguel',
    'last_name': 'Quinteros',
    'age': 39
}
print(dictionary['name'])
print(f"Mi nombre es: {dictionary['name']}")
```

Para añadir elementos a un diccionario solo debemos indicar entre los corchetes el nombre de la clave que agregamos y asignarle un valor.

```py3
dictionary = {
    'name': 'Miguel',
    'last_name': 'Quinteros',
    'age': 39
}
dictionary['city'] = 'San Miguel de Tucumán'
print(dictionary)
```

Para eliminar un elemento del diccionario utilizamos la palabra reservada `del`.

```py3
dictionary = {
    'name': 'Miguel',
    'last_name': 'Quinteros',
    'age': 39
}
del dictionary['age']
print(dictionary)
```

Para conocer la cantidad de claves con que cuenta el diccionario, es decir, conocer el tamaño del diccionario, utilizamos la función `len`.

```py3
dictionary = {
    'name': 'Miguel',
    'last_name': 'Quinteros',
    'age': 39
}
print(len(dictionary))
```

# Entrada y salida de datos

Para ingresar datos desde la terminar utilizamos la función `input()`, tenemos que asignar esta función a una variable para poder trabajar después con lo ingresado. La cadena que pasamos como parámetro a la función `input()` se va a mostrar en la consola antes de capturar el valor de entrada.

```py3
name = input('Ingresa tu nombre: ')
print(f'El nombre ingresado es: {name}')
```

Los valores capturados por `input()` se guardan de forma automática como `String`. Para poder realizar operaciones numéricas tenemos que convertir los valores a números mediante la función `int()`.

```py3
num1 = input('Ingres el primer valor: ')
num2 = input('Ingres el segundo valor: ')

result = int(num1) + int(num2)

print(f'La suma de los valores es: {result}')
print(f'La suma de los valores es: {int(num1) + int(num2)}')
```

# Control de datos

Cuando introducimos los datos por pantalla, que por defecto se guardan como `String` en la variable, podemos convertirlos en el tipo de dato que necesitemos utilizar. Mediante `int()` podemos convertir lo que ingresa por `input()` en un dato numérico entero.

```py3
num1 = int(input('Ingres el primer valor: '))
num2 = int(input('Ingres el segundo valor: '))

print(f'La suma de los valores es: {num1 + num2}')

```

Los tipos de datos a los que podemos convertir lo que ingresa por input son:

* Enteros: `int()`.

* Decimales: `float()`.
* Booleanos: `bool()`.
* Cadenas (String): `str()`.

Para el caso de `bool()`, si el valor que ingresa en `input()` es 0 el valor de la variable será `False`, si ingresa otro valor será `True`

# Condicionales

## Condicional if, else e if not

Cuando utilizamos condicionales como `if`, `else`, o `if not`, para indicar el código que se encuentra dentro del condicional utilizamos el espacio de la tecla tab.

```py3
age = int(input('Ingresa la edad: '))

if age >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
```

Para excluir valores mediante el condicional `if` podemos negar el valor a comprar mediante `!=` o utilizar `if not`. En el ejemplo solo las van a ser excluidos cuando `age` sea 16.

```py3
age = int(input('Ingresa la edad: '))

if age != 16:
    print('Puede pasar')

# funciona de la misma forma que el if anterior
if not age == 16:
    print('Puede pasar')
```

## Condicionales anidados

Para anidar los `if` seguimos utilizando el espacio de tab para indicar el código que pertenece a cada nivel de `if`. El máximo de anidaciones recomendables es de 3 `if`.

```py3
age = int(input('Ingresa la edad: '))
month = int(input('Ingresa el número del mes de nacimiento: '))

if age >= 18:
    print('Es mayor de edad')
    if month == 1:
        print('Naciste en enero')
    elif month == 2:
        print('Naciste en febrero')
    elif month == 3:
        print('Naciste en marzo')
else:
    print('Es menor de edad')
    if month > 3:
        print('Naciste después de marzo')
```

# Bucles

## Bucle for

Utilizamos `for` indicando una variable donde guarda el elemento sobre el que itera en ese momento y mediante `in` indicamos la lista o el iterable que vamos a recorrer. En el ejemplo, cada vez que itera el valor del elemento se guarda en `num`.

```py3
numbers = [1, 55, 88, 43, 4, 7, 9, 0, 22]

for num in numbers:
    print(num)
```

Si queremos crear una lista genérica de elementos, para iterar en, por ejemplo, el bucle `for`, utilizamos la función `range()`. En el ejemplo se crea una lista que va del 0 y que ocupa 20 elementos, es decir, los valores de esos elementos van del 0 al 19, que en total suman los 20 elementos.

```py3
list20 = range(0,20)
print(list20)

for item in list20:
    print(f'valor de item: {item}')
```

## Bucle while

Mediante `for` podemos recorrer un iterable. Mediante `while` podemos generar un bucle que va a suceder hasta que se cumpla una condición de salida. Para establecer la condición de salida podemos utilizar con contador.

```py3
count = 1

while count <= 10:
    print(f'Valor de count: {count}')
    count = count + 1

```

# Clases y objetos

## Clases

Para crear una nueva clase utilizamos la palabra reservada `class`. Si la clase va a quedar sin atributos ni métodos, es decir, vacía, utilizamos la palabra reservada `pass`. La clase vacía representaría los planos del objeto.

```py3
class Person:
    pass
```

Para crear un objeto de la clase que declaramos, es decir, crear una instancia de la clase, en la asignación de valor de la variable llamamos a la clase como si fuera una función.

```py3
class Person:
    pass

person1 = Person()
```
