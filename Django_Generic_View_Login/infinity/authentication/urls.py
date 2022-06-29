from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.LoginView.as_view(template_name="authentication/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard")
]

