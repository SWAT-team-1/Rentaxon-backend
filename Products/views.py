from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Product,Category
from .serializers import ProductsSerializer, CategorySerializer

#  Product views
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


#  Category views
class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
