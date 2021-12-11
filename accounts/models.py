from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, user_email, user_name, password,**other_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_email:
            raise ValueError('Users must have an email address')

        user = self.model(
            user_email=self.normalize_email(user_email),
            user_name=user_name,
            password=password,
        
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_email, user_name, password, **other_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_admin') is not True:
            raise ValueError(
                'Superuser must be assigned to is_admin=True.')

        return self.create_user(user_email, user_name, password, **other_fields)


class NewUser(AbstractBaseUser,PermissionsMixin):
    user_email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    avatar = models.CharField(max_length=1000, blank=True)
    address = models.TextField(max_length=250) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name','password']

    def __str__(self):
        return self.email
