
# Redux

Redux es un contenedor de estados previsible para apps creadas con JavaScript.

* Redux fue creados para apps creadas con JavaScript: Redux puede ser usado por cualquier framework o librería de JavaScript como React, Angular, Vue o JavaScript Vanilla.

* Redux es un contenedor de estados: Redux guarda el estado de la aplicación. El estado de la aplicación es el estado individual de todos los componentes de la aplicación. Esto incluye los datos y la lógica de la interfaz de usuario. Redux puede almacenar y modificar estos datos. Un ejemplo del estado de una aplicación puede ser el siguiente:

![application_state](./redux01.png)

* Redux es predecible: En Redux, todas las transiciones de estado, es decir, todas las modificaciones que se le hace a un estado son explicitas. Que sean explicitas significa que son conocidas y que es posible y rastrearlas, saber donde se hicieron. Con Redux, los cambios de estado de la aplicación se vuelven predecibles.

## Instalación

En la carpeta de nuestro proyecto, en la consola instalamos redux con el comando `npm install redux`.

## Tres conceptos fundamentales de Redux

En un caso de ejemplo, el de venta de un pastel en una tienda de pasteles, podemos reconocer tres situaciones entidades:
* La tienda
* El empleado
* El cliente

Estas tres entidades se relacionan en la actividad o acción de la venta de un pastel:
* El cliente
    * compra un pastel
* El empleado
    * revisa si hay stock y entrega el pastel
    * genera el recibo para el seguimiento de la venta

Podemos traducir este ejemplo en los tres conceptos fundamentales de redux

Escenario tienda de pasteles | Concepto en Redux | Explicación
--- | --- | ---
La tienda: guarda los pasteles en su deposito | __store__ | Guarda el estado de la aplicación
El cliente: quiere comprar un pastel | __action__ | Indica los cambios que se van a hacer en el estado de la aplicación
El empleado: realiza la venta | __reducer__ | Lleva a cabo el cambio de estado de la aplicación dependiendo de la acción

## Tres principios de Redux


