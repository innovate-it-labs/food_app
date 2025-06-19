from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
<<<<<<< HEAD
 
=======

>>>>>>> 563a36169d6fe5cce01fb8e922f0b34ef5863817
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
<<<<<<< HEAD
 
=======

>>>>>>> 563a36169d6fe5cce01fb8e922f0b34ef5863817
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)
<<<<<<< HEAD
 
=======

>>>>>>> 563a36169d6fe5cce01fb8e922f0b34ef5863817
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    objects = CustomUserManager()
 
 
=======

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


>>>>>>> 563a36169d6fe5cce01fb8e922f0b34ef5863817
