from django.urls import path, include
from rest_framework.routers import DefaultRouter
from system_admin.views import SystemAdminProfileViewSet
from system_admin.views import AreaViewSet
from system_admin.views import EventViewSet


router = DefaultRouter()
router.register(prefix='system_admin_profile', viewset=SystemAdminProfileViewSet, basename='system_admin_profile')
router.register(prefix='area', viewset=AreaViewSet, basename='area')
router.register(prefix='event', viewset=EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]