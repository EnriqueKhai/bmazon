from django.test import TestCase
from rest_framework.test import APITestCase

from products.models import Product, Category, Supplier

# Create your tests here.
class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count()
        category = Category(
            cat_name='Testing',
            cat_desc='something'
        )
        category.save()
        supplier = Supplier(
            company_name="Very cool company",
            email='niceemail@gmail.com'
        )
        supplier.save()
        product_attrs = {
            "prod_name": "New product",
            "prod_desc": "Very new",
            "price": '1.29',
            "prod_discount": '70.00',
            "supplier": 1,
            "category": 1
        }
        response = self.client.post('/api/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1,
        )
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)


class ProductListTestCase(APITestCase):
    def test_list_products(self):
        products_count = Product.objects.count()
        response = self.client.get('/api/products/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], products_count)
        self.assertEqual(len(response.data['results']), products_count)


class ProductUpdateTestCase(APITestCase):
    def test_update_product(self):
        product = Product.objects.first()
        response = self.client.patch(
            '/api/products/{}'.format(product.product_id),
            {
                'prod_name': 'New stuff',
                'prod_desc': 'Coool cool cool',
                'price': '123.45'
            },
            format='json',
        )
        updated = Product.objects.get(product_id=product.product_id)
        self.assertEqual(updated.name, 'New stuff')


class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().product_id
        self.client.delete('/api/products/{}'.format(product_id))
        self.assertEqual(
            Product.objects.count(),
            initial_product_count - 1,
        )
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, product_id=product_id
        )
