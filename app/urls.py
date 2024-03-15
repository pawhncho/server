from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('auth/login/', views.login),
    path('account/<token>/', views.account),
    path('search/<keyword>/', views.search),
    path('product/<uuid>/', views.product),
    path('categories/', views.categories),
    path('category/<uuid>/', views.category),
]
