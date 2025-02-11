from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IndexView, CadastrarUsuario, CachorrosView, GatoView, GatoDetalheView, CachorrosDetalheView, querocachorroView, querogatoView, feedback_sucessoView
from django.contrib.auth import views as auth_views


router = SimpleRouter()

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
    path('cadastro/', CadastrarUsuario.as_view(), name="cadastrar_usuario"),
    path('', IndexView.as_view(), name='index'),
    path('cachorros/', CachorrosView.as_view(), name='cachorros'),
    path('cachorro-detalhe/<int:id>/', CachorrosDetalheView.as_view(), name='cachorro-detalhe'),
    path('gatos/', GatoView.as_view(), name='gatos'),
    path('gato-detalhe/<int:id>/', GatoDetalheView.as_view(), name='gato-detalhe'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Logout.html'), name='logout'),
    path('querocachorro/<int:id>/', querocachorroView, name='querocachorro'),
    path('querogato/<int:id>/', querocachorroView, name='querogato'),
    path('queroadotar/sucesso/', feedback_sucessoView, name='feedback_sucesso')
]
