# Clausula SELECT

## Básico y alias

La consulta mas simple que podemos realizar es `SELECT`, donde `Paises` es el nombre de la base de datos a la que hacemos la consulta. Mediante `SELECT` indicamos cuales son las columnas que queremos seleccionar. El `*` funciona como un comodín que indica que vamos a seleccionar todas las columnas de esa tabla.

SELECT \* FROM Paises

Para el caso de querer consultar una columna llamada `Nombre` la sentencia quedaría como:

SELECT Nombre FROM Paises

Si son varias las columnas que queremos recuperar en la consulta las separamos por una coma `,` quedaría como:

SELECT Nombre, Codigo, Region FROM Paises

Para modificar el orden en que aparecen las columnas en la respuesta, simplemente modificamos el orden en que las llamamos en la consulta:

SELECT Codigo, Nombre, Region FROM Paises

Todas las instrucciones SQL soportan el salto de línea. El siguiente código dará el mismo resultado

SELECT Codigo,  
Nombre,  
Region  
FROM Paises

Cuando usamos la clausula `SELECT` podemos renombrar las columnas que la consulta devuelve. Para renombrar usamos la clausula `As`. El cambio de nombre aplica a la respuesta que trae la consulta. Esto no modifica el nombre de la columna en la tabla.

SELECT Codigo As Id,  
Nombre As Name,  
Region  
FROM Paises

## Operadores aritméticos