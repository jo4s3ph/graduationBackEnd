from rest_framework import serializers
from .models import StudentProfile
from .models import StudentPerformanceArea
from .models import StudentPerformanceEvent
from authentication.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = StudentProfile
        fields = [
            'id',
            'user',
            'faculty_department',
            'birth_date',
            'gender',
            'level',
            'gpa',
            'earned_points'
        ]



class StudentPerformanceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformanceArea
        fields = [
            'id',
            'student_profile_id',
            'challenge_area_id',
            'grade',
            'is_completed'
        ]

class StudentPerformanceEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformanceEvent
        fields = [
            'id',
            'student_profile_id',
            'challenge_event_id',
            'grade',
            'is_completed'
        ]
