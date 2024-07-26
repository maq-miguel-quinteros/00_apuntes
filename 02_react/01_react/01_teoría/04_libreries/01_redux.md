# ¿Por qué usar Redux en React?

Los componentes en React tienen su propio estado ¿Por qué deberíamos usar otra herramienta para manejar ese estado? Cuando necesitamos compartir un estado, entre diferentes componentes, nos vemos en la necesidad de pasar ese estado como prop a través de cada uno de los nodos del árbol de componentes, como se ve en la figura. Esto se convierte en una tarea engorrosa donde, además, pasamos el estado como prop por componentes que no lo necesitan.

![nodos_tree](redux01.png)

Con Redux, el estado está contenido fuera del árbol de componentes. Cuando un componente actualiza un estado se comunica directamente con el contenedor de estados de Redux, que actualiza el estado de una manera predefinida, predecible, y comunica el cambio con todos los componentes que consumen ese estado.

Podemos solucionar este mismo problema utilizando React context, que evita tener que pasar las props de un componente a otro hasta llegar al que lo necesita. También podemos utilizar los Hooks y useContext y con useReducer para realizar esta tarea. Redux es una solución que se implementó antes de que React context o los hooks estuvieran disponibles.

React es una librería de interfaz de usuario, mientras que Redux es una librería de manejo de estados. Para utilizar ambos en su conjunto, vamos a utilizar el paquete React-Redux, que es la librería oficial de Redux UI para vincular con React. React-Redux ofrece una serie de funciones que permiten conectar Redux con React.
