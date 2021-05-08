from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')


def info(request):
    return render(request, 'info.html')

def nos(request):
    return render(request, 'nos.html')
