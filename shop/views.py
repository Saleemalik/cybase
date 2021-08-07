import json
from typing import ContextManager
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, items

# Create your views here.
def home(request):
    products = Products.objects.all()
    product_sub = items.objects.all()
    if request.method == 'POST':
        size = request.POST['size']
        color = request.POST['color']
        product_name = request.POST['name']
        product_id = Products.objects.get(productName=product_name)
        product_id = product_id.id
        if size == "Select" :
            return JsonResponse('false1', safe=False)
        elif color == "Select" :
            return JsonResponse('false2', safe=False)
        else:
            try:
                price = items.objects.get(size=size, product_name=product_id, productColor=color)
                price = json.dumps(price.price)
    
                return JsonResponse(price, safe=False)
            except:
                return JsonResponse('false3', safe=False)
            
    Context = {
        'products': products,
        'product_sub': product_sub
    }
    return render(request, 'shop.html', Context)