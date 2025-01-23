from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):


    return render(request, 'home.html', context={'page':'Home Page'})

def about(request):
    context= {'page':'About Page'}
    return render(request, 'about.html', context)

def contact(request):
    context= {'page':'Contact Page'}
    return render(request, 'contact.html', context)




