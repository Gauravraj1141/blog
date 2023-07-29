from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("centralapp.urls")),
    path("user/",include("userprofile.urls")),
    path("products/",include("product.urls")),
    path("payment/",include("payment.urls")),
    path('paypal/', include('paypal.standard.ipn.urls'))
]

# Serve media files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)