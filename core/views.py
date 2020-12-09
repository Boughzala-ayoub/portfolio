from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'core/index.html')
def CV(request):
    return render(request, 'core/CV.html')
def projects(request):
    return render(request, 'core/projects.html')
def contact(request):
    return render(request, 'core/contact.html')
