from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> This is blog page</h1>')