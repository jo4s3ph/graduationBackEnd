from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.views import StudentProfileViewSet
from student.views import StudentProfermenceAreaViewSet
from student.views import StudentProfermenceEventViewSet


router = DefaultRouter()
router.register(prefix='student_profile', viewset=StudentProfileViewSet, basename='student_profile')
router.register(prefix='student_profermence_area', viewset=StudentProfermenceAreaViewSet, basename='student_profermence_area')
router.register(prefix='student_profermence_event', viewset=StudentProfermenceEventViewSet, basename='student_profermence_event')

urlpatterns = [
    path('', include(router.urls)),
]