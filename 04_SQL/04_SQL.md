# Cláusula SELECT

## Básico y alias

La consulta mas simple que podemos realizar es `SELECT`, donde `Paises` es el nombre de la base de datos a la que hacemos la consulta. Mediante `SELECT` indicamos cuales son las columnas que queremos seleccionar. El `*` funciona como un comodín que indica que vamos a seleccionar todas las columnas de esa tabla.

```sql
SELECT * FROM Paises
```

Para el caso de querer consultar una columna llamada `Nombre` la sentencia quedaría como:

```sql
SELECT Nombre FROM Paises
```

Si son varias las columnas que queremos recuperar en la consulta las separamos por una coma `,` quedaría como:

```sql
SELECT Nombre, Codigo, Region FROM Paises
```

Para modificar el orden en que aparecen las columnas en la respuesta, simplemente modificamos el orden en que las llamamos en la consulta:

```sql
SELECT Codigo, Nombre, Region FROM Paises
```

Todas las instrucciones SQL soportan el salto de línea. El siguiente código dará el mismo resultado

```sql
SELECT Codigo,  
Nombre,  
Region  
FROM Paises
```

Cuando usamos la clausula `SELECT` podemos renombrar las columnas que la consulta devuelve indicándole una Alias. Para renombrar usamos la clausula `As`. El alias que indicamos solo puede tener una palabra. Si el nombre es compuesto utilizamos mayúsculas para cada parte (Ej. PrecioMayorista). El cambio de nombre aplica a la respuesta que trae la consulta. Esto no modifica el nombre de la columna en la tabla.

```sql
SELECT Codigo As ProductId,
        Nombre As ProductName,
        Region
FROM Paises
```

## Operadores aritméticos

En una instrucción SQL podemos realizar operaciones aritméticas entre columnas que lo permitan. Las columnas `Precio` y `Costo` del ejemplo son columnas con valores numéricos. El resultado de la operación lo vamos a mostrar en una nueva columna. Las operaciones que se admiten son suma (+), resta (-), multiplicación (*) y división (/).

```sql
SELECT Nombre,
        Precio,
        Costo,
        Precio - Costo As Ganancia
FROM Productos
```

También podemos agregar operaciones aritméticas que no impliquen solo columnas.

```sql
SELECT Nombre,
        Precio,
        Costo,
        Precio - Costo As Ganancia
        Precio + 10 As Interes
FROM Productos
```

También podemos utilizar paréntesis para las operaciones aritméticas que queremos realizar.

```sql
SELECT Nombre,
        Precio As PrecioMayorista,
        Costo,
        Precio - Costo As Ganancia
        Precio + (Precio * 20) / 100 As PrecioMinorista
FROM Productos
```

Podemos indicar a la cláusula `SELECT` que nos devuelva una cantidad acotada de filas de la consulta realizada. Para eso utilizamos la palabra reservada `TOP` con la cantidad de resultados que queremos traer

```sql
SELECT TOP 10
        Nombre,
        Precio As PrecioMayorista,
        Costo,
        Precio - Costo As Ganancia
        Precio + (Precio * 20) / 100 As PrecioMinorista
FROM Productos
```

## Cláusula DISTINCT

La cláusula `DISTINCT` se utiliza para eliminar duplicados. En el ejemplo tenemos el mismo `CodigoPais` para varias `ciudades`. Mediante `DISTINCT` indicamos que la respuesta solo devuelva una instancia del mismo `CodigoPais`, es decir, si varias `ciudades` tienen el mismo `CodigoPais`, la respuesta va a traer solo uno de ellos.

```sql
SELECT DISTINCT CodigoPais FROM Ciudades
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver Id y nombre de todas las categorias
-- Renombrarlas como Numero y Categoria
SELECT
        Id As Numero,
        Nombre As Categoria
FROM Categorias

```

### Ejercicio 2

Podemos concatenar datos de tipo String para conseguir un nuevo String. Para generar un alias que no sea solo una palabra podemos indicar el mismo entre comillas `''`

```sql
-- Devolver apellido, nombre y fecha de nacimiento de todos los clientes del sistema
-- Apellido y nombre en una única columna llamada Nombre Completo, Separados sus valores por una coma
SELECT
        Apellido + ', ' + Nombre As 'Nombre Completo',
        FechaNacimiento
FROM Clientes
```

### Ejercicio 3

```sql
-- Devolver Nombre, Costo, Precio
-- Costo con Descuento de 30%
-- Ganacia si el Costo tiene un descuento del 30%
-- Ganacia con costo regular
-- Ganancia con costo regular y un 10% de descuento
SELECT
        Nombre,
        Precio,
        Costo,
        (Costo - (Costo * 30) / 100) As CostoDescontado,
        (Precio - (Costo - (Costo * 30) / 100)) As GananciaConCostoDescontado
        Precio - Costo As GananciaRegular
        (Precio - Costo) - ((Precio - Costo) * 10 / 100) As GananciaConDescuento
FROM Productos
```

# Cláusula WHERE

La cláusula `WHERE` nos permite filtrar datos de una tabla. `WHERE` permite dar una condición a la búsqueda que realiza `SELECT` indicando que, cuando esta condición se cumple, la consulta devuelva los datos. En el ejemplo indicamos que seleccione todos los registros de la tabla clientes pero que devuelva solo los que cumplen con la condición de `Id=2`.

```sql
SELECT *
FROM Clientes
WHERE Id=2
```

## Operadores lógicos en números

También podemos indicar condiciones que representan un rango de registros. En el ejemplo se devuelven todos las filas con su columna Id con un valor mayor que 2. Los operadores que podemos usar son `=`, `>`, `<`, `>=` y `<=`.

```sql
SELECT *
FROM Clientes
WHERE Id>2
```

Cuando necesitamos que la búsqueda devuelva registros que son distintos de un valor en particular utilizamos `<>` o `!=`. En el ejemplo va a devolver los registros cuyo valor de Id sea distinto del valor 2.

```sql
SELECT *
FROM Clientes
WHERE Id<>2
```

## Operadores lógicos en fechas

Para comparar fechas en SQL utilizamos un texto con el formato `AAAAMMDD` que serian 4 caracteres para el año, 2 caracteres para el mes y 2 caracteres para el día. Por ejemplo el 1 de septiembre de 1985 se representa como `19850901`. De esta forma podemos utilizar todos los operadores lógicos en columnas con valores de fechas mediante la cláusula `WHERE`.

