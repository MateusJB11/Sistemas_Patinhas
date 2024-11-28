from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from .form import CustomUserCreationForm
from .models import Cachorro, Gato



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CadastrarUsuario(FormView):
    template_name = 'Cadastro.html'
    form_class= CustomUserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')



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

class CachorrosView(TemplateView):
    template_name = 'Cachorros.html'

    def get_context_data(self, **kwargs):
        context = super(CachorrosView, self).get_context_data(**kwargs)
        context['cachorros'] = Cachorro.objects.all()
        return context

class GatoView(TemplateView):
    template_name = 'Gatos.html'

    def get_context_data(self, **kwargs):
        context = super(GatoView, self).get_context_data(**kwargs)
        context['gatos'] = Gato.objects.all()
        return context


# Create your views here.
