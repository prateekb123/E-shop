from django.db import models
from .product import Product
from .customers import Customer
import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='', blank=True) 
    phone = models.CharField(max_length=12, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    
    @staticmethod
    def getproducts_by_customer_id(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')
    
    def placeOrder(self):
        self.save()

    