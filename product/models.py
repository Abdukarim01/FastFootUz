from django.db import models
# Create your models here.
class Slider(models.Model):
    poster = models.ImageField("Tovar rasm",upload_to='sliderimgs/')
    name = models.CharField('Tovar nomi',max_length=300)
    name_plus = models.CharField('Tovar nomi qo\'shimcha',max_length=200,blank=True)
    about = models.TextField('Tovar haqida')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Category(models.Model):
    poster = models.ImageField("Kategoriya rasm",upload_to='categoryimgs/')
    name = models.CharField("Kategoriya nomi",max_length=100)
    slug = models.SlugField("*",max_length=100,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Product(models.Model):
    poster = models.ImageField("Tovar rasm",upload_to='prductsimgs/')
    name = models.CharField("Tovar nomi",max_length=200)
    slug = models.SlugField("*",max_length=200,unique=True)
    price = models.IntegerField("Tovar narxi")
    about = models.TextField("Tovar haqida")
    star = models.IntegerField("Tovar yulduzchalari")
    discut = models.IntegerField("Tovar chegirmasi",blank=True,default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product_category")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']