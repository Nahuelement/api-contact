import uuid
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone

# def recipe_image_file_path(instance, filename):
#     """Generate file path for new recipe image."""
#     ext = os.path.splitext(filename)[1]
#     filename = f'{uuid.uuid4()}{ext}'

#     return os.path.join('uploads', 'recipe', filename)

class UserManager(BaseUserManager):

    """Manager for users."""
    def create_user(self, email, password=None, **extra_fields):
        """crear, guardar nuevo usuario."""
        if not email:
            raise ValueError('Es necesario ingresar un mail .')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Crear y retornar nuevo usuario."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Recipe(models.Model):

    class Meta:
        ordering = ['created']


    firstName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=255, blank=True)
    Company = models.CharField(max_length=255, blank=True)
    Comment = models.TextField(max_length=None, blank=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.firstName














# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )


#     def __str__(self):
#         return self.name

# class Ingredient(models.Model):
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.name