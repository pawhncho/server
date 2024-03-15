from django.contrib import admin
from .models import Account, Feature, Category, Product, Image, Cart, Like

# Register your models here.
admin.site.register(Account)
admin.site.register(Feature)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(Like)
