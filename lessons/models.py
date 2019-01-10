import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length = 100)
    level = models.CharField(max_length = 20)
    date_published = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField()
    level = models.CharField(default='beginner', max_length = 20)
    favourite_lessons = models.ManyToManyField(Lesson)

    # def __dict__(self):
    #     dict = {}
    #     dict['name'] = "hello"
    #     dict['date_registered'] = self.date_registered
    #     dict['level'] = self.level
    #     favourite_lessons = m

    def get_favourite_lessons(self):
        return self.favourite_lessons.all()

    def add_favourite_lesson(self, lesson):
        self.favourite_lessons.add(lesson)

    def remove_favourite_lesson(self, lesson):
        self.favourite_lessons.remove(lesson)

    def clear_favourite_lessons(self):
        self.favourite_lessons.clear()

    def __str__(self):
        return self.user.username
