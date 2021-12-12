from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, user_email, user_name, password, phone_number):
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
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_name, password,phone_number):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            user_email,
            user_name=user_name,
            password=password,
            phone_number=phone_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser):
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
    objects = MyUserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name','password','phone_number']

    def __str__(self):
        return self.user_email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin