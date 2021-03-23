from django.shortcuts import render
from django.http import HttpResponse

def index(request):
      return render(request, 'index.html')

def index(request):
  return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
 return HttpResponse('<h1>My name is Tom and Bugs like me 🤪</h1>')

def bugs_index(request):
    return render(request, 'bugs/index.html', {'bugs': bugs})

class Bug:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

bugs = [
    Bug('BooBoo', 'Murder Hornet', 'Gentle Non-stinging Being', 1),
    Bug('Howie', 'House Fly', 'He really likes your eyes', 0),
    Bug('Dojo', 'Dragon Fly', 'A flying ace', 1)
]