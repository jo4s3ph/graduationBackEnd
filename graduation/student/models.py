from django.db import models
from django.conf import settings
from faculty_member.models import ChallengeArea, ChallengeEvent
from system_admin.models import FacultyDepartment



class StudentProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        ]
    
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    faculty_department = models.ForeignKey(to=FacultyDepartment, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, null=True, blank=True)
    level = models.PositiveIntegerField(null=False, default=1)
    gpa = models.FloatField(max_length=3, null=False, blank=True)
    earned_points = models.PositiveIntegerField(null=True, blank=True)
    
    
    class Meta:
        db_table = 'student_profile'


class StudentProfermenceArea(models.Model):
    student_profile_id = models.ForeignKey(to=StudentProfile, on_delete=models.CASCADE)
    challenge_area_id = models.ForeignKey(to=ChallengeArea, on_delete=models.PROTECT)
    grade = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'student_profermence_area'


class StudentProfermenceEvent(models.Model):
    student_profile_id = models.ForeignKey(to=StudentProfile, on_delete=models.CASCADE)
    challenge_event_id = models.ForeignKey(to=ChallengeEvent, on_delete=models.PROTECT)
    grade = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'student_profermence_event'