```sql
SELECT *
FROM Clientes
WHERE FechaNacimiento >= '19900101'
```

## Filtrar por valores de texto

La cláusula WHERE puede ser utilizada para comparar cualquier tipo de dato. En el caso de los datos de tipo texto compara cada uno de los caracteres que pasamos en la consulta y devuelve los que tienen el mismo valor en los registros de la tabla.

```sql
SELECT *
FROM Clientes
WHERE Apellido = 'Simon'
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver ClienteId y fecha de todas las ordenes realizadas hasta octubre del año 2017
SELECT
        ClienteId
        Fecha
FROM
        Ordenes
WHERE
        Fecha < '20171101'
```

### Ejercicio 2

```sql
-- Devolver Nombre, Codigo y NombreLocal renombrados como Pais, Abreviatura y Nomenclatura Local, de todos los países de la región Polynesia
SELECT
        Nombre As Pais,
        Codigo As Abreviatura,
        NombreLocal As 'Nomenclatura Local'
FROM
        Paises
WHERE
        Region = 'Polynesia'
```

### Ejercicio 3

```sql
-- Devolver en una sola columna Nombre, Apellido y Direccion de todos los clientes de la ciudad Bari, el formato debe ser "Nombre: nombre, Apellido: apellido, Dirección: direccion"

-- Ejecutamos la siguiente consulta primero para obtener el Id de la ciudad, ya que la tabla clientes solo tiene el Id de la ciudad del cliente, no tiene el nombre
-- SELECT Id FROM Ciudades WHERE Nombre = 'Bari'

SELECT
        'Nombre: ' + Nombre + 
        ', Apellido: ' + Apellido +
        ', Dirección: ' + Direccion 
        As 'Nombre, Apellido y Direccion'
FROM
        Clientes
WHERE
        CiudadId = 1473
```

# Cláusulas AND OR y NOT

### Cláusulas AND y OR

Podemos utilizar operaciones lógicas dentro de la cláusula `WHERE`. Para hacerlos disponemos de los operadores lógicos `AND`, `OR` y `NOT`. En el ejemplo va a devolver todos los registros que cumplan con ambas condiciones.

```sql
SELECT *
FROM
        Clientes
WHERE
        Nombre = 'Carla' AND Apellido = 'Snider'
```

Mediante la cláusula `OR` podemos evaluar que se cumpla mas de una condición para una columna. En el ejemplo va a devolver todos los registros cuyo nombre sea `Carla` o `Abel`.

```sql
SELECT *
FROM
        Clientes
WHERE
        Nombre = 'Carla' AND Nombre = 'Abel'
```

## Combinar operadores

Cuando utilizamos operadores lógicos el orden es importante. Pero algunos operadores lógicos tiene prioridad sobre otros.
* La evaluación se hace de izquierda a derecha.

* Se evalúan primer lo que está dentro de los paréntesis.
* Se evalúan los `NOT`, luego los `AND` y finalmente los `OR`.

En el ejemplo `Nombre = 'Carla' OR Nombre = 'Abel' AND Apellido = 'Snider'` se evalúa primero `Nombre = 'Abel' AND Apellido = 'Snider'` que no devuelve valores, por que no hay registros que cumplan esas dos condiciones. Al resultado de esto se evalúa `Nombre = 'Carla' OR` que va a devolver solo registros con `Nombre = 'Carla'`, ya que la primera parte no devuelve valores.

Para solucionar esto damos prioridad a `Nombre = 'Carla' OR Nombre = 'Abel'` mediante los `()`.

```sql
SELECT *
FROM
        Clientes
WHERE
        (Nombre = 'Carla' OR Nombre = 'Abel') AND Apellido = 'Snider'
```

## Cláusula NOT

La cláusula `NOT` se utiliza para negar la expresión que le sigue. En el ejemplo traemos todos los registros cuyo valor de la columna `Nombre` no sea `Carla`. El ejemplo también se puede resolver como `Nombre != 'Carla'`.

```sql
SELECT *
FROM
        Clientes
WHERE
        NOT Nombre = 'Carla'
```

Podemos aplicar la cláusula a un conjunto de operadores. En el ejemplo vamos a solicitar los registros cuyo `Nombre` no es `Abel` o cuyo `Apellido` no es `Snider`. `NOT` niega las comprobaciones de igual, es decir, las vuelve en `!=` pero también niega el `AND`, es decir, la vuelve en `OR`.

```sql
SELECT *
FROM
        Clientes
WHERE
        Nombre = 'Carla' OR NOT (Nombre = 'Abel' AND Apellido = 'Snider')
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver todos los productos cuyo precio sea mayor que el costo incrementado en un 40% o la ganancia sea de al menos 25
SELECT *
        Costo * 1.4 As CostoIncrementado
FROM
        Productos
WHERE
        Precio > Costo * 1.4 OR (Precio - Costo > 25 ) 
```

### Ejercicio 2

```sql
-- Devolver todas las ciudades argentinas y todas las ciudades brasileras excepto aquellas que pertenezcan a los de Buenos Aires y Racife

SELECT *
FROM
        Ciudades
WHERE
        (CodigoPais = 'ARG' AND NOT Distrito = 'Buenos Aires') OR 
        (CodigoPais = 'BRA' AND NOT Distrito = 'Racife')
```

### Ejercicio 3

```sql
-- Devolver las ordenes realizadas antes de febrero de 2018 que hayan vendido mas de 100 productos o ordenes realizadas después de julio del 2018 que no hayan vendido más de 50 productos

SELECT *
FROM ordenes
WHERE 
        Fecha < '20180201' AND Cantidad > 100
        OR
        Fecha > '20180731' AND NOT Cantidad >= 50
```

# Cláusula IN

## Cláusula IN

Utilizamos `IN` para conocer cuales, de una lista de valores, se encuentran en los datos almacenados en una columna. En el ejemplo filtramos los registros en los cuales `Codigo` contenga algunos de los calores de la lista `('ARG', 'AGO', 'AND')`. Utilizamos `IN` cuando queremos comparar el valor de una columna con una lista de valores.

```sql
SELECT *
FROM Paises
WHERE Codigo IN ('ARG', 'AGO', 'AND')
```

