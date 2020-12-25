"""bmazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from products.views import (
    ProductListCreate,
    ProductRetrieveUpdateDestroy,
    CategoryListCreate,
    CategoryRetrieveUpdateDestroy,
    SupplierListCreate,
    SupplierRetrieveUpdateDestroy,
)

urlpatterns = [
    path('api/', include([
        path('products', ProductListCreate.as_view()),
        path('products/<int:product_id>',
             ProductRetrieveUpdateDestroy.as_view()),
        path('categories', CategoryListCreate.as_view()),
        path('categories/<int:cat_id>',
             CategoryRetrieveUpdateDestroy.as_view()),
        path('suppliers', SupplierListCreate.as_view()),
        path('suppliers/<int:supplier_id>',
             SupplierRetrieveUpdateDestroy.as_view()),
    ])),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
