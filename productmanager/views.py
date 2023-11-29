from django.shortcuts import render, get_object_or_404,HttpResponse, get_list_or_404
from productmanager.models import Product

# Create your views here.

def get_product_by_id(request,id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(product)

def get_all_products(request):
    products = Product.objects.all()
    return_value = ""
    for product in products:
        return_value += str(product) + "\n"

    return HttpResponse(return_value)
