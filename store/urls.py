"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, login, signup, logout, cart, checkout, orders
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', home.Index.as_view(), name="index_page"),
    path('signup', signup.Signup.as_view(), name= 'signup_page' ),
    path('login', login.Login.as_view(), name="login_page" ),
    path('logout', logout.logout, name="logout_page" ),
    path('cart', cart.cart.as_view(), name="cart_page" ),
    path('checkout', checkout.checkout.as_view(), name="checkout_page" ),
    path('orders', auth_middleware(orders.orders.as_view()), name="order_page" )

]
