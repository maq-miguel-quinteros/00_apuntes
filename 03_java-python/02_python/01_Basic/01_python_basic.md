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

## Objetos

Para crear un objeto de la clase que declaramos, es decir, crear una instancia de la clase, en la asignación de valor de la variable llamamos a la clase como si fuera una función. Lo que estamos haciendo es construir un objeto de esa clase. Para que el objeto tenga atributos y métodos tenemos que declararlos en la definición de la clase.

```py3
class Person:
    name = ''
    last_name = ''
    age = 0 # 0 va a ser el valor por defecto del objeto que creamos, si no le damos nosotros un valor al crearlo

person1 = Person()
print(person1) # vemos como está identificado el objeto coche y a que valor en memoria apunta

print(person1.name) # vemos el contenido del atributo name que es un string vacío
```

Para dar valores a los atributos del objeto cuando lo creamos tenemos que definir en la clase el método `__init__()`. Para hacer esta definición utilizamos la palabra reservada `def`. Dentro de los parámetros que acompañan al método `__init__()` siempre tenemos que indicar primero `self`. Vamos a utilizar `self` para acceder a los atributos propios de la clase que vayamos a modificar mediante `__init__()` cuando construyamos un nuevo objeto de esa clase.

```py3
class Person:
    name = ''
    last_name = ''
    age = 0

    def __init__(self, name, last_name, age):
        self.name = name # self.name refiere a la variable name definida al comienzo de la clase mientras que name refiere al parámetro del método __init__()
        self.last_name = last_name
        self.age = age

person1 = Person()
print(person1) 

print(person1.name) 
```

Cuando vayamos a crear el objeto, cuando llamamos a la clase entre los paréntesis damos valores a los parámetros que indicamos en `__init__()` en el orden en que fueron declarados. Esto no aplica para el parámetro `self`, el cual no recibe ningún valor.

```py3
class Person:
    name = ''
    last_name = ''
    age = 0

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

person1 = Person('Miguel', 'Quinteros', 39)
print(person1) 
print(person1.name)

person2 = Person('Daniela', 'Diaz', 37)
print(person2) 
print(person2.last_name)
```

Para cambiar el valor de alguno de los atributos de un objeto creado, solo le asignamos el nuevo valor seleccionando el nombre del atributo del objeto mediante la notación de punto `.`.

```py3
class Person:
    name = ''
    last_name = ''
    age = 0

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

person1 = Person('Miguel', 'Quinteros', 39)
print(person1) 
print(person1.name)

person1.name = 'Ángel'
print(person1) 
print(person1.name)
```

Para agregar más atributos a la clase lo hacemos en la definición de la misma.

```py3
class Person:
    name = ''
    last_name = ''
    age = 0
    phone = 0

    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone

person1 = Person('Miguel', 'Quinteros', 39, 3815355225)
print(person1) 
print(person1.phone)
```

Podemos no declarar los nombres de los atributos al comienzo de la clase y declararlos directamente en el método `__init__()`.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone

person1 = Person('Miguel', 'Quinteros', 39, 3815355225)
print(person1) 
print(person1.phone)
```

## Métodos

Mediante los métodos añadimos funciones a nuestros objetos, es decir, cosas que pueden hacer.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone
    
    def say_hello(self):
        print(f'Hola, mi nombre es {self.name}')

    def say_hello_to_someone(self, someone_name)
        print(f'Hola {someone_name}, mi nombre es {self.name}')


person1 = Person('Miguel', 'Quinteros', 39, 3815355225)
person1.say_hello()

person1.say_hello_to_someone('Daniela')
```

# Encapsulamiento

Cuando encapsulamos un atributo de una clase, lo que hacemos es evitar que pueda accederse a ese atributo por fuera de la clase. Solo se puede acceder o modificar estos atributos mediante métodos de la clase que creamos previamente.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone
    
    def say_hello(self):
        print(f'Hola, mi nombre es {self.name}')

person1 = Person('Miguel', 'Quinteros', 39, 3815355225)

person1.name = 'Angel' # podemos modificar el valor del atributo desde fuera de la clase
person1.say_hello()


