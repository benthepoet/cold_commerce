from django.db import models

class Cart(models.Model):
    pass    

class Category(models.Model):
    name = models.CharField(max_length=64)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