Podemos utilizar NOT para negar esta condición.

```sql
SELECT *
FROM Paises
WHERE Codigo NOT IN ('ARG', 'AGO', 'AND')
```

Se pueden realizar consultas con `IN` para valores numéricos y de fechas con el formato `'AAAAMMDD'`.

## Ejercicios

### Ejercicio 1

```sql
-- Devolver cliente cuyos apellidos sean Myers, Lewis, Kent, Case o Berger
SELECT *
FROM Clientes
WHERE
        Apellido IN ('Myers', 'Lewis', 'Kent', 'Case', 'Berger')
```

### Ejercicio 2

```sql
-- Devolver Codigo, Nombre Continente y Region de todos los paises de America
SELECT Codigo, Nombre, Continente, Region
FROM Paises
WHERE Continente IN ('North America', 'South America')
```

### Ejercicio 3

```sql
-- Devolver todas las ciudades de los paises hispanoparlantes

-- Necesitamos conseguir el idioma de los paises
-- SELECT PaisCodigo FROM PaisesIdioma WHERE PaisIdioma = 'Spanish'

SELECT Nombre, CodigoPais, Distrito
FROM Ciudades
WHERE CodigoPais IN ('...INGRESAMOS LOS 28 PaisCodigo DE LA CONSULTA ANTERIOR')
```

# Cláusula BETWEEN

## Cláusula BETWEEN

Cuando necesitamos acotar una búsqueda a un rango entre dos valores, por ejemplo un valor para la columna `Id` que vaya del `100` al `200`, utilizamos la sintaxis `WHERE Id >= 100 AND Id <=200`. Podemos obtener el mismo resultado mediante la cláusula `BETWEEN`. La cláusula `BETWEEN` incluye a lo extremos, es decir, si no queremos tomar los valores de `100` y `200` debemos indicar `101` y `199`.

```sql
SELECT *
FROM Ciudades
WHERE Id BETWEEN 100 AND 200
```

Podemos utilizar `BETWEEN` para consultar rangos de fechas.

```sql
SELECT *
FROM Clientes
WHERE FechaNacimiento BETWEEN '19900101' AND '19901231'
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver clientes nacidos entre 1950 y 1980 y clientes nacidos entre 1990 y 2010
SELECT *
FROM Clientes
WHERE FechaNacimiento 
        BETWEEN '19500101' AND '19800101' OR 
        BETWEEN '19900101' AND '20100101'
```

### Ejercicio 2

```sql
-- Devolver ordenes realizadas: antes de enero de 2016, entre marzo y noviembre de 2017 o marzo y noviembre de 2018, después de enero de 2019

SELECT *
FROM Ordenes
WHERE
        Fecha < '20160101' OR
        Fecha BETWEEN '20170301' AND '20171130' OR 
        Fecha BETWEEN '20180301' AND '20181201' OR
        Fecha > '20190131'

```

### Ejercicio 3

```sql
-- Devolver Id, Nombre, Apellido y Direccion de los clientes con Id mayores a 80 pero menores a 125, excepto por los clientes 99 y 100. Y ademas devolver los clientes con Id 13, 17, 19, 28 y 56

SELECT ID, Nombre, Apellido, Direccion
FROM Clientes
WHERE
        Id BETWEEN 80 AND 125 AND Id NOT In (99, 100) OR
        Id IN (13, 17, 19, 28 y 56)
```

# Cláusula LIKE

## Cláusula LIKE y comodín '%'

A la sentencia `WHERE Apellido = 'Guerra'` la podemos reemplazar por `WHERE Apellido LIKE 'Guerra'`. El resultado es el mismo pero con con la cláusula `LIKE` podemos usar comodines. Los comodines son caracteres especiales que se utilizan para reemplazar otros caracteres. Los comodines son:

* % : iguala cualquier cantidad de caracteres.
* _ : iguala solo un caracter

De esta forma si queremos una respuesta con todos los clientes cuyo apellido comienza con G utilizamos `LIKE` mas el comodín.

```sql
SELECT *
FROM Clientes
WHERE Apellido LIKE 'G%'
```

Podemos utilizar el comodín de forma inversa. Es decir, los apellidos que terminan con uno o varios caracteres.

```sql
SELECT *
FROM Clientes
WHERE Apellido LIKE '%ne'
```

Si queremos buscar los apellidos que contienen ciertos caracteres.

```sql
SELECT *
FROM Clientes
WHERE Apellido LIKE '%ue%'
```

## Comodín '_'

El comodín '_' reemplaza solo un caracter en la búsqueda que realizamos mediante `LIKE`. En el ejemplo va a devolver todos los apellidos que terminen en `uerra` y comiencen con cualquier caracter.

```sql
SELECT *
FROM Clientes
WHERE Apellido LIKE '_uerra'
```

Cada '_' representa un caracter. Podemos hacer búsquedas combinadas.

```sql
SELECT *
FROM Clientes
WHERE Apellido LIKE '_u__ra'
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver Id, Nombre, Costo y Precio de todos los productos relacionados con queso siempre y cuando su costo no se menor a 10 ni mayor a 30

SELECT Id, Nombre, Costo, Precio
FROM Productos
WHERE Nombre LIKE '%queso%' AND Costo BETWEEN 10 AND 30
```

### Ejercicio 2

```sql
-- Devolver todos los clientes cuyo nombre tenga como segunda letra, la letra 'a' y termine con la letra 'e'

SELECT *
FROM Clientes
WHERE Nombre LIKE '_a%e'
```

### Ejercicio 3

```sql
-- Devolver todos los clientes cuyo apellido no tenga la letra 'r' en la tercera posición y su penúltima posición sea la letra 'e'

SELECT *
FROM Clientes 
WHERE Apellido NOT LIKE '__r%' AND Apellido LIKE '%e_'
```

# Cláusula IS NULL

## Cláusula IS NULL

Utilizamos `IS NULL` para devolver todos los registros de una columna que no tengan valores asignados. Cuando un registro de una columna no tiene datos esta aparece como NULL.

```sql
SELECT *
FROM Clientes
WHERE Telefono IS NULL
```

Si queremos conocer todos los clientes que si tienen valores en una columna en particular, es decir, todos los que no son `NULL`, podemos utilizar `NOT`. Podemos indicarlo como el ejemplo o de la forma `IS NOT NULL`. En el ejemplo traemos todos los registros cuyo teléfono no tiene valor `NULL`.

