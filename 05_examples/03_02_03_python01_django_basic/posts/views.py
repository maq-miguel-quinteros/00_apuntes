# Se utiliza para crear una respuesta http a pedido get, post, put etc
from django.http import HttpResponse

# Mediante render convertimos el template en la respuesta a la petición http get
from django.shortcuts import render

# Lo utilizamos para poder generar una vista con los métodos que ofrece como el método get
from django.views.generic.base import View

class HelloWord(View):
    # Redefinimos el método get de View para generar una respuesta
    def get(self, request):
        # Creamos un diccionario con datos, pero el mismo puede venir de una clase de python en otro archivo etc.
        context = {
            'name': 'Miguel Ángel Quinteros',
            'age': 39,
            'languages': ['Python', 'Django', 'React']
        }

        # Pasamos los datos que queremos que se utilicen en el template como un tercer parámetro de un atributo del método render llamado context
        return render(request, 'hello_word.html', context=context)