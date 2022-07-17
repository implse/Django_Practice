from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms

# Index
def index(request):
    return render(request, "authentication/index.html")

# Login User
def login_user(request):
    form = forms.LoginForm()
    warning_message = ""
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,"authentication/dashboard.html",  {"username": username})
            else:
                warning_message = "invalid username or password"
    return render(request, "authentication/login.html", context={"form": form, "warning_message": warning_message})

# Logout User
def logout_user(request):
    logout(request)
    return redirect("index")  

# Success
@login_required
def dashboard(request):
    return render(request, "authentication/dashboard.html")

