from django.shortcuts import render
from .models import Portfolio 

# Create your views here.
def portafolio(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio/portafolio.html', {'projects': projects})
