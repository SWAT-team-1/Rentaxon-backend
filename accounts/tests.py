from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from  .models import NewUser


class APITest(APITestCase):
    
    def setUp(self):

        self.test_user = get_user_model().objects.create_user(user_email='moayad@gmail.com',user_name='Moayad',password='1234',phone_number='+962796814625')
        self.test_user.save()

        account_info={
            "email": "moayad@gmail.com",
            "password": "1234"}

        response= self.client.post('api/token/',account_info,format='text/html')
        token=response.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    def test_list(self):

        response = self.client.get('api/v1/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_exist_user(self):
        assert  self.test_user.user_name=="moayad"
        assert  self.test_user.phone_number=="+962796814625"


    def test_create_user(self):
     
        url ='api/v1/user/create/'
        data={
      "user_email": "osama@gmail.com",
      "password":"osama123",
      "user_name": "osama",
      "phone_number": "0796814655",
      "address": "Jordan/Amman",
      "avatar":"imageurl"
    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, self.test_user.id)
        self.assertEqual(NewUser.objects.count(), 2)