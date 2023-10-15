from django.shortcuts import render, HttpResponse, redirect
from .models import Member
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm
# Create your views here.
def home(request):
    #Check to see if logging in
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have logged in!")
            return redirect('home')
        else:
            messages.success(request, "You enter wrong username or password!")
            return redirect('home')
    else:
        return render(request, "home.html")

def members(request):
    names = Member.objects.all()
    context = {
        'names':names,
    }
    return render(request, "members.html", context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')
    
def register_user(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You have successfully register!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})