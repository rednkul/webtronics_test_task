from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import Group

import jwt

from .managers import CustomUserManager


# Authentication


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField( unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    groups = models.ManyToManyField(Group, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


