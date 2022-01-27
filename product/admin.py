from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Slider)
class SliderAdminRegister(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdminRegister(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdminRegister(admin.ModelAdmin):
    list_display = ['id','name','price','discut']
    list_editable = ['price','discut']
    search_fields = ['name','category']
    prepopulated_fields = {"slug":('name',)}