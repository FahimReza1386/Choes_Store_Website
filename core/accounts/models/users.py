from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
            Custom Create User model with email and password .
        """

        if not email:
            raise ValueError(_("The email User Must Be Set."))
        
        email = self.normalize_email(email)
        user = self.model(email=email , **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, password, **extra_fileds):
        extra_fileds.setdefault("is_staff", True)
        extra_fileds.setdefault("is_superuser", True)
        extra_fileds.setdefault("is_verified", True)


        if extra_fileds.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        elif extra_fileds.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fileds)
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True , max_length=200)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    first_name = models.CharField(max_length=80)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"