from rest_framework import serializers
from .models import FacultyMemberProfile
from .models import TopicArea, ParagraphArea, ChallengeArea, QuestionArea, OptionsArea
from .models import TopicEvent, ParagraphEvent, ChallengeEvent, QuestionEvent, OptionsEvent

class FacultyMemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMemberProfile
        fields = [
            'id',
            'faculty_department',
            'birth_date',
            'gender'
        ]




# Area

class TopicAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicArea
        fields = [
            'id',
            'area_id',
            'faculty_member_id',
            'topic_title',
            'source',
            'description',
            'date_created',
            'date_updated'
        ]

class ParagraphAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphArea
        fields = [
            'id',
            'topic_area_id',
            'paragraph_title',
            'content',
            'example',
            'date_created',
            'date_updated'
        ]

class ChallengeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeArea
        fields = [
            'id',
            'topic_area_id',
            'difficulty',
            'description',
            'date_created',
            'date_updated'
        ]

class QuestionAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionArea
        fields = [
            'id',
            'challenge_area_id',
            'question_title',
            'total_points',
            'time_value',
            'description',
            'date_created',
            'date_updated'
        ]

class OptionsAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsArea
        fields = [
            'id',
            'questions_area_id',
            'option_syntax',
            'is_correct',
            'date_created',
            'date_updated'
        ]




# Event

class TopicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicEvent
        fields = [
            'id',
            'event_id',
            'faculty_member_id',
            'topic_title',
            'source',
            'description',
            'date_created',
            'date_updated'
        ]

class ParagraphEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphEvent
        fields = [
            'id',
            'topic_event_id',
            'paragraph_title',
            'content',
            'example',
            'date_created',
            'date_updated'
        ]

class ChallengeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeEvent
        fields = [
            'id',
            'topic_event_id',
            'difficulty',
            'description',
            'date_created',
            'date_updated'
        ]

class QuestionEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionEvent
        fields = [
            'id',
            'challenge_event_id',
            'question_title',
            'total_points',
            'time_value',
            'description',
            'date_created',
            'date_updated'
        ]

class OptionsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsEvent
        fields = [
            'id',
            'questions_event_id',
            'option_syntax',
            'is_correct',
            'date_created',
            'date_updated'
        ]
