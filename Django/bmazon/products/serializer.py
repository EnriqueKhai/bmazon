from rest_framework import serializers

from products.models import Product, Category, Supplier, Stock


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'cat_name',
            'cat_desc'
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'company_name',
            'country',
            'email'
        ]


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.IntegerField(
        source='supplier.supplier_id',
        read_only=True
    )
    category = serializers.IntegerField(
        source='category.cat_id',
        read_only=True
    )
    prod_image = serializers.FileField(required=False)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=2, decimal_places=2,
    )

    class Meta:
        model = Product
        fields = [
            'product_id',
            'prod_name',
            'prod_desc',
            'price',
            'prod_image',
            'prod_discount',
            'supplier',
            'category'
        ]


class StockSerializer(serializers.ModelSerializer):
    product = serializers.IntegerField(source='product.id', read_only=True)

    class Meta:
        model = Stock
        fields = [
            'product',
            'quantity_in_stock'
        ]
