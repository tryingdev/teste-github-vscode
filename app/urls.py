from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
]