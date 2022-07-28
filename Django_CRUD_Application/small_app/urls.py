from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_product/', views.create_product, name='create_product'),
    path('read_product/<str:product_id>/', views.read_product, name='read_product'),
    path('update_product/<str:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<str:product_id>', views.delete_product, name='delete_product')

]
