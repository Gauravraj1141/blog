from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Q
import json
from product.models import TradeProduct,CartItem,Cart
from userprofile.models import User
from django.http import HttpResponse
# payment integration
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
# from django.contrib.auth.decorators import login_required
from django.urls import reverse


class ShowCart(View):
    template_name = 'products/cart.html'
     
    def get(self, request):
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(Q(cart__user__username = request.user) | Q(cart__user__email = request.user)).values()
            cart_total_amount = 0
            cart_product_quantity = 0
            email = request.user.email
            product_data_store = []
            for cart_item in cart_items:
                    product_data = TradeProduct.objects.filter(product_id=cart_item['product_id']).values()
                    for data in product_data:
                        product_data_store.append(data)
                        # fetch total price of cart 
                        quantity = cart_item['quantity']
                        price = data['product_price']
                        cart_product_quantity += quantity
                        cart_total_amount += (quantity*price)
            
            # payment button add and total amount add
            host = request.get_host()
            print("host>>",host)
            paypal_dict = {
                            'business': settings.PAYPAL_RECEIVER_EMAIL,
                            'amount': cart_total_amount,
                            'item_name': 'Order nyse trade',
                            'currency_code': 'USD',
                            'custom_value':"gaurav rjaput",
                            'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
                            'return_url': 'http://{}{}'.format(host,
                                                            reverse("payment-success")),
                            'cancel_return': 'http://{}{}'.format(host,
                                                                reverse('payment-failed')),
                        
                        }
            if cart_total_amount > 0:
                 form = PayPalPaymentsForm(initial=paypal_dict)
            else: 
                form = None
            context = {'email':email,'login': True,'products':product_data_store,'total_amount':cart_total_amount, 'total_products':cart_product_quantity,"payment_button":form}
            
            return render(request, self.template_name, context)
        else:
             return redirect("login")

   

def add_to_cart(request,id):
        try:
            if request.user.is_authenticated:
                product = TradeProduct.objects.get(product_id=id)
                cart = Cart.objects.get(user=request.user)
                cart_item = CartItem.objects.create(product=product,cart=cart)
                response_data = {"status": 200, "user": str(request.user),"cart_item_id":str(cart_item)}
                return HttpResponse(json.dumps(response_data),  content_type="application/json")
            else:
                response_data = {"status": 200, "user": 'annoymous'}
                return HttpResponse(json.dumps(response_data),  content_type="application/json")
        except Exception as ex:
                return HttpResponse("exception")


def delete_cart(request,id):
        try:
            if request.user.is_authenticated:
                product = TradeProduct.objects.get(product_id=id)
                cart = Cart.objects.get(user=request.user)
                cart_item = CartItem.objects.filter(product=product,cart=cart).delete()
                response_data = {"status": 200, "user": str(request.user),"cart_item":cart_item}
                return redirect("show-cart")
            else:
                response_data = {"status": 400, "user": 'annoymous'}
                return HttpResponse(json.dumps(response_data),  content_type="application/json")
        except Exception as ex:
                return HttpResponse("exception")
         