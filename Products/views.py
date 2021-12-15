from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Product,Category,Review ,Favorite
from .serializers import ProductsSerializer, CategorySerializer, FavoriteSerializer ,ReviewSerializer
from .permissions import IsOwnerOrReadOnly
#  Product views
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    permissions_class = (IsOwnerOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


#  Category views
class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    permissions_class = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Favorite views

class FavoriteList(ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDetail(RetrieveUpdateDestroyAPIView):
    permissions_class = (IsOwnerOrReadOnly)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


# Review views

class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(RetrieveUpdateDestroyAPIView):
    permissions_class = (IsOwnerOrReadOnly)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer