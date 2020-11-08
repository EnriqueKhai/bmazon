from rest_framework import serializers

from products.models import Product, Category, Supplier, Stock


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.IntegerField(source='supplier.id', read_only=True)
    category = serializers.IntegerField(source='category.id', read_only=True)
    prod_image = serializers.FileField(required=False)

    def get_supplier(self, obj):
        return obj.supplier_id

    def get_category(self, obj):
        return obj.category_id

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


class StockSerializer(serializers.ModelSerializer):
    product = serializers.IntegerField(source='product.id', read_only=True)

    class Meta:
        model = Stock
        fields = [
            'product',
            'quantity_in_stock'
        ]
