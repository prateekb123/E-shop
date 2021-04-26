from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.customers import Customer
from django.views import View
from store.models.orders import Order



class checkout(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:

            order = Order(customer = Customer(id = customer),
                        product = product,
                        quantity = cart.get(str(product.id)),
                        price = product.price,
                        address = address,
                        phone = phone
                        )
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('cart_page')