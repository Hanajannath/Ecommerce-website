from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from adminapp.forms import RegisterForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout
from userapp.models import UserProfile

def welcome(request):
    return render(request,'welcome.html')
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            UserProfile.objects.create(user=user)  
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
        else:
           
            messages.error(request, "Registration failed. Please correct it.")
    else:
        form = RegisterForm()
    return render(request, 'Register.html', {"form": form})
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            if user.is_staff or user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('cards')
        else:
            messages.error(request,"Invalid username or password!")
            return redirect('login')
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
from django.contrib.auth import logout
def logout_view(request):
    request.session.flush()   # clears cart + session data
    logout(request)           # logs out user
    return redirect('welcome')
def dashboard(request):
    return render(request,'dashboard.html')


