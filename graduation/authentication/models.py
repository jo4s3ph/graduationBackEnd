from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    ROLE = [
        ('A', 'SystemAdmin'),
        ('F', 'FacultyMember'),
        ('S', 'Student')
    ]
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True)
    edu_id = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=32, choices=ROLE, null=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = ["username"]
