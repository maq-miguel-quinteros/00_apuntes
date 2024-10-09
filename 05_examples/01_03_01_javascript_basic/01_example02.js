class Producto {

    // atributo de clase
    static contadorProductos = 0;

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    // getter y setter
    get idProducto() { return this._idProducto; }

    get nombre() { return this._nombre; }
    set nombre(nombre) { this._nombre = nombre; }

    get precio() { return this._precio; }
    set precio(precio) { return this._precio = precio; }

    toString() {

        // el $ extra que tiene la sentencia $${this._precio} se va a imprimir como el símbolo y al lado el valor del atributo this._precio
        return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}  `;
    }
}


class Orden {
    static contadorOrdenes = 0;

    // con el método get como static estamos simulando una constante de clase
    static get MAX_PRODUCTOS() {
        return 5;
    }

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
    }

    // getter y setter
    get idOrden() { return this._idOrden; }

    agregarProducto(producto) {

        // revisame si el array _productos tiene menos de 5 elemenos y mediante push sumamos a la al array un elemenos de tipo productos
        if (this._productos.length < Orden.MAX_PRODUCTOS) {
            this._productos.push(producto);
        }
        else {

            // mensaje que se muestra si el array _productos tiene mas de 5 elementos
            console.log('No se pueden agregar más productos');
        }
    }

    calcularTotal() {
        let totalVenta = 0;

        // mediante for of recorremos un array elementos por elemento, el elemento se guarda en la variable  producto, con of indicamos cual es el array sobre el cual vamos a iterar
        for (let producto of this._productos) {
            totalVenta += producto.precio;
        }
        return totalVenta;
    }

    mostrarOrden() {
        let productosOrden = '';
        for (let producto of this._productos) {

            // en productosOrden armamos el string que vamos a mostrar despues con \n hacemos un salto de línea antes de sumar el string del método toString
            productosOrden += '\n{' + producto.toString() + '}';
        }

        // mostramos los datos de la orden y al final la lista de productos guardada en productosOrden
        console.log(`Orden: ${this._idOrden} Total: $${this.calcularTotal()}, Productos: ${productosOrden} `);
    }
}

// creamos objetos de tipo Producto
let producto1 = new Producto('Pantalón', 200);
let producto2 = new Producto('Camisa', 100);

// creamos un objeto de tipo Orden  y agregamos los productos creados a la orden, despues mostramos la orden
let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.mostrarOrden();

let orden2 = new Orden();
let producto3 = new Producto('Cinturon', 50);
orden2.agregarProducto(producto3);
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.mostrarOrden();