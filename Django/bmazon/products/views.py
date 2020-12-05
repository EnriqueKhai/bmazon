import django_filters
from django.shortcuts import render
from .models import Product, Category, Supplier, Stock
from .serializer import (
    ProductSerializer,
    CategorySerializer,
    SupplierSerializer,
    StockSerializer
)
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')

    class Meta:
        model = Product
        fields = ['prod_name', 'price']


# Create your views here.
class ProductsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('product_id', )
    search_fields = ('prod_name', 'prod_desc')
    pagination_class = ProductsPagination


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(category_id=request.data['category'],
                            supplier_id=request.data['supplier'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'product_id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        product = Product.objects.get(pk=product_id)
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        serializer = ProductSerializer(product, data=request.data,  partial=True)
        if serializer.is_valid(raise_exception=True):
            if 'category' in request.data:
                serializer.save(category_id=request.data['category'])
            if 'supplier' in request.data:
                serializer.save(supplier_id=request.data['supplier'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('cat_id', )
    search_fields = ('cat_name', 'cat_desc')
    pagination_class = CategoryPagination

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'cat_id'
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class SupplierPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class SupplierList(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('supplier_id', )
    search_fields = ('company_name', 'email')
    pagination_class = SupplierPagination

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SupplierRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    lookup_field = 'supplier_id'
    serializer_class = SupplierSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
