from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def delete(request):
    return render(request, 'delete.html')

def detail(request):
    return render(request, 'detail.html')

def index(request):
    return render(request, 'index.html')

def update(request):
    return render(request, 'update.html')