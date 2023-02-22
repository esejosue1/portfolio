from django.shortcuts import render
from .models import Projects, Category, Knowledge,Experience
# Create your views here.
def home(request):
    mainProjects=Projects.objects.filter()
    categories=Category.objects.filter()
    knowledge=Knowledge.objects.filter()
    experience=Experience.objects.filter()
    

    context={
        "mainProjects":mainProjects,
        "categories":categories,
        "knowledge":knowledge,
        "experience":experience
    }
    return render(request, "index.html", context)