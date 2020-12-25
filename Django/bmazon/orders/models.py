from django.db import models
from products.models import Product
from accounts.models import Account


# Create your models here.
class OrderBase(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    order_discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    estimated_delivery = models.DateTimeField(blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
        managed = False
        app_label = 'orders'


class Order(OrderBase):
    product = models.ForeignKey(Product, related_name='order_prod', on_delete=models.PROTECT)
    account = models.ForeignKey(Account, related_name='order_cust', on_delete=models.CASCADE)

    class Meta:
        app_label = 'orders'

    def __str__(self):
        return '{} by {}'.format(self.order_id)


class CurrencyConversion(models.Model):
    conversion_id = models.AutoField(primary_key=True)
    from_curr = models.CharField(max_length=45)
    to_curr = models.CharField(max_length=45)
    rate = models.DecimalField(max_digits=7, decimal_places=3)

    class Meta:
        app_label = 'orders'

    def __str__(self):
        return '{} to {} at {}'.format(self.from_curr, self.to_curr, self.rate)
