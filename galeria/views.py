from django.shortcuts import render
from galeria.models import Fotografia

# Create your views here.




def index(request):
    fotografias = Fotografia.objects.all()

    return render(request, 'galeria/index.html', {"dados": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')