```sql
SELECT *
FROM Clientes
WHERE NOT Telefono IS NULL
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver todos los productos que tengan proveedor

SELECT *
FROM Productos
WHERE ProveedorId IS NOT NULL
```

### Ejercicio 2

```sql
-- Devolver todos los clientes que no tengan telefono

SELECT *
FROM Clientes
WHERE Telefono IS NULL
```

# Cláusula ORDER BY

## ORDER BY DESC

La Cláusula `ORDER BY` se utiliza para establecer el orden en que queremos devolver los datos de una consulta. Si no especificamos un orden, por defecto los datos se van a devolver en orden ascendente de la clave primaria. La cláusula `ORDER BY` se coloca siempre al final de la consulta y soporta una lista de columnas. Si no especificamos el tipo de orden para la cláusula `ORDER BY` por defecto será ascendente. Para modificar esto utilizamos `DESC`.

```sql
SELECT *
FROM Clientes
ORDER BY Apellido DESC
```

## ORDER BY ASC

Podemos hacer explicito el orden ascendente mediante `ASC`.

```sql
SELECT *
FROM Clientes
ORDER BY Apellido ASC
```

## Combinar ordenes

El orden de las columnas que indicamos a `ORDER BY`. En el ejemplo se va a ordenar primero por FechaNacimiento y si dos registros coinciden en su FechaNacimiento se va a ordenar por Apellido. 

```sql
SELECT FechaNacimiento, Apellido
FROM Clientes
ORDER BY FechaNacimiento, Apellido
```

Podemos indicar diferentes ordenes para cada una de las columnas. En el ejemplo, se va a ordenar por FechaNacimiento en forma ascendente (por defecto) y por Apellido en forma descendente.

```sql
SELECT FechaNacimiento, Apellido
FROM Clientes
ORDER BY FechaNacimiento, Apellido DESC
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver Nombre, Apellido y Direccion de todos los clientes ordenados por facha de nacimiento desde el mes mas reciente al mas antiguo

SELECT Nombre, Apellido, Direccion
FROM Clientes
ORDER BY FechaNacimiento DESC
```

### Ejercicio 2

```sql
-- Devolver Nombre, ProveedorId y Ganancia de todos los productos, ordenados de mayor a menor, con el product de mayor ganacia primero en la lista

SELECT Nombre, ProveedorId,
        Precio - Costo As Ganancia
FROM Productos
ORDER BY Precio - Costo DESC
```

### Ejercicio 3

```sql
-- Devolver todos los clientes y ordenarlos por nombre de A a Z, si el nombre coincide ordenar por Apellido de Z a A, si ambos coinciden elegir primer el cliente con mayor edad

SELECT *
FROM Clientes
ORDER BY Nombre, Apellido DESC, FechaNacimiento
```

# Cláusula INNER JOIN

## Cláusula INNER JOIN

Podemos combinar más de una tabla utilizando `INNER JOIN`. Para hacerlo utilizamos las claves foráneas, es decir, las columnas que hacen referencia al Id de otra tabla de la base. Por ejemplo la tabla Productos tiene las columnas ProveedorId y CategoriaId que hacen referencia a registros en las tablas Proveedores y Categorias respectivamente.

En el ejemplo estamos indicando solicitando que se devuelvan todos los registros de la tabla Productos y todos los registros de la tabla Categorias siempre que CategoriasId de la tabla Productos sea igual Id de la tabla Categorias.

```sql
SELECT *
FROM Productos
INNER JOIN Categorias On CategoriaId = Id
```

La consulta anterior va a generar un error. Esto sucede por que ambas tablas, Productos y Categorias tiene una columna Id que va a ser devuelva por la consulta. Para solucionarlo utilizamos los Alias. En el ejemplo indicamos como alias de Productos la letra p y como alias de Categorias la letra c. Cuando vamos a hacer la comparación de valores de Id indicamos p.CategoriaId, es decir, la columna CategoriaId de la tabla Productos con alias p se debe comparar con c.Id, es decir, la columna Id de la tabla Categorias con alias c.

```sql
SELECT *
FROM Productos As p
INNER JOIN Categorias As c On p.CategoriaId = c.Id
```

Esto mismo se puede indicar sin la cláusula `As`.

```sql
SELECT *
FROM Productos p
INNER JOIN Categorias c On p.CategoriaId = c.Id
```

## Múltiples JOIN



Podemos hacer múltiples combinaciones mediante INNER JOIN. De la misma forma que con el ejemplo de Categorias usamos la clave foranea para buscar las coincidencias en las siguientes tablas.

```sql
SELECT *
FROM Productos p
INNER JOIN Categorias c On p.CategoriaId = c.Id
INNER JOIN Proveedores pr On p.ProveedorId = pr.Id
```

En el caso de tener valores nulos en la columna CategoriaId o ProveedorID ese registro no va a aparecer en el resultado. Esto sucede por que `INNER JOIN` no devuelve filas donde el valor que se evalua es nulo. Es decir si, por ejemplo, si ProveedorId de Productos tiene valor `NULL` ese registro, junto con las columnas de Categorias y las columnas de Proveedores, no va a aparecer en el resultado de la consulta.

Para que los valores de la consulta aparezcan tiene que cumplirse las condiciones de los dos `JOIN`

## Palabras opcionales

La palabra `INNER` es opcional. Podemos realizar la consulta indicando solo `JOIN`. Por defecto los `JOIN` son `INNER JOIN` a menos que indiquemos algo diferente. La consulta puede quedar de la siguiente manera:

```sql
SELECT *
FROM Productos p
JOIN Categorias c On p.CategoriaId = c.Id
JOIN Proveedores pr On p.ProveedorId = pr.Id
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver nombre de proveedores, precio y costo de productos cuya ganacia sea mayor a 20

SELECT 
        p.Nombre
        Precio
        Costo
FROM Productos
JOIN Proveedores p On ProveedorId = p.Id
WHERE Precio - Costo > 20

```

### Ejercicio 2

```sql
-- Devolver Fecha, Apellido y nombre del cliente y nombre de producto de todos los clientes que hayan comprado productos entre 2016 y 2019 ordenado primero por mas reciente y segundo por apellido A - Z

SELECT Fecha, c.Apellido, c.Nombre, p.Nombre
FROM Ordenes
JOIN Clientes c On ClienteId = c.Id
JOIN Productos p On ProductoId = p.Id
WHERE Fecha BETWEEN '20160101' AND '20191231'
ORDER BY Fecha DESC, c.Apellido
```

