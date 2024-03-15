from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, Feature, Category, Product, Image, Cart, Like

# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',\
                    'email', 'date_joined']

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Account
        fields = ['uuid', 'image', 'user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['uuid', 'name', 'image', 'products']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'price',\
                    'image', 'categories', 'features',\
                        'off_percent', 'off_price', 'images', 'likes']

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['uuid', 'name', 'value']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['uuid', 'image', 'product']

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['uuid', 'products', 'user']

class LikeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ['uuid', 'product', 'user']
