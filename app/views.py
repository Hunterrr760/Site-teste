from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

#FORMULARIO DE CADASTRO
def create(request):
    return render(request, 'create.html')

#INSERÇÃO DOS DADOS DOS USUARIOS NOS BANCOS
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senhas diferentes, as mesmas devem ser iguais!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Você foi cadastrado com sucesso!'
        data['msg'] = 'alert-success'
    return render(request, 'create.html', data)

#FORMULARIO DO PAINEL DE LOGIN
def painel(request):
    return render(request, 'painel.html')

#PROCESSAR O LOGIN
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou Senha invalidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)
    
#PAGINA INICIAL DO DASHBOARD
def dashboard(request):
    return render(request, 'dashboard/home.html')

#LOGOUT DO SISTEMA  
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar a senha
def changePassword(request):
    user = User.objects.get(email= request.user.email)
    user.set_password(request.POST['password'])
    user.save
    logout(request)
    return redirect('/painel/')