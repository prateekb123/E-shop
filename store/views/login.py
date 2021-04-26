from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customers import Customer
from django.views import View



class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.getCustomer_by_email(email)
        print(customer)

        error_message = None
    

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email']= customer.email

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('index_page')
            else:
                error_message = "Email or Password Incorrect"
        else:
            error_message = "Email or Password Incorrect"
        return render(request, 'login.html', {'error':error_message})

        
