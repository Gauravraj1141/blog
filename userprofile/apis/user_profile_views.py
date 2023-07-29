from django.shortcuts import redirect, render
from django.views import View
from userprofile.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from centralapp.apis.email_send import send_otp_to_user
import random
import json
from product.models import Cart


class RegisterUser(View):
    template_name = 'userprofile/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("profile")
        return render(request, self.template_name, {'login': False})

    def post(self, request):
        try:
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password != confirm_password:
                return render(request, self.template_name, {'status': "Confirm passwrod doesn't match"})
            user = User.objects.create(
                username=request.POST['username'], email=request.POST['email'], password=request.POST['password'], email_is_verified=True)
            # create cart for this user 
            cart = Cart.objects.create(user=user)
            return redirect('login')
        except Exception as ex:
            return render(request, self.template_name, {'status': ex})


class LoginUser(View):
    template_name = 'userprofile/login.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, self.template_name, {'login': False})
        else:
            return redirect("profile")

    def post(self, request):
        username = request.POST['email_or_username']
        password = request.POST['password']
        try:
            authuser = authenticate(username=username, password=password)
            login(request, authuser)
            return redirect("home")
        except Exception as ex:
            messages.warning(request, "Username or Password is incorrect. Please try again." )
            return render(request, self.template_name, {'status': ex})


class LogoutUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("home")
        else:
            return redirect("login")


class Profile(View):
    template_name = "userprofile/profile.html"

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            context = {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user.phone
            }
            return render(request, self.template_name, context)
        else:
            return redirect("login")


class ProfileEdit(View):
    template_name = "userprofile/profile_edit.html"

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            user_data = User.objects.filter(
                Q(username=user) | Q(email=user)).first()
            first_name = user_data.first_name
            last_name = user_data.last_name
            phone = user_data.phone
            if first_name == None:
                first_name = ""
            if last_name == None:
                last_name = ""
            if phone == None:
                phone = ""

            context = {"username": user_data.username, 'email': user_data.email,
                       'password': user_data.password, 'first_name': first_name, 'last_name': last_name, 'phone': phone}
            return render(request, self.template_name, context)
        else:
            return redirect("login")

    def post(self, request):
        if request.user.is_authenticated:
            try:
                user = request.POST
                update_profile_data = User.objects.filter(username=user['username']).update(
                    first_name=user['first_name'], last_name=user['last_name'], phone=user['phone'])
                return redirect('profile')
            except Exception as ex:
                return redirect('profile')
        else:
            return redirect("login")


@csrf_exempt
def otp_send(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            otp = random.randint(1000, 9999)
            data = dict(zip(("otp","email"),(otp,email)))
            send_otp_to_user(data)
            response_data = {"status": 200, "otp": otp}
            return HttpResponse(json.dumps(response_data),  content_type="application/json")
        except Exception as ex:
            return HttpResponse(ex)
    return HttpResponse("NOt a post request")


