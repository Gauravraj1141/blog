from django.shortcuts import redirect, render
from django.views import View
from userprofile.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import login_required
    

@login_required
def payment_success(request):
            return render(request, 'payment/payment_success.html')


@login_required
def payment_failed(request):
            return render(request, 'payment/payment_failed.html')
