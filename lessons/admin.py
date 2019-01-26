from django.contrib import admin

# Register your models here.

from .models import Lesson, Student, Topic

admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Topic)
