from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Account(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    image = models.ImageField(upload_to='users-image', default='default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')

class Feature(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='categories-image', blank=True, null=True)

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=32)
    image = models.ImageField(upload_to='products-image', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='products')
    features = models.ManyToManyField(Feature, blank=True)
    off_percent = models.CharField(max_length=8, blank=True, null=True)
    off_price = models.CharField(max_length=32, blank=True, null=True)

class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    image = models.ImageField(upload_to='products-images', blank=True, null=True)
    product = models.ManyToManyField(Product, related_name='images')

class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    products = models.ManyToManyField(Product, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cart')

class Like(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['product', 'user']
