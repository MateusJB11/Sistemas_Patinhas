from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IndexView, CadastrarUsuario, logar

router = SimpleRouter()

urlpatterns = [
    path('login/', logar, name='login'),
    path('cadastro/', CadastrarUsuario.as_view(), name="cadastrar_usuario"),
    path('', IndexView.as_view(), name='index'),
]
