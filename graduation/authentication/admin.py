from django.contrib import admin
from .models import OneTimePassword, User

admin.site.register(User)  # Register the User model with the admin site
admin.site.register(OneTimePassword)  # Register the OneTimePassword model with the admin site

