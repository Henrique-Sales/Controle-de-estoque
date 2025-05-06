from django.shortcuts import render
from usuarios.forms import loginForm
# Create your views here.

def login(request):
    dados = loginForm()
    return render(request, 'usuarios/login.html',{'form':dados})

def cadastro(request):
    return render(request,'usuarios/cadastro.html')

    