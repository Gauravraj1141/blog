from django.urls import path
from centralapp.apis.home_stuff import Home, AboutUs, ContactUs, Sales

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("about-us",AboutUs.as_view(),name="about-us"),
    path("contact-us",ContactUs.as_view(),name="contact-us"),
    path("sales",Sales.as_view(),name="sales"),
]