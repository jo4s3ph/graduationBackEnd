from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faculty_member.views import FacultyMemberProfileViewSet

from faculty_member.views import TopicAreaViewSet
from faculty_member.views import ParagraphAreaViewSet
from faculty_member.views import ChallengeAreaViewSet
from faculty_member.views import QuestionAreaViewSet
from faculty_member.views import OptionsAreaViewSet

from faculty_member.views import TopicEventViewSet
from faculty_member.views import ParagraphEventViewSet
from faculty_member.views import ChallengeEventViewSet
from faculty_member.views import QuestionEventViewSet
from faculty_member.views import OptionsEventViewSet

router = DefaultRouter()
router.register(prefix='faculty_member_profile', viewset=FacultyMemberProfileViewSet, basename='faculty_member_profile')



# Area 
router.register(prefix='topic_area', viewset=TopicAreaViewSet, basename='topic_area')
router.register(prefix='paragraph_area', viewset=ParagraphAreaViewSet, basename='paragraph_area')
router.register(prefix='challenge_area', viewset=ChallengeAreaViewSet, basename='challenge_area')
router.register(prefix='question_area', viewset=QuestionAreaViewSet, basename='question_area')
router.register(prefix='options_area', viewset=OptionsAreaViewSet, basename='options_area')



# Event 
router.register(prefix='topic_event', viewset=TopicEventViewSet, basename='topic_event')
router.register(prefix='paragraph_event', viewset=ParagraphEventViewSet, basename='paragraph_event')
router.register(prefix='challenge_event', viewset=ChallengeEventViewSet, basename='challenge_event')
router.register(prefix='question_event', viewset=QuestionEventViewSet, basename='question_event')
router.register(prefix='options_event', viewset=OptionsEventViewSet, basename='options_event')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
