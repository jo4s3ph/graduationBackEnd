from django.db import models
from django.conf import settings


class SystemAdminProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, null=True, blank=True)


    class Meta:
        db_table = 'system_admin_profile'



class FacultyDepartment(models.Model):

    admin_profile = models.ForeignKey(to=SystemAdminProfile, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100, null=True, blank=True)
    faculty_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(null=True, default=False)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)
    

    class Meta:
        db_table = 'faculty_department'



class Area(models.Model):

    admin_profile = models.ForeignKey(to=SystemAdminProfile, on_delete=models.CASCADE)
    faculty_department = models.ForeignKey(to=FacultyDepartment, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(null=False, default=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'area'
        


class Event(models.Model):

    admin_profile = models.ForeignKey(to=SystemAdminProfile, on_delete=models.CASCADE)
    faculty_department = models.ForeignKey(to=FacultyDepartment, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(null=False, default=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)
    date_start = models.DateTimeField(null=False, blank=True)
    date_end = models.DateTimeField(null=False, blank=True)

    class Meta:
        db_table = 'event'


