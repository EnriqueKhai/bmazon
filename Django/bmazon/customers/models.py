from django.db import models

# Create your models here.
class CustomerBase(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    postal_code = models.PositiveIntegerField()
    phone = models.CharField(max_length=20,null=True, blank=True)

    class Meta:
        managed = False
        abstract = True
        app_label = 'customers'


class Customer(CustomerBase):
    def __str__(self):
        return self.customer_id
    
    class Meta:
        app_label = 'customers'
