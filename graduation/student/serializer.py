from rest_framework import serializers
from .models import StudentProfile
from .models import StudentProfermenceArea
from .models import StudentProfermenceEvent


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'level',
            'gpa',
            'earned_points'
        ]



class StudentProfermenceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfermenceArea
        fields = [
            'id',
            'student_profile_id',
            'challenge_area_id',
            'grade'
        ]




class StudentProfermenceEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfermenceEvent
        fields = [
            'id',
            'student_profile_id',
            'challenge_event_id',
            'grade'
        ]
