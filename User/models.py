from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,address="",password=None):
        if username is None:
            raise ValueError("Users must have Username")
        
        if email is None:
            raise ValueError("Users must have Email")
        
        user = self.model(username = username,email = self.normalize_email(email),address = address)
        user.set_password(password)
        user.save()
        return user 
    def create_superuser(self,username,email,password=None):
        if password is None:
            raise ValueError("Password should not be None")
        
        user = self.create_user(username, email, password=password)
        user.is_superuser = True 
        user.is_staff = True
        user.save()
        return user 

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''
