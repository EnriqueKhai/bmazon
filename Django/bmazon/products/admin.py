from django.contrib import admin
from .models import Supplier, Category, Product, Stock

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)