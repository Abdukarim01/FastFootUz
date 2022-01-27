from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/',sign_up,name="sign_up"),
    path('signin/',sign_in,name="sign_in"),
    path('logout/',logoutuser,name="logout"),
    path('cart/',cart,name="cart"),
    path('addcart/',addcart,name="addcart"),
    path('deletecart/',deletecart,name="deletecart"),
]