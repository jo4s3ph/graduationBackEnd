from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from student.models import StudentProfile
from student.serializer import StudentProfileSerializer
from student.models import StudentProfermenceArea
from student.serializer import StudentProfermenceAreaSerializer
from student.models import StudentProfermenceEvent
from student.serializer import StudentProfermenceEventSerializer


class StudentProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = StudentProfile.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = StudentProfileSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']



class StudentProfermenceAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = StudentProfermenceArea.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = StudentProfermenceAreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_profile_id', 'challenge_area_id']



class StudentProfermenceEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = StudentProfermenceEvent.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = StudentProfermenceEventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_profile_id', 'challenge_event_id']
