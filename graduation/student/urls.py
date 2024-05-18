from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.views import LeaderboardViewSet, StudentProfileViewSet
from student.views import StudentPerformanceAreaViewSet
from student.views import StudentPerformanceEventViewSet

router = DefaultRouter()
router.register(prefix='student_profile', viewset=StudentProfileViewSet, basename='student_profile')
router.register(prefix='student_performance_area', viewset=StudentPerformanceAreaViewSet, basename='student_performance_area')
router.register(prefix='student_performance_event', viewset=StudentPerformanceEventViewSet, basename='student_performance_event')
router.register(prefix='leaderboard', viewset=LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
