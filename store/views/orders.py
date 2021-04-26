from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View
from store.models.orders import Order

class orders(View):


    def get(self, request):
        customer = request.session.get('customer_id')
        orders_1 = Order.getproducts_by_customer_id(customer)
        return render(request, 'orders.html', {'orders':orders_1})


