from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from faculty_member.models import FacultyMemberProfile
from faculty_member.serializer import FacultyMemberProfileSerializer

from faculty_member.models import TopicArea
from faculty_member.serializer import TopicAreaSerializer
from faculty_member.models import ParagraphArea
from faculty_member.serializer import ParagraphAreaSerializer
from faculty_member.models import ChallengeArea
from faculty_member.serializer import ChallengeAreaSerializer
from faculty_member.models import QuestionArea
from faculty_member.serializer import QuestionAreaSerializer
from faculty_member.models import OptionsArea
from faculty_member.serializer import OptionsAreaSerializer

from faculty_member.models import TopicEvent
from faculty_member.serializer import TopicEventSerializer
from faculty_member.models import ParagraphEvent
from faculty_member.serializer import ParagraphEventSerializer
from faculty_member.models import ChallengeEvent
from faculty_member.serializer import ChallengeEventSerializer
from faculty_member.models import QuestionEvent
from faculty_member.serializer import QuestionEventSerializer
from faculty_member.models import OptionsEvent
from faculty_member.serializer import OptionsEventSerializer




class FacultyMemberProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = FacultyMemberProfile.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = FacultyMemberProfileSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


# Area 

class TopicAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = TopicArea.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = TopicAreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['area_id', 'faculty_member']


class ParagraphAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = ParagraphArea.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = ParagraphAreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic_area_id']


class ChallengeAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = ChallengeArea.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = ChallengeAreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty_profile_id', 'topic_area_id']    


class QuestionAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = QuestionArea.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = QuestionAreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['challenge_area_id']


class OptionsAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = OptionsArea.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = OptionsAreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['questions_area_id']



# Event

class TopicEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = TopicEvent.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = TopicEventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event_id', 'faculty_member']


class ParagraphEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = ParagraphEvent.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = ParagraphEventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic_event_id']


class ChallengeEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = ChallengeEvent.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = ChallengeEventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty_profile_id', 'topic_event_id']    


class QuestionEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = QuestionEvent.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = QuestionEventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['challenge_area_id']


class OptionsEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = OptionsEvent.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = OptionsEventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['questions_event_id']