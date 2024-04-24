from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from system_admin.models import SystemAdminProfile
from system_admin.serializer import SystemAdminProfileSerializer


class SystemAdminProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch']
    queryset = SystemAdminProfile.objects.all() # SELECT * FROM SystemAdminProfile;
    serializer_class = SystemAdminProfileSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']