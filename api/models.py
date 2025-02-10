from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, id, password=None, **extra_fields):
        if not id:
            raise ValueError('The ID field is required')
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(id, password, **extra_fields)

class User(AbstractUser):
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    id = models.CharField(max_length=255, unique=True, primary_key=True)
    id_type = models.CharField(max_length=10, choices=[('phone', 'Phone'), ('email', 'Email')])

    username = None
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.id_type = 'email' if '@' in str(self.id) else 'phone'
        super().save(*args, **kwargs)
