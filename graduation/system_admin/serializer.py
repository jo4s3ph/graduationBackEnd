from rest_framework import serializers
from .models import SystemAdminProfile
from .models import Area
from .models import Event


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


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            'id',
            'area_name',
            'description',
            'date_created',
            'date_ubdated'
        ]



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'faculty_name',
            'description',
            'date_created',
            'date_ubdated',
            'date_start',
            'date_end'
        ]