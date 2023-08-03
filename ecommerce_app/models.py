from django.db import models

# Create your models here.

class shopmodel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username


class usermodel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class addproductmodel(models.Model):
    name = models.CharField(max_length=30)
    proid = models.IntegerField()
    image = models.ImageField(upload_to='ecommerce_app/static')
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class cartmodel(models.Model):
    name = models.CharField(max_length=30)
    proid = models.IntegerField()
    image = models.ImageField(upload_to='ecommerce_app/static')
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name


