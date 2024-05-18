from django.db import models
from django.conf import settings
from faculty_member.models import ChallengeArea, ChallengeEvent
from system_admin.models import FacultyDepartment

class StudentProfileManager(models.Manager):
    def get_leaderboard(self):
        # Retrieve students ordered by earned points in descending order and select related user fields
        return self.get_queryset().select_related('user').order_by('-earned_points')

class StudentProfile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    faculty_department = models.ForeignKey(to=FacultyDepartment, on_delete=models.CASCADE, default=1)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=MALE, null=True, blank=True)
    level = models.PositiveIntegerField(null=False, default=1)
    gpa = models.FloatField(null=True, blank=True)
    earned_points = models.PositiveIntegerField(null=True, blank=True, default=0)
    
    objects = StudentProfileManager()  # Custom manager

    class Meta:
        db_table = 'student_profile'

class StudentPerformanceArea(models.Model):
    student_profile_id = models.ForeignKey(to=StudentProfile, on_delete=models.CASCADE)
    challenge_area_id = models.ForeignKey(to=ChallengeArea, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(null=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'student_performance_area'

class StudentPerformanceEvent(models.Model):
    student_profile_id = models.ForeignKey(to=StudentProfile, on_delete=models.CASCADE)
    challenge_event_id = models.ForeignKey(to=ChallengeEvent, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(null=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'student_performance_event'

class MyModel(models.Model):
    # model fields
    class Meta:
        db_table = 'custom_table_name'  # custom table name
