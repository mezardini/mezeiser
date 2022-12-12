from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_product', views.create_product, name='create_product'),
    path('product', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('category', views.category, name='category'),
]