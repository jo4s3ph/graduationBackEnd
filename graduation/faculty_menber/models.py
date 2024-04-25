from django.db import models
from django.conf import settings
from system_admin.models import Area, Event


class FacultyMemberProfile(models.Model):
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
        db_table = 'faculty_member_profile'


class TopicArea(models.Model):
    area_id = models.ForeignKey(to=Area, on_delete=models.CASCADE)
    faculty_member = models.ForeignKey(to=FacultyMemberProfile, on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=100, null=False, blank=True)
    source = models.CharField(max_length=2048, null=False, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'topic_area'


class ParagrapArea(models.Model):
    topic_area_id = models.ForeignKey(to=TopicArea, on_delete=models.CASCADE)
    paragraph_title = models.CharField(max_length=100, null=False, blank=True)
    content = models.TextField(max_length=4000, null=False,)
    example = models.TextField(max_length=4000, null=True,)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'paragraph_area'


class ChallengeArea(models.Model):
    HARD = 'H'
    EASY = 'E'
    SIMPLE = 'S'

    DIFFICULTY_CHOICES = [
        (HARD, 'Hard'),
        (EASY, 'Easy'),
        (SIMPLE, 'Simple')
    ]

    faculty_profile_id = models.ForeignKey(to=FacultyMemberProfile, on_delete=models.CASCADE)
    topic_area_id = models.ForeignKey(TopicArea, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, null=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'challenge_area'


class TopicEvent(models.Model):
    event_id = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    faculty_member = models.ForeignKey(to=FacultyMemberProfile, on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=100, null=False, blank=True)
    source = models.CharField(max_length=2048, null=False, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'topic_event'


class ParagrapEvent(models.Model):
    topic_event_id = models.ForeignKey(to=TopicEvent, on_delete=models.CASCADE)
    paragraph_title = models.CharField(max_length=100, null=False, blank=True)
    content = models.TextField(max_length=4000, null=False,)
    example = models.TextField(max_length=4000, null=True,)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'paragraph_event'


class ChallengeEvent(models.Model):
    HARD = 'H'
    EASY = 'E'
    SIMPLE = 'S'

    DIFFICULTY_CHOICES = [
        (HARD, 'Hard'),
        (EASY, 'Easy'),
        (SIMPLE, 'Simple')
    ]

    faculty_profile_id = models.ForeignKey(to=FacultyMemberProfile, on_delete=models.CASCADE)
    topic_event_id = models.ForeignKey(to=TopicEvent, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, null=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'challenge_event'


class QuestionArea(models.Model):
    challenge_area_id = models.ForeignKey(to=ChallengeArea, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=500, null=False)
    total_points = models.PositiveIntegerField(null=False)
    time_value = models.PositiveIntegerField(null=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'question_area'


class OptionsArea(models.Model):
    questions_area_id = models.ForeignKey(to=QuestionArea, on_delete=models.CASCADE)
    option_syntax = models.CharField(max_length=500, null=False)
    is_correct = models.BooleanField(null=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table ='options_area'


class QuestionEvent(models.Model):
    challenge_area_id = models.ForeignKey(to=ChallengeEvent, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=500, null=False)
    total_points = models.PositiveIntegerField(null=False)
    time_value = models.PositiveIntegerField(null=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table ='question_event'


class OptionsEvent(models.Model):
    questions_event_id = models.ForeignKey(to=QuestionEvent, on_delete=models.CASCADE)
    option_syntax = models.CharField(max_length=500, null=False)
    is_correct = models.BooleanField(null=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=True)
    date_ubdated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'options_event'
