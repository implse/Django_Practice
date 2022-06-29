from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.


# Index
def index(request):
    return render(request, "authentication/index.html")

# Login user
def login_user(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,"authentication/dashboard.html",  {"username": username})
            else:
                return render(request, "authentication/login.html", {"warning_message": "invalid username or password"})
    return render(request, "authentication/login.html")

# Logout user
def logout_user(request):
    logout(request)
    return redirect("index")  

# Success
@login_required
def dashboard(request):
    return render(request, "authentication/dashboard.html")