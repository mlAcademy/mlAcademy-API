from django.conf.urls import url

from lessons import views
from .views import LessonRudView, LessonAPIView, ComputeView, SearchView, AllTopicsView, AllLessonsForTopic, AllStudents

urlpatterns = [
   url('topics/', AllTopicsView.as_view(), name='topics'),
   url('search/', SearchView.as_view(), name = 'search'),
   url('compute/', ComputeView.as_view(), name = 'compute'),
   url(r'^$', LessonAPIView.as_view(), name = 'lesson-create'),
   url(r'^(?P<pk>\d+)/$', LessonRudView.as_view(), name = 'lesson-rud'),
   url('lessons/', AllLessonsForTopic.as_view(), name='lessons-per-topic'),
   url('students/', AllStudents.as_view(), name='all_students'),
   #url('get-student/', A)
]
