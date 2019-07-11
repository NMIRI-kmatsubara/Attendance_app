from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.views import generic
from .forms import LoginForm
from .models import Practice, Attend

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def schedule(request):
    practices = Practice.objects.all().order_by('date')
    return render(request, 'app/schedule.html', {'practices': practices})

def schedule_detail(request, practice_id):
    #指定したIDの練習内容を取得
    prac = Practice.objects.get(pk=practice_id)

    Attend_members = prac.practice_field.all().filter(check_attend='出席')
    return render(request, 'app/schedule_detail.html', {'Attend_members': Attend_members})



class Top(generic.TemplateView):
    template_name = 'app/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'app/top.html'

