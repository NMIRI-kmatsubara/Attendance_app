from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.views import generic
from .forms import LoginForm
from .models import Practice

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def schedule(request):
    practices = Practice.objects.all().order_by('date')
    return render(request, 'app/schedule.html', {'practices': practices})

class Top(generic.TemplateView):
    template_name = 'app/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'app/top.html'