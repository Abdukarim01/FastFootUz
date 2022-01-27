from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'index.html')

def shopall(request):
    return render(request,'shop.html')

def category(request,c_name,c_id):
    category = Category.objects.get(id=c_id,slug=c_name)
    category_product = Product.objects.filter(category=category)
    context = {
        "category_product":category_product,
        "category_name":category
    }
    return render(request,'category.html',context)

def getdetail(request,p_slug,p_id):
    product = Product.objects.get(slug=p_slug,id=p_id)
    context = {
        "detail_product":product
    }
    return render(request,'shop-single.html',context)