from django.contrib import admin
from Products.models import Category, Product ,Review ,Favorite

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Favorite)