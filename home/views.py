from django.shortcuts import render
from .models import Projects
# Create your views here.
def home(request):
    mainProjects=Projects.objects.filter()
    context={
        "mainProjects":mainProjects
    }
    return render(request, "index.html", context)