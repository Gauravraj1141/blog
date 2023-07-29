from django.urls import path, re_path
from payment.apis.proceed_payment_views import payment_success, payment_failed
# from django.conf.urls import url
from paypal.standard.ipn import views
urlpatterns = [
    path("payment-success/",payment_success,name="payment-success"),
    path("payment-failed/",payment_failed,name="payment-failed"),
]
   

