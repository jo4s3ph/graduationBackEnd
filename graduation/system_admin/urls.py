from django.urls import path, include
from rest_framework.routers import DefaultRouter
from system_admin.views import SystemAdminProfileViewSet


router = DefaultRouter()
router.register(prefix='system_admin_profile', viewset=SystemAdminProfileViewSet, basename='system_admin_profile')

urlpatterns = [
    path('', include(router.urls)),
]