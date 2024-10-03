console.log('El tipo de dato `object` (objeto)')
var object = {
    name: "Juan",
    lastName: "Perez",
    phone: "55443322"
}
console.log(object);

console.log('\n');

console.log ('typeof de un tipo de dato String')
var name = "Carlos";
console.log(typeof name);

console.log ('typeof de un tipo de dato number')
var age = 5;
console.log(typeof age);

console.log ('typeof de un tipo de dato object')
var person = {
    name: "Juan",
    lastName: "Perez",
    phone: "55443322"
}
console.log(typeof person);

console.log ('typeof de un tipo de dato boolean')
var boolean = false;
console.log(typeof boolean);

console.log ('typeof de un tipo de dato function')
function myFunction() { }
console.log(typeof myFunction);

console.log ('typeof de un tipo de dato Symbol')
var symbol = Symbol("mi simbolo");
console.log(typeof symbol);

console.log ('typeof de un tipo de dato Class')
class Person {
	constructor(newName, newLastName) {
		this.name = newName;
		this.lastName = newLastName;
	}
}
console.log(typeof Person);

console.log('\n');