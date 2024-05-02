from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from system_admin.models import SystemAdminProfile, FacultyDepartment, Area, Event
from system_admin.serializer import SystemAdminProfileSerializer, FacultyDepartmentSerializer, AreaSerializer, EventSerializer


class SystemAdminProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = SystemAdminProfile.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = SystemAdminProfileSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']



class FacultyDepartmentViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = FacultyDepartment.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = FacultyDepartmentSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['admin_profile']



class AreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = Area.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = AreaSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['admin_profile', 'faculty_department']



class EventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = Event.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = EventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['admin_profile', 'faculty_department']