### Ejercicio 3

```sql
-- Devolver Fecha, Apellido, nombre y pais del cliente y nombre de producto de todos los clientes que hayan comprado productos entre 2016 y 2019 ordenado primero por mas reciente y segundo por apellido A - Z

SELECT Fecha, c.Apellido, c.Nombre, pais.Nombre, p.Nombre
FROM Ordenes
JOIN Clientes c On ClienteId = c.Id

JOIN Ciudades ciu On c.CiudadId = ciu.Id
JOIN Paises pais On ciu.CodigoPais = Pais.Codigo

JOIN Productos p On ProductoId = p.Id

WHERE Fecha BETWEEN '20160101' AND '20191231'
ORDER BY Fecha DESC, c.Apellido
```

# Cláusula OUTER JOIN

## LEFT JOIN

Cuando hacemos un `JOIN` entre dos tablas, por ejemplo una tabla Clientes y una tabla Ordenes, los valores devueltos van a ser todos los que cumplan condición de igualdad en ambas tablas. Cuando queremos que la consulta nos devuelva, además de los datos que cumplen con la condición, también los datos que no cumplen con la condición, de la primera tabla, la tabla Clientes, utilizamos `LEFT JOIN`. `LEFT JOIN` va a devolver los datos que cumplan con la condición del JOIN y los datos de la tabla de la izquierda de la consulta que no cumplan con la condición. En el ejemplo la consulta devuelve todos los registros de la tabla Clientes, aunque estos no tengan ninguna orden realizada. En la respuesta, en las columnas de la tabla Ordenes sus valores aparecerán como NULL, para los clientes que no tengan ninguna orden hecha.

```sql
SELECT *
FROM Clientes c
LEFT JOIN Ordenes o On o.ClienteId = c.Id
ORDER BY c.Id
```

## RIGHT JOIN

Funciona de la misma manera que `LEFT JOIN` solo que va a traer todos los compos de la tabla de la derecha de la consulta en lugar que los campos de la tabla de la izquierda. La consulta devuelve todos los campos que cumplen con la condición del ´, de la tabla de la izquierda, y todos los campos, aunque no cumplan con la condición, de la tabla de la derecha del `JOIN`. El ejemplo devuelve lo mismo que el ejemplo anterior al estar invertidas el orden de las tablas en la consulta 

```sql
SELECT *
FROM Ordenes o
LEFT JOIN Clientes c On o.ClienteId = c.Id
ORDER BY c.Id
```

La palabra `OUTER` en `LEFT OUTER JOIN` o `RIGHT OUTER JOIN` es opcional, puede escribirse directamente `LEFT JOIN` y `RIGHT JOIN`.

## Ejercicios

### Ejercicio 1

```sql
-- Devolver nombre y apellido del cliente que no hayan realizado ninguna orden, no hayan realizado una orden fuera del año 2018

-- mediante distinct indicamos que no traiga clientes repetidos
SELECT DISTINCT c.Nombre, c.Apellido
FROM Clientes c
LEFT JOIN Ordenes On ClienteId = c.id
-- en lugar de aplicar where, que va a descartar los registros con fecha null, es decir, los registros de los clientes que no tengan hechas ordenes, hacemos un and a la condición del left join indicando que queremos que descarte los de las fechas indicadas en el between
    AND Fecha NOT BETWEEN '20180101' AND '20181231'
```

### Ejercicio 2

```sql
-- Devolver Id y nombre de todos los productos que nunca se han vendido

SELECT DISTINCT p.Id, p.Nombre
FROM Productos p
LEFT JOIN Ordenes o On o.ProductoId = p.Id
WHERE o.Id = NULL
```

### Ejercicio 3

```sql
-- Devolver nombre y código de paises que tengan clientes pero nunca hayan participado en una transacción

SELECT DISTINCT pais.Nombre, pais.CodigoPais
FROM Paises pais
    INNER JOIN Ciudades ciu ON ciu.CodigoPais = pais.Codigo
    INNER JOIN Clientes cli ON cli.CiudadId = ciu.Id
    LEFT JOIN Ordenes o ON o.ClienteId = cli.Id
WHERE Id = NULL
```

# Cláusula UNION

## UNION ALL

La cláusula `UNION` permite concatenar el resultado de dos consultas, es decir, si con `JOIN` combinamos columnas con `UNION` combinamos filas. En el ejemplo, después de mostrar todas las filas de la columnas Apellido de la tabla Clientes, que pueden ser 100 por ejemplo, va a mostrar todas las filas de la columna Nombre de la tabla Proveedores, que pueden ser otras 100. En total mostraría como resultado una columna con 200 filas (100 de Apellido y 100 de Nombre)

```sql
SELECT Apellido
FROM CLientes

UNION ALL

SELECT Nombre
FROM Proveedores
```

## UNION y ORDER BY

Algunas particularidades de la cláusula `UNION`:

* La cantidad de columnas de las consultas que unimos tiene que ser la misma. En el ejemplo, hacemos la consulta de dos columnas de Clientes y queremos hacer `UNION` con solo una columna de Proveedores, esto dará un error.

```sql
SELECT Apellido, Nombre
FROM CLientes

UNION ALL

SELECT Nombre
FROM Proveedores
```

* El título de la columna de resultado en un `UNION` va a estar dado por la primer consulta. En el ejemplo el título de la columna resultado de la `UNION` va a ser Apellido, a menos que le brindemos otro.

```sql
-- Se van a generar 2 columnas, una con título Tipo que, para los Apellidos de la tabla Clientes va a mostrar la palabra Cliente, y para los Nombre de la tabla Proveedor va a mostrar Proveedor. La segunda columna va a tener el dato correspondiente al Cliente o Proveedor y se va a llamar CLienteProveedor
SELECT 'Cliente' As Tipo, Apellido As ClienteProveedor
FROM CLientes

UNION ALL

    -- Los alias que indicamos aquí no van a tener efecto
SELECT 'Preveedor' As TipoSinEfecto, Nombre As NombreSinEfecto
FROM Proveedores
```

