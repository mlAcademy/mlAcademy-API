from django.shortcuts import render

from rest_framework import generics
from lessons.models import Lesson
from .serializers import LessonSerializer
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

class ComputeView(views.APIView):

    def get(self, request):
        # Validate the incoming input (provided through query parameters)
        serializer = ComputeInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # Get the model input
        data = serializer.validated_data
        model_input = data["model_input"]

        # Perform the complex calculations
        result = compute(model_input)
        # Return it in your custom format
        return Response({
            "complex_result": result,
        })
