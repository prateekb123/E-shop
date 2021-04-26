from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customers import Customer
from django.views import View



class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')


    def post(self, request):
        return self.registerUser(request)

    def registerUser(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone_number')

        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'phone' : phone
        }

        #validation
        error_message = None

        customer = Customer(first_name = first_name,
                                last_name = last_name,
                                email = email,
                                password = password,
                                phone = phone)

        
        error_message = self.CustomerValidation(customer)

        #saving/registering
        if error_message == None: 

            #hashing password before saving
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index_page')
        else:
            data = {
                'error' : error_message,
                'values' : value
            }
            
            return render(request, 'signup.html', data)

    
    def CustomerValidation(self, customer):
        error_message = None

        if (not customer.first_name) or len(customer.first_name)<4:
                error_message = "First Name Required (Min 4 letters) !!"
        elif (not customer.last_name) or len(customer.last_name)<4:
            error_message = "Last Name Required (Min 4 letters) !!"
        elif (not customer.phone) or len(customer.phone)<10:
            error_message = "Phone number Required (Min 10 digits) !!"
        elif customer.isExists():
                error_message = "Email Address already registered"

        return error_message

