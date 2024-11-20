from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CadastrarUsuario(TemplateView):
    template_name = 'Cadastro.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.POST = None
        self.method = None

    def cadastrar(request):
        if request.method == "POST":
            form_usuario = UserCreationForm(request.POST)
            if form_usuario.is_valid():
                form_usuario.save()
                return redirect('Index')
        else:
            form_usuario = UserCreationForm()
        return render(request, 'Cadastro.html', {'form_usuario': form_usuario})


def logar(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        usuario = authenticate(request, username=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

# Create your views here.
