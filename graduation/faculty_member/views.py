from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from faculty_member.models import ChallengeArea, FacultyMemberProfile, OptionsArea, ParagraphArea, QuestionArea, TopicArea
from faculty_member.serializer import ChallengeAreaSerializer, FacultyMemberProfileSerializer, OptionsAreaSerializer, ParagraphAreaSerializer, QuestionAreaSerializer, TopicAreaSerializer

from faculty_member.models import ChallengeEvent, OptionsEvent, ParagraphEvent, QuestionEvent, TopicEvent
from faculty_member.serializer import ChallengeEventSerializer, OptionsEventSerializer, ParagraphEventSerializer, QuestionEventSerializer, TopicEventSerializer

class FacultyMemberProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = FacultyMemberProfile.objects.all()  # Retrieve all faculty member profiles
    serializer_class = FacultyMemberProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Filter by user




# Area 

class TopicAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = TopicArea.objects.all()  # Retrieve all topic areas
    serializer_class = TopicAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['area_id']  # Filter by area ID

class ParagraphAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = ParagraphArea.objects.all()  # Retrieve all paragraph areas
    serializer_class = ParagraphAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic_area_id']  # Filter by topic area ID

class ChallengeAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = ChallengeArea.objects.all()  # Retrieve all challenge areas
    serializer_class = ChallengeAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic_area_id']  # Filter by topic area ID

class QuestionAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = QuestionArea.objects.all()  # Retrieve all question areas
    serializer_class = QuestionAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['challenge_area_id']  # Filter by challenge area ID

class OptionsAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = OptionsArea.objects.all()  # Retrieve all options areas
    serializer_class = OptionsAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['questions_area_id']  # Filter by questions area ID




# Event

class TopicEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']  # Allowed HTTP methods
    queryset = TopicEvent.objects.all()  # Retrieve all topic events
    serializer_class = TopicEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event_id']  # Filter by event ID

class ParagraphEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']  # Allowed HTTP methods
    queryset = ParagraphEvent.objects.all()  # Retrieve all paragraph events
    serializer_class = ParagraphEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic_event_id']  # Filter by topic event ID

class ChallengeEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']  # Allowed HTTP methods
    queryset = ChallengeEvent.objects.all()  # Retrieve all challenge events
    serializer_class = ChallengeEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic_event_id']  # Filter by topic event ID

class QuestionEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']  # Allowed HTTP methods
    queryset = QuestionEvent.objects.all()  # Retrieve all question events
    serializer_class = QuestionEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['challenge_event_id']  # Filter by challenge event ID

class OptionsEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']  # Allowed HTTP methods
    queryset = OptionsEvent.objects.all()  # Retrieve all options events
    serializer_class = OptionsEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['questions_event_id']  # Filter by questions event ID
