from django.shortcuts import render
from .models import Projects, Category, Knowledge
# Create your views here.
def home(request):
    mainProjects=Projects.objects.filter()
    categories=Category.objects.filter()
    knowledge=Knowledge.objects.filter()
    

    context={
        "mainProjects":mainProjects,
        "categories":categories,
        "knowledge":knowledge
    }
    return render(request, "index.html", context)