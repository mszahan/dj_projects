from django.shortcuts import render, get_object_or_404
from .models import Product


def index (request):
    products = Product.objects.all()
    return render(request, 'food_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'food_detail.html', {'product':product})
