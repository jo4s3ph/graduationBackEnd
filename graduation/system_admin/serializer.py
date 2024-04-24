from rest_framework import serializers
from .models import SystemAdminProfile


class SystemAdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAdminProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'gender'
        ]