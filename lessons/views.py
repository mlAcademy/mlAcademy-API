from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404

from .models import Lesson, Student
from django.contrib.auth.models import User
from django.core import serializers

from django.forms.models import model_to_dict
# Create your views here.

def get_all_lessons(request):
    # return JsonResponse(serializers.serialize('json', Lesson.objects.all()))
    all_lessons = [model_to_dict(x) for x in Lesson.objects.all()]
    return JsonResponse({
        'number_of_lessons' : len(all_lessons),
        'lessons' : all_lessons
    })

def get_lesson_with_name(request, lessonname):
    try:
        lesson = Lesson.objects.get(name = lessonname.replace('_', ' '))
    except Lesson.DoesNotExist:
        raise Http404("Lesson with name {} does not exist".format(lessonname.replace('_', ' ')))
    return JsonResponse(model_to_dict(lesson))

def get_lesson_with_id(request, lessonid):
    try:
        lesson = Lesson.objects.get(id = lessonid)
    except Lesson.DoesNotExist:
        raise Http404("Lesson with id {} does not exist".format(lessonid))
    return JsonResponse(model_to_dict(lesson))

def get_favourite_lessons(request, name):
    try:
        user = User.objects.get(username = name)
    except User.DoesNotExist:
        raise Http404("User with username {} does not exist".format(name))
    favourites = [model_to_dict(x) for x in user.student.get_favourite_lessons()]
    return JsonResponse({
        'user' : name,
        'number_of_lessons' : len(favourites),
        'favourite_lessons' : favourites
    })

def student_to_dict(student):
    dict = model_to_dict(student, fields = ["date_registered", "level"])
    dict["name"] = student.user.username
    dict["favourite_lessons"] = [x.name for x in student.get_favourite_lessons()]
    return dict

def get_all_students(request):
    students = [student_to_dict(x) for x in Student.objects.all()]
    return JsonResponse({
        'number_of_students' : len(students),
        'students' : students
    })

def get_student(request, name):
    student = User.objects.get(username = name).student
    return JsonResponse(student_to_dict(student))
