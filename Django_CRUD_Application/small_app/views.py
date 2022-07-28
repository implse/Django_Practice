from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Index views
def index(request):
    """ 
    render a template containing all products + menu
    """
    all_product = Product.objects.all().order_by('-created_at')
    context = {'products': all_product }
    return render(request, 'index.html', context=context)

# Create view
def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form }
    return render(request, 'create_product.html', context=context)

# Read view
def read_product(request, product_id):
    if request.method == 'GET':
        product_detail = Product.objects.get(id=product_id)
        if product_detail == 'None':
            return redirect('home')
    context = {'product_detail': product_detail}
    return render(request, 'read_product.html', context=context)

# Update view
def update_product(request, product_id):
    product_detail = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, instance=product_detail)       
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form }
    return render(request, 'update_product.html', context=context)

# Delete view
def delete_product(request, product_id):
    product_to_delete = Product.objects.get(id=product_id)
    product_to_delete.delete()
    return redirect('index')

