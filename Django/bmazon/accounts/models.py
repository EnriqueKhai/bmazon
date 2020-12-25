from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


# Create your models here.
class AccountBase(models.Model):
    ACCOUNT_TYPE = (
        ('C', 'Customer'),
        ('S', 'Supplier'),
        ('A', 'Admin')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=500)
    country = CountryField(default='SG')
    city = models.CharField(max_length=50)
    postal_code = models.PositiveIntegerField(blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE)

    class Meta:
        managed = False
        abstract = True
        app_label = 'accounts'


class Account(AccountBase):
    def __str__(self):
        return 'Account: {}'.format(self.account_id)

    class Meta:
        app_label = 'accounts'