* Para ordenar una consulta con `UNION`, la cláusula `ORDER BY` tiene que ir al final de todas las consultas, además se debe ordenar por una columna de la primera consulta. En el ejemplo ordenamos por Apellido pero la cláusula `ORDER BY` va después de la segunda consulta

```sql
SELECT 'Cliente' As Tipo, Apellido As ClienteProveedor
FROM CLientes

UNION ALL

SELECT 'Preveedor' As TipoSinEfecto, Nombre As NombreSinEfecto
FROM Proveedores
ORDER BY Apellido
```

* `UNION ALL` concatena todas las filas de las columnas indicadas. La cláusula `UNION` sola elimina los valores duplicados de la respuesta a la consulta.

```sql
-- Si hay apellidos duplicados no van a aparecer en la respuesta
SELECT 'Cliente' As Tipo, Apellido As ClienteProveedor
FROM CLientes

UNION

-- Si hay nombres duplicados no van a aparecer en la respuesta
SELECT 'Proveedor' As TipoSinEfecto, Nombre As NombreSinEfecto
FROM Proveedores
ORDER BY Apellido
```

## UNION en la misma tabla

Podemos hacer un `UNION` de filas de la misma tabla. En el ejemplo va a traer los productos cuya ganancia sea mayor a 50 como prioritarios y de 20 a 50 como no prioritarios.

```sql
SELECT 'Prioritaros' As Tipo, *
FROM Productos
WHERE Precio - Costo > 50

UNION

SELECT 'No prioritaros' As Tipo, *
FROM Productos
WHERE Precio - Costo BETWEEN 20 AND 50
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver un único listado:
-- Id y nombre de productos cuyo costo sea mayor a 80 pero menor a 100
-- Id y nombre de categorias que no comiencen con la letra C
-- Id y Nombre de proveedores cuya segunda letra no sea e ni su última letra sea n

SELECT 'Producto' As Tipo, p.Id, p.Nombre
FROM Productos p
WHERE Costo BETWEEN 80 AND 100

UNION ALL

SELECT 'Categoria' As Tipo, c.Id, c.Nombre 
FROM Categorias c
WHERE c.Nombre NOT LIKE 'C%'

UNION ALL

SELECT 'Proveedor' As Tipo, pr.Id, pr.Nombre
FROM Proveedores pr
WHERE pr.Nombre NOT LIKE '_e%' AND pr.Nombre NOT LIKE '%n'
```

### Ejercicio 2

```sql
-- Devolver nombre de producto, apellido y nombre como cliente, fecha de orden y texto mayorista para aquellas ordenes con pedidos mayores a 50 y texto minorista para aquellas ordenes con pedidos menores a 50

SELECT p.Nombre, c.Apellido + ', ' + c.Nombre As Cliente, Fecha, 'Mayorista' As Tipo
FROM Ordenes
    INNER JOIN Productos p On ProductoId = p.Id
    INNER JOIN Clientes c On ClienteId = c.Id
WHERE Cantidad > 50

UNION ALL

SELECT p.Nombre, c.Apellido + ' ' + c.Nombre As Cliente, Fecha, 'Minorista' As Tipo
FROM Ordenes
    INNER JOIN Productos p On ProductoId = p.Id
    INNER JOIN Clientes c On ClienteId = c.Id
WHERE Cantidad < 50
```

### Ejercicio 3

```sql
-- Devolver un solo listado de productos, precio y nombre de categoria con precios actualizados
-- descuento del 10% para bebidas, aumento del 15 para carnes
-- agregar un impuesto fijo de 13.5 para lacteos

SELECT p.Nombre, p.Precio - (Precio * 0.1) As Precio, c.Nombre As Categoria
FROM Productos p
    INNER JOIN Categorias c On CategoriaId = c.Id
WHERE p.CategoriaId = 1 -- bebidas

UNION ALL

SELECT p.Nombre, p.Precio + (Precio * 0.15) As Precio, c.Nombre As Categoria
FROM Productos p
    INNER JOIN Categorias c On CategoriaId = c.Id
WHERE p.CategoriaId = 4 -- carnes

UNION ALL

SELECT p.Nombre, p.Precio + 13.5 As Precio, c.Nombre As Categoria
FROM Productos p
    INNER JOIN Categorias c On CategoriaId = c.Id
WHERE p.CategoriaId = 6 -- lacteos

UNION

SELECT p.Nombre, p.Precio As Precio, c.Nombre As Categoria
FROM Productos p
    INNER JOIN Categorias c On CategoriaId = c.Id
WHERE p.CategoriaId NOT IN (1, 4, 6) -- Resto de los productos

ORDER BY c.Nombre
```

# Cláusula GROUP BY

## GROUP BY

`GROUP BY` permite organizar las filas de una consulta en grupos, que están determinados por las columnas que se especifican en la consulta. La consulta va a devolver las filas sin repetir valores para ProveedorId, es decir, varios productos tienen el mismo ProveedorId, la consulta va a devover solo una fila por cada valor de ProveedorId diferente.

```sql
SELECT ProveedorId
FROM Productos
GROUP BY ProveedorId
```

Podemos traer los nombres de los Proveedores que se corresponden con el ProveedorId del producto, de esta forma solo vamos a tener el nombre de cada proveedor sin repeticiones.

```sql
SELECT ProveedorId, p.Nombre
FROM Productos
    JOIN Proveedores p On ProveedorId = p.Id
GROUP BY ProveedorId, p.Nombre
```

En la cláusula `SELECT` tenemos que tener todas las columnas que indicamos agrupar con `GROUP BY`.

## Ejercicios

### Ejercicio 1

```sql
-- Devolver solo paises de la tabla ciudades

SELECT p.Nombre
FROM Ciudades
    JOIN Paises p On CodigoPais = p.CodigoPais
GROUP BY p.Nombre
```

# Cláusula COUNT

## COUNT

`COUNT` es una función de agregado que se utiliza con `GROUP BY`. Se utiliza para contar cuantas veces aparece un valor indicado dentro de un grupo. En el ejemplo traemos los nombres de los proveedores y contamos cuantas veces cada uno de estos se repiten en la tabla Productos, es decir, contamos la cantidad de productos que tenemos para cada proveedor.

```sql
SELECT prov.Nombre, COUNT(prod.Id) As CantidadProductos
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
ORDER BY prov.Nombre
```

