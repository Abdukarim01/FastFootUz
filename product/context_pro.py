from django.contrib.auth.models import User
from .models import *
from account.models import Cart,CartProduct


def viewproducts(request):
    bell = []
    context = {}
    if request.user.is_authenticated:
       if request.user.is_staff == False:
          cart = Cart.objects.get(usercart=request.user.id)
          to_cart = CartProduct.objects.filter(to_cart=cart.id)
          context["cart_item"] = to_cart
          context["cart_len"] = len(to_cart)

          for i in to_cart:
              bell.append((i.product.price * i.quantity ) - ((i.product.price * i.quantity / 100) * i.product.discut ))
          context["sum_all"] = sum(bell)
    else:
        context["all_users"] = User.objects.all()

    context["sliders"] = Slider.objects.all()
    context["lens"] = range(0, len(Slider.objects.all()))
    context["categories"] = Category.objects.all()
    context["products"] = Product.objects.all()
    return context

