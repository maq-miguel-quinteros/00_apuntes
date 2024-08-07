# Redux

Redux es un contenedor de estados previsible para apps creadas con JavaScript.

* Redux fue creados para apps creadas con JavaScript: Redux puede ser usado por cualquier framework o librería de JavaScript como React, Angular, Vue o JavaScript Vanilla.

* Redux es un contenedor de estados: Redux guarda el estado de la aplicación. El estado de la aplicación es el estado individual de todos los componentes de la aplicación. Esto incluye los datos y la lógica de la interfaz de usuario. Redux puede almacenar y modificar estos datos. Un ejemplo del estado de una aplicación puede ser el siguiente:

![application_state](./redux01.png)

* Redux es predecible: En Redux, todas las transiciones de estado, es decir, todas las modificaciones que se le hace a un estado son explicitas. Que sean explicitas significa que son conocidas y que es posible y rastrearlas, saber donde se hicieron. Con Redux, los cambios de estado de la aplicación se vuelven predecibles.

prueba 
```mermaid

graph TD;
	A-->B;
	A-->C;
	B-->D;
	C-->D;
```

## otra

```javascript
let a = 20;
```

```mermaid

graph TD;
	A-->B;
	A-->C;
	B-->D;
	C-->D;
```

```mermaid

graph TD;
	A-->B;
	A-->C;
	B-->D;
	C-->D;
```
