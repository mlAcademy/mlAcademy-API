from django.conf.urls import url

from lessons import views
from .views import LessonRudView, LessonAPIView, ComputeView, SearchView, AllTopicsView, AllLessonsForTopic

urlpatterns = [
   url('topics/', AllTopicsView.as_view(), name='topics'),
   url('search/', SearchView.as_view(), name = 'search'),
   url('test/', ComputeView.as_view(), name = 'compute'),
   url(r'^$', LessonAPIView.as_view(), name = 'lesson-create'),
   url(r'^(?P<pk>\d+)/$', LessonRudView.as_view(), name = 'lesson-rud'),
   url('lessons/', AllLessonsForTopic.as_view(), name='lessons-per-topic')
]
