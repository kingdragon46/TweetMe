from distutils.command.build_scripts import first_line_re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, user_name, password, **other_fields):
        if not user_name:
            raise ValueError(_("You must provide a username"))
        user = self.model(user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, password, **other_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(user_name, password, **other_fields)


class User(AbstractUser):
    user_name = models.CharField(_('username'), max_length=100, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    first_name = models.CharField(max_length=50)
    access_token = models.CharField(max_length=200, null=True, blank=True)
    refresh_token = models.CharField(max_length=200, null=True, blank=True)
    user_date= models.DateTimeField(_("Date & Time"),default=timezone.now)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.user_name