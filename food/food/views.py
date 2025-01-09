from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def index (request):
    products = Product.objects.all()
    return render(request, 'food_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'food_detail.html', {'product':product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form':form})


def update_product(request, id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form':form, 'product':product})


# def create_product(request):
#     form = ProductForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food_list')
#     return render(request, 'product_form.html', {'form':form})
    
