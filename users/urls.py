from django.urls import path
# É colocado em apelido para a contrib do Django para não dar conflito com as "views"
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Mostra a tela de login. A função LoginView do Django já tem tudo pronto,
    # somente que precisamos dizer qual  o template que vamos usar. Nesse caso,
    # estamos usando o template users/login.html. O name='login' serve para
    # que possamos usar o nome 'login' como chave para obter a URL dessa view.
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]   