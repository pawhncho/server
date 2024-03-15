from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Account, Feature, Category, Product, Image, Cart, Like
from .serializers import UserSerializer, AccountSerializer, CategorySerializer,\
                            ProductSerializer, FeatureSerializer, ImageSerializer,\
                                CartSerializer, LikeSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        if authenticate(username=username, password=password):
            user = authenticate(username=username, password=password)
            if Token.objects.filter(user=user).exists():
                token = Token.objects.filter(user=user).first()
                return Response(token.key)
            else:
                return Response(False)
        else:
            return Response(False)
    else:
        return Response('Login API')

@api_view(['GET'])
def account(request, token):
    if Token.objects.filter(key=token).exists():
        token = Token.objects.filter(key=token).first()
        if token.user:
            if Account.objects.filter(user=token.user).exists():
                account = Account.objects.filter(user=token.user).first()
                serializer = AccountSerializer(account, read_only=True)
                return Response(serializer.data)
            else:
                return Response(False)
        else:
            return Response(False)
    else:
        return Response(False)

@api_view(['GET'])
def search(request, keyword):
    result = {}
    if Category.objects.filter(name__contains=keyword).exists():
        categories = Category.objects.filter(name__contains=keyword).all()
        categories_serializer = CategorySerializer(categories, read_only=True, many=True)
        result['categories'] = categories_serializer.data
    if Product.objects.filter(name__contains=keyword).exists():
        products = Product.objects.filter(name__contains=keyword).all()
        products_serializer = ProductSerializer(products, read_only=True, many=True)
        result['products'] = products_serializer.data
    return Response(result)

@api_view(['GET'])
def product(request, uuid):
    if Product.objects.filter(uuid=uuid).exists():
        product = Product.objects.filter(uuid=uuid).first()
        serializer = ProductSerializer(product, read_only=True)
        return Response(serializer.data)
    else:
        return Response(False)

@api_view(['GET'])
def categories(request):
    _categories = Category.objects.all()
    serializer = CategorySerializer(_categories, read_only=True, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category(request, uuid):
    if Category.objects.filter(uuid=uuid).exists():
        category = Category.objects.filter(uuid=uuid).first()
        category_serializer = CategorySerializer(category, read_only=True)
        if category.products.exists():
            products = category.products.all()
            products_serializer = ProductSerializer(products, read_only=True, many=True)
            return Response({
                'category': category_serializer.data,
                'products': products_serializer.data,
            })
        else:
            return Response({
                'category': category_serializer.data,
                'products': False,
            })
    else:
        return Response(False)
