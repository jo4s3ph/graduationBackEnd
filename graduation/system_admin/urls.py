from django.urls import path, include
from rest_framework.routers import DefaultRouter
from system_admin.views import SystemAdminProfileViewSet, FacultyDepartmentViewSet, AreaViewSet, EventViewSet

router = DefaultRouter()
router.register(prefix='system_admin_profile', viewset=SystemAdminProfileViewSet, basename='system_admin_profile')
router.register(prefix='faculty_department', viewset=FacultyDepartmentViewSet, basename='faculty_department')
router.register(prefix='area', viewset=AreaViewSet, basename='area')
router.register(prefix='event', viewset=EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
