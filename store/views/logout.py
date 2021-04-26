from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customers import Customer
from django.views import View



def logout(request):
    request.session.clear()
    return redirect('login_page')