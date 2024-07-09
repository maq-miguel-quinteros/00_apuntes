# Hooks

Los _hooks_ son funciones que proporcionan características propias de un componente de clase a un componente de función, es decir, que le permite tener un estado y un ciclo de vida.

## Algunas reglas básicas para trabajar con _hooks_

* Solo crear _hooks_ en componentes de función de **Rect**.
* No crear ni llamar a _hooks_ dentro de funciones regulares de JavaScript.
* Solo crear _hooks_ en la parte de arriba del componente de función, justo debajo de la declaración del componente.
	* No crear _hooks_ dentro de loop, de condicionales ni de funciones anidadas.

## Incumbencias de los de los diferentes hooks

* useState: lo utilizamos para manipular variables de estado de los componentes de react.

* useEffect: lo utilizamos para manipular efectos secundarios en los componentes de estado de react.

* useContext: lo utilizamos para manipular el context API, es decir, para pasar datos a traves del árbol de componentes tener que utilizar las props de cada uno de los hijos desde un componente superior a uno inferior del árbol.

* useReducer: lo utilizamos para manipular reducers de javascript.
