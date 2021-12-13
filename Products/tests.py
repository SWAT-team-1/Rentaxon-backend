from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth import get_user_model


class ProductTests(TestCase):
    def setUp(self):
        self.client = Client()
    def test_product_list_page_status_code(self):
        url = reverse("product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class CategoryTests(TestCase):
    def test_category_list_page_status_code(self):
        url = reverse("category_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    # def get_tokens(self):
    #     tokens_urls = "http://localhost:8000/api/token/"
    #     url_data = {
    #         "user_email": "admin@admin.com",
    #         "password": "admin"
    #     }
    #     response = self.client.post(tokens_urls, url_data)
    #     data = response
    #     tokens = data["access"]
    #     return tokens

    # def test_create_category(self):
    #     tokens = self.get_tokens()
    #     url = "http://localhost:8000/api/v1/category/"
    #     data = {"category_name": "tools",}
    #     headers = {
    #         "Authorization" : f"Bearer {tokens}",

    #     }
    #     response = self.client.post(url, data, headers)
    #     return response


    # def test_create_category(self):
    #     response = self.client.post(
    #         reverse("add"),
    #         {
    #             "category_name": "tools",
    #         }, follow=True
    #     )
    #     self.assertRedirects(response, reverse("category_detail", args="2"))

    # def test_create_product(self):
    #     response = self.client.post(
    #         reverse("product_create"),
    #         {
    #             "name": "Rake",
    #             "rating": "2",
    #             "reviewer": self.user.id,
    #         }, follow=True
    #     )

    #     self.assertRedirects(response, reverse("product_detail", args="2"))
        # self.assertContains(response, "Details about Rake")

