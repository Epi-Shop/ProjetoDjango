from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """ Ele vai ver se o usuário está logado, caso esteja, ele vai fazer o logout"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register(request):
    """Cadastra um novo usuário."""
    if request.method != 'POST':
        # Se nenhum dado foi submetido; cria um formulário em branco
        form = UserCreationForm()
    else:
        # Dados de registro foram submetidos; processa os dados
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Loga o usuário em e redireciona para a página inicial
            # Passoword1 = Password2 é a senha que o usuário digitou
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    # Mostra um formulário em branco
    context = {'form': form}
    return render(request, 'users/register.html', context)

def login_view(request):
    """Realiza o login do usuário."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'users/login.html')
