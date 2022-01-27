from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Cart)
class CartAdminRegister(admin.ModelAdmin):
    list_display = ['usercart']

@admin.register(CartProduct)
class CartProductAdminRegister(admin.ModelAdmin):
    list_display = ['to_cart','product']