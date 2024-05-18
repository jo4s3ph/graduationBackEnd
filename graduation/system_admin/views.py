from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from system_admin.models import SystemAdminProfile, FacultyDepartment, Area, Event
from system_admin.serializer import SystemAdminProfileSerializer, FacultyDepartmentSerializer, AreaSerializer, EventSerializer

class SystemAdminProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = SystemAdminProfile.objects.all()  # Retrieve all system admin profiles
    serializer_class = SystemAdminProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Filter by user

class FacultyDepartmentViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = FacultyDepartment.objects.all()  # Retrieve all faculty departments
    serializer_class = FacultyDepartmentSerializer
    filter_backends = [DjangoFilterBackend]

class AreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = Area.objects.all()  # Retrieve all areas
    serializer_class = AreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty_department']  # Filter byfaculty department

class EventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = Event.objects.all()  # Retrieve all events
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty_department']  # Filter by faculty department
