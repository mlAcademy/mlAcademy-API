from django.contrib.auth.models import User, Group

from rest_framework import serializers

from lessons.models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
