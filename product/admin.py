from django.contrib import admin
from product.models import TradeProduct, Cart, CartItem

@admin.register(TradeProduct)
class TradeProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_description', 'product_price', 'product_image' )
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'user', 'total_price', )
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_item_id', 'cart', 'product', 'quantity', )
    
