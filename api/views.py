from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def product_list(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe = False)

def product_detail(request, id):
    try:
        product = Product.objects.filter(id=id).values().first()
        return JsonResponse(product)
    except:
        return JsonResponse({'error' : 'Not found'}, status = 404)

def category_list(request):
    categories = Category.objects.all().values()
    return JsonResponse(list(categories), safe = False)

def category_detail(request, id):
    try:
        category = Category.objects.filter(id=id).values().first()
        return JsonResponse(category)
    except:
        return JsonResponse({'error' : 'Not found'}, status = 404)

def category_products(request, id ):
    products = Product.objects.filter(category_id = id).values()
    return JsonResponse(list(products), safe = False)




# Create your views here.
