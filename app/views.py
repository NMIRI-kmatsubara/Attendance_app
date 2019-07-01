from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def schedule(request):
    return render(request, 'app/schedule.html')