## COUNT (*) y COUNT DISTINCT

* `COUNT (*)`: nos permite contar todas las filas de una tabla en particular. El ejemplo devuelve un registro con el número de filas de la tabla Clientes.

```sql
SELECT COUNT(*)
FROM CLientes
```

```sql
-- Devuelve la cuenta de clientes con Nombre = 'Carla'
SELECT COUNT(*)
FROM CLientes
WHERE Nombre = 'Carla'
```

* `COUNT DISTINCT`: devuelve la cantidad de filas donde no se repite el valor que indicamos entre paréntesis. En el ejemplo va a contar la cantidad de nombres distintos que hay en la tabla clientes.

```sql
SELECT COUNT(DISTINCT Nombre)
FROM CLientes
```

## Ejercicios

### Ejercicio 1

```sql
-- Devolver la cantidad de productos vendidos por categoría, ordenado de mayor a menor

SELECT cat.Nombre, COUNT(cat.CategoriaId)
FROM Ordenes
    INNER JOIN Productos prod On Prod.Id = ProductoId
    INNER JOIN Categorias cat On cat.Id = Prod.CategoriaId
GROUP BY prod.CategoriaId, cat.Nombre
ORDER BY COUNT(cat.CategoriaId) DESC
```

### Ejercicio 2

```sql
-- Devolver la cantidad de clientes que alguna vez ordenaron algo, por pais

SELECT pais.Codigo, pais.Nombre, COUNT(pais.codigo) As Cantidad
FROM Ordenes
    INNER JOIN Clientes cli On cli.Id = ClienteId
    INNER JOIN Ciudades ciu On ciu.Id = cli.CiudadId
    INNER JOIN Paises pais On Pais.CodigoPais = ciu.CodigoPais
GROUP BY pais.Nombre, COUNT(cli.Id)
```

### Ejercicio 3

```sql
-- Devolver la cantidad de productos cuya ganancia está entre 5 y 20 y su proveedor no está vacío.

SELECT COUNT(*)
FROM Productos
WHERE (Precio - Costo) BETWEEN 5 AND 20 AND ProveedorId IS NOT NULL

```

# Cláusula SUM

## Cláusula SUM

Es una función de agregado que suma las filas de la columna que le indicamos. El ejemplo suma todos los valores de la columna precio en la tabla productos. Los devuelve como una única celda.

```sql
SELECT SUM(Precio)
FROM Productos
```

En el ejemplo traemos todos los proveedores por nombre y la suma de los costos de estos proveedores en los productos.

```sql
SELECT prov.Nombre, SUM(prod.Costo) As CostoProducto
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
ORDER By prov.Nombre
```

Dentro de la función `SUM` podemos pasar una expresión. En el ejemplo calculamos la ganancia que tenemos de cada proveedor.

```sql
SELECT prov.Nombre, SUM(prod.Precio - prod.Costo) As ProveedorGanancia
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
ORDER By prov.Nombre
```

## Ejercicios

### Ejercicio 1

```sql
-- Determinar cual es la categoria mas existosa calculado el total vendido por categoria

SELECT cat.Id, cat.Nombre, SUM(prod.Precio * ord.Cantidad) As TotalVendido
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Categorias cat On cat.Id = prod.CategoriaId
GROUP BY cat.Id, cat.Nombre
ORDER BY SUM(prod.Precio * ord.Cantidad) DESC
```

### Ejercicio 2

```sql
-- Determinar cual es el proveedor mas costoso del sistema calculando el total por proveedor

SELECT prov.Id, prov.Nombre, SUM(prod.Costo) As CostoTotal
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Id, prov.Nombre
ORDER BY SUM(prod.Costo) DESC
```

### Ejercicio 3

```sql
-- Mostrar el total consumido por idioma del cliente y ordenado de mayor a menor

SELECT idio.PaisIdioma, SUM(prod.Precio * ord.Cantidad)
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Clientes cli On cli.Id = ord.ClienteId
    JOIN Ciudades ciu On ciu.Id = cli.CiudadId
    JOIN Paises pais On pais.Codigo = ciu.CodigoPais
    JOIN PaisesIdioma idio On idio.CodigoPais = pais.Codigo
GROUP BY idio.PaisIdioma
ORDER BY SUM(prod.Precio * ord.Cantidad) DESC
```

# Cláusula AVG

## Cláusula AVG

`AVG` significa average, es una cláusula que se utiliza para calcular el promedio de un grupo de valores. En el ejemplo obtenemos el precio promedio de todos los productos de la tabla.

```sql
SELECT AVG(Precio)
FROM Productos

```

En el ejemplo obtenemos el precio promedio de los productos por cada proveedor.

```sql
SELECT prov.Nombre, AVG(prod.Precio) As PrecioPromedio
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
ORDER BY prov.Nombre
```

Podemos tener expresiones dentro de la función `AVG`. El ejemplo devuelve la ganancia promedio de cada proveedor.

```sql
SELECT prov.Nombre, AVG(prod.Precio - prod.Costo) As GananciaPromedio
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
ORDER BY prov.Nombre
```

## Ejercicios

### Ejercicio 1

```sql
-- Determinar el promedio vendido por ciudad ordenados de mayor a menor

SELECT ciu.Nombre, AVG(prod.Precio * ord.Cantidad) As PromedioVendido
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Clientes cli On cli.Id = ord.ClienteId
    JOIN Ciudades ciu On ciu.Id = cli.CiudadId
GROUP BY ciu.Nombre
ORDER BY AVG(ord.Cantidad) DESC
```

### Ejercicio 2

```sql
-- Determinar el promedio vendido a clientes nacidos entre 1930 y 1970

SELECT clie.Id, cli.Nombre, cli.Apellido, AVG (prod.Precio * ord.Cantidad) As PromedioVendido
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Clientes cli On cli.Id = ord.ClienteId
WHERE FechaNacimiento BETWEEN '19300101' AND '19701231'
GROUP BY clie.Id, cli.Nombre, cli.Apellido
```

### Ejercicio 3

```sql
-- Determinar el promedio invertido por proveedor para productos con al menos 1 venta 

SELECT prov.Id, prov.Nombre, AVG(prod.Costo) As PromedioInvertido
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
WHERE ord.Cantidad >= 1
GROUP BY prov.Id, prov.Nombre
ORDER BY AVG(prod.Costo) DESC
```

