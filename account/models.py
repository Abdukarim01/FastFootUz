from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
class Cart(models.Model):
    usercart = models.OneToOneField(User,on_delete=models.CASCADE,related_name="usercart")

class CartProduct(models.Model):
    to_cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="to_cart")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    quantity = models.IntegerField(default=1)

    def bell(self):
        return (self.product.price * self.quantity) - ((self.product.price * self.quantity / 100) * self.product.discut)

    # def delete(self):
    #     self.product.delete()
