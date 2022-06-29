from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


# Index
def index(request):
    return render(request, "authentication/index.html")


# Success
@login_required
def dashboard(request):
    return render(request, "authentication/dashboard.html")