# Cláusulas MAX y MIN

## MAX y MIN

La función de agregado `MAX` devuelve el máximo valor de una columna. El ejemplo devuelve una celda con el valor del mayor precio de la tabla productos. 

```sql
SELECT MAX(Precio)
FROM Productos
```

La función de agregado `MIN` devuelve el menor valor de una columna. 

```sql
SELECT MIN(Precio)
FROM Productos
```

Las funciones soportan valores de tipo texto. Si le pasamos a las funciones columnas con datos de tipo texto nos va a devolver el primero registro o el último en orden alfabético. Para valores de tipo fecha devuelve también la fecha mas antigua con `MIN` y la fecha más reciente con `MAX`.

Las funciones MAX y MIN ignoran los valores nulos en las columnas.

## Ejercicios

### Ejercicio 1

```sql
--Encontrar el cliente mas joven que alguna vez haya realizado una compra

SELECT cli.Id, cli.Nombre, cli.Apellido, MAX(cli.FechaNacimiento)
FROM Ordenes ord
    JOIN Clientes cli On cli.Id = ord.ClienteId
GROUP BY cli.Id, cli.Nombre, cli.Apellido
ORDER BY MAX(cli.FechaNacimiento) DESC
```

### Ejercicio 2

```sql
-- Determinar el producto de menor costo en cada categoria que se haya vendido al menos una vez

SELECT cat.Nombre, prod.Nombre, MIN(prod.Costo) As MenorCosto
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Categorias cat On cat.Id = ord.CategoriaId
GROUP BY cat.Nombre, prod.Nombre
ORDER BY MIN(prod.Costo) DESC
```

### Ejercicio 3

```sql
-- Determinar cual es el pais al cual se realizaron la mayor y la menor venta, ordenando los resultados

SELECT pais.Codigo, pais.Nombre, MAX(ord.Cantidad * prod.Precio) As TotalVendido
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Clientes cli On cli.Id = ord.ClienteId
    JOIN Ciudades ciu On ciu.Id = cli.CiudadId
    JOIN Paises pais On pais.Codigo = ciu.CodigoPais
GROUP BY pais.Codigo, pais.Nombre
ORDER BY MAX(ord.Cantidad * prod.Precio) DESC
```

# Cláusula HAVING



## HAVING

La cláusula `HAVING` se utiliza para filtrar grupos en base a condiciones específicas. Cumple la misma función que la cláusula `WHERE` pero para los grupos. Con la cláusula `HAVING` solo los grupos que cumplen con la condición son devueltos en la consulta. En el ejemplo, para ver los proveedores con precio total mayor a 100 no podemos usar `WHERE`, por que `WHERE` se ejecuta antes de `GROUP BY`. Para filtrar los datos después de generar los grupos usamos `HAVING`.

```sql
SELECT prov.Nombre, SUM(prod.Precio) As PrecioTotal
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
-- aqui va la cláusula WHERE
GROUP BY prov.Nombre
HAVING SUM(prod.Precio) > 100
ORDER BY prov.Nombre
```

En la cláusula `HAVING` podemos utilizar todas los modificadores que utilizamos en la cláusula `WHERE`.

```sql
SELECT prov.Nombre, SUM(prod.Precio) As PrecioTotal
FROM Productos prod
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
HAVING SUM(prod.Precio) BETWEEN 100 AND 200
ORDER BY prov.Nombre
```

## Ejercicios

### Ejercicio 1

```sql
-- devolver solo aquellos proveedores en donde el precio promedio de sus productos supere el valor de su producto mas caro dividido por dos. El proveedor debe tener un productos que se haya vendido una vez

SELECT prov.Nombre, AVG(prod.Precio) As PromedioTotal, MAXC(prod.Precio) As ProductoMasCaro
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Proveedores prov On prov.Id = prod.ProveedorId
GROUP BY prov.Nombre
HAVING AVG(prod.Precio) > (MAX(prod.Precio) / 2)
ORDER BY AVG(prod.Precio)
```

### Ejercicio 2

```sql
-- Mostrar el total y el promedio consumido por
-- idioma de cliente
-- ordenado de mayor a menor 
-- solo para los idiomas en donde la mitad de lo consumido es mayor al promedio total consumido

SELECT  
        idio.PaisIdioma, 
        SUM(ord.Cantidad * prod.Precio) As TotalConsumido, 
        AVG(ord.Cantidad * prod.Precio) As PromedioConsumido
FROM Ordenes ord
    JOIN Productos prod On prod.Id = ord.ProductoId
    JOIN Clientes cli On cli.Id = ord.ClienteId
    JOIN Ciudades ciu On ciu.Id = cli.CiudadId
    JOIN Paises pais On pais.Codigo = ciu.CodigoPais
    JOIN PaisesIdioma idio On idio.CodigoPais = pais.Codigo
GROUP BY idio.PaisIdioma
HAVING SUM(ord.Cantidad * prod.Precio) / 2 > AVG(ord.Cantidad * prod.Precio)
ORDER BY SUM(ord.Cantidad * prod.Precio)
```

# Cláusula INSERT

## INSERT

`INSERT` se utiliza para insertar nuevos registros en una tabla. Se puede utilizar especificando columnas y valores a ser insertados. En el ejemplo no indicamos la columna Id ya que la misma se genera en forma automática cada vez que se crea un nuevo registro. AL hacer el INSERT nos va a devolver un mensaje indicando que una fila fue afectada.

```sql
INSERT INTO Clientes (Nombre, Apellido, FechaNacimiento, CiudadId, Telefono, Direccion) 
    VALUES ('Quentin', 'Tarantino', '19630327', 3794, NULL, '9601 Wilshire Blvd, 3rd Floor, Beverly Hills, CA 90210-5213')
```

Podemos indicar solo las columnas sobre las que queremos insertar los datos. Las columnas que no indicamos quedan con sus valores en `NULL`.

```sql
INSERT INTO Clientes (Nombre, Apellido, FechaNacimiento, CiudadId) 
    VALUES ('Steven', 'Spielberg', '19461218', 3794)
```

Si estamos agregando valores para todas las columnas de la tabla, no es necesario indicar las columnas de la tabla, solo los `VALUES` que vamos a insertar. En este caso es importante el orden de los valores, ya que tienen que insertarse en el orden en que está configurada la tabla.
