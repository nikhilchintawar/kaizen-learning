from django.contrib import admin
from api.courses.models.courses import Courses
from api.courses.models.course_lessons import Course_Lessons
from api.courses.models.course_creator import Course_Creator

# Register your models here.

admin.site.register(Courses)
admin.site.register(Course_Lessons)
admin.site.register(Course_Creator)
