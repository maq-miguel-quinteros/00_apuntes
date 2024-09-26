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
