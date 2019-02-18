import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    #level = models.CharField(max_length = 20)
    date_published = models.DateTimeField()
    content = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='lesson description')
    prerequisites = models.ManyToManyField('self', related_name='prerequisites_rname',
                                           related_query_name='prerequisites_rqueryname',
                                           blank=True, symmetrical=False)
    difficulty = models.IntegerField(default = 0)
    COLOUR_CHOICES = [('1', 'brand'), ('2', 'accent-2'), ('3', 'accent-3'), ('4', 'accent-4')]
    colour = models.CharField(max_length = 10, choices = COLOUR_CHOICES, default = '1')
    lesson1 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name='lesson1', null=True, blank=True)
    lesson2 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson2', null=True, blank=True)
    lesson3 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson3', null=True, blank=True)
    lesson4 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson4', null=True, blank=True)
    lesson5 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson5', null=True, blank=True)
    lesson6 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson6', null=True, blank=True)
    lesson7 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson7', null=True, blank=True)
    lesson8 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson8', null=True, blank=True)
    lesson9 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson9', null=True, blank=True)
    lesson10 = models.ForeignKey('Lesson', on_delete=models.SET_NULL, default= None, related_name = 'lesson10', null=True, blank=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField()
    level = models.CharField(default='beginner', max_length=20)
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
