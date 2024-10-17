const user = {
    name: 'Miguel',
    age: 39,
    zodiac: 'Virgo'
}
function print_info(data){
    return '<h1>Hola ' + data.name + '</h1>'
}

// crea el elemento h1 en body como se define en el return de la función
document.body.innerHTML = print_info(user) 

// podemos declarar la función indicando cual es el atributo que necesitamos del objeto que nos van a pasar por parámetro
function print_info_2({age}){
    return '<h2>Tu edad es ' + age + '</h2>'
}

// vuelve a crear el h1 y suma el h2 al documento
// pasamos el objeto user pero la función solo va a usar el atributo age del objeto que pasamos
document.body.innerHTML = print_info(user) + print_info_2(user)

function print_info_3(data){
    // creamos tres constantes desestructurando el objeto que llega por parámetro
    const {name, age, zodiac} = data
    return '<p>Tu nombre es ' + name + ', tu edad es '+age+' y tu signo es ' + zodiac + '</p>'
}
document.body.innerHTML = print_info(user) + print_info_2(user) + print_info_3(user)