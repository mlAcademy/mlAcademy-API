from django.contrib.auth.models import User, Group

from rest_framework import serializers

from lessons.models import Lesson
from lessons.models import Topic

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
