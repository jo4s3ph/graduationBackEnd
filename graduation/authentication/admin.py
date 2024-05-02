from django.contrib import admin
from .models import OneTimePassword, User



admin.site.register(User)
admin.site.register(OneTimePassword)
