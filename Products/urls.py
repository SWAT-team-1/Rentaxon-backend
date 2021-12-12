from django.urls import path
from .views import ProductList, ProductDetail,CategoryList,CategoryDetail, FavoriteList,FavoriteDetail , ReviewList ,ReviewDetail

urlpatterns = [
    path("", ProductList.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("category/", CategoryList.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category_detail"),
    path("favourite/", FavoriteList.as_view(), name="Favorite_list"),
    path("favourite/<int:pk>/", FavoriteDetail.as_view(), name="Favorite_detail"),
    path("reviews/", ReviewList.as_view(), name="reviews_list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="reviews_detail"),
]
