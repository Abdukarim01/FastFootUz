from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('',home,name='home'),
    path('shop/',shopall,name="shopall"),
    path('category/<str:c_name>/<int:c_id>/',category,name="category"),
    path('detail/<str:p_slug>/<int:p_id>',getdetail,name="product_detail")
]