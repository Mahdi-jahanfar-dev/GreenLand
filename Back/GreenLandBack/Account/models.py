from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError


# custom user manager for custom user model
class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):

        if not username:
            raise ValidationError('you should write the username')
        
        if not email:
            raise ValidationError('you should wirte the email')
        
        email = BaseUserManager.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValidationError('is_staff must be set to True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValidationError('is_superuser must be set to True')
        
        user = self.create_user(username=username, email=email, **extra_fields)
        return user
    

# custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    full_name = models.CharField(max_length=100,)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    allow_users_add_greenlands = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "email"]

    def __str__(self):
        return f"{self.username}-{self.email}"