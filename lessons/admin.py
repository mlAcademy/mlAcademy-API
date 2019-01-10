from django.contrib import admin

# Register your models here.

from .models import Lesson, Student

admin.site.register(Lesson)
admin.site.register(Student)
