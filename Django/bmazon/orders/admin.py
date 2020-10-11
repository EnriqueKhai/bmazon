from django.contrib import admin
from .models import Order, CurrencyConversion

# Register your models here.
admin.site.register(Order)
admin.site.register(CurrencyConversion)
