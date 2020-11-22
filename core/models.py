from django.db import models

class Cart(models.Model):
    pass    

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return ("%s - %s" % (self.product.name, self.name))
