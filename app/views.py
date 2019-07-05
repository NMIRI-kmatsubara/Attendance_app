from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.views import generic
from .forms import LoginForm


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def schedule(request):
    return render(request, 'app/schedule.html')

class Top(generic.TemplateView):
    template_name = 'app/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'app/top.html'