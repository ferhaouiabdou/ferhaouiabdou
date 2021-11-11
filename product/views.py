from django.shortcuts import render
from .models import Product
# Create your views here.


def product(request):
    context = {
        'products' : Product.objects.all()
    }
    return render (request , 'product/product.html' , context)

def products(request):
    return render (request , 'product/products.html')


def search(request):
    return render (request , 'product/search.html')