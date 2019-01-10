from django.urls import path

from . import views

app_name = 'lessons'

urlpatterns = [

    path('all_lessons/', views.get_all_lessons, name='get_all_lessons'),
    path('lesson/<int:lessonid>/', views.get_lesson_with_id, name='get_lesson_with_id'),
    path('lesson/<str:lessonname>/', views.get_lesson_with_name, name='get_lesson_with_name'),
    path('favourites/<str:name>/', views.get_favourite_lessons, name='get_favourtie_lessons'),
    path('all_students/', views.get_all_students, name='get_all_students'),
    path('student/<str:name>', views.get_student, name='get_user'),

]
