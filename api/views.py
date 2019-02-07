from django.shortcuts import render

from rest_framework import generics
from lessons.models import Lesson, Topic
from .serializers import LessonSerializer, TopicSerializer
# Create your views here.

class LessonAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.all()

class LessonRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.all()

class TopicRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.all()

from rest_framework.response import Response
from rest_framework import serializers, views

import subprocess
import os

def compute(script):
    with open('INPUT.py', 'w+') as f:
        f.write(script)

    os.system("python INPUT.py > OUTPUT.txt")

    with open("OUTPUT.txt") as f:
        response = f.read()

    return response

class ComputeInputSerializer(serializers.Serializer):
    model_input = serializers.CharField()

class SearchInputSerializer(serializers.Serializer):
    topic = serializers.IntegerField()
    lesson = serializers.IntegerField()

class LessonsForTopicInputSerializer(serializers.Serializer):
    topic = serializers.IntegerField()

class SearchView(views.APIView):
    def get(self, request):
        serializer = SearchInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        topic_id = data["topic"]
        lesson_id = data["lesson"]

        topic = Topic.objects.get(pk=topic_id)
        lesson = topic.lessons.all()[lesson_id]

        return Response({
            "content" : lesson.content
        })

class AllTopicsView(views.APIView):
    def get(self, request):
        return Response({
            "topics_ids" : [x.pk for x in Topic.objects.all()],
            "topics_names" : [x.name for x in Topic.objects.all()]
        })

from django.core import serializers

class AllLessonsForTopic(views.APIView):
    def get(self, request):
        serializer = LessonsForTopicInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        topic_id = data["topic"]

        lessons = Topic.objects.get(pk=topic_id).lessons.all()
        data = serializers.serialize("json", lessons)
        rendered_lessons = [{"name" : x.name, "published" : x.date_published, "content" : x.content, "code" : x.code} for x in lessons]

        return Response({
            "number_of_lessons" : len(lessons),
            "lessons" : rendered_lessons
            #"lessons" : lessons
        })

class ComputeView(views.APIView):

    def get(self, request):
        serializer = ComputeInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        model_input = data["model_input"]

        result = compute(model_input)
        return Response({
            "complex_result": result,
        })
