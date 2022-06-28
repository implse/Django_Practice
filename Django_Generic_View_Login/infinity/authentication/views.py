from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


# Index
def index(request):
    return render(request, "authentication/index.html")


# Success
@login_required
def dashboard(request):
    print(request.POST)
    return render(request, "authentication/dashboard.html")