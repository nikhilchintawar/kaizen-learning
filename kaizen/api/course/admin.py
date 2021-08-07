from django.contrib import admin

from .models import Courses, Course_Lessons, Course_Authors

# Register your models here.
admin.site.register(Courses)
admin.site.register(Course_Authors)
admin.site.register(Course_Lessons)
