from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

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
            'prod_discount',
            'prod_image',
            'supplier',
            'category'
        ]