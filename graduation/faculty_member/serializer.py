from rest_framework import serializers
from .models import FacultyMemberProfile

from .models import TopicArea
from .models import ParagraphArea
from .models import ChallengeArea
from .models import QuestionArea
from .models import OptionsArea

from .models import TopicEvent
from .models import ParagraphEvent
from .models import ChallengeEvent
from .models import QuestionEvent
from .models import OptionsEvent


class FacultyMemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMemberProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'gender'
        ]



# Area

class TopicAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicArea
        fields = [
            'id',
            'topic_title',
            'source',
            'description',
            'date_created',
            'date_ubdated'
        ]



class ParagraphAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphArea
        fields = [
            'id',
            'paragraph_title',
            'content',
            'example',
            'date_created',
            'date_ubdated'
        ]



class ChallengeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeArea
        fields = [
            'id',
            'difficulty',
            'description',
            'date_created',
            'date_ubdated'
        ]



class QuestionAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionArea
        fields = [
            'id',
            'question_title',
            'total_points',
            'time_value',
            'description',
            'date_created',
            'date_ubdated'
        ]



class OptionsAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsArea
        fields = [
            'id',
            'option_syntax',
            'is_correct',
            'date_created',
            'date_ubdated'
        ]




# Event

class TopicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicEvent
        fields = [
            'id',
            'topic_title',
            'source',
            'description',
            'date_created',
            'date_ubdated'
        ]



class ParagraphEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphEvent
        fields = [
            'id',
            'paragraph_title',
            'content',
            'example',
            'date_created',
            'date_ubdated'
        ]



class ChallengeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeEvent
        fields = [
            'id',
            'difficulty',
            'description',
            'date_created',
            'date_ubdated'
        ]



class QuestionEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionEvent
        fields = [
            'id',
            'question_title',
            'total_points',
            'time_value',
            'description',
            'date_created',
            'date_ubdated'
        ]



class OptionsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsEvent
        fields = [
            'id',
            'option_syntax',
            'is_correct',
            'date_created',
            'date_ubdated'
        ]
