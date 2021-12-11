from django.urls import path
from .views import UserList ,CustomUserCreate

urlpatterns = [
    path("", UserList.as_view(), name="user_list"),
    path("create/", CustomUserCreate.as_view(), name="user_create"),
    
]
