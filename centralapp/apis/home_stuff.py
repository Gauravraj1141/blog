from django.shortcuts import redirect, render
from django.views import View
from userprofile.models import User
from django.contrib import messages
from django.db.models import Q
from centralapp.apis.email_send import send_email_to_sales, send_email_to_customer_service

class Home(View):
    template_name = 'central/home.html'

    def get(self, request):
        if request.user.is_authenticated:
            login = True
        else:
            login = False
        context = {'login':login}
        return render(request, self.template_name, context)

class AboutUs(View):
        template_name = 'central/about_us.html'
        def get(self,request):
            if request.user.is_authenticated:
                  login = True
            else:
                  login = False
            return render(request, self.template_name, {"login":login})




class ContactUs(View):
        template_name = 'central/contact_us.html'
        def get(self,request):
            if request.user.is_authenticated:
                  login = True
            else:
                  login = False
            return render(request, self.template_name, {"login":login})
        def post(self,request):
            if request.user.is_authenticated:
                  login = True
                  data = dict(zip(("name","email","phone_number","query"),(request.POST['name'],request.POST['email'],request.POST['phone'],request.POST['message'])))
                #   send email to customer service 
                  send_email_to_customer_service(data)
                  messages.success(request,"Your request has been submitted to customer team!")
                  return render(request, self.template_name, {"login":login})
            else:
                  login = False
            return render(request, self.template_name, {"login":login})
        

# sales form stuff  



class Sales(View):
        template_name = 'central/sales.html'
        def get(self,request):
            if request.user.is_authenticated:
                  login = True
            else:
                  login = False
            return render(request, self.template_name, {"login":login})
        def post(self,request):
            if request.user.is_authenticated:
                  login = True
                  data = dict(zip(("name","email","phone_number","query"),(request.POST['name'],request.POST['email'],request.POST['phone'],request.POST['message'])))
                  print(data) 
                  response = send_email_to_sales(data)
                  print(response)
                  messages.success(request,"Your request has been submitted to sales team!")
                  return render(request, self.template_name, {"login":login})
            else:
                  login = False
                  print(request.POST['name'])
                  print(request.POST)
            return render(request, self.template_name, {"login":login})
        

