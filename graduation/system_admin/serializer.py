from rest_framework import serializers
from .models import SystemAdminProfile, FacultyDepartment, Area, Event


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
            'date_ubdated'
        ]





class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            'id',
            'admin_profile',
            'area_name',
            'description',
            'is_active',
            'date_created',
            'date_ubdated'
        ]



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'admin_profile',
            'event_name',
            'description',
            'is_active',
            'date_created',
            'date_ubdated',
            'date_start',
            'date_end'
        ]