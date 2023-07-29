from django.shortcuts import redirect, render
from django.views import View
from userprofile.models import User
from django.db.models import Q

class Dashboard(View):
    pass