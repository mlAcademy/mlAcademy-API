from django.core import serializers as coreSerializers
from rest_framework.response import Response
import os
import sys
import subprocess
from rest_framework import serializers, views
from django.shortcuts import render
from rest_framework import generics
from lessons.models import Lesson, Topic, Student
from .serializers import LessonSerializer, TopicSerializer, StudentSerializer


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


def compute(script):
    if ('import os' in script) or ('import sys' in script):
        return 0

    with open('INPUT.py', 'w+') as f:
        f.write(script)

    code = -1
    try:
        if sys.platform == 'linux':
            code = os.system(
                "timeout 30 python INPUT.py > OUTPUT.txt 2>ERROR.txt")
        elif sys.platform == 'darwin':
            code = os.system(
                "gtimeout 30 python INPUT.py > OUTPUT.txt 2>ERROR.txt")
    except Exception as e:
        return 1

    if code == 31744:
        return 2

    with open("OUTPUT.txt") as f:
        output = f.read()

    with open("ERROR.txt") as f:
        error = f.read()

    return (output, error)


class ComputeInputSerializer(serializers.Serializer):
    input = serializers.CharField()


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
            "content": lesson.content
        })


class AllTopicsView(views.APIView):

    def get(self, request):
        topics = []
        for topic in Topic.objects.all():
            details = {}
            details["id"] = topic.pk
            details["name"] = topic.name
            details["available"] = topic.available
            details["description"] = topic.description
            details["image_url"] = topic.image_url
            details["difficulty"] = topic.difficulty
            details["colour"] = topic.colour
            details["prerequisites"] = [
                {'id': x.pk, 'name': x.name} for x in topic.prerequisites.all()]
            topics.append(details)
        topics = sorted(
            [topic for topic in topics if topic['available']], key=lambda x: x["difficulty"])
        return Response({
            "topics": topics
        })


class AllLessonsForTopic(views.APIView):
    def get(self, request):
        serializer = LessonsForTopicInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        topic_id = data["topic"]

        #lessons = Topic.objects.get(pk=topic_id).lessons.all()
        topic = Topic.objects.get(pk=topic_id)
        lessons = []
        for i in range(1, 11):
            lesson = getattr(topic, "lesson" + str(i))
            if lesson == None:
                break
            lessons.append(lesson)

        data = coreSerializers.serialize("json", lessons)
        rendered_lessons = [{"name": x.name, "published": x.date_published,
                             "content": x.content, "code": x.code} for x in lessons]

        return Response({
            "number_of_lessons": len(lessons),
            "lessons": rendered_lessons
            # "lessons" : lessons
        })


class AllStudents(views.APIView):
    def get(self, request):
        if len(request.query_params) == 0:
            return Response({
                'student_uids': [x.uid for x in Student.objects.all()]
            })
        student_uid = request.query_params['uid']
        try:
            student = Student.objects.get(uid=student_uid)
        except Exception as e:
            return Response({"error": "user doesn't exist or duplicate users"})

        return Response({
            'uid': student_uid,
            'topics': [x.pk for x in student.completed_topics.all()],
            'lessons': [x.pk for x in student.completed_lessons.all()]
        })

    def post(self, request):
        params = request.query_params

        if 'action' not in params:
            return Response({"Please specify the action you want to perform!"})

        # ADD LESSON
        if params['action'] == 'add-lesson':
            try:
                s = Student.objects.get(uid=params['uid'])
                l = Lesson.objects.get(id=params['lesson-id'])
            except Exception as e:
                return Response("Invalid lesson or user id!")
            s.completed_lessons.add(l)
            s.save()
            return Response("Added new lesson")

        # ADD TOPIC
        if params['action'] == 'add-topic':
            try:
                s = Student.objects.get(uid=params['uid'])
                t = Topic.objects.get(id=params['topic-id'])
            except Exception as e:
                return Response("Invalid topic or user id!")
            s.completed_topics.add(t)
            s.save()
            return Response("Added new topic")

        # REMOVE LESSON
        if params['action'] == 'remove-lesson':
            try:
                s = Student.objects.get(uid=params['uid'])
                l = Lesson.objects.get(id=params['lesson-id'])
            except Exception as e:
                return Response("Invalid lesson or user id!")
            s.completed_lessons.remove(l)
            s.save()
            return Response("Lesson removed")

        # REMOVE TOPIC
        if params['action'] == 'remove-topic':
            try:
                s = Student.objects.get(uid=params['uid'])
                t = Topic.objects.get(id=params['topic-id'])
            except Exception as e:
                return Response("Invalid topic or user id!")
            s.completed_topics.remove(t)
            s.save()
            return Response("Topic removed")

        # CREATE USER
        if params['action'] == 'create-user':
            if 'uid' not in params:
                return Response("Include uid to create a new user")
            if Student.objects.filter(uid=params['uid']):
                return Response("User with that uid already exists")
            s = Student(uid=params['uid'])
            s.save()
            return Response("Created new user with id {}!".format(params['uid']))

        # DELETE USER
        if params['action'] == 'delete-user':
            if 'uid' not in params:
                return Response("Include uid to delete a user")
            try:
                s = Student.objects.get(uid=params['uid'])
            except Exception as e:
                return Response("User does not exist")
            s.delete()
            return Response("Deleted user with id {}!".format(params['uid']))


class StudentAPIView(generics.CreateAPIView):
    lookup_field = 'uid'
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class StudentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class ComputeView(views.APIView):

    def get(self, request):
        serializer = ComputeInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        input = data["input"]

        result = compute(input)
        if result == 0:
            return Response({
                "error": "forbidden_imports"
            })
        if result == 1:
            return Response({
                "error": "wrong_environment"
            })
        if result == 2:
            return Response({
                "error": "timeout_exceeded"
            })
        return Response({
            "output": result[0],
            "error_output": result[1]
        })
