from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AccountManager

class Accounts(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
      (1, 'institution'),
      (2, 'teacher'),
      (3, 'student'),
    )
    iid = models.IntegerField()
    userid = models.IntegerField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    groups = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=False
        )
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['iid', 'name', 'user_type']

    objects = AccountManager()

    def __str__(self):
        return self.name