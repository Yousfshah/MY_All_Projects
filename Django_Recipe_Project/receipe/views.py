from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login-page/')
def reciepes(request):
    if request.method == 'POST':
        receipe_name= request.POST.get('receipe_name')
        receipe_description= request.POST.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')

        receipe.objects.create(
            receipe_name=receipe_name, 
            receipe_description=receipe_description, 
            receipe_image=receipe_image, 
        )
        return redirect('/reciepes/')
    
    queryset= receipe.objects.all()

    if request.GET.get('search'):
        queryset= queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context= {'receipe':queryset}

    return render(request, 'recipies.html', context)

@login_required(login_url='/login-page/')
def delete_receipe(request, id):
    queryset= receipe.objects.get(id= id)
    queryset.delete()
    return redirect('/reciepes/')

@login_required(login_url='/login-page/')
def update_receipe(request, id):
    queryset= receipe.objects.get(id= id)
    context= {'receipe':queryset}
    if request.method == 'POST':
        receipe_name= request.POST.get('receipe_name')
        receipe_description= request.POST.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')

        queryset.receipe_name= receipe_name
        queryset.receipe_description= receipe_description

        if receipe_image:
            queryset.receipe_image= receipe_image

        queryset.save()
        return redirect('/reciepes/')

    return render(request, 'update_receipe.html', context)

def login_page(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login-page/')
        user= authenticate(username= username, password= password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login-page/')     

        else:
            login(request, user)
            return redirect('/reciepes/')     
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login-page/')

def register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register-page/')

        user= User.objects.create(
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account successfully created')

        return redirect('/register-page/')


    return render(request, 'register.html')