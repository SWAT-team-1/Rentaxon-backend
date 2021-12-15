from django.test.testcases import TestCase
from django.urls.base import reverse
from rest_framework import status
from  .models import NewUser


class APITest(TestCase):
    
    def test_create_user(self):
     
        url ='http://127.0.0.1:8000/api/v1/user/create/'
        data={
      "user_email": "moayad21@gmail.com",
      "password":"moayad123",
      "user_name": "moayad",
      "phone_number": "+962796814645",
      "address": "Jordan/Amman",
      "avatar":"imageurl"
    }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        response2 = self.client.get('http://127.0.0.1:8000/api/v1/user/')
        self.assertEqual(response2.data[0]["user_name"],"moayad")

    def test_user_list(self):
        url ='http://127.0.0.1:8000/api/v1/user/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)