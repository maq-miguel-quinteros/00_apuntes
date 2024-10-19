const user = {
    name: 'Miguel',
    address: {
        city: 'Tucumán'
    },
    location: {
        city: 'San Miguel de Tucumán'
    }
}
console.log(user.address.city)
console.log(user.location.city) // devuelve un error

// forma normal de resolverlo. Si location no está definido no ingresa en el condicional
if (user.location){
    console.log(user.location.city)
}

// mediante optional chaining indicamos con ? cual es la variable que tiene que evaluar si existe
console.log(user.location?.city) // devuelve undefined