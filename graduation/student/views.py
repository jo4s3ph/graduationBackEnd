from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from student.models import StudentProfile
from student.serializer import StudentProfileSerializer
from student.models import StudentPerformanceArea
from student.serializer import StudentPerformanceAreaSerializer
from student.models import StudentPerformanceEvent
from student.serializer import StudentPerformanceEventSerializer

class StudentProfileViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = StudentProfile.objects.all()  # Retrieve all student profiles
    serializer_class = StudentProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Filter by user

class LeaderboardViewSet(ModelViewSet):
    http_method_names = ['get']  # Allowed HTTP methods
    queryset = StudentProfile.objects.all().order_by('-earned_points')  # Retrieve all student profiles ordered by earned points
    serializer_class = StudentProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Filter by user

    @action(detail=False, methods=['get'])
    def leaderboard(self, request):
        # Retrieve and return the leaderboard
        queryset = StudentProfile.objects.get_leaderboard()  # Use the custom manager method
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class StudentPerformanceAreaViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = StudentPerformanceArea.objects.all()  # Retrieve all student performance areas
    serializer_class = StudentPerformanceAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_profile_id', 'challenge_area_id']  # Filter by student profile ID and challenge area ID

class StudentPerformanceEventViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']  # Allowed HTTP methods
    queryset = StudentPerformanceEvent.objects.all()  # Retrieve all student performance events
    serializer_class = StudentPerformanceEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_profile_id', 'challenge_event_id']  # Filter by student profile ID and challenge event ID

def leaderboard(request):
    # Fetch the student profiles ordered by earned points in descending order
    profiles = StudentProfile.objects.all().order_by('-earned_points')
    data = list(profiles.values('user__username', 'faculty_department__name', 'earned_points', 'level'))
    return JsonResponse({'data': data})
