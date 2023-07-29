from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Q
import json
from product.models import TradeProduct, CartItem


class ShowProducts(View):
    template_name = 'products/show_products.html'
    def get(self, request):
        products_details = TradeProduct.objects.all().values()
       
        if request.user.is_authenticated:
            products_details1 = []
            for data in products_details:
                # check the product in cart 
                p_id = data['product_id']
                product_in_cart = CartItem.objects.filter(Q(product__product_id = p_id) & (Q(cart__user__username = request.user)|Q(cart__user__email=request.user))).exists()
                data['product_in_cart'] = product_in_cart
                products_details1.append(data)
            return render(request, self.template_name, {'login': True,'products':products_details1})
        return render(request, self.template_name, {'login': False,'products':products_details})
