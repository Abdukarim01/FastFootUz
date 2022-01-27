from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Cart,Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account.models import Cart,CartProduct
# Create your views here.
def sign_up(request):
    username_error = False
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            username_error = True
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()
            success = authenticate(username=username, password=password)
            login(request, success)
            createcart = Cart.objects.create(usercart=User.objects.get(id=request.user.id))
            return redirect("/")

    context = {
        "username_error":username_error,
        "exsit_username":request.POST.get('username')
    }
    return render(request,'sign_up.html',context)

def sign_in(request):
    in_error = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        success = authenticate(username=username, password=password)
        if success:
            login(request, success)
            return redirect("/")
        else:
            in_error = True
    context = {
        "in_error":in_error
    }
    return render(request,'sign_in.html',context)

def cart(request):
    return render(request,'cart.html')

def logoutuser(request):
    logout(request)
    return redirect("/")

@csrf_exempt
def addcart(request):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(usercart=request.user.id)
            CartProduct.objects.create(product_id=int(request.POST.get('pr_id')), to_cart_id=cart.id,
                                       quantity=int(request.POST.get('pr_quant')))
        except:
            pass
        return JsonResponse({"status":'save'})
    else:
        return JsonResponse({"status":'error'})

@csrf_exempt
def deletecart(request):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(usercart=request.user.id)
            trash = request.POST.get('tr_id')
            to_cart = CartProduct.objects.filter(to_cart_id=cart.id,product_id=trash)
            to_cart.delete()
            to_cart.save()
        except:
            pass
        return JsonResponse({"status": 200})

    else:
         return JsonResponse({"status":400})
