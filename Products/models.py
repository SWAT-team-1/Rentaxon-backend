from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=64)
    product_location = models.CharField(max_length=256)
    product_description = models.TextField(default="", null=True, blank=True)
    product_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0)
    product_img_1 = models.CharField(max_length=256)
    product_img_2 = models.CharField(max_length=256)
    product_img_3 = models.CharField(max_length=256)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name




class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    product_favorite = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_favorite.product_name

class Review(models.Model):
    reviewed = models.ForeignKey(get_user_model(),related_name='reviewed',null=True,on_delete=models.CASCADE)
    review_content = models.TextField(max_length=500)
    auther = models.ForeignKey(get_user_model(),related_name='auther',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.review_content
