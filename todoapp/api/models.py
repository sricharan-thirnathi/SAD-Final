from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.CharField(max_length=249, null=True, blank=True, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    regisDate = models.DateTimeField(default=timezone.now, verbose_name="Regis Date")
    created_by = models.CharField(max_length=150)
    public = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=['created_by', ]), ]
