/*
En el ejercicio utilizamos las ``para indicar que, lo que esta entre las tildes, va a formatearse como un`string`respetando los espacios y los saltos de línea. Lo que encontramos entre las tiles se formatea como está escrito. Para poder consultar los valores de los atributos utilizamos`${this.atributo}`, esto indica que, en lugar de mostrar es sentencia, muestre el valor guardado en el atributo al que hace referencia.
 */

class Persona {

    // atributo de clase
    static contadorPersonas = 0;

    // constructor de la clase
    constructor(nombre, apellido, edad) {

        // el atributo de objeto _idPersona se asigna valor a partir del atributo de clase contadorPersonas
        this._idPersona = ++Persona.contadorPersonas;

        // atributos de objeto
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    // getter y setter

    // idPersona no requiere setter por que su valor se asigna en el constructor mediante el atributo de clase contadorPersonas
    get idPersona() { return this._idPersona; }

    get nombre() { return this._nombre; }
    set nombre(nombre) { this._nombre = nombre; }

    get apellido() { return this._apellido; }
    set apellido(apellido) { this._apellido = apellido; }

    get edad() { return this._edad; }
    set edad(edad) { this._edad = edad; }

    // sobreescribimos el método toString para devolver como string los datos de los atributos del objeto
    toString() {

        // damos formato al string de salida mediante las ``
        return `${this._idPersona} ${this._nombre} ${this._apellido} ${this.edad}`;

    }

}

// la clase Empleado hereda de la clase Persona, es decir Empleado es la clase hijo y Persona la clase padre
class Empleado extends Persona {

    // atributo de clase
    static contadorEmpleados = 0;

    // constructor de la clase
    constructor(nombre, apellido, edad, sueldo) {

        // llama al constructor de la clase padre, es decir el constructo de la clase Persona
        super(nombre, apellido, edad);

        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;


    }

    // getter y setter
    get idEmpleado() { return this._idEmpleado; }

    get sueldo() { return this._sueldo; }
    set sueldo(sueldo) { this._sueldo = sueldo; }

    toString() {

        // llamamos al metodo toString de la clase padre Persona mediante la palabra reservada super
        return `${super.toString()} ${this._idEmpleado} ${this._sueldo}`;
    }

}

class Cliente extends Persona {

    // atributo de clase
    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro) {

        // llamamos al contructor de la clase padre Persona
        super(nombre, apellido, edad);

        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente() { return this._idCliente; }

    get fechaRegistro() { return this._fechaRegistro; }
    set fechaRegistro(fechaRegistro) { this._fechaRegistro = fechaRegistro; }

    toString() {
        return `${super.toString()} ${this._idCliente} ${this._fechaRegistro}`;
    }

}

// prueba clase Persona
let persona1 = new Persona('Juan', 'Perez', 28);
console.log(persona1.toString());
let persona2 = new Persona('Carlos', 'Ramirez', 35);
console.log(persona2.toString());

// prueba clase Empleado
let empleado1 = new Empleado('Karla', 'Gomez', '25', 5000);
console.log(empleado1.toString());
let empleado2 = new Empleado('Laura', 'Quintero', 33, 7000);
console.log(empleado2.toString());

// prueba de clase Cliente
let cliente1 = new Cliente('Miguel', 'Cervantes', 30, new Date());
console.log(cliente1.toString());
let cliente2 = new Cliente('Maria', 'Lara', 38, new Date());
console.log(cliente2.toString());