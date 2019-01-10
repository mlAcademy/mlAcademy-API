from django.conf.urls import url

from lessons import views
from .views import LessonRudView, LessonAPIView, ComputeView

urlpatterns = [
   url('test/', ComputeView.as_view(), name = 'compute'),
   url(r'^$', LessonAPIView.as_view(), name = 'lesson-create'),
   url(r'^(?P<pk>\d+)/$', LessonRudView.as_view(), name = 'lesson-rud')
]
