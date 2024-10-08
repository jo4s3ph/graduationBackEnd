from typing import Any
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def email_validator(self, email):
        # Validate the email address
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a valid email address"))

    def create_user(self, email, first_name, last_name, password, edu_id, **extra_fields):
        # Create a regular user
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))
        if not first_name:
            raise ValueError(_("First name is required"))
        if not last_name:
            raise ValueError(_("Last name is required"))

        if extra_fields.get("role") == 'A' or extra_fields.get("role") == 'F':
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_verified", True)
            extra_fields.setdefault("is_active", True)
        
        # if extra_fields.get("role") == 'F':
        #     extra_fields.setdefault("is_staff", True)
        #     extra_fields.setdefault("is_verified", True)
        #     extra_fields.setdefault("is_active", True)
        
        user = self.model(email=email, first_name=first_name, last_name=last_name, edu_id=edu_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password, **extra_fields):
        # Create a superuser with additional attributes and validations
        if extra_fields.get("role") == 'A':
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
            extra_fields.setdefault("is_verified", True)
            extra_fields.setdefault("is_active", True)

       
