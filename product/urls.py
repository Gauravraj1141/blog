from django.urls import path
from product.apis.manage_products import ShowProducts
from product.apis.manage_cart import add_to_cart,delete_cart,ShowCart


urlpatterns = [
    path("show-products",ShowProducts.as_view(),name="show-products"),
    path("show-cart",ShowCart.as_view(),name="show-cart"),
    path("add-to-cart/<int:id>/",add_to_cart,name="add-to-cart"),
    path("delete-cart/<int:id>/",delete_cart,name="delete-cart")
]
   


