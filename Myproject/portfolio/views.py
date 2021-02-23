from django.shortcuts import render
from .models import Project

# Create your views here.
def Home(request):
    var = Project.objects.all()
    return render(request, 'portfolio/home.html', {'display': var})