```

Para encapsular los atributos de una clase, cuando declaramos el atributo los hacemos con dos guiones bajos `__` previos al nombre del mismo. En el ejemplo el atributo `other_phone`, al no tener los dos guión bajo puede ser accedido desde fuera del objeto

```py3
class Person:
    __name = ''
    __last_name = ''
    __age = 0
    __phone = 0

    def __init__(self, name, last_name, age, phone, other_phone):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.other_phone = other_phone

    def say_hello(self):
        print(f'Hola, mi nombre es {self.__name}, y mi otro teléfono es {self.other_phone}')

person1 = Person('Miguel', 'Quinteros', 39, 3815355225, 4271907)

person1.name = 'Angel' # dará un error
person1.__name = 'Angel' # dará un error
person1.other_phone = '0303456' # funciona correctamente 

person1.say_hello()

```

# Herencia

Una clase hijo hereda de una clase padre. Para indicar la herencia, en la declaración de la clase hijo, mediante paréntesis, indicamos cual es la clase padre desde la que va a heredar. Heredar implica que la clase hijo va a contar con todos los atributos u métodos de la clase padre, va a poder redefinir estos y va a poder tener los suyos propios. En el ejemplo utilizamos los atributos, el constructor `__init__` y el método `say_hello` de la clase `Person` en la clase `Client`.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone
    
    def say_hello(self):
        print(f'Hola, mi nombre es {self.name}')

class Client(Person):
    pass

client1 = Client('Miguel', 'Quinteros', 39, 3815355225, 4271997)
client1.say_hello()
```

Para agregar atributos al constructor de `Client` redefinimos el método `__init__`. En el mismo vamos a seguir utilizando los atributos de `Person` pero le vamos a sumar atributos propios de `Client`.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone
    
    def say_hello(self):
        print(f'Hola, mi nombre es {self.name}')

class Client(Person):
    corporate_phone = 0

    def __init__(self, name, last_name, age, phone, corporate_phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.corporate_phone = corporate_phone
    
    def say_corporate_phone(self):
        print(f'Hola, mi nombre es {self.name} y mi teléfono corporativo es {self.corporate_phone}' )

client1 = Client('Miguel', 'Quinteros', 39, 3815355225, 4271997)
client1.say_hello()
client1.say_corporate_phone()
```

# Herencia múltiple

Para realizar la herencia múltiple solo tenemos que agregar una coma `,` y la siguiente clase desde la que queremos heredar en la definición de la clase hijo.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone    
    def say_hello(self):
        print(f'Hola, mi nombre es {self.name}')
class Male:
    pass

class Female:
    __pregnant: false
    def set_pregnant(self, pregnant):
        self.__pregnant = pregnant

class Client(Person, Female):
    corporate_phone = 0
    def __init__(self, name, last_name, age, phone, corporate_phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.corporate_phone = corporate_phone    
    def say_corporate_phone(self):
        print(f'Hola, mi nombre es {self.name} y mi teléfono corporativo es {self.corporate_phone}' )

client1 = Client('Daniela', 'Diaz', 37, 3815355225, 4271997)
client1.say_hello()
client1.say_corporate_phone()
client1.set_pregnant(True)
```

# Importaciones

Podemos guardar las clases relacionadas con `Person`, o solamente la clase `Person` en un archivo `.py` y hacer lo mismo con cada una de las clases. Cuando necesitamos utilizar la clase, sus atributos y métodos la podemos importar.

En un archivo `person.py` vamos a guardar los siguiente.

```py3
class Person:
    def __init__(self, name, last_name, age, phone):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone    
    def say_hello(self):
        print(f'Hola, mi nombre es {self.name}')

class Female:
    __pregnant: false
    def set_pregnant(self, pregnant):
        self.__pregnant = pregnant
```

En el archivo `main.py` importamos la clase `Person`. Si indicamos `import person` traemos todo el contenido del archivo `person.py` que además de la clase `Person` puede contener otras cosas que no nos interesan. Para importar solo la clase utilizamos la palabra reservada `from`. Si necesitamos importar más de una clase del mismo archivo podemos utilizar una coma en la sentencia del `from import`

```py3
from person import Person, Female

class Client(Person, Female):
    pass

client1 = Client('Daniela', 'Diaz', 37, 3815355225, 4271997)
client1.say_hello()
client1.set_pregnant(True)
```

En caso de encontrarse dentro de carpetas las clases que queremos importar utilizamos la notación de punto de la forma `from Class.Persons.person import Person, Female`.
