from rest_framework import serializers
from .models import SystemAdminProfile, FacultyDepartment, Area, Event

class SystemAdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAdminProfile
        fields = [
            'id',
            'birth_date',
            'gender'
        ]

class FacultyDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyDepartment
        fields = [
            'id',
            'admin_profile',
            'department_name',
            'faculty_name',
            'description',
            'is_active',
            'date_created',
            'date_updated'
        ]

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            'id',
            'admin_profile',
            'faculty_department',
            'area_name',
            'description',
            'is_active',
            'date_created',
            'date_updated'
        ]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'admin_profile',
            'faculty_department',
            'event_name',
            'description',
            'is_active',
            'date_created',
            'date_updated',
            'date_start',
            'date_end'
        ]
