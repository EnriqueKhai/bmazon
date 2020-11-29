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

from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('api/', include([
        path('products/', views.ProductList.as_view()),
        path('products/new', views.ProductCreate.as_view()),
        path('products/<int:product_id>',
            views.ProductRetrieveUpdateDestroy.as_view()),
        path('categories', views.CategoryList.as_view()),
        path('categories/<int:cat_id>',
            views.CategoryRetrieveUpdateDestroy.as_view()),
        path('suppliers', views.SupplierList.as_view()),
        path('suppliers/<int:supplier_id>',
            views.SupplierRetrieveUpdateDestroy.as_view()),
    ])),
    path('admin/', admin.site.urls),
]
