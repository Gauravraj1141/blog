from django.db import models
from userprofile.models import User

class TradeProduct(models.Model):
    product_id = models.AutoField(primary_key=True,editable=False)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(null=True)
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to="nyseimages", blank=True, null=True)

    def __str__(self):
        return str(self.product_id)
    

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.cart_id)

class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(TradeProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.cart_item_id)