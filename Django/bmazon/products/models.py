from django.db import models

# Create your models here.
class SupplierBase(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=45)
    email = models.CharField(max_length=255,null=True,blank=True)

    class Meta:
        abstract = True
        managed = False
        app_label = 'products'


class Supplier(SupplierBase):
    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.company_name


class CategoryBase(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=255)
    cat_desc = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        abstract = True
        managed = False
        app_label = 'products'


class Category(CategoryBase):
    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.cat_name


class ProductBase(models.Model):
    product_id = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=255)
    prod_desc = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    prod_discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    prod_image = models.FileField()

    class Meta:
        abstract = True
        managed = False
        app_label = 'products'


class Product(ProductBase):
    supplier = models.ForeignKey(Supplier, related_name='prod_supplier', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='prod_category', on_delete=models.CASCADE)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return 'Product: {}'.format(self.prod_name)


class StockBase(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        managed = False
        app_label = 'products'


class Stock(StockBase):
    product = models.ForeignKey(Product, related_name='stock_prod', on_delete=models.CASCADE)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return '{} has {} in stock'.format(self.product, self.quantity_in_stock)