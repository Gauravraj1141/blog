from django.urls import path
from userprofile.apis.user_profile_views import  RegisterUser, LoginUser, LogoutUser, Profile, ProfileEdit , otp_send

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile-edit/', ProfileEdit.as_view(), name='profile-edit'),
    path('otp-send/', otp_send, name='otp-send')
]