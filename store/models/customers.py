from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)

    def register(self):
        self.save()
        

    def isExists(self):
        return Customer.objects.filter(email = self.email)


    @staticmethod
    def getCustomer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False