from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    HIDDEN_FIELDS = (
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
        'user_permissions',
        'groups',
        'date_joined',
        'subscriptions',
    )

    subscriptions = models.ManyToManyField('self', symmetrical=False, related_name='related_to', blank=True)
