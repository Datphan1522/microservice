from django.db import models



class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    product_id = models.CharField(max_length=50)
    #
    # class Meta:
    #     db_table = 'cart_items'
    #     ordering = ['date_added']
    #
    # def total(self):
    #     return self.quantity * self.product.price
    #
    # def name(self):
    #     return self.product.name
    #
    # def price(self):
    #     return self.product.price
    #
    # def get_absolute_url(self):
    #     return self.product.get_absolute_url()
    #
    # def augment_quantity(self, quantity):
    #     self.quantity = self.quantity + int(quantity)
    #     self.save()
