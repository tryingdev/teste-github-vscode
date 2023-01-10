from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import  login_required

def home(request):
    return render(request, 'login.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe usuário com esse nick')

        user = User.objects.create_user(username=username, email = email, password = password)

        return HttpResponse('Cadastrado com sucesso!!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return plataforma(request)
        else:
            return HttpResponse('algo invalido')

@login_required(login_url="/app/login/")
def plataforma(request):
    return  render(request, 'index.html')