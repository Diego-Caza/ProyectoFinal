from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import logout as do_logout
from django.shortcuts import redirect

from .forms import RegisterForm

class NewUser(CreateView):
	model = User
	template_name = 'usuarios/registrousu.html'
	form_class = RegisterForm

	def get_success_url(self):
		return reverse('login')

def logout(request):
	# Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('inicio')